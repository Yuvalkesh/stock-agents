# Trading Strategy Overview

## Approach: Multi-Agent Swing Trading

We use a 5-agent AI pipeline to identify, analyze, and execute swing trades. Each agent has a specific role and personality, creating checks and balances that prevent impulsive or poorly-analyzed trades.

## Edge
Our edge comes from:
1. **Multi-source analysis**: News sentiment + technical analysis + macro regime, all aligned
2. **Aggressive filtering**: Only trades scoring 8/10+ pass through. Most candidates are rejected
3. **Strict risk management**: 1% risk per trade, ATR-based stops, bracket orders
4. **Compound learning**: Every trade updates the memory system, making future decisions better
5. **Emotional discipline**: AI doesn't panic, FOMO, or revenge trade

## Strategy Selection
We run 5 proven strategies, each suited to different market conditions:

1. **Connors RSI(2)** — Mean reversion in uptrending stocks
2. **MACD + RSI** — Momentum entries with confirmation
3. **Bollinger Squeeze** — Volatility breakout plays
4. **MA Crossover** — Trend-following with pullback entries
5. **VIX Fear** — Buying panic in healthy markets

See `C-core/strategy-dna.md` for exact parameters.

## Trade Selection Process
1. Morning scan identifies macro regime and news catalysts
2. Technical analysis runs all 5 strategies on candidate tickers
3. Data merger aligns news with technicals, flags contradictions
4. Decision maker scores candidates (need 8/10)
5. Gatekeeper runs risk checklist (14 items, all must pass)
6. Only then does a trade execute

## Expected Outcome
- 6-10 trades per month
- 55-65% win rate
- 2-4% monthly return
- Maximum 10% monthly drawdown

## What Makes Us Different
Most retail trading systems fail because of:
- Too many trades (overtrading)
- No risk management (sizing too large)
- No learning loop (repeating mistakes)
- Emotional decisions (FOMO, revenge trading)

We solve all four.
