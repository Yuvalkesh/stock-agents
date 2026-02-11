# Stock Trading Multi-Agent System

## What Is This?
An automated swing trading system that uses 5 AI agents to analyze markets, identify high-probability setups, and execute trades via Alpaca paper trading ($100K).

## How It Works
1. **Data Fetcher** pulls news, prices, and macro indicators
2. **Agent 1 (Head of Investment)** assesses market regime and identifies tickers
3. **Agent 2 (Stock Analyst)** runs technical analysis with 5 strategies
4. **Agent 3 (Data Merger)** synthesizes news + technicals, flags contradictions
5. **Agent 4 (Swing Trader MegaBot)** scores and decides on each trade (need 8/10)
6. **Agent 5 (Gatekeeper Boss)** runs 14-point risk checklist (all must pass)
7. **Trade Executor** places bracket orders on Alpaca (entry + stop + target)
8. **Position Monitor** tracks positions hourly
9. **Post-Mortem** logs results and updates learning system

## Vault Structure
```
stock/
├── A-agents/        → 5 agent definitions (personality, inputs, outputs)
├── C-core/          → Identity, strategies, risk rules, watchlist, pipeline
├── M-memory/        → Learning log, trade journal, strategy performance
├── O-output/        → Daily scans, trade outputs, rejected trades
├── P-portfolio/     → Current positions, account status, pending orders
├── R-references/    → Best/worst trades, strategy benchmarks
└── S-strategy/      → Strategy overview, monthly targets
```

## 5 Trading Strategies
1. **Connors RSI(2)** — Mean reversion (~75% win rate)
2. **MACD + RSI** — Momentum entries (~73% win rate)
3. **Bollinger Squeeze** — Volatility breakout (~65% win rate)
4. **MA Crossover** — Trend following (~60% win rate)
5. **VIX Fear** — Buying panic (~80% win rate)

## Targets
- Monthly return: 2-4%
- Trades per month: 6-10
- Win rate: 55-65%
- Max drawdown: 10% monthly

## See Also
- [[QUICK-START]] — How to run the system
- [[WORKFLOWS]] — Daily workflow details
- [[C-core/pipeline-routing]] — How agents connect
- [[C-core/strategy-dna]] — Exact strategy parameters
- [[C-core/risk-management-rules]] — Hard limits
