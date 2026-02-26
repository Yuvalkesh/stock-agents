"""Writes all outputs to the Obsidian vault as markdown files."""

import logging
from datetime import datetime
from pathlib import Path
from typing import Any

from config import (
    VAULT_PATH, MEMORY_PATH, OUTPUT_PATH, PORTFOLIO_PATH, REFERENCES_PATH,
)
from vault_reader import get_trade_output_dir, get_scan_output_dir, get_rejected_dir

logger = logging.getLogger(__name__)


def write_file(path: Path, content: str) -> None:
    """Write content to a markdown file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    logger.info(f"Wrote: {path}")


# ------------------------------------------------------------------ #
# Agent Outputs
# ------------------------------------------------------------------ #
def save_agent_output(date_str: str, agent_number: int, content: str) -> Path:
    """Save an agent's output to the trades directory."""
    file_map = {
        1: "01-investment-brief.md",
        2: "02-analyst-report.md",
        3: "03-merged-data.md",
        4: "04-trade-decision.md",
        5: "05-gatekeeper-verdict.md",
    }
    filename = file_map.get(agent_number, f"agent-{agent_number}-output.md")
    trade_dir = get_trade_output_dir(date_str)
    path = trade_dir / filename
    write_file(path, content)
    return path


def save_rejected_trade(date_str: str, symbol: str, content: str) -> Path:
    """Save a rejected trade for learning."""
    rejected_dir = get_rejected_dir()
    path = rejected_dir / f"{date_str}-{symbol}-rejected.md"
    write_file(path, content)
    return path


def save_scan_output(date_str: str, content: str) -> Path:
    """Save a daily scan output."""
    scan_dir = get_scan_output_dir(date_str)
    path = scan_dir / "daily-scan.md"
    write_file(path, content)
    return path


def save_approved_trades_json(date_str: str, trades: list) -> Path:
    """Save approved trades as JSON so execute can read them without re-running the scan."""
    import json
    scan_dir = get_scan_output_dir(date_str)
    path = scan_dir / "approved-trades.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(trades, indent=2), encoding="utf-8")
    logger.info(f"Wrote: {path}")
    return path


def load_approved_trades_json(date_str: str) -> list | None:
    """Load approved trades saved by the morning scan. Returns None if not found."""
    import json
    from vault_reader import get_scan_output_dir
    path = get_scan_output_dir(date_str) / "approved-trades.json"
    if not path.exists():
        return None
    trades = json.loads(path.read_text(encoding="utf-8"))
    return trades if trades else None


# ------------------------------------------------------------------ #
# Trade Journal
# ------------------------------------------------------------------ #
def write_trade_journal_entry(trade_data: dict[str, Any]) -> Path:
    """Write a trade journal entry after a position closes."""
    symbol = trade_data.get("symbol", "UNKNOWN")
    direction = trade_data.get("direction", "long")
    date = trade_data.get("entry_date", datetime.now().strftime("%Y-%m-%d"))

    entry_price = trade_data.get("entry_price", 0)
    exit_price = trade_data.get("exit_price", 0)
    shares = trade_data.get("shares", 0)
    strategy = trade_data.get("strategy", "unknown")
    pnl = trade_data.get("pnl", 0)
    r_multiple = trade_data.get("r_multiple", 0)
    exit_reason = trade_data.get("exit_reason", "unknown")
    thesis = trade_data.get("thesis", "")
    lessons = trade_data.get("lessons", "")

    pnl_pct = ((exit_price - entry_price) / entry_price * 100) if entry_price else 0
    if direction.lower() == "short":
        pnl_pct = -pnl_pct

    content = f"""# Trade Journal — {symbol} {direction.upper()} — {date}

## Summary
| Metric | Value |
|--------|-------|
| Symbol | {symbol} |
| Direction | {direction.upper()} |
| Strategy | {strategy} |
| Entry Date | {date} |
| Exit Date | {trade_data.get('exit_date', 'N/A')} |
| Entry Price | ${entry_price:.2f} |
| Exit Price | ${exit_price:.2f} |
| Shares | {shares} |
| P&L | ${pnl:.2f} ({pnl_pct:.2f}%) |
| R-Multiple | {r_multiple:.2f}R |
| Exit Reason | {exit_reason} |

## Thesis
{thesis}

## What Worked
{trade_data.get('what_worked', '_To be filled._')}

## What Didn't Work
{trade_data.get('what_didnt_work', '_To be filled._')}

## Lesson Learned
{lessons or '_To be filled._'}
"""

    filename = f"{date}-{symbol}-{direction}.md"
    path = MEMORY_PATH / "trade-journal" / filename
    write_file(path, content)

    # Copy to best/worst references
    if r_multiple >= 2:
        ref_path = REFERENCES_PATH / "best-trades" / filename
        write_file(ref_path, content)
    elif r_multiple <= -1:
        ref_path = REFERENCES_PATH / "worst-trades" / filename
        write_file(ref_path, content)

    return path


