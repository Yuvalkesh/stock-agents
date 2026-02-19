"""Executes trades on Alpaca using bracket orders."""

import logging
import re
from typing import Any

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import (
    MarketOrderRequest,
    StopLossRequest,
    TakeProfitRequest,
)
from alpaca.trading.enums import OrderSide, TimeInForce, OrderClass
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

import config

logger = logging.getLogger(__name__)


class TradeExecutor:
    """Handles all Alpaca trading operations."""

    def __init__(self):
        self.trading_client = TradingClient(
            config.ALPACA_API_KEY,
            config.ALPACA_SECRET_KEY,
            paper=config.ALPACA_PAPER,
        )
        self.data_client = StockHistoricalDataClient(
            config.ALPACA_API_KEY,
            config.ALPACA_SECRET_KEY,
        )

    # ------------------------------------------------------------------ #
    # Account Info
    # ------------------------------------------------------------------ #
    def get_account(self) -> dict[str, Any]:
        """Get current account information."""
        try:
            account = self.trading_client.get_account()
            return {
                "equity": float(account.equity),
                "cash": float(account.cash),
                "buying_power": float(account.buying_power),
                "portfolio_value": float(account.portfolio_value),
                "daily_pnl": float(account.equity) - float(account.last_equity),
                "daily_pnl_pct": (
                    (float(account.equity) - float(account.last_equity))
                    / float(account.last_equity)
                    * 100
                    if float(account.last_equity) > 0
                    else 0
                ),
            }
        except Exception as e:
            logger.error(f"Error getting account: {e}")
            return {
                "equity": 100000,
                "cash": 100000,
                "buying_power": 100000,
                "portfolio_value": 100000,
                "daily_pnl": 0,
                "daily_pnl_pct": 0,
            }

    # ------------------------------------------------------------------ #
    # Positions
    # ------------------------------------------------------------------ #
    def get_positions(self) -> list[dict[str, Any]]:
        """Get all current positions."""
        try:
            positions = self.trading_client.get_all_positions()
            return [
                {
                    "symbol": pos.symbol,
                    "qty": float(pos.qty),
                    "side": pos.side,
                    "avg_entry_price": float(pos.avg_entry_price),
                    "current_price": float(pos.current_price),
                    "unrealized_pl": float(pos.unrealized_pl),
                    "unrealized_plpc": float(pos.unrealized_plpc) * 100,
                    "market_value": float(pos.market_value),
                }
                for pos in positions
            ]
        except Exception as e:
            logger.error(f"Error getting positions: {e}")
            return []

    def get_total_exposure(self) -> float:
        """Get total exposure as percentage of equity."""
        account = self.get_account()
        positions = self.get_positions()
        total_value = sum(abs(p["market_value"]) for p in positions)
        equity = account["equity"]
        return (total_value / equity * 100) if equity > 0 else 0

    # ------------------------------------------------------------------ #
    # Order Placement
    # ------------------------------------------------------------------ #
    def place_bracket_order(
        self,
        symbol: str,
        qty: int,
        side: str,
        take_profit_price: float,
        stop_loss_price: float,
    ) -> dict[str, Any]:
        """
        Place a bracket order (market entry + stop loss + take profit).
        This is the primary order type for the system.
        """
        if qty <= 0:
            return {"success": False, "error": "Invalid quantity"}

        try:
            order_side = OrderSide.BUY if side.lower() == "buy" else OrderSide.SELL
            take_profit_price = round(take_profit_price, 2)
            stop_loss_price = round(stop_loss_price, 2)

            order_request = MarketOrderRequest(
                symbol=symbol,
                qty=qty,
                side=order_side,
                time_in_force=TimeInForce.DAY,
                order_class=OrderClass.BRACKET,
                take_profit=TakeProfitRequest(limit_price=take_profit_price),
                stop_loss=StopLossRequest(stop_price=stop_loss_price),
            )

            order = self.trading_client.submit_order(order_request)

            logger.info(
                f"BRACKET ORDER: {side.upper()} {qty} {symbol} | "
                f"Stop: ${stop_loss_price} | Target: ${take_profit_price}"
            )

            # Validate bracket order has all legs (stop + target)
            try:
                order_detail = self.trading_client.get_order_by_id(order.id)
                legs = order_detail.legs or []
                if len(legs) < 2:
                    logger.error(
                        f"BRACKET INCOMPLETE: {symbol} — only {len(legs)} legs "
                        f"(expected 2: stop + target). Cancelling order."
                    )
                    self.cancel_order(str(order.id))
                    return {
                        "success": False,
                        "error": f"Bracket order incomplete — {len(legs)}/2 legs confirmed",
                    }
                logger.info(
                    f"Bracket validated: {symbol} — {len(legs)} legs confirmed"
                )
            except Exception as val_err:
                logger.warning(
                    f"Could not validate bracket legs for {symbol}: {val_err}. "
                    f"Order submitted but legs unverified."
                )

            return {
                "success": True,
                "order_id": str(order.id),
                "symbol": symbol,
                "qty": qty,
                "side": side,
                "status": str(order.status),
                "take_profit_price": take_profit_price,
                "stop_loss_price": stop_loss_price,
            }

        except Exception as e:
            logger.error(f"Error placing bracket order for {symbol}: {e}")
            return {"success": False, "error": str(e)}

    # ------------------------------------------------------------------ #
    # Close Position
    # ------------------------------------------------------------------ #
    def close_position(self, symbol: str) -> dict[str, Any]:
        """Close an entire position for a symbol."""
        try:
            self.trading_client.close_position(symbol)
            logger.info(f"CLOSED position: {symbol}")
            return {"success": True, "symbol": symbol}
        except Exception as e:
            logger.error(f"Error closing {symbol}: {e}")
            return {"success": False, "error": str(e)}

    # ------------------------------------------------------------------ #
    # Orders
    # ------------------------------------------------------------------ #
    def get_open_orders(self) -> list[dict[str, Any]]:
        """Get all open/pending orders."""
        try:
            orders = self.trading_client.get_orders()
            return [
                {
                    "id": str(o.id),
                    "symbol": o.symbol,
                    "qty": float(o.qty),
                    "side": str(o.side),
                    "type": str(o.type),
                    "status": str(o.status),
                    "submitted_at": str(o.submitted_at),
                }
                for o in orders
            ]
        except Exception as e:
            logger.error(f"Error getting orders: {e}")
            return []

    def cancel_order(self, order_id: str) -> bool:
        """Cancel a specific order."""
        try:
            self.trading_client.cancel_order_by_id(order_id)
            logger.info(f"CANCELLED order: {order_id}")
            return True
        except Exception as e:
            logger.error(f"Error cancelling order {order_id}: {e}")
            return False

    # ------------------------------------------------------------------ #
    # Market Status
    # ------------------------------------------------------------------ #
    def is_market_open(self) -> bool:
        """Check if the market is currently open."""
        try:
            clock = self.trading_client.get_clock()
            return clock.is_open
        except Exception as e:
            logger.error(f"Error checking market status: {e}")
            return False

    # ------------------------------------------------------------------ #
    # Parse Trade Parameters from Agent Output
    # ------------------------------------------------------------------ #
    @staticmethod
    def parse_trade_params(gatekeeper_output: str) -> dict[str, Any] | None:
        """Extract trade parameters from Gatekeeper GO output."""
        text = gatekeeper_output
        params: dict[str, Any] = {}

        # Extract symbol
        symbol_match = re.search(r"Symbol:\s*(\w+)", text)
        if symbol_match:
            params["symbol"] = symbol_match.group(1)

        # Extract direction
        dir_match = re.search(r"Direction:\s*(LONG|SHORT|BUY|SELL)", text, re.IGNORECASE)
        if dir_match:
            direction = dir_match.group(1).upper()
            params["side"] = "buy" if direction in ("LONG", "BUY") else "sell"

        # Extract entry price
        entry_match = re.search(r"Entry:\s*\$?([\d,.]+)", text)
        if entry_match:
            params["entry_price"] = float(entry_match.group(1).replace(",", ""))

        # Extract stop price
        stop_match = re.search(r"Stop(?:\s*Loss)?:\s*\$?([\d,.]+)", text)
        if stop_match:
            params["stop_loss"] = float(stop_match.group(1).replace(",", ""))

        # Extract target price
        target_match = re.search(r"Target:\s*\$?([\d,.]+)", text)
        if target_match:
            params["take_profit"] = float(target_match.group(1).replace(",", ""))

        # Extract shares
        shares_match = re.search(r"Shares:\s*(\d+)", text)
        if shares_match:
            params["qty"] = int(shares_match.group(1))

        # Validate we have all required fields
        required = ["symbol", "side", "stop_loss", "take_profit", "qty"]
        if all(k in params for k in required):
            return params

        logger.warning(f"Could not parse all trade params. Got: {list(params.keys())}")
        return None
