"""Runs each agent through Anthropic Claude API with vault context."""

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
    read_watchlist,
    read_latest_rising_stars,
)

logger = logging.getLogger(__name__)

client = Anthropic(api_key=config.ANTHROPIC_API_KEY)


def _call_llm(system_prompt: str, user_prompt: str) -> str:
    """Send a prompt to Anthropic and return the response text."""
    try:
        response = client.messages.create(
            model=config.LLM_MODEL,
            max_tokens=config.LLM_MAX_TOKENS,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt},
            ],
        )
        return response.content[0].text
    except Exception as e:
        logger.error(f"Anthropic API error: {e}")
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
    fundamentals: dict[str, dict] | None = None,
) -> str:
    """Run the Head of Investment agent."""
    agent_def = read_agent_definition(1)
    learning_log = read_learning_log()
    watchlist = read_watchlist()
    rising_stars = read_latest_rising_stars()

    news_summary = "\n".join(
        f"- [{a['ticker']}] {a['headline']} ({a['source']})"
        for a in news[:12]
    )
    general_summary = "\n".join(
        f"- {a['headline']} ({a['source']})" for a in general_news[:5]
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

    # Format fundamentals data
    fundamentals_summary = ""
    if fundamentals:
        lines = []
        for ticker, f in fundamentals.items():
            if not f:
                continue
            pe = f.get("pe_trailing")
            fwd_pe = f.get("pe_forward")
            rev_growth = f.get("revenue_growth")
            earn_growth = f.get("earnings_growth")
            margin = f.get("profit_margin")
            debt = f.get("debt_to_equity")
            target = f.get("analyst_target")
            rec = f.get("analyst_recommendation")
            mcap = f.get("market_cap")
            mcap_str = f"${mcap/1e9:.1f}B" if mcap else "N/A"

            lines.append(
                f"| {ticker} | {mcap_str} | "
                f"{pe:.1f} | {fwd_pe:.1f} | "
                f"{rev_growth*100:.1f}% | {earn_growth*100:.1f}% | "
                f"{margin*100:.1f}% | {debt:.0f} | "
                f"${target:.0f} | {rec} |"
                if pe and fwd_pe and rev_growth is not None
                and earn_growth is not None and margin is not None
                and debt is not None and target
                else f"| {ticker} | {mcap_str} | "
                f"{pe or 'N/A'} | {fwd_pe or 'N/A'} | "
                f"{f'{rev_growth*100:.1f}%' if rev_growth is not None else 'N/A'} | "
                f"{f'{earn_growth*100:.1f}%' if earn_growth is not None else 'N/A'} | "
                f"{f'{margin*100:.1f}%' if margin is not None else 'N/A'} | "
                f"{f'{debt:.0f}' if debt is not None else 'N/A'} | "
                f"{f'${target:.0f}' if target else 'N/A'} | {rec or 'N/A'} |"
            )
        if lines:
            fundamentals_summary = (
                "## Company Fundamentals\n"
                "| Ticker | Mkt Cap | P/E | Fwd P/E | Rev Growth | "
                "Earn Growth | Margin | D/E | Analyst Target | Rating |\n"
                "|--------|---------|-----|---------|------------|"
                "------------|--------|-----|----------------|--------|\n"
                + "\n".join(lines) + "\n\n"
                "Use fundamentals to filter: avoid stocks with negative earnings growth, "
                "extreme P/E (>50 or negative), or debt/equity >200. "
                "Prefer stocks where analyst target is above current price.\n\n"
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
        f"{fundamentals_summary}"
        f"## Upcoming Earnings\n{earnings_summary or 'None in next 5 days for watchlist.'}\n\n"
        f"## Current Portfolio\n{portfolio}\n\n"
        f"## Watchlist\n{watchlist}\n\n"
    )

    if rising_stars:
        user_prompt += (
            f"## Recent Rising Stars Discoveries\n{rising_stars}\n\n"
            "IMPORTANT: Consider the Rising Stars tickers above alongside the usual "
            "watchlist. These were identified by the automated scanner as showing "
            "breakout potential. Include at least 1-2 rising star tickers in your "
            "analysis if their sector aligns with today's macro bias.\n\n"
        )

    user_prompt += (
        "Now produce your Investment Brief. Follow your output format exactly.\n\n"
        "CRITICAL: After the Decision section, output one final machine-readable "
        "line listing ONLY the tickers you want analyzed for NEW entries this "
        "session (exclude any held/monitor-only positions), comma-separated, "
        "exactly in this format:\n"
        "SELECTED_TICKERS: AAA, BBB, CCC\n"
        "This line is parsed programmatically and handed to the Stock Analyst — "
        "if it is missing or wrong, no trades can happen."
    )

    return _call_llm(system_prompt, user_prompt)


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

        # Include pre-computed trade parameters for confirmed setups
        trade_params = analysis.get("trade_params", {})
        if trade_params:
            ticker_data += f"\n**Pre-Computed Trade Parameters (use these exact values):**\n"
            for strat_name, params in trade_params.items():
                ticker_data += f"\n_{strat_name}_:\n"
                ticker_data += f"  - Entry: ${params['entry']}\n"
                ticker_data += f"  - Stop Loss: ${params['stop_loss']} ({params['stop_basis']})\n"
                ticker_data += f"  - Take Profit: ${params['take_profit']} ({params['target_basis']})\n"
                ticker_data += f"  - Risk/Share: ${params['risk_per_share']}\n"
                ticker_data += f"  - Reward/Share: ${params['reward_per_share']}\n"
                ticker_data += f"  - R:R Ratio: {params['rr_ratio']}:1\n"
                ticker_data += (
                    f"  - Min R:R for this strategy: {params['min_rr_required']}:1 "
                    f"({'PASS' if params['meets_min_rr'] else 'FAIL'})\n"
                )

    system_prompt = (
        "You are the Stock Analyst agent in a swing trading system.\n\n"
        f"## Your Agent Definition\n{agent_def}\n\n"
        f"## Strategy DNA (exact parameters)\n{strategy_dna}\n\n"
        "Follow your output format EXACTLY as specified in your agent definition. "
        "Output valid markdown. Be precise with numbers.\n\n"
        "CRITICAL: When trade parameters (Entry, Stop Loss, Take Profit, R:R Ratio) "
        "are provided as 'Pre-Computed Trade Parameters', you MUST use those exact values. "
        "Do NOT recalculate them. These are computed by the system with verified arithmetic."
    )

    user_prompt = (
        f"# Technical Data for {date_str}\n\n"
        f"Here is the computed technical analysis for each ticker:\n"
        f"{ticker_data}\n\n"
        "Now produce your Technical Analysis Report. Follow your output format exactly. "
        "For each ticker, assess whether each strategy has a confirmed setup. "
        "For confirmed setups, use the Pre-Computed Trade Parameters exactly as given — "
        "do not recalculate Entry, Stop Loss, Take Profit, or R:R Ratio."
    )

    return _call_llm(system_prompt, user_prompt)


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
        "Output valid markdown.\n\n"
        "CRITICAL: When Agent 02 provides Entry, Stop Loss, Take Profit, and R:R Ratio "
        "values, you MUST copy those exact values into your output. Do NOT recalculate them. "
        "Only calculate Position Size = floor(account_risk / risk_per_share)."
    )

    user_prompt = (
        f"# Merge Request for {date_str}\n\n"
        f"## Agent 01 — Investment Brief\n{agent1_output}\n\n"
        f"## Agent 02 — Technical Analysis Report\n{agent2_output}\n\n"
        f"## Account Equity: ${account_equity:,.2f}\n\n"
        "Now produce your Merged Analysis. Follow your output format exactly. "
        "Copy the Entry, Stop Loss, Take Profit, and R:R Ratio exactly from Agent 02. "
        "Calculate position sizing: shares = floor(1% of equity / risk per share)."
    )

    return _call_llm(system_prompt, user_prompt)


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

    return _call_llm(system_prompt, user_prompt)


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
        "Use the two-tier system: Hard checks must ALL pass (immediate NO-GO on failure). "
        "Soft checks (5, 10, 12, 14) produce warnings — up to 2 warnings allowed, 3+ = NO-GO. "
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

    return _call_llm(system_prompt, user_prompt)


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
    """Parse Agent 1 output to determine PROCEED/STAND DOWN and extract tickers.

    Ticker extraction is structured, not prose-scraping. In priority order:
      1. An explicit ``SELECTED_TICKERS: AAA, BBB, ...`` line.
      2. The first column of the ``## Tickers for Analysis`` markdown table.
      3. Legacy whole-document regex scrape (last-resort fallback only).

    Rows whose catalyst/strategy marks them as held / monitor-only (e.g. the
    current MRVL position) are excluded so Agent 2 spends its budget on
    genuinely new candidates, not names we already hold.
    """
    import re

    if "STAND DOWN" in agent1_output.upper():
        return {"proceed": False, "tickers": [], "raw_text": agent1_output}

    def _clean(sym: str) -> str | None:
        sym = sym.strip().strip("*`_ ").upper()
        return sym if re.fullmatch(r"[A-Z]{1,5}", sym) else None

    def _dedupe(seq: list[str]) -> list[str]:
        out: list[str] = []
        for s in seq:
            if s and s not in out:
                out.append(s)
        return out

    MONITOR_FLAGS = ("MONITOR", "CURRENTLY HELD", "POSITION MANAGEMENT", "HOLD ONLY")

    # --- 1. Explicit machine-readable line (most robust) ---------------- #
    line_match = re.search(r"SELECTED_TICKERS\s*[:=]\s*(.+)", agent1_output, re.IGNORECASE)
    if line_match:
        raw = re.split(r"[,\s/|]+", line_match.group(1).strip())
        tickers = _dedupe(t for t in (_clean(x) for x in raw) if t)
        if tickers:
            return {"proceed": True, "tickers": tickers[:8], "raw_text": agent1_output}

    # --- 2. "Tickers for Analysis" markdown table ---------------------- #
    tickers = []
    in_table = False
    for line in agent1_output.split("\n"):
        low = line.lower()
        if "tickers for analysis" in low:
            in_table = True
            continue
        if in_table:
            stripped = line.strip()
            # Table ends at the next blank line or new heading.
            if stripped.startswith("#") or stripped == "":
                if tickers:  # only stop once we've collected the table body
                    break
                continue
            if not stripped.startswith("|"):
                continue
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if not cells:
                continue
            first = cells[0]
            # Skip header row and the |---|---| separator.
            if first.lower() in ("ticker", "symbol") or set(first) <= set("-: "):
                continue
            # Skip held / monitor-only rows so we surface NEW candidates.
            rowtext = " ".join(cells).upper()
            if any(flag in rowtext for flag in MONITOR_FLAGS):
                continue
            sym = _clean(first)
            if sym:
                tickers.append(sym)
    tickers = _dedupe(tickers)
    if tickers:
        return {"proceed": True, "tickers": tickers[:8], "raw_text": agent1_output}

    # --- 3. Legacy fallback: whole-document scrape (rarely needed) ------ #
    skip_words = {
        "THE", "AND", "FOR", "NOT", "YES", "BUY", "SELL", "AI",
        "EST", "AM", "PM", "ETF", "SMA", "RSI", "ATR", "AVOID",
        "EMA", "VIX", "USD", "DAY", "HIGH", "LOW", "GDP", "FED",
        "RISK", "MIXED", "STAND", "DOWN", "PROCEED", "CPI", "ISM",
        "SETUP", "NO", "ON", "OFF", "TO", "OR", "IF", "PMI", "PE",
        "TODAY", "DATE", "NONE", "ALL", "ADD", "NEW",
        "MACD", "VWAP", "BB", "ADX", "BTC", "MA",
        "ABOVE", "BELOW", "BULLISH", "BEARISH",
        "SIGNAL", "STRONG", "WEAK", "MODERATE",
        "STABLE", "SECTOR", "CATALYST", "STRATEGY",
        "MOVE", "EXPECTED", "TREND", "BIAS",
    }
    known = set(config.DEFAULT_WATCHLIST)
    fallback = []
    for line in agent1_output.split("\n"):
        for m in re.findall(r"\b([A-Z]{1,5})\b", line):
            if m in skip_words:
                continue
            # Prefer known-universe names; otherwise require >=2 chars.
            if (m in known or len(m) >= 2) and m not in fallback:
                fallback.append(m)
    return {
        "proceed": True,
        "tickers": fallback[:8],
        "raw_text": agent1_output,
    }
