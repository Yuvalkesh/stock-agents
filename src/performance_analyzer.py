"""Generates post-trade analysis and monthly reviews."""

import logging
from datetime import datetime
from pathlib import Path
from typing import Any

from anthropic import Anthropic

import config
from config import MEMORY_PATH
from vault_reader import (
    read_learning_log,
    read_portfolio_positions,
    read_account_status,
)
from memory_logger import write_file

logger = logging.getLogger(__name__)

client = Anthropic(api_key=config.ANTHROPIC_API_KEY)


def generate_monthly_review(year: int, month: int) -> str:
    """Generate a comprehensive monthly review using OpenAI."""
    month_str = f"{year}-{month:02d}"

    # Gather all trade journals for the month
    journal_dir = MEMORY_PATH / "trade-journal"
    journal_entries = []
    if journal_dir.exists():
        for f in sorted(journal_dir.glob(f"{month_str}*.md")):
            journal_entries.append(f.read_text(encoding="utf-8"))

    # Gather strategy performance logs
    strat_dir = MEMORY_PATH / "strategy-performance"
    strat_logs = []
    if strat_dir.exists():
        for f in sorted(strat_dir.glob("*.md")):
            strat_logs.append(f.read_text(encoding="utf-8"))

    learning_log = read_learning_log()
    account_status = read_account_status()

    system_prompt = (
        "You are a trading performance analyst. Generate a comprehensive "
        "monthly review of trading performance. Be honest, data-driven, "
        "and constructive. Identify what worked, what didn't, and specific "
        "improvements for next month. Output valid markdown."
    )

    user_prompt = f"""# Monthly Review Request — {month_str}

## Trade Journal Entries ({len(journal_entries)} trades)
{'---'.join(journal_entries) if journal_entries else 'No trades this month.'}

## Strategy Performance Logs
{'---'.join(strat_logs)}

## Learning Log
{learning_log}

## Current Account Status
{account_status}

Generate a comprehensive monthly review with:
1. Performance summary (P&L, win rate, avg R, Sharpe estimate)
2. Best and worst trades analysis
3. Strategy-by-strategy breakdown
4. Risk management adherence
5. Key lessons learned
6. Specific recommendations for next month
7. Comparison to 2-4% monthly target
"""

    try:
        response = client.messages.create(
            model=config.LLM_MODEL,
            max_tokens=config.LLM_MAX_TOKENS,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt},
            ],
        )
        review_content = response.content[0].text
    except Exception as e:
        logger.error(f"Error generating monthly review: {e}")
        review_content = f"# Monthly Review — {month_str}\n\nError generating review: {e}"

    # Save the review
    review_path = MEMORY_PATH / "monthly-reviews" / f"{month_str}-review.md"
    write_file(review_path, review_content)

    logger.info(f"Monthly review saved: {review_path}")
    return review_content


def generate_trade_post_mortem(trade_data: dict[str, Any]) -> str:
    """Generate an AI-powered post-mortem analysis for a single trade."""
    system_prompt = (
        "You are a trading coach analyzing a completed trade. "
        "Be specific and actionable. Focus on what can be improved. "
        "Output valid markdown."
    )

    user_prompt = f"""Analyze this completed trade:

Symbol: {trade_data.get('symbol')}
Direction: {trade_data.get('direction')}
Strategy: {trade_data.get('strategy')}
Entry: ${trade_data.get('entry_price', 0):.2f} on {trade_data.get('entry_date')}
Exit: ${trade_data.get('exit_price', 0):.2f} on {trade_data.get('exit_date')}
P&L: ${trade_data.get('pnl', 0):.2f} ({trade_data.get('r_multiple', 0):.2f}R)
Exit Reason: {trade_data.get('exit_reason')}
Original Thesis: {trade_data.get('thesis', 'N/A')}

Provide:
1. What went right
2. What went wrong
3. Was the entry timing good?
4. Was the stop placement appropriate?
5. Key lesson for future trades
"""

    try:
        response = client.messages.create(
            model=config.LLM_MODEL,
            max_tokens=1024,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.content[0].text
    except Exception as e:
        logger.error(f"Error generating post-mortem: {e}")
        return f"Error generating post-mortem: {e}"
