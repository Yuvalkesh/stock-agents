"""Event-driven backtester using the same TechnicalAnalyzer strategies."""

import logging
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
import yfinance as yf

import config
from technical_analysis import TechnicalAnalyzer, REGIME_STRATEGY_MAP

logger = logging.getLogger(__name__)


class Trade:
    """Represents a single backtest trade."""

    def __init__(
        self,
        symbol: str,
        strategy: str,
        direction: str,
        entry_date: str,
        entry_price: float,
        stop_loss: float,
        take_profit: float,
        shares: int = 100,
    ):
        self.symbol = symbol
        self.strategy = strategy
        self.direction = direction
        self.entry_date = entry_date
        self.entry_price = entry_price
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.shares = shares
        self.exit_date: str = ""
        self.exit_price: float = 0.0
        self.exit_reason: str = ""
        self.pnl: float = 0.0
        self.r_multiple: float = 0.0
        self.bars_held: int = 0
        self.trailing_stop: float | None = None

    @property
    def risk_per_share(self) -> float:
        return abs(self.entry_price - self.stop_loss)


class BacktestResult:
    """Aggregated results from a backtest run."""

    def __init__(self, strategy: str, tickers: list[str], start: str, end: str):
        self.strategy = strategy
        self.tickers = tickers
        self.start_date = start
        self.end_date = end
        self.trades: list[Trade] = []
        self.equity_curve: list[float] = []

    @property
    def total_trades(self) -> int:
        return len(self.trades)

    @property
    def wins(self) -> list[Trade]:
        return [t for t in self.trades if t.pnl > 0]

    @property
    def losses(self) -> list[Trade]:
        return [t for t in self.trades if t.pnl <= 0]

    @property
    def win_rate(self) -> float:
        return len(self.wins) / self.total_trades * 100 if self.total_trades else 0

    @property
    def avg_r(self) -> float:
        rs = [t.r_multiple for t in self.trades]
        return sum(rs) / len(rs) if rs else 0

    @property
    def profit_factor(self) -> float:
        gross_profit = sum(t.pnl for t in self.wins)
        gross_loss = abs(sum(t.pnl for t in self.losses))
        return gross_profit / gross_loss if gross_loss > 0 else float("inf")

    @property
    def total_pnl(self) -> float:
        return sum(t.pnl for t in self.trades)

    @property
    def avg_hold_days(self) -> float:
        bars = [t.bars_held for t in self.trades]
        return sum(bars) / len(bars) if bars else 0

    @property
    def max_drawdown(self) -> float:
        if not self.equity_curve:
            return 0
        peak = self.equity_curve[0]
        max_dd = 0
        for val in self.equity_curve:
            if val > peak:
                peak = val
            dd = (peak - val) / peak * 100 if peak > 0 else 0
            max_dd = max(max_dd, dd)
        return max_dd

    @property
    def sharpe_ratio(self) -> float:
        if len(self.trades) < 2:
            return 0
        returns = [t.pnl for t in self.trades]
        avg = np.mean(returns)
        std = np.std(returns)
        if std == 0:
            return 0
        # Annualized: assume ~20 trades/year
        return (avg / std) * np.sqrt(min(20, self.total_trades))


