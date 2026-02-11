"""Reads markdown files from the Obsidian vault for agent context."""

import logging
from pathlib import Path
from typing import Optional

from config import (
    VAULT_PATH, AGENTS_PATH, CORE_PATH, MEMORY_PATH,
    OUTPUT_PATH, PORTFOLIO_PATH, REFERENCES_PATH,
)

logger = logging.getLogger(__name__)


def read_file(path: Path) -> str:
    """Read a single markdown file and return its contents."""
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        logger.warning(f"File not found: {path}")
        return ""
    except Exception as e:
        logger.error(f"Error reading {path}: {e}")
        return ""


def read_agent_definition(agent_number: int) -> str:
    """Read an agent definition file (01-05)."""
    agent_files = {
        1: "01-head-of-investment.md",
        2: "02-stock-analyst.md",
        3: "03-data-merger.md",
        4: "04-swing-trader-megabot.md",
        5: "05-gatekeeper-boss.md",
    }
    filename = agent_files.get(agent_number, "")
    if not filename:
        return ""
    return read_file(AGENTS_PATH / filename)


def read_core_file(name: str) -> str:
    """Read a core file by name (without extension)."""
    return read_file(CORE_PATH / f"{name}.md")


def read_strategy_dna() -> str:
    return read_core_file("strategy-dna")


def read_risk_rules() -> str:
    return read_core_file("risk-management-rules")


def read_watchlist() -> str:
    return read_core_file("watchlist")


def read_pipeline_routing() -> str:
    return read_core_file("pipeline-routing")


def read_trading_identity() -> str:
    return read_core_file("trading-identity")


def read_learning_log() -> str:
    return read_file(MEMORY_PATH / "learning-log.md")


def read_portfolio_positions() -> str:
    return read_file(PORTFOLIO_PATH / "current-positions.md")


def read_account_status() -> str:
    return read_file(PORTFOLIO_PATH / "account-status.md")


def read_pending_orders() -> str:
    return read_file(PORTFOLIO_PATH / "pending-orders.md")


def read_best_trades() -> str:
    """Read all best trade references."""
    best_dir = REFERENCES_PATH / "best-trades"
    if not best_dir.exists():
        return "_No best trades logged yet._"
    files = sorted(best_dir.glob("*.md"))
    if not files:
        return "_No best trades logged yet._"
    return "\n\n---\n\n".join(read_file(f) for f in files[-5:])  # Last 5


def read_worst_trades() -> str:
    """Read all worst trade references."""
    worst_dir = REFERENCES_PATH / "worst-trades"
    if not worst_dir.exists():
        return "_No worst trades logged yet._"
    files = sorted(worst_dir.glob("*.md"))
    if not files:
        return "_No worst trades logged yet._"
    return "\n\n---\n\n".join(read_file(f) for f in files[-5:])  # Last 5


def read_strategy_performance(strategy_name: str) -> str:
    """Read performance log for a specific strategy."""
    name_map = {
        "connors_rsi": "connors-rsi-log.md",
        "macd_rsi": "macd-rsi-log.md",
        "bollinger_squeeze": "bollinger-squeeze-log.md",
        "ma_crossover": "ma-crossover-log.md",
        "vix_fear": "vix-fear-log.md",
    }
    filename = name_map.get(strategy_name, "")
    if not filename:
        return ""
    return read_file(MEMORY_PATH / "strategy-performance" / filename)


def read_previous_agent_output(date_str: str, agent_number: int) -> str:
    """Read a previous agent's output for a given date."""
    file_map = {
        1: "01-investment-brief.md",
        2: "02-analyst-report.md",
        3: "03-merged-data.md",
        4: "04-trade-decision.md",
        5: "05-gatekeeper-verdict.md",
    }
    filename = file_map.get(agent_number, "")
    if not filename:
        return ""
    return read_file(OUTPUT_PATH / "trades" / date_str / filename)


def get_trade_output_dir(date_str: str) -> Path:
    """Get or create the output directory for a trading day."""
    trade_dir = OUTPUT_PATH / "trades" / date_str
    trade_dir.mkdir(parents=True, exist_ok=True)
    return trade_dir


def get_scan_output_dir(date_str: str) -> Path:
    """Get or create the scan output directory for a date."""
    scan_dir = OUTPUT_PATH / "scans" / date_str
    scan_dir.mkdir(parents=True, exist_ok=True)
    return scan_dir


def get_rejected_dir() -> Path:
    """Get or create the rejected trades directory."""
    rejected_dir = OUTPUT_PATH / "rejected"
    rejected_dir.mkdir(parents=True, exist_ok=True)
    return rejected_dir
