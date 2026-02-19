"""Monitors open positions and updates portfolio files."""

import logging
from typing import Any

from trade_executor import TradeExecutor
from memory_logger import (
    update_positions_file,
    update_account_status,
    update_pending_orders,
    write_trade_journal_entry,
    update_strategy_performance,
    append_to_learning_log,
)

logger = logging.getLogger(__name__)


class PositionMonitor:
    """Monitors positions and detects closed trades."""

    def __init__(self, executor: TradeExecutor):
        self.executor = executor
        self._known_positions: dict[str, dict[str, Any]] = {}

    def update_portfolio_files(self) -> None:
        """Refresh all portfolio markdown files with live data."""
        account = self.executor.get_account()
        positions = self.executor.get_positions()
        orders = self.executor.get_open_orders()

        update_account_status(account)
        update_positions_file(positions)
        update_pending_orders(orders)

        logger.info(
            f"Portfolio updated: {len(positions)} positions, "
            f"equity=${account['equity']:,.2f}"
        )

    def register_trade_stop(self, symbol: str, stop_loss: float) -> None:
        """Store the stop_loss for a position so R-multiple uses actual risk."""
        if symbol in self._known_positions:
            self._known_positions[symbol]["stop_loss"] = stop_loss
        else:
            self._known_positions[symbol] = {"stop_loss": stop_loss}

    def check_for_closed_trades(self) -> list[dict[str, Any]]:
        """
        Compare current positions to known positions.
        If a position disappeared, it was closed (stop/target hit).
        """
        current_positions = self.executor.get_positions()
        current_symbols = {p["symbol"] for p in current_positions}

        closed_trades: list[dict[str, Any]] = []

        for symbol, known in list(self._known_positions.items()):
            if symbol not in current_symbols:
                # Position was closed
                logger.info(f"Position closed: {symbol}")
                closed_trades.append({
                    "symbol": symbol,
                    "entry_price": known.get("avg_entry_price", 0),
                    "shares": known.get("qty", 0),
                    "direction": known.get("side", "long"),
                    "strategy": known.get("strategy", "unknown"),
                    "entry_date": known.get("entry_date", "unknown"),
                    "stop_loss": known.get("stop_loss", 0),
                })
                del self._known_positions[symbol]

        # Update known positions (preserve stop_loss if already stored)
        for pos in current_positions:
            if pos["symbol"] not in self._known_positions:
                self._known_positions[pos["symbol"]] = pos

        return closed_trades

    def process_closed_trade(self, trade: dict[str, Any]) -> None:
        """Process a closed trade: log journal entry, update strategy performance."""
        from datetime import datetime
        from data_fetcher import DataFetcher

        symbol = trade["symbol"]
        fetcher = DataFetcher()
        current_price = fetcher.fetch_current_price(symbol)

        if current_price is None:
            logger.warning(f"Could not fetch exit price for {symbol}")
            current_price = trade.get("entry_price", 0)

        entry_price = trade["entry_price"]
        shares = trade["shares"]
        direction = trade["direction"]

        # Calculate P&L
        if direction.lower() in ("long", "buy"):
            pnl = (current_price - entry_price) * shares
        else:
            pnl = (entry_price - current_price) * shares

        # Calculate R-multiple using actual stop distance from bracket order
        stop_loss = trade.get("stop_loss", 0)
        if stop_loss and stop_loss > 0:
            risk_per_share = abs(entry_price - stop_loss)
        else:
            risk_per_share = entry_price * 0.01  # Fallback: 1% estimate
        r_multiple = pnl / (risk_per_share * shares) if risk_per_share * shares > 0 else 0

        trade_data = {
            "symbol": symbol,
            "direction": direction,
            "strategy": trade.get("strategy", "unknown"),
            "entry_date": trade.get("entry_date", datetime.now().strftime("%Y-%m-%d")),
            "exit_date": datetime.now().strftime("%Y-%m-%d"),
            "entry_price": entry_price,
            "exit_price": current_price,
            "shares": shares,
            "pnl": pnl,
            "r_multiple": r_multiple,
            "exit_reason": "bracket_order_filled",
            "thesis": trade.get("thesis", ""),
        }

        # Write trade journal
        write_trade_journal_entry(trade_data)

        # Update strategy performance
        strategy = trade.get("strategy", "unknown")
        if strategy != "unknown":
            update_strategy_performance(strategy, trade_data)

        # Update learning log
        result = "WIN" if pnl > 0 else "LOSS"
        append_to_learning_log(
            f"**{result}**: {symbol} {direction} via {strategy} — "
            f"P&L: ${pnl:.2f} ({r_multiple:.2f}R)"
        )

        logger.info(
            f"Post-mortem complete: {symbol} {direction} — "
            f"P&L: ${pnl:.2f} ({r_multiple:.2f}R)"
        )

    def run_monitor_cycle(self) -> None:
        """Run a full monitor cycle: update files + check for closed trades."""
        self.update_portfolio_files()
        closed = self.check_for_closed_trades()
        for trade in closed:
            self.process_closed_trade(trade)
