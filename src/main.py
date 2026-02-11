"""
Stock Trading Multi-Agent System — Main Orchestrator

Runs the full 5-agent pipeline with loop-back mechanism.
Modes: scan, execute, monitor, review, full, scout
"""

import argparse
import logging
import sys
from datetime import datetime
from typing import Any

from config import MAX_LOOPBACKS, DEFAULT_WATCHLIST
from data_fetcher import DataFetcher
from technical_analysis import TechnicalAnalyzer
from agent_runner import (
    run_agent_1,
    run_agent_2,
    run_agent_3,
    run_agent_4,
    run_agent_5,
    parse_gatekeeper_verdict,
    parse_agent1_decision,
)
from trade_executor import TradeExecutor
from position_monitor import PositionMonitor
from memory_logger import (
    save_agent_output,
    save_rejected_trade,
    save_scan_output,
    update_positions_file,
    update_account_status,
    update_pending_orders,
    append_to_learning_log,
)
from performance_analyzer import generate_monthly_review
from email_notifier import (
    send_morning_report,
    send_trade_executed_alert,
    send_end_of_day_report,
    send_rising_stars_report,
)

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


class TradingOrchestrator:
    """Orchestrates the full multi-agent trading pipeline."""

    def __init__(self):
        self.fetcher = DataFetcher()
        self.analyzer = TechnicalAnalyzer()
        self.executor = TradeExecutor()
        self.monitor = PositionMonitor(self.executor)
        self.date_str = datetime.now().strftime("%Y-%m-%d")

    # ------------------------------------------------------------------ #
    # Mode: SCAN — Morning scan + full agent pipeline
    # ------------------------------------------------------------------ #
    def run_scan(self) -> dict[str, Any]:
        """Run the full scan pipeline: fetch data → 5 agents → decisions."""
        logger.info(f"=== MORNING SCAN — {self.date_str} ===")

        # Step 0: Fetch all data
        logger.info("Step 0: Fetching data...")
        data = self.fetcher.fetch_all()

        # Get account info for sizing
        account = self.executor.get_account()
        equity = account["equity"]

        # Update portfolio files
        self.monitor.update_portfolio_files()

        # ---------------------------------------------------------- #
        # Step 1: Agent 1 — Head of Investment
        # ---------------------------------------------------------- #
        logger.info("Step 1: Running Agent 1 (Head of Investment)...")
        from vault_reader import read_portfolio_positions
        portfolio = read_portfolio_positions()

        agent1_output = run_agent_1(
            news=data["news"],
            general_news=data["general_news"],
            macro=data["macro"],
            earnings=data["earnings"],
            portfolio=portfolio,
            date_str=self.date_str,
        )
        save_agent_output(self.date_str, 1, agent1_output)
        logger.info("Agent 1 complete.")

        # Parse Agent 1 decision
        agent1_decision = parse_agent1_decision(agent1_output)
        if not agent1_decision["proceed"]:
            logger.info("Agent 1 says STAND DOWN. No trades today.")
            append_to_learning_log(
                f"**STAND DOWN**: Agent 1 recommended no trading on {self.date_str}. "
                f"Macro regime: {data['macro'].get('regime', 'UNKNOWN')}"
            )
            return {"status": "stand_down", "reason": "Agent 1 STAND DOWN"}

        tickers = agent1_decision["tickers"]
        if not tickers:
            tickers = DEFAULT_WATCHLIST[:5]
        logger.info(f"Agent 1 selected tickers: {tickers}")

        # ---------------------------------------------------------- #
        # Step 2: Agent 2 — Stock Analyst
        # ---------------------------------------------------------- #
        logger.info("Step 2: Running technical analysis + Agent 2...")

        # Fetch OHLCV and run technical analysis
        ticker_analyses = {}
        sp500_df = self.fetcher.fetch_ohlcv("^GSPC", period="1y")

        for ticker in tickers:
            df = self.fetcher.fetch_ohlcv(ticker, period="1y")
            if df.empty:
                logger.warning(f"No data for {ticker}, skipping")
                continue
            analysis = self.analyzer.analyze_ticker(
                ticker, df,
                vix_data=data["vix_data"],
                sp500_df=sp500_df,
            )
            ticker_analyses[ticker] = analysis

        if not ticker_analyses:
            logger.warning("No ticker data available. Aborting scan.")
            return {"status": "error", "reason": "No ticker data"}

        agent2_output = run_agent_2(ticker_analyses, self.date_str)
        save_agent_output(self.date_str, 2, agent2_output)
        logger.info("Agent 2 complete.")

        # Filter to tickers with confirmed setups
        confirmed_tickers = {
            t: a for t, a in ticker_analyses.items() if a.get("has_setup")
        }
        if not confirmed_tickers:
            logger.info("No setups confirmed by technical analysis. Done.")
            return {"status": "no_setups", "tickers_analyzed": len(ticker_analyses)}

        logger.info(
            f"Confirmed setups: {list(confirmed_tickers.keys())}"
        )

        # ---------------------------------------------------------- #
        # Step 3: Agent 3 — Data Merger
        # ---------------------------------------------------------- #
        logger.info("Step 3: Running Agent 3 (Data Merger)...")
        agent3_output = run_agent_3(
            agent1_output, agent2_output, equity, self.date_str
        )
        save_agent_output(self.date_str, 3, agent3_output)
        logger.info("Agent 3 complete.")

        # ---------------------------------------------------------- #
        # Step 4 + 5: Agent 4 (Decision) + Agent 5 (Gatekeeper) with loop-backs
        # ---------------------------------------------------------- #
        return self._run_decision_loop(
            agent3_output, account, data, self.date_str
        )

    def _run_decision_loop(
        self,
        agent3_output: str,
        account: dict[str, Any],
        data: dict[str, Any],
        date_str: str,
    ) -> dict[str, Any]:
        """Run Agent 4 → Agent 5 with loop-back mechanism."""
        loopback_count = 0
        loopback_instructions = ""
        approved_trades: list[dict[str, Any]] = []

        while loopback_count <= MAX_LOOPBACKS:
            # ---- Agent 4: Swing Trader MegaBot ---- #
            logger.info(
                f"Step 4: Running Agent 4 (MegaBot) "
                f"[loop {loopback_count}]..."
            )
            agent4_output = run_agent_4(
                agent3_output, date_str, loopback_instructions
            )
            save_agent_output(date_str, 4, agent4_output)

            # Check if Agent 4 says PASS
            if "DECISION: PASS" in agent4_output.upper() or (
                "PASS" in agent4_output.upper()
                and "BUY" not in agent4_output.upper()
                and "SHORT" not in agent4_output.upper()
            ):
                logger.info("Agent 4 says PASS. No trade.")
                save_rejected_trade(
                    date_str, "ALL",
                    f"# Rejected by Agent 4 (MegaBot)\n\n{agent4_output}"
                )
                return {"status": "pass", "reason": "Agent 4 PASS"}

            # ---- Agent 5: Gatekeeper Boss ---- #
            logger.info(
                f"Step 5: Running Agent 5 (Gatekeeper) "
                f"[loop {loopback_count}]..."
            )
            positions = self.executor.get_positions()
            total_exposure = self.executor.get_total_exposure()

            agent5_output = run_agent_5(
                agent4_output=agent4_output,
                account_equity=account["equity"],
                daily_pnl_pct=account["daily_pnl_pct"],
                monthly_drawdown_pct=0,  # TODO: track monthly drawdown
                open_positions_count=len(positions),
                total_exposure_pct=total_exposure,
                date_str=date_str,
            )
            save_agent_output(date_str, 5, agent5_output)

            # Parse verdict
            verdict = parse_gatekeeper_verdict(agent5_output)

            if verdict["go"]:
                logger.info("Gatekeeper says GO! Trade approved.")
                trade_params = TradeExecutor.parse_trade_params(agent5_output)
                if trade_params:
                    approved_trades.append(trade_params)
                else:
                    logger.warning("Could not parse trade params from GO verdict")
                break

            elif verdict["fixable"] and loopback_count < MAX_LOOPBACKS:
                loopback_count += 1
                loopback_instructions = (
                    f"The Gatekeeper (Agent 5) rejected this trade. "
                    f"Loop {loopback_count}/{MAX_LOOPBACKS}.\n\n"
                    f"Gatekeeper feedback:\n{agent5_output}\n\n"
                    f"Please address the specific concerns and re-evaluate."
                )
                logger.info(
                    f"Gatekeeper NO-GO (fixable). Looping back "
                    f"({loopback_count}/{MAX_LOOPBACKS})..."
                )

            else:
                logger.info("Gatekeeper NO-GO (killed). Trade rejected.")
                save_rejected_trade(
                    date_str, "ALL",
                    f"# Rejected by Gatekeeper\n\n"
                    f"## Agent 4 Decision\n{agent4_output}\n\n"
                    f"## Gatekeeper Verdict\n{agent5_output}"
                )
                return {"status": "rejected", "reason": "Gatekeeper NO-GO"}

        # Save approved trades for execution
        if approved_trades:
            trades_summary = "\n".join(
                f"- {t['symbol']} {t['side'].upper()} {t['qty']} shares "
                f"(stop: ${t['stop_loss']}, target: ${t['take_profit']})"
                for t in approved_trades
            )
            save_scan_output(
                date_str,
                f"# Approved Trades — {date_str}\n\n{trades_summary}"
            )
            return {"status": "approved", "trades": approved_trades}

        return {"status": "no_trades"}

    # ------------------------------------------------------------------ #
    # Mode: EXECUTE — Execute approved trades
    # ------------------------------------------------------------------ #
    def run_execute(self) -> dict[str, Any]:
        """Execute any approved trades from the scan."""
        logger.info(f"=== EXECUTE MODE — {self.date_str} ===")

        # Read the scan output for today
        from vault_reader import get_scan_output_dir
        scan_dir = get_scan_output_dir(self.date_str)
        scan_file = scan_dir / "daily-scan.md"

        if not scan_file.exists():
            logger.info("No scan output found. Running scan first...")
            scan_result = self.run_scan()
            if scan_result.get("status") != "approved":
                return {"status": "no_trades", "scan_result": scan_result}
            approved_trades = scan_result.get("trades", [])
        else:
            # Parse approved trades from scan output
            # In practice, we'd store these as JSON; for now, re-run scan
            logger.info("Scan output exists. Running full pipeline...")
            scan_result = self.run_scan()
            if scan_result.get("status") != "approved":
                return {"status": "no_trades", "scan_result": scan_result}
            approved_trades = scan_result.get("trades", [])

        results = []
        for trade in approved_trades:
            logger.info(
                f"Executing: {trade['side'].upper()} {trade['qty']} "
                f"{trade['symbol']}"
            )
            result = self.executor.place_bracket_order(
                symbol=trade["symbol"],
                qty=trade["qty"],
                side=trade["side"],
                take_profit_price=trade["take_profit"],
                stop_loss_price=trade["stop_loss"],
            )
            results.append(result)

            if result["success"]:
                logger.info(f"Order placed: {result['order_id']}")
            else:
                logger.error(f"Order failed: {result.get('error')}")

        # Update portfolio files
        self.monitor.update_portfolio_files()

        return {"status": "executed", "results": results}

    # ------------------------------------------------------------------ #
    # Mode: MONITOR — Check positions
    # ------------------------------------------------------------------ #
    def run_monitor(self) -> dict[str, Any]:
        """Run position monitoring cycle."""
        logger.info(f"=== MONITOR MODE — {self.date_str} ===")
        self.monitor.run_monitor_cycle()
        return {"status": "monitored"}

    # ------------------------------------------------------------------ #
    # Mode: REVIEW — Post-market review
    # ------------------------------------------------------------------ #
    def run_review(self) -> dict[str, Any]:
        """Run post-market review."""
        logger.info(f"=== REVIEW MODE — {self.date_str} ===")

        # Update portfolio
        self.monitor.run_monitor_cycle()

        # Check if end of month
        now = datetime.now()
        import calendar
        _, last_day = calendar.monthrange(now.year, now.month)
        if now.day >= last_day - 1:  # Last 2 days of month
            logger.info("End of month — generating monthly review...")
            generate_monthly_review(now.year, now.month)

        return {"status": "reviewed"}

    # ------------------------------------------------------------------ #
    # Mode: FULL — Run everything in sequence
    # ------------------------------------------------------------------ #
    def run_full(self) -> dict[str, Any]:
        """Run scan → execute → monitor → review."""
        scan_result = self.run_scan()
        if scan_result.get("status") == "approved":
            exec_result = self.run_execute()
        else:
            exec_result = {"status": "skipped"}
        monitor_result = self.run_monitor()
        review_result = self.run_review()

        return {
            "scan": scan_result,
            "execute": exec_result,
            "monitor": monitor_result,
            "review": review_result,
        }


