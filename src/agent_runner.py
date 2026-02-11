"""Runs each agent through Claude API with vault context."""

import json
import logging
from typing import Any

from anthropic import Anthropic

import config
from vault_reader import (
    read_agent_definition,
    read_strategy_dna,
    read_risk_rules,
    read_learning_log,
    read_portfolio_positions,
    read_account_status,
    read_pending_orders,
    read_best_trades,
    read_worst_trades,
    read_previous_agent_output,
)

logger = logging.getLogger(__name__)

client = Anthropic(api_key=config.ANTHROPIC_API_KEY)


def _call_claude(system_prompt: str, user_prompt: str) -> str:
    """Send a prompt to Claude and return the response text."""
    try:
        response = client.messages.create(
            model=config.CLAUDE_MODEL,
            max_tokens=config.CLAUDE_MAX_TOKENS,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return response.content[0].text
    except Exception as e:
        logger.error(f"Claude API error: {e}")
        raise


# ------------------------------------------------------------------ #
# Agent 1: Head of Investment
# ------------------------------------------------------------------ #
def run_agent_1(
    news: list[dict],
    general_news: list[dict],
    macro: dict[str, Any],
    earnings: dict[str, str | None],
    portfolio: str,
    date_str: str,
) -> str:
    """Run the Head of Investment agent."""
    agent_def = read_agent_definition(1)
    learning_log = read_learning_log()

    news_summary = "\n".join(
        f"- [{a['ticker']}] {a['headline']} ({a['source']})"
        for a in news[:30]
    )
    general_summary = "\n".join(
        f"- {a['headline']} ({a['source']})" for a in general_news[:10]
    )
    macro_summary = "\n".join(
        f"- {k}: value={v.get('value')}, change={v.get('change_pct')}%"
        for k, v in macro.items()
        if isinstance(v, dict)
    )
    regime = macro.get("regime", "UNKNOWN")
    earnings_summary = "\n".join(
        f"- {ticker}: {date or 'Unknown'}"
        for ticker, date in earnings.items()
        if date
    )

    system_prompt = (
        "You are the Head of Investment agent in a swing trading system.\n\n"
        f"## Your Agent Definition\n{agent_def}\n\n"
        f"## Learning Log\n{learning_log}\n\n"
        "Follow your output format EXACTLY as specified in your agent definition. "
        "Output valid markdown."
    )

    user_prompt = (
        f"# Market Data for {date_str}\n\n"
        f"## Market Regime Indicators\n{macro_summary}\n"
        f"Current regime signal: **{regime}**\n\n"
        f"## Stock-Specific News (Last 7 Days)\n{news_summary}\n\n"
        f"## General Market News\n{general_summary}\n\n"
        f"## Upcoming Earnings\n{earnings_summary or 'None in next 5 days for watchlist.'}\n\n"
        f"## Current Portfolio\n{portfolio}\n\n"
        "Now produce your Investment Brief. Follow your output format exactly."
    )

    return _call_claude(system_prompt, user_prompt)


# ------------------------------------------------------------------ #
# Agent 2: Stock Analyst
# ------------------------------------------------------------------ #
def run_agent_2(
    ticker_analyses: dict[str, dict[str, Any]],
    date_str: str,
) -> str:
    """Run the Stock Analyst agent."""
    agent_def = read_agent_definition(2)
    strategy_dna = read_strategy_dna()

    # Build analysis summary per ticker
    ticker_data = ""
    for ticker, analysis in ticker_analyses.items():
        ticker_data += f"\n### {ticker}\n"
        ticker_data += f"- Price: ${analysis.get('price', 'N/A')}\n"
        ticker_data += f"- ATR(14): ${analysis.get('atr', 'N/A')}\n"
        ticker_data += f"- Relative Volume: {analysis.get('rel_volume', 'N/A')}x\n"
        ticker_data += f"- Support: ${analysis.get('support', 'N/A')}\n"
        ticker_data += f"- Resistance: ${analysis.get('resistance', 'N/A')}\n"
        ticker_data += f"\n**Strategy Results:**\n"
        for strat_name, strat_result in analysis.get("strategies", {}).items():
            ticker_data += (
                f"- {strat_name}: "
                f"Setup={'YES' if strat_result.get('setup') else 'NO'} — "
                f"{strat_result.get('reason', '')}\n"
            )
            if strat_result.get("values"):
                for k, v in strat_result["values"].items():
                    ticker_data += f"  - {k}: {v}\n"

    system_prompt = (
        "You are the Stock Analyst agent in a swing trading system.\n\n"
        f"## Your Agent Definition\n{agent_def}\n\n"
        f"## Strategy DNA (exact parameters)\n{strategy_dna}\n\n"
        "Follow your output format EXACTLY as specified in your agent definition. "
        "Output valid markdown. Be precise with numbers."
    )

    user_prompt = (
        f"# Technical Data for {date_str}\n\n"
        f"Here is the computed technical analysis for each ticker:\n"
        f"{ticker_data}\n\n"
        "Now produce your Technical Analysis Report. Follow your output format exactly. "
        "For each ticker, assess whether each strategy has a confirmed setup."
    )

    return _call_claude(system_prompt, user_prompt)


# ------------------------------------------------------------------ #
# Agent 3: Data Merger
# ------------------------------------------------------------------ #
def run_agent_3(
    agent1_output: str,
    agent2_output: str,
    account_equity: float,
    date_str: str,
) -> str:
    """Run the Data Merger agent."""
    agent_def = read_agent_definition(3)
    risk_rules = read_risk_rules()

    system_prompt = (
        "You are the Data Merger agent in a swing trading system.\n\n"
        f"## Your Agent Definition\n{agent_def}\n\n"
        f"## Risk Management Rules\n{risk_rules}\n\n"
        "Follow your output format EXACTLY. Calculate position sizing using "
        f"1% risk per trade on account equity of ${account_equity:,.2f}. "
        "Output valid markdown."
    )

    user_prompt = (
        f"# Merge Request for {date_str}\n\n"
        f"## Agent 01 — Investment Brief\n{agent1_output}\n\n"
        f"## Agent 02 — Technical Analysis Report\n{agent2_output}\n\n"
        f"## Account Equity: ${account_equity:,.2f}\n\n"
        "Now produce your Merged Analysis. Follow your output format exactly. "
        "Calculate exact trade parameters including position sizing."
    )

    return _call_claude(system_prompt, user_prompt)


# ------------------------------------------------------------------ #
# Agent 4: Swing Trader MegaBot
# ------------------------------------------------------------------ #
def run_agent_4(
    agent3_output: str,
    date_str: str,
    loopback_instructions: str = "",
) -> str:
    """Run the Swing Trader MegaBot agent."""
    agent_def = read_agent_definition(4)
    portfolio = read_portfolio_positions()
    learning_log = read_learning_log()
    best_trades = read_best_trades()
    worst_trades = read_worst_trades()

    system_prompt = (
        "You are the Swing Trader MegaBot agent in a swing trading system.\n\n"
        f"## Your Agent Definition\n{agent_def}\n\n"
        f"## Current Portfolio\n{portfolio}\n\n"
        f"## Learning Log\n{learning_log}\n\n"
        f"## Best Trades Reference\n{best_trades}\n\n"
        f"## Worst Trades Reference\n{worst_trades}\n\n"
        "Follow your output format EXACTLY. Score honestly — no rounding up. "
        "Output valid markdown."
    )

    user_prompt = (
        f"# Decision Request for {date_str}\n\n"
        f"## Agent 03 — Merged Analysis\n{agent3_output}\n\n"
    )
    if loopback_instructions:
        user_prompt += (
            f"## LOOPBACK INSTRUCTIONS FROM GATEKEEPER\n"
            f"{loopback_instructions}\n\n"
            "The Gatekeeper has sent this trade back for revision. "
            "Address the specific concerns above and re-score.\n\n"
        )
    user_prompt += "Now produce your Trade Decision. Follow your output format exactly."

    return _call_claude(system_prompt, user_prompt)


# ------------------------------------------------------------------ #
# Agent 5: Gatekeeper Boss
# ------------------------------------------------------------------ #
def run_agent_5(
    agent4_output: str,
    account_equity: float,
    daily_pnl_pct: float,
    monthly_drawdown_pct: float,
    open_positions_count: int,
    total_exposure_pct: float,
    date_str: str,
) -> str:
    """Run the Gatekeeper Boss agent."""
    agent_def = read_agent_definition(5)
    risk_rules = read_risk_rules()
    portfolio = read_portfolio_positions()
    account_status = read_account_status()
    pending_orders = read_pending_orders()

    system_prompt = (
        "You are the Gatekeeper Boss agent in a swing trading system.\n\n"
        f"## Your Agent Definition\n{agent_def}\n\n"
        f"## Risk Management Rules\n{risk_rules}\n\n"
        f"## Current Portfolio\n{portfolio}\n\n"
        f"## Account Status\n{account_status}\n\n"
        f"## Pending Orders\n{pending_orders}\n\n"
        "Follow your output format EXACTLY. Run EVERY check. "
        "If ANY check fails, the verdict is NO-GO. NO exceptions. "
        "Output valid markdown."
    )

    user_prompt = (
        f"# Gatekeeper Review for {date_str}\n\n"
        f"## Agent 04 — Trade Decision\n{agent4_output}\n\n"
        f"## Live Account Metrics\n"
        f"- Account Equity: ${account_equity:,.2f}\n"
        f"- Today's P&L: {daily_pnl_pct:.2f}%\n"
        f"- Monthly Drawdown: {monthly_drawdown_pct:.2f}%\n"
        f"- Open Positions: {open_positions_count}\n"
        f"- Total Exposure: {total_exposure_pct:.1f}%\n\n"
        "Now run your zero-tolerance checklist and produce your verdict. "
        "Follow your output format exactly."
    )

    return _call_claude(system_prompt, user_prompt)


# ------------------------------------------------------------------ #
# Parse Gatekeeper Verdict
# ------------------------------------------------------------------ #
def parse_gatekeeper_verdict(verdict_text: str) -> dict[str, Any]:
    """Parse the gatekeeper's verdict to determine GO/NO-GO."""
    text_upper = verdict_text.upper()

    # Look for the verdict
    if "VERDICT: GO" in text_upper and "VERDICT: NO-GO" not in text_upper:
        is_go = True
    elif "NO-GO" in text_upper or "REJECTED" in text_upper:
        is_go = False
    elif "APPROVED FOR EXECUTION" in text_upper:
        is_go = True
    else:
        # Default to NO-GO if unclear
        is_go = False

    # Check if fixable
    fixable = "FIXABLE" in text_upper and "YES" in text_upper.split("FIXABLE")[1][:20]

    return {
        "go": is_go,
        "fixable": fixable and not is_go,
        "raw_text": verdict_text,
    }


def parse_agent1_decision(agent1_output: str) -> dict[str, Any]:
    """Parse Agent 1 output to determine PROCEED/STAND DOWN and extract tickers."""
    text_upper = agent1_output.upper()

    if "STAND DOWN" in text_upper:
        return {"proceed": False, "tickers": [], "raw_text": agent1_output}

    # Extract tickers from the output — look for common stock ticker patterns
    import re
    # Look for tickers in table rows or lists
    tickers = []
    for line in agent1_output.split("\n"):
        # Match common ticker patterns (1-5 uppercase letters)
        matches = re.findall(r'\b([A-Z]{1,5})\b', line)
        for m in matches:
            if m in config.DEFAULT_WATCHLIST or len(m) >= 2:
                # Filter out common words
                skip_words = {
                    "THE", "AND", "FOR", "NOT", "YES", "BUY", "SELL",
                    "EST", "AM", "PM", "ETF", "SMA", "RSI", "ATR",
                    "EMA", "VIX", "USD", "DAY", "HIGH", "LOW",
                    "RISK", "MIXED", "STAND", "DOWN", "PROCEED",
                    "SETUP", "NO", "ON", "OFF", "TO", "OR", "IF",
                    "TODAY", "DATE", "NONE", "ALL",
                }
                if m not in skip_words and m not in tickers:
                    tickers.append(m)

    return {
        "proceed": True,
        "tickers": tickers[:8],  # Max 8 tickers
        "raw_text": agent1_output,
    }
