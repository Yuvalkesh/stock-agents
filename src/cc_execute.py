"""Push an approved trade to the machine (Alpaca) — called by the wiki-analyzer
skill ONLY after the human approves a setup from the scan report.

Reuses TradeExecutor.place_entry, so it honors the live exit policy
(LET_WINNERS_RUN → market entry + trailing stop; else fixed bracket).

    python src/cc_execute.py --symbol AAPL --qty 8 --side buy \
        --stop 287.96 --target 309.11

Prints a JSON result. Paper account (config.ALPACA_PAPER).
"""

import argparse
import json

from trade_executor import TradeExecutor


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbol", required=True)
    ap.add_argument("--qty", type=int, required=True)
    ap.add_argument("--side", default="buy", choices=["buy", "sell"])
    ap.add_argument("--stop", type=float, required=True, help="stop-loss price")
    ap.add_argument("--target", type=float, required=True, help="take-profit price")
    args = ap.parse_args()

    ex = TradeExecutor()
    result = ex.place_entry(
        symbol=args.symbol.upper(),
        qty=args.qty,
        side=args.side,
        take_profit_price=args.target,
        stop_loss_price=args.stop,
    )
    # place_entry already attaches the trailing stop (LET_WINNERS_RUN) or the
    # bracket legs, so the position is protected on fill.
    print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
