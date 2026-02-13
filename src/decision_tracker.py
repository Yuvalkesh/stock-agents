"""Tracks every trade decision and reviews them in hindsight.

Saves a structured record every time a trade is passed or rejected.
Before each morning scan, reviews past decisions by checking what
actually happened to the price, then updates the learning log.
"""

import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

import yfinance as yf

from config import MEMORY_PATH
from memory_logger import append_to_learning_log

logger = logging.getLogger(__name__)

DECISION_LOG_PATH = MEMORY_PATH / "decision-log.json"

# How many trading days to wait before reviewing a decision
REVIEW_AFTER_DAYS = 5


def _load_decisions() -> list[dict[str, Any]]:
    """Load the decision log from disk."""
    if not DECISION_LOG_PATH.exists():
        return []
    try:
        return json.loads(DECISION_LOG_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, Exception) as e:
        logger.error(f"Error reading decision log: {e}")
        return []


def _save_decisions(decisions: list[dict[str, Any]]) -> None:
    """Write the decision log to disk."""
    DECISION_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    DECISION_LOG_PATH.write_text(
        json.dumps(decisions, indent=2), encoding="utf-8"
    )


def log_decision(
    date_str: str,
    ticker: str,
    strategy: str,
    entry_price: float,
    stop_loss: float,
    take_profit: float,
    decision: str,
    reason: str,
    score: int | None = None,
) -> None:
    """Record a trade decision (pass, rejected, stand_down, no_setups).

    Called every time the pipeline decides NOT to trade.
    """
    decisions = _load_decisions()

    record = {
        "date": date_str,
        "ticker": ticker,
        "strategy": strategy,
        "entry_price": entry_price,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "decision": decision,
        "reason": reason,
        "score": score,
        "reviewed": False,
        "review_result": None,
    }

    decisions.append(record)
    _save_decisions(decisions)
    logger.info(f"Decision logged: {decision} on {ticker} ({strategy}) — {reason}")