class Backtester:
    """Event-driven backtester for the 5 trading strategies."""

    def __init__(self, initial_equity: float = 100_000):
        self.initial_equity = initial_equity
        self.analyzer = TechnicalAnalyzer()

    def run(
        self,
        strategy: str,
        tickers: list[str],
        start_date: str,
        end_date: str | None = None,
        use_regime_filter: bool = False,
    ) -> BacktestResult:
        """
        Run a backtest for a single strategy across given tickers.

        Args:
            strategy: one of connors_rsi, macd_rsi, bollinger_squeeze, ma_crossover, vix_fear
            tickers: list of ticker symbols
            start_date: YYYY-MM-DD start
            end_date: YYYY-MM-DD end (default: today)
            use_regime_filter: if True, skip signals when regime doesn't match

        Returns:
            BacktestResult with all trades and metrics
        """
        end_date = end_date or datetime.now().strftime("%Y-%m-%d")
        result = BacktestResult(strategy, tickers, start_date, end_date)
        equity = self.initial_equity

        logger.info(
            f"Backtesting {strategy} on {tickers} from {start_date} to {end_date}"
        )

        # Fetch VIX and S&P 500 data for regime detection and VIX strategy
        vix_df = self._fetch_data("^VIX", start_date, end_date)
        sp500_df = self._fetch_data("^GSPC", start_date, end_date)

        for ticker in tickers:
            df = self._fetch_data(ticker, start_date, end_date)
            if df.empty or len(df) < 50:
                logger.warning(f"Not enough data for {ticker}, skipping")
                continue

            trades = self._backtest_ticker(
                ticker, df, strategy, vix_df, sp500_df, equity, use_regime_filter
            )
            result.trades.extend(trades)

        # Build equity curve
        equity_curve = [self.initial_equity]
        running = self.initial_equity
        for trade in sorted(result.trades, key=lambda t: t.entry_date):
            running += trade.pnl
            equity_curve.append(running)
        result.equity_curve = equity_curve

        logger.info(
            f"Backtest complete: {result.total_trades} trades, "
            f"WR={result.win_rate:.1f}%, PF={result.profit_factor:.2f}, "
            f"Total P&L=${result.total_pnl:,.2f}"
        )

        return result

    def _fetch_data(self, ticker: str, start: str, end: str) -> pd.DataFrame:
        """Fetch OHLCV data with buffer for indicator warmup."""
        try:
            # Add 250-day buffer for indicator calculations (200 SMA needs it)
            from datetime import timedelta
            start_dt = datetime.strptime(start, "%Y-%m-%d") - timedelta(days=365)
            df = yf.download(
                ticker,
                start=start_dt.strftime("%Y-%m-%d"),
                end=end,
                interval="1d",
                progress=False,
            )
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            return df
        except Exception as e:
            logger.error(f"Error fetching backtest data for {ticker}: {e}")
            return pd.DataFrame()

    def _backtest_ticker(
        self,
        ticker: str,
        df: pd.DataFrame,
        strategy: str,
        vix_df: pd.DataFrame,
        sp500_df: pd.DataFrame,
        equity: float,
        use_regime_filter: bool,
    ) -> list[Trade]:
        """Walk forward through bars for a single ticker."""
        trades: list[Trade] = []
        active_trade: Trade | None = None

        # Minimum lookback for indicators
        min_bars = 250
        if len(df) <= min_bars:
            return trades

        close = df["Close"]
        high = df["High"]
        low = df["Low"]

        atr_series = self.analyzer.calc_atr(high, low, close, period=14)

        for i in range(min_bars, len(df)):
            current_date = str(df.index[i].date())
            current_bar = df.iloc[i]
            bar_high = float(current_bar["High"])
            bar_low = float(current_bar["Low"])
            bar_close = float(current_bar["Close"])

            # ---- Check exits first ---- #
            if active_trade:
                active_trade.bars_held += 1
                exit_reason = None
                exit_price = None

                # Stop loss hit
                if active_trade.direction == "long" and bar_low <= active_trade.stop_loss:
                    exit_price = active_trade.stop_loss
                    exit_reason = "stop_loss"
                elif active_trade.direction == "short" and bar_high >= active_trade.stop_loss:
                    exit_price = active_trade.stop_loss
                    exit_reason = "stop_loss"

                # Take profit hit (skipped entirely in "let winners run" mode)
                if not exit_reason and not config.LET_WINNERS_RUN:
                    if active_trade.direction == "long" and bar_high >= active_trade.take_profit:
                        exit_price = active_trade.take_profit
                        exit_reason = "take_profit"
                    elif active_trade.direction == "short" and bar_low <= active_trade.take_profit:
                        exit_price = active_trade.take_profit
                        exit_reason = "take_profit"

                # Trailing stop check
                if not exit_reason and active_trade.trailing_stop:
                    if active_trade.direction == "long" and bar_low <= active_trade.trailing_stop:
                        exit_price = active_trade.trailing_stop
                        exit_reason = "trailing_stop"

                # Time stop: stagnant
                if not exit_reason and active_trade.bars_held >= config.TIME_STOP_STAGNANT_DAYS:
                    pct_move = abs(bar_close - active_trade.entry_price) / active_trade.entry_price * 100
                    if pct_move < 0.5:
                        exit_price = bar_close
                        exit_reason = "time_stop_stagnant"

                # Time stop: max hold (disabled when letting winners run)
                if (not exit_reason and not config.LET_WINNERS_RUN
                        and active_trade.bars_held >= config.TIME_STOP_MAX_HOLD_DAYS):
                    exit_price = bar_close
                    exit_reason = "time_stop_max_hold"

                # Strategy-specific exit for Connors RSI
                if not exit_reason and strategy == "connors_rsi":
                    sma5 = self.analyzer.calc_sma(close.iloc[:i + 1], period=5)
                    if not sma5.empty and bar_close > float(sma5.iloc[-1]):
                        exit_price = bar_close
                        exit_reason = "connors_exit_above_sma5"

                # Update trailing stop if in profit
                if not exit_reason and active_trade.direction == "long":
                    profit_per_share = bar_close - active_trade.entry_price
                    if active_trade.risk_per_share > 0:
                        r_curr = profit_per_share / active_trade.risk_per_share
                        if r_curr >= config.TRAILING_STOP_TRIGGER_R:
                            trail_pct = config.TRAILING_STOP_DEFAULTS.get(strategy, 2.0)
                            new_trail = bar_close * (1 - trail_pct / 100)
                            if active_trade.trailing_stop is None or new_trail > active_trade.trailing_stop:
                                active_trade.trailing_stop = new_trail

                if exit_reason and exit_price:
                    active_trade.exit_date = current_date
                    active_trade.exit_price = exit_price
                    active_trade.exit_reason = exit_reason
                    if active_trade.direction == "long":
                        active_trade.pnl = (exit_price - active_trade.entry_price) * active_trade.shares
                    else:
                        active_trade.pnl = (active_trade.entry_price - exit_price) * active_trade.shares
                    if active_trade.risk_per_share > 0:
                        active_trade.r_multiple = active_trade.pnl / (
                            active_trade.risk_per_share * active_trade.shares
                        )
                    trades.append(active_trade)
                    active_trade = None
                    continue

            # ---- Check entries (only if no active trade) ---- #
            if active_trade:
                continue

            # Run the strategy on data up to current bar
            window = df.iloc[:i + 1]

            # Regime filter
            if use_regime_filter:
                regime = self._detect_regime(vix_df, sp500_df, current_date)
                allowed = REGIME_STRATEGY_MAP.get(regime, REGIME_STRATEGY_MAP["UNKNOWN"])
                if strategy not in allowed:
                    continue

            signal = self._get_signal(strategy, ticker, window, vix_df, sp500_df, i)

            if signal and signal.get("setup"):
                current_atr = float(atr_series.iloc[i]) if i < len(atr_series) else bar_close * 0.02

                entry_price = bar_close
                direction = "long"

                # Calculate stop and target based on strategy
                stop_loss, take_profit = self._calc_stops(
                    strategy, signal, entry_price, current_atr, direction
                )

                # Position sizing (simplified for backtest)
                risk_per_share = abs(entry_price - stop_loss)
                if risk_per_share <= 0:
                    continue
                risk_dollars = equity * config.MAX_RISK_PER_TRADE
                shares = int(risk_dollars / risk_per_share)
                shares = max(shares, 1)
                max_shares = int(equity * config.MAX_SINGLE_POSITION / entry_price)
                shares = min(shares, max_shares)

                active_trade = Trade(
                    symbol=ticker,
                    strategy=strategy,
                    direction=direction,
                    entry_date=current_date,
                    entry_price=entry_price,
                    stop_loss=stop_loss,
                    take_profit=take_profit,
                    shares=shares,
                )

        # Close any open trade at the end
        if active_trade:
            active_trade.exit_date = str(df.index[-1].date())
            active_trade.exit_price = float(close.iloc[-1])
            active_trade.exit_reason = "backtest_end"
            if active_trade.direction == "long":
                active_trade.pnl = (active_trade.exit_price - active_trade.entry_price) * active_trade.shares
            else:
                active_trade.pnl = (active_trade.entry_price - active_trade.exit_price) * active_trade.shares
            if active_trade.risk_per_share > 0:
                active_trade.r_multiple = active_trade.pnl / (
                    active_trade.risk_per_share * active_trade.shares
                )
            trades.append(active_trade)

        return trades

    def _get_signal(
        self,
        strategy: str,
        ticker: str,
        window: pd.DataFrame,
        vix_df: pd.DataFrame,
        sp500_df: pd.DataFrame,
        bar_index: int,
    ) -> dict[str, Any] | None:
        """Get strategy signal for current bar."""
        if len(window) < 50:
            return None

        try:
            if strategy == "connors_rsi":
                return self.analyzer.strategy_connors_rsi(window)
            elif strategy == "macd_rsi":
                return self.analyzer.strategy_macd_rsi(window)
            elif strategy == "bollinger_squeeze":
                return self.analyzer.strategy_bollinger_squeeze(window)
            elif strategy == "ma_crossover":
                return self.analyzer.strategy_ma_crossover(window)
            elif strategy == "vix_fear":
                if ticker not in ("SPY", "QQQ"):
                    return None
                vix_data = self._get_vix_data_at(vix_df, bar_index)
                sp_window = sp500_df.iloc[:bar_index + 1] if not sp500_df.empty else pd.DataFrame()
                return self.analyzer.strategy_vix_fear(vix_data, sp_window)
        except Exception:
            pass
        return None

    def _calc_stops(
        self,
        strategy: str,
        signal: dict,
        entry: float,
        atr: float,
        direction: str,
    ) -> tuple[float, float]:
        """Calculate stop loss and take profit prices."""
        if strategy == "connors_rsi":
            stop = entry - 2 * atr
            target = signal.get("exit_target", entry + 3 * atr)
            if target and target > 0:
                return round(stop, 2), round(target, 2)
            return round(stop, 2), round(entry + 3 * atr, 2)

        elif strategy == "macd_rsi":
            stop = entry - 1.5 * atr
            target = entry + 3 * atr
            return round(stop, 2), round(target, 2)

        elif strategy == "bollinger_squeeze":
            stop = signal.get("stop_level", entry - 2 * atr)
            target = signal.get("exit_target", entry + 2.5 * atr)
            return round(stop, 2), round(target, 2)

        elif strategy == "ma_crossover":
            stop = entry - 1.5 * atr
            target = entry + 3 * atr
            return round(stop, 2), round(target, 2)

        elif strategy == "vix_fear":
            # SPY 3%, QQQ 4%
            stop = entry * 0.97
            target = entry * 1.06
            return round(stop, 2), round(target, 2)

        # Default
        stop = entry - 2 * atr
        target = entry + 4 * atr
        return round(stop, 2), round(target, 2)

    def _detect_regime(
        self, vix_df: pd.DataFrame, sp500_df: pd.DataFrame, date_str: str
    ) -> str:
        """Detect market regime at a given date."""
        try:
            date = pd.Timestamp(date_str)
            if vix_df.empty or sp500_df.empty:
                return "UNKNOWN"

            # Find closest date
            vix_close = vix_df["Close"]
            sp_close = sp500_df["Close"]

            vix_at = vix_close[vix_close.index <= date]
            sp_at = sp_close[sp_close.index <= date]

            if vix_at.empty or sp_at.empty or len(sp_at) < 2:
                return "UNKNOWN"

            vix_val = float(vix_at.iloc[-1])
            sp_change = (float(sp_at.iloc[-1]) - float(sp_at.iloc[-2])) / float(sp_at.iloc[-2]) * 100

            if vix_val < 22 and sp_change > 0:
                return "RISK-ON"
            elif vix_val > 28 or sp_change < -1:
                return "RISK-OFF"
            else:
                return "MIXED"
        except Exception:
            return "UNKNOWN"

    def _get_vix_data_at(self, vix_df: pd.DataFrame, bar_index: int) -> dict[str, Any]:
        """Get VIX data at a specific bar index."""
        if vix_df.empty or bar_index >= len(vix_df):
            return {"vix": None, "sma_10": None, "spike_pct": 0}

        close = vix_df["Close"].iloc[:bar_index + 1]
        if len(close) < 10:
            return {"vix": None, "sma_10": None, "spike_pct": 0}

        vix_current = float(close.iloc[-1])
        sma_10 = float(close.rolling(10).mean().iloc[-1])
        spike_pct = ((vix_current - sma_10) / sma_10 * 100) if sma_10 else 0

        return {
            "vix": round(vix_current, 2),
            "sma_10": round(sma_10, 2),
            "spike_pct": round(spike_pct, 2),
            "fear_signal": spike_pct >= 20,
        }

    # ------------------------------------------------------------------ #
    # Report Generation
    # ------------------------------------------------------------------ #
    def generate_report(self, result: BacktestResult) -> str:
        """Generate a markdown report for a backtest result."""
        lines = [
            f"# Backtest Report — {result.strategy}",
            f"",
            f"## Parameters",
            f"- **Strategy**: {result.strategy}",
            f"- **Tickers**: {', '.join(result.tickers)}",
            f"- **Period**: {result.start_date} to {result.end_date}",
            f"- **Initial Equity**: ${self.initial_equity:,.2f}",
            f"",
            f"## Performance Summary",
            f"| Metric | Value |",
            f"|--------|-------|",
            f"| Total Trades | {result.total_trades} |",
            f"| Win Rate | {result.win_rate:.1f}% |",
            f"| Average R | {result.avg_r:.2f}R |",
            f"| Profit Factor | {result.profit_factor:.2f} |",
            f"| Total P&L | ${result.total_pnl:,.2f} |",
            f"| Max Drawdown | {result.max_drawdown:.1f}% |",
            f"| Sharpe Ratio | {result.sharpe_ratio:.2f} |",
            f"| Avg Hold Days | {result.avg_hold_days:.1f} |",
            f"",
        ]

        # Exit reason breakdown
        exit_reasons: dict[str, int] = {}
        for t in result.trades:
            exit_reasons[t.exit_reason] = exit_reasons.get(t.exit_reason, 0) + 1

        lines.append("## Exit Reasons")
        lines.append("| Reason | Count | % |")
        lines.append("|--------|-------|---|")
        for reason, count in sorted(exit_reasons.items(), key=lambda x: -x[1]):
            pct = count / result.total_trades * 100 if result.total_trades else 0
            lines.append(f"| {reason} | {count} | {pct:.0f}% |")
        lines.append("")

        # Trade log
        lines.append("## Trade Log")
        lines.append("| # | Symbol | Entry | Exit | Entry$ | Exit$ | P&L | R | Reason | Bars |")
        lines.append("|---|--------|-------|------|--------|-------|-----|---|--------|------|")
        for i, t in enumerate(sorted(result.trades, key=lambda x: x.entry_date), 1):
            pnl_str = f"${t.pnl:+,.2f}"
            lines.append(
                f"| {i} | {t.symbol} | {t.entry_date} | {t.exit_date} "
                f"| ${t.entry_price:.2f} | ${t.exit_price:.2f} "
                f"| {pnl_str} | {t.r_multiple:+.2f}R "
                f"| {t.exit_reason} | {t.bars_held} |"
            )
        lines.append("")

        # Best and worst trades
        if result.trades:
            best = max(result.trades, key=lambda t: t.r_multiple)
            worst = min(result.trades, key=lambda t: t.r_multiple)
            lines.append("## Notable Trades")
            lines.append(
                f"- **Best**: {best.symbol} on {best.entry_date} — "
                f"{best.r_multiple:+.2f}R (${best.pnl:+,.2f})"
            )
            lines.append(
                f"- **Worst**: {worst.symbol} on {worst.entry_date} — "
                f"{worst.r_multiple:+.2f}R (${worst.pnl:+,.2f})"
            )

        return "\n".join(lines)

    def save_report(self, result: BacktestResult, report: str) -> Path:
        """Save a backtest report to the strategy directory."""
        report_dir = config.STRATEGY_PATH / "backtest-results"
        report_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{result.strategy}-{timestamp}.md"
        path = report_dir / filename
        path.write_text(report, encoding="utf-8")
        logger.info(f"Backtest report saved: {path}")
        return path
