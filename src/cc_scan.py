"""Claude Code scan helper — gathers ALL inputs for a trading decision with
ZERO LLM/API-token cost, and prints them as a compact markdown brief.

The reasoning (the 5 agents) is done by Claude Code itself via the /stock-scan
skill, so the only paid API here is market data + Alpaca (free/cheap). Run:

    python src/cc_scan.py            # scan + print brief
    python src/cc_scan.py --json     # same data as JSON

This deliberately does NOT call agent_runner (no Anthropic tokens).
"""

import argparse
import json
import sys

import config
from data_fetcher import DataFetcher
from technical_analysis import TechnicalAnalyzer
from trade_executor import TradeExecutor
from vault_reader import read_watchlist_tickers


def gather() -> dict:
    fetcher = DataFetcher()
    analyzer = TechnicalAnalyzer()
    tickers = read_watchlist_tickers() or config.DEFAULT_WATCHLIST

    data = fetcher.fetch_all(tickers=tickers)
    sp500_df = fetcher.fetch_ohlcv("^GSPC", period="1y")

    setups = []
    screened = []
    for t in tickers:
        df = fetcher.fetch_ohlcv(t, period="1y")
        if df is None or df.empty:
            continue
        screened.append(t)
        analysis = analyzer.analyze_ticker(
            t, df, vix_data=data.get("vix_data"), sp500_df=sp500_df
        )
        tp = analysis.get("trade_params") or {}
        if not tp:
            continue
        news = [n["headline"] for n in data.get("news", []) if n.get("ticker") == t][:3]
        fund = (data.get("fundamentals") or {}).get(t, {})
        for strat, params in tp.items():
            entry = params.get("entry")
            stop = params.get("stop_loss")
            tgt = params.get("take_profit")
            rr = None
            if entry and stop and tgt and entry != stop:
                rr = round(abs(tgt - entry) / abs(entry - stop), 2)
            setups.append({
                "ticker": t, "strategy": strat,
                "entry": entry, "stop": stop, "target": tgt, "rr": rr,
                "price": analysis.get("latest_price") or analysis.get("price"),
                "rel_vol": analysis.get("rel_vol"),
                "support": analysis.get("support"),
                "resistance": analysis.get("resistance"),
                "earnings": (data.get("earnings") or {}).get(t),
                "pe": fund.get("pe_forward") or fund.get("pe_trailing"),
                "analyst_target": fund.get("analyst_target"),
                "rating": fund.get("analyst_recommendation"),
                "earnings_growth": fund.get("earnings_growth"),
                "news": news,
            })

    ex = TradeExecutor()
    account = ex.get_account()
    positions = ex.get_positions()
    exposure = ex.get_total_exposure()

    return {
        "macro": data.get("macro", {}),
        "account": account,
        "positions": positions,
        "exposure_pct": exposure,
        "setups": setups,
        "screened": screened,
        "limits": {
            "max_positions": config.MAX_OPEN_POSITIONS,
            "max_risk_per_trade_pct": config.MAX_RISK_PER_TRADE * 100,
            "max_single_position_pct": config.MAX_SINGLE_POSITION * 100,
            "max_total_exposure_pct": config.MAX_TOTAL_EXPOSURE * 100,
            "min_conviction": config.MIN_CONVICTION_SCORE,
            "let_winners_run": config.LET_WINNERS_RUN,
            "trailing_stop_pct": getattr(config, "LIVE_TRAILING_STOP_PCT", None),
        },
    }


def to_markdown(d: dict) -> str:
    m = d["macro"]; a = d["account"]; L = d["limits"]
    out = ["# Stock Scan Brief (no LLM tokens used)\n"]

    out.append("## Macro")
    out.append(f"- Regime: **{m.get('regime', 'UNKNOWN')}**")
    for k, v in m.items():
        if isinstance(v, dict):
            out.append(f"- {k}: value={v.get('value')}, change={v.get('change_pct')}%")
    out.append("")

    out.append("## Account")
    out.append(f"- Equity: ${a.get('equity', 0):,.0f} | Cash: ${a.get('cash', 0):,.0f} "
               f"| Buying power: ${a.get('buying_power', 0):,.0f}")
    out.append(f"- Total exposure: {d['exposure_pct']:.1f}% (limit {L['max_total_exposure_pct']:.0f}%)")
    out.append(f"- Open positions: {len(d['positions'])} (limit {L['max_positions']})")
    for p in d["positions"]:
        out.append(f"   • {p.get('symbol')}: {p.get('qty')} sh, "
                   f"uPnL ${p.get('unrealized_pl', 0):,.0f} ({p.get('unrealized_plpc', 0):+.1f}%)")
    out.append(f"- Risk rules: ≤{L['max_risk_per_trade_pct']:.0f}% risk/trade, "
               f"≤{L['max_single_position_pct']:.0f}%/position, conviction ≥{L['min_conviction']}/12")
    out.append(f"- Exit policy: let_winners_run={L['let_winners_run']}, "
               f"trailing stop {L['trailing_stop_pct']}%")
    out.append("")

    out.append(f"## Confirmed Setups ({len(d['setups'])})")
    if not d["setups"]:
        out.append("- None today. No technical setup fired across the watchlist.")
    for s in d["setups"]:
        out.append(f"\n### {s['ticker']} — {s['strategy']}")
        out.append(f"- Entry ${s['entry']} | Stop ${s['stop']} | Target ${s['target']} | R:R {s['rr']}")
        out.append(f"- Price ${s['price']} | RelVol {s['rel_vol']} | "
                   f"Support ${s['support']} | Resistance ${s['resistance']}")
        out.append(f"- Earnings: {s['earnings'] or 'n/a'} | Fwd P/E {s['pe']} | "
                   f"Analyst target ${s['analyst_target']} ({s['rating']}) | "
                   f"EarnGrowth {s['earnings_growth']}")
        if s["news"]:
            out.append("- News: " + " | ".join(s["news"]))
    out.append("")
    out.append(f"## Screened (no setup): {', '.join(d['screened'])}")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    d = gather()
    if args.json:
        print(json.dumps(d, indent=2, default=str))
    else:
        print(to_markdown(d))


if __name__ == "__main__":
    main()
