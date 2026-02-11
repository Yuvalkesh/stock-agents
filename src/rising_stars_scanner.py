"""Rising Stars Scanner — finds stocks showing early breakout patterns."""

import logging
from datetime import datetime
from typing import Any

import numpy as np
import pandas as pd
import yfinance as yf
import ta

from config import DEFAULT_WATCHLIST, VAULT_PATH
from memory_logger import write_file
from vault_reader import get_scan_output_dir

logger = logging.getLogger(__name__)

# S&P 500 high-volume tickers to scan (beyond watchlist)
SCAN_UNIVERSE = [
    "AVGO", "CRM", "COST", "NFLX", "AMD", "ADBE", "PEP", "TMO",
    "LIN", "CSCO", "ACN", "MCD", "ABT", "DHR", "TXN", "QCOM",
    "INTU", "ISRG", "AMAT", "BKNG", "PANW", "LRCX", "ADP",
    "MDLZ", "SNPS", "CDNS", "KLAC", "CRWD", "MRVL", "FTNT",
    "ABNB", "DASH", "COIN", "SQ", "SHOP", "SNOW", "DDOG",
    "NET", "ZS", "PLTR", "SOFI", "RBLX", "U", "ROKU",
    "ENPH", "SEDG", "FSLR", "RIVN", "LCID",
    "BA", "CAT", "DE", "GE", "HON", "RTX", "LMT",
    "V", "MA", "PYPL", "AXP",
    "PFE", "ABBV", "LLY", "MRK", "BMY", "GILD", "AMGN",
    "DIS", "CMCSA", "T", "VZ",
    "COP", "SLB", "EOG", "MPC", "PSX",
    "LOW", "TGT", "SBUX", "NKE", "MO",
    "BRK-B", "C", "BAC", "WFC", "MS", "SCHW",
]


