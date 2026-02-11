"""Fetches news, price data, and macro indicators."""

import logging
from datetime import datetime, timedelta
from typing import Any

import numpy as np
import pandas as pd
import requests
import yfinance as yf

from config import NEWS_API_KEY, MACRO_SYMBOLS, DEFAULT_WATCHLIST

logger = logging.getLogger(__name__)


class DataFetcher:
    """Fetches all data needed for the agent pipeline."""

    def __init__(self):
        self.finnhub_base = "https://finnhub.io/api/v1"

    # ------------------------------------------------------------------ #
    # News
    # ------------------------------------------------------------------ #
    def fetch_news(self, tickers: list[str] | None = None) -> list[dict]:
        """Fetch recent news headlines from Finnhub for given tickers."""
        if not NEWS_API_KEY:
            logger.warning("NEWS_API_KEY not set — skipping news fetch")
            return []

        tickers = tickers or DEFAULT_WATCHLIST[:10]
        all_articles: list[dict] = []
        today = datetime.now().strftime("%Y-%m-%d")
        week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

        for ticker in tickers:
            try:
                url = (
                    f"{self.finnhub_base}/company-news"
                    f"?symbol={ticker}&from={week_ago}&to={today}"
                    f"&token={NEWS_API_KEY}"
                )
                resp = requests.get(url, timeout=10)
                resp.raise_for_status()
                articles = resp.json()
                # Keep the 5 most recent per ticker
                for article in articles[:5]:
                    all_articles.append({
                        "ticker": ticker,
                        "headline": article.get("headline", ""),
                        "summary": article.get("summary", ""),
                        "source": article.get("source", ""),
                        "url": article.get("url", ""),
                        "datetime": article.get("datetime", 0),
                        "category": article.get("category", ""),
                    })
            except Exception as e:
                logger.error(f"Error fetching news for {ticker}: {e}")

        logger.info(f"Fetched {len(all_articles)} articles for {len(tickers)} tickers")
        return all_articles

    def fetch_general_market_news(self) -> list[dict]:
        """Fetch general market news from Finnhub."""
        if not NEWS_API_KEY:
            return []
        try:
            url = f"{self.finnhub_base}/news?category=general&token={NEWS_API_KEY}"
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            articles = resp.json()
            return [
                {
                    "headline": a.get("headline", ""),
                    "summary": a.get("summary", ""),
                    "source": a.get("source", ""),
                    "datetime": a.get("datetime", 0),
                }
                for a in articles[:10]
            ]
        except Exception as e:
            logger.error(f"Error fetching general news: {e}")
            return []

    # ------------------------------------------------------------------ #
    # Price / OHLCV Data
    # ------------------------------------------------------------------ #
    def fetch_ohlcv(
        self, ticker: str, period: str = "1y", interval: str = "1d"
    ) -> pd.DataFrame:
        """Fetch OHLCV data using yfinance."""
        try:
            df = yf.download(
                ticker, period=period, interval=interval, progress=False
            )
            if df.empty:
                logger.warning(f"No OHLCV data for {ticker}")
                return pd.DataFrame()
            # Flatten multi-level columns if present
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            return df
        except Exception as e:
            logger.error(f"Error fetching OHLCV for {ticker}: {e}")
            return pd.DataFrame()

    def fetch_current_price(self, ticker: str) -> float | None:
        """Get the latest closing price for a ticker."""
        try:
            t = yf.Ticker(ticker)
            hist = t.history(period="1d")
            if hist.empty:
                return None
            return float(hist["Close"].iloc[-1])
        except Exception as e:
            logger.error(f"Error fetching price for {ticker}: {e}")
            return None

    # ------------------------------------------------------------------ #
    # Macro Indicators
    # ------------------------------------------------------------------ #
    def fetch_macro(self) -> dict[str, Any]:
        """Fetch macro indicators: VIX, S&P 500, 10Y yield, BTC."""
        macro: dict[str, Any] = {}

        for name, symbol in MACRO_SYMBOLS.items():
            try:
                df = yf.download(symbol, period="15d", interval="1d", progress=False)
                if isinstance(df.columns, pd.MultiIndex):
                    df.columns = df.columns.get_level_values(0)
                if df.empty or len(df) < 2:
                    macro[name] = {"value": None, "change_pct": None}
                    continue
                latest = float(df["Close"].iloc[-1])
                prev = float(df["Close"].iloc[-2])
                change_pct = ((latest - prev) / prev * 100) if prev else 0
                macro[name] = {
                    "value": round(latest, 2),
                    "change_pct": round(change_pct, 2),
                }
            except Exception as e:
                logger.error(f"Error fetching macro {name} ({symbol}): {e}")
                macro[name] = {"value": None, "change_pct": None}

        # Derive market regime
        vix_val = (macro.get("vix") or {}).get("value")
        sp_change = (macro.get("sp500") or {}).get("change_pct")
        btc_change = (macro.get("btc") or {}).get("change_pct")

        if vix_val and sp_change is not None and btc_change is not None:
            if vix_val < 22 and sp_change > 0 and btc_change > -1:
                macro["regime"] = "RISK-ON"
            elif vix_val > 28 or sp_change < -1:
                macro["regime"] = "RISK-OFF"
            else:
                macro["regime"] = "MIXED"
        else:
            macro["regime"] = "UNKNOWN"

        logger.info(f"Macro regime: {macro['regime']}")
        return macro

    # ------------------------------------------------------------------ #
    # Earnings Calendar
    # ------------------------------------------------------------------ #
    def fetch_earnings_calendar(
        self, tickers: list[str] | None = None
    ) -> dict[str, str | None]:
        """Return next earnings date per ticker (or None)."""
        tickers = tickers or DEFAULT_WATCHLIST
        earnings: dict[str, str | None] = {}
        for ticker in tickers:
            try:
                t = yf.Ticker(ticker)
                cal = t.calendar
                if cal is not None and not (isinstance(cal, pd.DataFrame) and cal.empty):
                    if isinstance(cal, dict):
                        ed = cal.get("Earnings Date")
                        if ed:
                            if isinstance(ed, list) and len(ed) > 0:
                                earnings[ticker] = str(ed[0].date()) if hasattr(ed[0], 'date') else str(ed[0])
                            else:
                                earnings[ticker] = str(ed)
                        else:
                            earnings[ticker] = None
                    elif isinstance(cal, pd.DataFrame):
                        earnings[ticker] = None
                    else:
                        earnings[ticker] = None
                else:
                    earnings[ticker] = None
            except Exception:
                earnings[ticker] = None
        return earnings

    # ------------------------------------------------------------------ #
    # VIX-specific for VIX Fear Strategy
    # ------------------------------------------------------------------ #
    def fetch_vix_data(self) -> dict[str, Any]:
        """Fetch VIX data with 10-day SMA for VIX Fear strategy."""
        try:
            df = yf.download("^VIX", period="30d", interval="1d", progress=False)
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            if df.empty or len(df) < 10:
                return {"vix": None, "sma_10": None, "spike_pct": None}

            vix_current = float(df["Close"].iloc[-1])
            sma_10 = float(df["Close"].rolling(10).mean().iloc[-1])
            spike_pct = ((vix_current - sma_10) / sma_10 * 100) if sma_10 else 0

            return {
                "vix": round(vix_current, 2),
                "sma_10": round(sma_10, 2),
                "spike_pct": round(spike_pct, 2),
                "fear_signal": spike_pct >= 20,
            }
        except Exception as e:
            logger.error(f"Error fetching VIX data: {e}")
            return {"vix": None, "sma_10": None, "spike_pct": None}

    # ------------------------------------------------------------------ #
    # Full Data Package
    # ------------------------------------------------------------------ #
    def fetch_all(
        self, tickers: list[str] | None = None
    ) -> dict[str, Any]:
        """Fetch everything needed for the pipeline."""
        tickers = tickers or DEFAULT_WATCHLIST
        logger.info(f"Fetching data for {len(tickers)} tickers...")

        return {
            "news": self.fetch_news(tickers),
            "general_news": self.fetch_general_market_news(),
            "macro": self.fetch_macro(),
            "earnings": self.fetch_earnings_calendar(tickers),
            "vix_data": self.fetch_vix_data(),
            "timestamp": datetime.now().isoformat(),
        }
