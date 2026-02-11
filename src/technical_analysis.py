"""Technical analysis engine implementing all 5 trading strategies."""

import logging
from typing import Any

import numpy as np
import pandas as pd
import ta

logger = logging.getLogger(__name__)


class TechnicalAnalyzer:
    """Runs the 5 verified trading strategies on OHLCV data."""

    # ------------------------------------------------------------------ #
    # Indicator Calculations
    # ------------------------------------------------------------------ #
    @staticmethod
    def calc_rsi(close: pd.Series, period: int = 14) -> pd.Series:
        return ta.momentum.rsi(close, window=period)

    @staticmethod
    def calc_macd(
        close: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9
    ) -> dict[str, pd.Series]:
        macd_line = ta.trend.macd(close, window_slow=slow, window_fast=fast)
        signal_line = ta.trend.macd_signal(
            close, window_slow=slow, window_fast=fast, window_sign=signal
        )
        histogram = ta.trend.macd_diff(
            close, window_slow=slow, window_fast=fast, window_sign=signal
        )
        return {"macd": macd_line, "signal": signal_line, "histogram": histogram}

    @staticmethod
    def calc_bollinger(
        close: pd.Series, period: int = 20, std_dev: float = 2.0
    ) -> dict[str, pd.Series]:
        upper = ta.volatility.bollinger_hband(close, window=period, window_dev=std_dev)
        middle = ta.volatility.bollinger_mavg(close, window=period)
        lower = ta.volatility.bollinger_lband(close, window=period, window_dev=std_dev)
        bandwidth = ta.volatility.bollinger_wband(close, window=period, window_dev=std_dev)
        return {
            "upper": upper,
            "middle": middle,
            "lower": lower,
            "bandwidth": bandwidth,
        }

    @staticmethod
    def calc_ema(close: pd.Series, period: int) -> pd.Series:
        return ta.trend.ema_indicator(close, window=period)

    @staticmethod
    def calc_sma(close: pd.Series, period: int) -> pd.Series:
        return ta.trend.sma_indicator(close, window=period)

    @staticmethod
    def calc_atr(
        high: pd.Series, low: pd.Series, close: pd.Series, period: int = 14
    ) -> pd.Series:
        return ta.volatility.average_true_range(high, low, close, window=period)

    # ------------------------------------------------------------------ #
    # Strategy 1: Connors RSI(2) Mean Reversion
    # ------------------------------------------------------------------ #
    def strategy_connors_rsi(self, df: pd.DataFrame) -> dict[str, Any]:
        """
        Buy when RSI(2) < 10 AND price > 200 SMA.
        Exit when price closes > 5-day SMA.
        """
        close = df["Close"]
        rsi2 = self.calc_rsi(close, period=2)
        sma200 = self.calc_sma(close, period=200)
        sma5 = self.calc_sma(close, period=5)

        latest_rsi2 = float(rsi2.iloc[-1]) if not rsi2.empty else None
        latest_price = float(close.iloc[-1])
        latest_sma200 = float(sma200.iloc[-1]) if not sma200.empty else None
        latest_sma5 = float(sma5.iloc[-1]) if not sma5.empty else None

        if latest_rsi2 is None or latest_sma200 is None or np.isnan(latest_rsi2):
            return {"strategy": "connors_rsi", "setup": False, "reason": "Insufficient data"}

        above_200sma = latest_price > latest_sma200
        rsi_oversold = latest_rsi2 < 10

        return {
            "strategy": "connors_rsi",
            "setup": above_200sma and rsi_oversold,
            "reason": (
                f"RSI(2)={latest_rsi2:.1f} ({'< 10 OVERSOLD' if rsi_oversold else '>= 10'}), "
                f"Price vs 200 SMA={'ABOVE' if above_200sma else 'BELOW'}"
            ),
            "values": {
                "rsi2": round(latest_rsi2, 2) if latest_rsi2 else None,
                "sma200": round(latest_sma200, 2) if latest_sma200 else None,
                "sma5": round(latest_sma5, 2) if latest_sma5 else None,
                "price": round(latest_price, 2),
            },
            "exit_target": latest_sma5,
        }

    # ------------------------------------------------------------------ #
    # Strategy 2: MACD + RSI Momentum
    # ------------------------------------------------------------------ #
    def strategy_macd_rsi(self, df: pd.DataFrame) -> dict[str, Any]:
        """
        Buy on MACD bullish crossover + RSI(14) 40-70 + price > 50 SMA.
        """
        close = df["Close"]
        volume = df["Volume"]
        rsi14 = self.calc_rsi(close, period=14)
        macd = self.calc_macd(close)
        sma50 = self.calc_sma(close, period=50)

        latest_rsi = float(rsi14.iloc[-1]) if not rsi14.empty else None
        latest_macd = float(macd["macd"].iloc[-1]) if not macd["macd"].empty else None
        latest_signal = float(macd["signal"].iloc[-1]) if not macd["signal"].empty else None
        latest_hist = float(macd["histogram"].iloc[-1]) if not macd["histogram"].empty else None
        prev_hist = float(macd["histogram"].iloc[-2]) if len(macd["histogram"]) > 1 else None
        latest_price = float(close.iloc[-1])
        latest_sma50 = float(sma50.iloc[-1]) if not sma50.empty else None

        if any(v is None or (isinstance(v, float) and np.isnan(v)) for v in [latest_rsi, latest_macd, latest_sma50]):
            return {"strategy": "macd_rsi", "setup": False, "reason": "Insufficient data"}

        # MACD bullish crossover: histogram just turned positive
        macd_cross = (
            latest_hist is not None
            and prev_hist is not None
            and latest_hist > 0
            and prev_hist <= 0
        )
        rsi_in_range = 40 <= latest_rsi <= 70
        above_sma50 = latest_price > latest_sma50

        # Volume confirmation
        avg_vol = float(volume.rolling(20).mean().iloc[-1]) if len(volume) >= 20 else 0
        curr_vol = float(volume.iloc[-1])
        vol_confirms = curr_vol > avg_vol if avg_vol > 0 else False

        return {
            "strategy": "macd_rsi",
            "setup": macd_cross and rsi_in_range and above_sma50 and vol_confirms,
            "reason": (
                f"MACD cross={'YES' if macd_cross else 'NO'}, "
                f"RSI(14)={latest_rsi:.1f} ({'in range' if rsi_in_range else 'out of range'}), "
                f"Price vs 50 SMA={'ABOVE' if above_sma50 else 'BELOW'}, "
                f"Volume={'CONFIRMS' if vol_confirms else 'WEAK'}"
            ),
            "values": {
                "rsi14": round(latest_rsi, 2),
                "macd": round(latest_macd, 2),
                "macd_signal": round(latest_signal, 2),
                "macd_histogram": round(latest_hist, 4) if latest_hist else None,
                "sma50": round(latest_sma50, 2),
                "price": round(latest_price, 2),
                "rel_volume": round(curr_vol / avg_vol, 2) if avg_vol > 0 else 0,
            },
        }

    # ------------------------------------------------------------------ #
    # Strategy 3: Bollinger Band Squeeze Breakout
    # ------------------------------------------------------------------ #
    def strategy_bollinger_squeeze(self, df: pd.DataFrame) -> dict[str, Any]:
        """
        Buy when bandwidth hits 6-month low then price breaks above upper band
        with 1.5x volume.
        """
        close = df["Close"]
        volume = df["Volume"]
        bb = self.calc_bollinger(close)
        rsi14 = self.calc_rsi(close, period=14)

        latest_price = float(close.iloc[-1])
        latest_upper = float(bb["upper"].iloc[-1]) if not bb["upper"].empty else None
        latest_lower = float(bb["lower"].iloc[-1]) if not bb["lower"].empty else None
        latest_middle = float(bb["middle"].iloc[-1]) if not bb["middle"].empty else None
        latest_bw = float(bb["bandwidth"].iloc[-1]) if not bb["bandwidth"].empty else None
        latest_rsi = float(rsi14.iloc[-1]) if not rsi14.empty else None

        if any(v is None or (isinstance(v, float) and np.isnan(v)) for v in [latest_upper, latest_bw]):
            return {"strategy": "bollinger_squeeze", "setup": False, "reason": "Insufficient data"}

        # 6-month low bandwidth (126 trading days)
        bw_lookback = min(126, len(bb["bandwidth"]))
        bw_min = float(bb["bandwidth"].iloc[-bw_lookback:].min())
        is_squeeze = latest_bw <= bw_min * 1.05  # Within 5% of 6-month low

        # Breakout above upper band
        breakout = latest_price > latest_upper

        # Volume confirmation
        avg_vol = float(volume.rolling(20).mean().iloc[-1]) if len(volume) >= 20 else 0
        curr_vol = float(volume.iloc[-1])
        vol_confirms = curr_vol > avg_vol * 1.5 if avg_vol > 0 else False

        rsi_bullish = latest_rsi is not None and latest_rsi > 50

        return {
            "strategy": "bollinger_squeeze",
            "setup": is_squeeze and breakout and vol_confirms and rsi_bullish,
            "reason": (
                f"Squeeze={'YES' if is_squeeze else 'NO'} (BW={latest_bw:.4f}, min={bw_min:.4f}), "
                f"Breakout={'YES' if breakout else 'NO'}, "
                f"Volume={'1.5x+' if vol_confirms else 'WEAK'}, "
                f"RSI(14)={f'{latest_rsi:.1f}' if latest_rsi else 'N/A'}"
            ),
            "values": {
                "bandwidth": round(latest_bw, 4) if latest_bw else None,
                "bandwidth_6m_low": round(bw_min, 4),
                "upper_band": round(latest_upper, 2) if latest_upper else None,
                "lower_band": round(latest_lower, 2) if latest_lower else None,
                "middle_band": round(latest_middle, 2) if latest_middle else None,
                "price": round(latest_price, 2),
                "rel_volume": round(curr_vol / avg_vol, 2) if avg_vol > 0 else 0,
            },
            "exit_target": latest_middle,
            "stop_level": latest_lower,
        }

    # ------------------------------------------------------------------ #
    # Strategy 4: MA Crossover (10 EMA / 50 EMA)
    # ------------------------------------------------------------------ #
    def strategy_ma_crossover(self, df: pd.DataFrame) -> dict[str, Any]:
        """
        Buy on bullish crossover with pullback to 10 EMA.
        """
        close = df["Close"]
        volume = df["Volume"]
        ema10 = self.calc_ema(close, period=10)
        ema50 = self.calc_ema(close, period=50)
        rsi14 = self.calc_rsi(close, period=14)

        latest_price = float(close.iloc[-1])
        latest_ema10 = float(ema10.iloc[-1]) if not ema10.empty else None
        latest_ema50 = float(ema50.iloc[-1]) if not ema50.empty else None
        latest_rsi = float(rsi14.iloc[-1]) if not rsi14.empty else None

        if any(v is None or (isinstance(v, float) and np.isnan(v)) for v in [latest_ema10, latest_ema50]):
            return {"strategy": "ma_crossover", "setup": False, "reason": "Insufficient data"}

        # Check for bullish crossover in last 5 days
        bullish_cross = False
        if len(ema10) >= 6 and len(ema50) >= 6:
            for i in range(-5, 0):
                if (
                    float(ema10.iloc[i - 1]) <= float(ema50.iloc[i - 1])
                    and float(ema10.iloc[i]) > float(ema50.iloc[i])
                ):
                    bullish_cross = True
                    break

        # Currently 10 EMA > 50 EMA
        ema_bullish = latest_ema10 > latest_ema50

        # Pullback to 10 EMA (within 0.5%)
        pullback_zone = abs(latest_price - latest_ema10) / latest_ema10 < 0.005
        above_ema10 = latest_price >= latest_ema10

        # Volume check
        avg_vol = float(volume.rolling(20).mean().iloc[-1]) if len(volume) >= 20 else 0
        curr_vol = float(volume.iloc[-1])
        vol_ok = curr_vol > avg_vol if avg_vol > 0 else False

        rsi_ok = latest_rsi is not None and latest_rsi > 45

        setup = (bullish_cross or ema_bullish) and pullback_zone and above_ema10 and rsi_ok

        return {
            "strategy": "ma_crossover",
            "setup": setup,
            "reason": (
                f"Crossover={'YES' if bullish_cross else 'NO'}, "
                f"EMA10 vs EMA50={'BULLISH' if ema_bullish else 'BEARISH'}, "
                f"Pullback zone={'YES' if pullback_zone else 'NO'}, "
                f"Above EMA10={'YES' if above_ema10 else 'NO'}, "
                f"RSI(14)={f'{latest_rsi:.1f}' if latest_rsi else 'N/A'}"
            ),
            "values": {
                "ema10": round(latest_ema10, 2),
                "ema50": round(latest_ema50, 2),
                "price": round(latest_price, 2),
                "rsi14": round(latest_rsi, 2) if latest_rsi else None,
                "rel_volume": round(curr_vol / avg_vol, 2) if avg_vol > 0 else 0,
            },
        }

    # ------------------------------------------------------------------ #
    # Strategy 5: VIX Buy-the-Fear
    # ------------------------------------------------------------------ #
    def strategy_vix_fear(
        self, vix_data: dict[str, Any], sp500_df: pd.DataFrame
    ) -> dict[str, Any]:
        """
        Buy SPY/QQQ when VIX closes 20%+ above its 10-day SMA.
        Only if S&P 500 > 200 SMA.
        """
        vix_val = vix_data.get("vix")
        sma10 = vix_data.get("sma_10")
        spike_pct = vix_data.get("spike_pct")

        if vix_val is None or sma10 is None:
            return {"strategy": "vix_fear", "setup": False, "reason": "No VIX data"}

        fear_signal = spike_pct >= 20

        # Check S&P 500 > 200 SMA
        sp_above_200 = False
        if not sp500_df.empty:
            close = sp500_df["Close"]
            sma200 = self.calc_sma(close, period=200)
            if not sma200.empty:
                latest_sp = float(close.iloc[-1])
                latest_sp_sma = float(sma200.iloc[-1])
                sp_above_200 = latest_sp > latest_sp_sma

        return {
            "strategy": "vix_fear",
            "setup": fear_signal and sp_above_200,
            "reason": (
                f"VIX={vix_val}, 10d SMA={sma10}, "
                f"Spike={spike_pct:.1f}% ({'>=20% FEAR' if fear_signal else '<20%'}), "
                f"S&P vs 200 SMA={'ABOVE' if sp_above_200 else 'BELOW'}"
            ),
            "values": {
                "vix": vix_val,
                "vix_sma10": sma10,
                "vix_spike_pct": spike_pct,
            },
            "eligible_tickers": ["SPY", "QQQ"],
        }

    # ------------------------------------------------------------------ #
    # Full Analysis for a Ticker
    # ------------------------------------------------------------------ #
    def analyze_ticker(
        self,
        ticker: str,
        df: pd.DataFrame,
        vix_data: dict | None = None,
        sp500_df: pd.DataFrame | None = None,
    ) -> dict[str, Any]:
        """Run all applicable strategies on a single ticker."""
        if df.empty or len(df) < 50:
            return {
                "ticker": ticker,
                "error": "Insufficient data",
                "strategies": {},
            }

        close = df["Close"]
        high = df["High"]
        low = df["Low"]
        volume = df["Volume"]

        # Common indicators
        atr = self.calc_atr(high, low, close, period=14)
        latest_atr = float(atr.iloc[-1]) if not atr.empty else None
        latest_price = float(close.iloc[-1])

        avg_vol = float(volume.rolling(20).mean().iloc[-1]) if len(volume) >= 20 else 0
        curr_vol = float(volume.iloc[-1])
        rel_vol = round(curr_vol / avg_vol, 2) if avg_vol > 0 else 0

        # Support / resistance from recent highs/lows
        recent = df.tail(20)
        resistance = float(recent["High"].max())
        support = float(recent["Low"].min())

        # Run strategies
        strategies = {
            "connors_rsi": self.strategy_connors_rsi(df),
            "macd_rsi": self.strategy_macd_rsi(df),
            "bollinger_squeeze": self.strategy_bollinger_squeeze(df),
            "ma_crossover": self.strategy_ma_crossover(df),
        }

        # VIX Fear only for SPY/QQQ
        if ticker in ("SPY", "QQQ") and vix_data and sp500_df is not None:
            strategies["vix_fear"] = self.strategy_vix_fear(vix_data, sp500_df)

        # Find confirmed setups
        confirmed = [
            name for name, result in strategies.items() if result.get("setup")
        ]

        return {
            "ticker": ticker,
            "price": round(latest_price, 2),
            "atr": round(latest_atr, 2) if latest_atr else None,
            "rel_volume": rel_vol,
            "avg_volume": int(avg_vol),
            "current_volume": int(curr_vol),
            "resistance": round(resistance, 2),
            "support": round(support, 2),
            "strategies": strategies,
            "confirmed_setups": confirmed,
            "has_setup": len(confirmed) > 0,
        }