class RisingStarsScanner:
    """Scans for stocks showing early breakout patterns."""

    def scan(self) -> list[dict[str, Any]]:
        """Run the full rising stars scan. Returns ranked candidates."""
        # Filter out tickers already on watchlist
        candidates = [t for t in SCAN_UNIVERSE if t not in DEFAULT_WATCHLIST]
        logger.info(f"Scanning {len(candidates)} tickers for rising stars...")

        # Fetch S&P 500 for relative strength comparison
        sp500 = yf.download("^GSPC", period="3mo", interval="1d", progress=False)
        if isinstance(sp500.columns, pd.MultiIndex):
            sp500.columns = sp500.columns.get_level_values(0)
        sp500_return_20d = 0.0
        if len(sp500) >= 20:
            sp500_return_20d = (
                (float(sp500["Close"].iloc[-1]) - float(sp500["Close"].iloc[-20]))
                / float(sp500["Close"].iloc[-20]) * 100
            )

        results = []
        for ticker in candidates:
            try:
                score, details = self._score_ticker(ticker, sp500_return_20d)
                if score >= 3:
                    results.append({
                        "ticker": ticker,
                        "score": score,
                        **details,
                    })
            except Exception as e:
                logger.debug(f"Error scanning {ticker}: {e}")
                continue

        # Sort by score descending, take top 5
        results.sort(key=lambda x: x["score"], reverse=True)
        top_results = results[:5]

        logger.info(
            f"Found {len(results)} rising stars, top 5: "
            f"{[r['ticker'] for r in top_results]}"
        )
        return top_results

    def _score_ticker(
        self, ticker: str, sp500_return_20d: float
    ) -> tuple[int, dict[str, Any]]:
        """Score a ticker on 7 rising star criteria. Returns (score, details)."""
        df = yf.download(ticker, period="1y", interval="1d", progress=False)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        if df.empty or len(df) < 60:
            return 0, {}

        close = df["Close"]
        volume = df["Volume"]
        high = df["High"]
        low = df["Low"]

        latest_price = float(close.iloc[-1])
        if latest_price < 10:
            return 0, {}

        avg_vol_20 = float(volume.rolling(20).mean().iloc[-1])
        if avg_vol_20 < 500_000:
            return 0, {}

        score = 0
        signals = []

        # 1. Volume explosion: 3x+ avg volume for recent days
        recent_vol = float(volume.iloc[-5:].mean())
        vol_ratio = recent_vol / avg_vol_20 if avg_vol_20 > 0 else 0
        if vol_ratio >= 3:
            score += 1
            signals.append(f"Volume explosion: {vol_ratio:.1f}x average")
        elif vol_ratio >= 2:
            score += 1
            signals.append(f"High volume: {vol_ratio:.1f}x average")

        # 2. Breaking out of consolidation
        if len(close) >= 30:
            range_30d = float(high.iloc[-30:].max()) - float(low.iloc[-30:].min())
            avg_price_30d = float(close.iloc[-30:].mean())
            range_pct = (range_30d / avg_price_30d * 100) if avg_price_30d else 0
            high_30d = float(high.iloc[-30:].max())
            if range_pct < 10 and latest_price > high_30d * 0.99:
                score += 1
                signals.append(f"Breaking {range_pct:.1f}% consolidation range")

        # 3. New 52-week high on volume
        if len(close) >= 252:
            high_52w = float(high.iloc[-252:].max())
        else:
            high_52w = float(high.max())
        near_52w_high = latest_price >= high_52w * 0.97
        if near_52w_high and vol_ratio >= 1.2:
            score += 1
            signals.append(f"Near 52-week high (${high_52w:.2f})")

        # 4. Relative strength vs S&P 500
        if len(close) >= 20:
            stock_return_20d = (
                (float(close.iloc[-1]) - float(close.iloc[-20]))
                / float(close.iloc[-20]) * 100
            )
            rel_strength = stock_return_20d - sp500_return_20d
            if rel_strength > 5:
                score += 1
                signals.append(
                    f"Relative strength: +{rel_strength:.1f}% vs S&P"
                )
        else:
            stock_return_20d = 0
            rel_strength = 0

        # 5. Moving average alignment (10 EMA > 50 EMA > 200 SMA)
        ema10 = ta.trend.ema_indicator(close, window=10)
        ema50 = ta.trend.ema_indicator(close, window=50)
        sma200 = ta.trend.sma_indicator(close, window=200)
        if not ema10.empty and not ema50.empty and not sma200.empty:
            e10 = float(ema10.iloc[-1])
            e50 = float(ema50.iloc[-1])
            s200 = float(sma200.iloc[-1])
            if not (np.isnan(e10) or np.isnan(e50) or np.isnan(s200)):
                if e10 > e50 > s200:
                    score += 1
                    signals.append("MA alignment: 10 EMA > 50 EMA > 200 SMA")

        # 6. RSI momentum (between 55-75 = strong but not overbought)
        rsi = ta.momentum.rsi(close, window=14)
        if not rsi.empty:
            latest_rsi = float(rsi.iloc[-1])
            if 55 <= latest_rsi <= 75:
                score += 1
                signals.append(f"RSI momentum sweet spot: {latest_rsi:.1f}")

        # 7. Price acceleration (this month > last month return)
        if len(close) >= 40:
            return_this_month = (
                (float(close.iloc[-1]) - float(close.iloc[-20]))
                / float(close.iloc[-20]) * 100
            )
            return_last_month = (
                (float(close.iloc[-20]) - float(close.iloc[-40]))
                / float(close.iloc[-40]) * 100
            )
            if return_this_month > return_last_month and return_this_month > 3:
                score += 1
                signals.append(
                    f"Accelerating: {return_this_month:.1f}% this month "
                    f"vs {return_last_month:.1f}% last month"
                )

        # Monthly change
        month_change = 0
        if len(close) >= 20:
            month_change = (
                (float(close.iloc[-1]) - float(close.iloc[-20]))
                / float(close.iloc[-20]) * 100
            )

        return score, {
            "price": round(latest_price, 2),
            "month_change": round(month_change, 1),
            "vol_ratio": round(vol_ratio, 1),
            "rel_strength": round(rel_strength, 1),
            "signals": signals,
            "avg_volume": int(avg_vol_20),
        }

    def generate_report(self, results: list[dict[str, Any]], date_str: str) -> str:
        """Generate markdown report of rising stars."""
        if not results:
            return f"# Rising Stars Scan — {date_str}\n\nNo rising stars found today."

        lines = [f"# Rising Stars Scan — {date_str}\n"]
        lines.append("## New Discoveries\n")

        add_tickers = []
        for i, r in enumerate(results, 1):
            lines.append(f"### {i}. {r['ticker']}")
            lines.append(f"- **Score**: {r['score']}/7 criteria met")
            lines.append(f"- **Price**: ${r['price']} ({r['month_change']:+.1f}% this month)")
            lines.append(f"- **Volume**: {r['vol_ratio']}x average (5-day)")
            lines.append(f"- **Relative Strength vs S&P**: {r['rel_strength']:+.1f}%")
            lines.append(f"- **Signals**:")
            for sig in r["signals"]:
                lines.append(f"  - {sig}")
            action = "Add to watchlist" if r["score"] >= 4 else "Watch for now"
            lines.append(f"- **Recommended**: {action}")
            lines.append("")
            if r["score"] >= 4:
                add_tickers.append(r["ticker"])

        lines.append("## Watchlist Update Recommendation")
        if add_tickers:
            lines.append(f"**Add**: {', '.join(add_tickers)}")
        else:
            lines.append("**Add**: None this scan (watching only)")
        lines.append("")

        report = "\n".join(lines)

        # Save to vault
        scan_dir = get_scan_output_dir(date_str)
        path = scan_dir / "rising-stars.md"
        write_file(path, report)

        return report

    def update_watchlist(self, tickers_to_add: list[str]) -> None:
        """Add new tickers to the watchlist markdown file."""
        if not tickers_to_add:
            return

        watchlist_path = VAULT_PATH / "C-core" / "watchlist.md"
        content = watchlist_path.read_text(encoding="utf-8")

        # Add before "## Macro Indicators"
        new_section = "\n### Rising Stars (Auto-Discovered)\n"
        new_section += "| Ticker | Name | Sector | Notes |\n"
        new_section += "|--------|------|--------|-------|\n"
        for ticker in tickers_to_add:
            new_section += f"| {ticker} | — | — | Added by Rising Stars Scout |\n"

        if "### Rising Stars" in content:
            # Update existing section
            parts = content.split("### Rising Stars")
            before = parts[0]
            # Find the next section after Rising Stars
            rest = parts[1]
            next_section_idx = rest.find("\n## ")
            if next_section_idx > 0:
                after = rest[next_section_idx:]
            else:
                after = ""
            content = before + new_section + after
        elif "## Macro Indicators" in content:
            content = content.replace(
                "## Macro Indicators",
                new_section + "\n## Macro Indicators"
            )
        else:
            content += "\n" + new_section

        write_file(watchlist_path, content)
        logger.info(f"Added to watchlist: {tickers_to_add}")


def run_rising_stars_scan(date_str: str | None = None) -> list[dict[str, Any]]:
    """Run a rising stars scan and generate report."""
    date_str = date_str or datetime.now().strftime("%Y-%m-%d")
    scanner = RisingStarsScanner()
    results = scanner.scan()
    scanner.generate_report(results, date_str)

    # Auto-add tickers scoring 4+
    add_tickers = [r["ticker"] for r in results if r["score"] >= 4]
    if add_tickers:
        scanner.update_watchlist(add_tickers)

    return results