# ------------------------------------------------------------------ #
# Determine mode from schedule
# ------------------------------------------------------------------ #
def get_mode_from_schedule() -> str:
    """Determine which mode to run based on current time (EST)."""
    from datetime import timezone, timedelta
    est = timezone(timedelta(hours=-5))
    now = datetime.now(est)
    hour, minute = now.hour, now.minute

    if hour < 7:
        return "scan"
    elif hour == 9 and minute <= 35:
        return "execute"
    elif 10 <= hour <= 15:
        return "monitor"
    elif hour >= 16:
        return "review"
    else:
        return "scan"


# ------------------------------------------------------------------ #
# Main
# ------------------------------------------------------------------ #
def main():
    parser = argparse.ArgumentParser(
        description="Stock Trading Multi-Agent System"
    )
    parser.add_argument(
        "--mode",
        choices=["scan", "execute", "monitor", "review", "full", "scout", "scheduled", "manual"],
        default="full",
        help="Pipeline mode to run",
    )
    args = parser.parse_args()

    mode = args.mode
    if mode == "scheduled":
        mode = get_mode_from_schedule()
        logger.info(f"Scheduled mode resolved to: {mode}")
    elif mode == "manual":
        mode = "full"

    orchestrator = TradingOrchestrator()

    date_str = datetime.now().strftime("%Y-%m-%d")

    try:
        if mode == "scout":
            from rising_stars_scanner import run_rising_stars_scan
            results = run_rising_stars_scan()
            result = {"status": "scouted", "found": len(results)}
            send_rising_stars_report(date_str, results)

        elif mode == "scan":
            # Run rising stars scout on Mondays
            if datetime.now().weekday() == 0:  # Monday
                from rising_stars_scanner import run_rising_stars_scan
                logger.info("Monday — running Rising Stars Scout...")
                scout_results = run_rising_stars_scan()
                send_rising_stars_report(date_str, scout_results)
            result = orchestrator.run_scan()
            send_morning_report(date_str, result)

        elif mode == "execute":
            result = orchestrator.run_execute()
            exec_results = result.get("results", [])
            if exec_results:
                send_trade_executed_alert(date_str, exec_results)

        elif mode == "monitor":
            result = orchestrator.run_monitor()

        elif mode == "review":
            result = orchestrator.run_review()
            send_end_of_day_report(date_str)

        elif mode == "full":
            # Run rising stars scout on Mondays
            if datetime.now().weekday() == 0:  # Monday
                from rising_stars_scanner import run_rising_stars_scan
                logger.info("Monday — running Rising Stars Scout...")
                scout_results = run_rising_stars_scan()
                send_rising_stars_report(date_str, scout_results)
            result = orchestrator.run_full()
            send_morning_report(date_str, result.get("scan", {}))
            exec_results = result.get("execute", {}).get("results", [])
            if exec_results:
                send_trade_executed_alert(date_str, exec_results)
            send_end_of_day_report(date_str)
        else:
            result = orchestrator.run_full()

        logger.info(f"Pipeline complete. Result: {result.get('status', 'unknown')}")

    except Exception as e:
        logger.error(f"Pipeline error: {e}", exc_info=True)
        append_to_learning_log(f"**ERROR**: Pipeline failed on {datetime.now()}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