def review_past_decisions(fetcher=None) -> list[dict[str, Any]]:
    """Review unreviewed decisions that are old enough.

    Fetches the current price for each ticker and evaluates whether
    the skipped trade would have been profitable.

    Returns a list of review findings.
    """
    decisions = _load_decisions()
    if not decisions:
        return []

    cutoff = (datetime.now() - timedelta(days=REVIEW_AFTER_DAYS)).strftime("%Y-%m-%d")
    to_review = [
        d for d in decisions
        if not d.get("reviewed") and d["date"] <= cutoff and d["ticker"] != "ALL"
    ]

    if not to_review:
        logger.info("No past decisions ready for review yet.")
        return []

    logger.info(f"Reviewing {len(to_review)} past decisions...")
    findings = []

    for record in to_review:
        ticker = record["ticker"]
        entry = record["entry_price"]
        stop = record["stop_loss"]
        target = record["take_profit"]

        if not entry or entry <= 0:
            record["reviewed"] = True
            record["review_result"] = "skipped — no entry price"
            continue

        try:
            # Fetch price history since the decision date
            df = yf.download(
                ticker, start=record["date"], interval="1d", progress=False
            )
            if hasattr(df.columns, "levels"):
                df.columns = df.columns.get_level_values(0)

            if df.empty or len(df) < 2:
                continue  # Not enough data yet

            # Check what happened after the decision
            high_since = float(df["High"].max())
            low_since = float(df["Low"].min())
            current_price = float(df["Close"].iloc[-1])
            days_elapsed = len(df)

            hit_target = high_since >= target if target > entry else low_since <= target
            hit_stop = low_since <= stop if stop < entry else high_since >= stop

            # Determine outcome
            if hit_target and not hit_stop:
                outcome = "MISSED_WIN"
                pnl_pct = round((target - entry) / entry * 100, 2)
                verdict = (
                    f"MISSED OPPORTUNITY: {ticker} reached target ${target:.2f} "
                    f"(+{pnl_pct}%) within {days_elapsed} days. "
                    f"We passed because: {record['reason']}. "
                    f"Strategy: {record['strategy']}. "
                    f"LESSON: This type of pass was WRONG — consider loosening "
                    f"criteria for {record['strategy']} setups."
                )
            elif hit_stop and not hit_target:
                outcome = "GOOD_PASS"
                pnl_pct = round((stop - entry) / entry * 100, 2)
                verdict = (
                    f"GOOD CALL: {ticker} hit stop ${stop:.2f} ({pnl_pct}%) "
                    f"within {days_elapsed} days. We correctly passed. "
                    f"Reason: {record['reason']}. "
                    f"Strategy: {record['strategy']}. "
                    f"LESSON: This type of pass was CORRECT — keep applying "
                    f"this filter."
                )
            elif hit_target and hit_stop:
                # Both hit — check which came first
                target_day = None
                stop_day = None
                for i in range(len(df)):
                    if target_day is None and float(df["High"].iloc[i]) >= target:
                        target_day = i
                    if stop_day is None and float(df["Low"].iloc[i]) <= stop:
                        stop_day = i

                if stop_day is not None and (target_day is None or stop_day < target_day):
                    outcome = "GOOD_PASS"
                    pnl_pct = round((stop - entry) / entry * 100, 2)
                    verdict = (
                        f"GOOD CALL: {ticker} hit stop first on day {stop_day + 1}, "
                        f"then later recovered. We correctly passed. "
                        f"Strategy: {record['strategy']}."
                    )
                else:
                    outcome = "MISSED_WIN"
                    pnl_pct = round((target - entry) / entry * 100, 2)
                    verdict = (
                        f"MISSED OPPORTUNITY: {ticker} hit target first on day "
                        f"{(target_day or 0) + 1} (+{pnl_pct}%). "
                        f"We passed because: {record['reason']}. "
                        f"Strategy: {record['strategy']}. "
                        f"LESSON: This filter was too strict."
                    )
            else:
                # Neither hit — evaluate based on current price
                move_pct = round((current_price - entry) / entry * 100, 2)
                if move_pct > 1:
                    outcome = "MISSED_PARTIAL"
                    verdict = (
                        f"PARTIAL MISS: {ticker} is at ${current_price:.2f} "
                        f"({move_pct:+.2f}% from entry) after {days_elapsed} days. "
                        f"Hasn't hit target (${target:.2f}) or stop (${stop:.2f}) yet. "
                        f"We passed because: {record['reason']}. "
                        f"Strategy: {record['strategy']}."
                    )
                elif move_pct < -1:
                    outcome = "GOOD_PASS"
                    verdict = (
                        f"GOOD CALL: {ticker} dropped to ${current_price:.2f} "
                        f"({move_pct:+.2f}%) after {days_elapsed} days. "
                        f"We correctly passed. Strategy: {record['strategy']}."
                    )
                else:
                    outcome = "NEUTRAL"
                    verdict = (
                        f"NEUTRAL: {ticker} is flat at ${current_price:.2f} "
                        f"({move_pct:+.2f}%) after {days_elapsed} days. "
                        f"Strategy: {record['strategy']}."
                    )

            record["reviewed"] = True
            record["review_result"] = outcome
            record["review_details"] = {
                "current_price": current_price,
                "high_since": high_since,
                "low_since": low_since,
                "days_elapsed": days_elapsed,
                "hit_target": hit_target,
                "hit_stop": hit_stop,
            }

            findings.append({
                "record": record,
                "outcome": outcome,
                "verdict": verdict,
            })

            # Write to learning log
            append_to_learning_log(f"**HINDSIGHT REVIEW ({outcome})**: {verdict}")
            logger.info(f"Reviewed {ticker} ({record['date']}): {outcome}")

        except Exception as e:
            logger.error(f"Error reviewing {ticker}: {e}")
            continue

    # Save updated decisions
    _save_decisions(decisions)

    # Log summary
    if findings:
        missed = sum(1 for f in findings if f["outcome"] == "MISSED_WIN")
        good = sum(1 for f in findings if f["outcome"] == "GOOD_PASS")
        logger.info(
            f"Review complete: {len(findings)} decisions reviewed — "
            f"{missed} missed opportunities, {good} good passes"
        )

    return findings