# ------------------------------------------------------------------ #
# Learning Log
# ------------------------------------------------------------------ #
def append_to_learning_log(entry: str) -> None:
    """Append a new entry to the learning log."""
    log_path = MEMORY_PATH / "learning-log.md"
    existing = log_path.read_text(encoding="utf-8") if log_path.exists() else ""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    new_entry = f"\n### {timestamp}\n{entry}\n"

    # Insert after the last section marker we can find
    if "## Common Mistakes" in existing:
        parts = existing.rsplit("## Common Mistakes", 1)
        updated = parts[0] + new_entry + "\n## Common Mistakes" + parts[1]
    else:
        updated = existing + new_entry

    write_file(log_path, updated)


# ------------------------------------------------------------------ #
# Strategy Performance
# ------------------------------------------------------------------ #
def update_strategy_performance(
    strategy_name: str, trade_data: dict[str, Any]
) -> None:
    """Update the strategy performance log with a new trade result."""
    name_map = {
        "connors_rsi": "connors-rsi-log.md",
        "macd_rsi": "macd-rsi-log.md",
        "bollinger_squeeze": "bollinger-squeeze-log.md",
        "ma_crossover": "ma-crossover-log.md",
        "vix_fear": "vix-fear-log.md",
    }
    filename = name_map.get(strategy_name)
    if not filename:
        logger.warning(f"Unknown strategy: {strategy_name}")
        return

    path = MEMORY_PATH / "strategy-performance" / filename
    existing = path.read_text(encoding="utf-8") if path.exists() else ""

    # Append trade to the log table
    new_row = (
        f"| {trade_data.get('entry_date', 'N/A')} "
        f"| {trade_data.get('symbol', 'N/A')} "
        f"| {trade_data.get('direction', 'N/A')} "
        f"| ${trade_data.get('entry_price', 0):.2f} "
        f"| ${trade_data.get('exit_price', 0):.2f} "
        f"| ${trade_data.get('pnl', 0):.2f} "
        f"| {trade_data.get('r_multiple', 0):.2f}R "
        f"| {trade_data.get('notes', '')} |\n"
    )

    if "<!-- Entries added" in existing:
        updated = existing.replace(
            "<!-- Entries added automatically after each trade -->",
            new_row + "<!-- Entries added automatically after each trade -->",
        )
    else:
        updated = existing + "\n" + new_row

    write_file(path, updated)


# ------------------------------------------------------------------ #
# Portfolio Files
# ------------------------------------------------------------------ #
def update_positions_file(positions: list[dict[str, Any]]) -> None:
    """Update current-positions.md with live position data."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    if not positions:
        rows = "\n_No open positions._\n"
        total_exposure = 0
        unrealized_pnl = 0
    else:
        rows = ""
        total_exposure = 0
        unrealized_pnl = 0
        for p in positions:
            rows += (
                f"| {p['symbol']} | {p.get('side', 'long')} | {int(p['qty'])} "
                f"| ${p['avg_entry_price']:.2f} | — "
                f"| — | — | — "
                f"| ${p['unrealized_pl']:.2f} |\n"
            )
            total_exposure += abs(p.get("market_value", 0))
            unrealized_pnl += p.get("unrealized_pl", 0)

    content = f"""# Current Positions

## Open Positions
| Ticker | Direction | Shares | Entry Price | Entry Date | Stop Loss | Target | Strategy | Unrealized P&L |
|--------|-----------|--------|-------------|------------|-----------|--------|----------|----------------|
{rows}
## Position Summary
| Metric | Value |
|--------|-------|
| Total Positions | {len(positions)} |
| Total Exposure | ${total_exposure:,.2f} |
| Unrealized P&L | ${unrealized_pnl:,.2f} |

## Last Updated
{now}
"""
    write_file(PORTFOLIO_PATH / "current-positions.md", content)


def update_account_status(account: dict[str, Any]) -> None:
    """Update account-status.md with live account data."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    content = f"""# Account Status

## Alpaca Paper Trading Account

| Metric | Value |
|--------|-------|
| Current Equity | ${account.get('equity', 0):,.2f} |
| Cash | ${account.get('cash', 0):,.2f} |
| Buying Power | ${account.get('buying_power', 0):,.2f} |
| Today's P&L | ${account.get('daily_pnl', 0):,.2f} ({account.get('daily_pnl_pct', 0):.2f}%) |

## Last Updated
{now}
"""
    write_file(PORTFOLIO_PATH / "account-status.md", content)


def update_pending_orders(orders: list[dict[str, Any]]) -> None:
    """Update pending-orders.md with current open orders."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    if not orders:
        rows = "\n_No pending orders._\n"
    else:
        rows = ""
        for o in orders:
            rows += (
                f"| {o.get('id', 'N/A')[:8]} | {o.get('symbol', 'N/A')} "
                f"| {o.get('side', 'N/A')} | {o.get('type', 'N/A')} "
                f"| {int(o.get('qty', 0))} | — "
                f"| {o.get('status', 'N/A')} | {o.get('submitted_at', 'N/A')} |\n"
            )

    content = f"""# Pending Orders

## Active Orders
| Order ID | Ticker | Direction | Type | Shares | Limit/Stop Price | Status | Submitted |
|----------|--------|-----------|------|--------|-----------------|--------|-----------|
{rows}
## Last Updated
{now}
"""
    write_file(PORTFOLIO_PATH / "pending-orders.md", content)
