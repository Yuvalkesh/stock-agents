# Strategy Benchmarks

## Performance Targets per Strategy

| Strategy | Target Win Rate | Target Avg R | Min Trades to Evaluate |
|----------|----------------|--------------|----------------------|
| Connors RSI(2) | 75% | 1.2R | 10 trades |
| MACD + RSI | 73% | 1.5R | 10 trades |
| Bollinger Squeeze | 65% | 2.0R | 8 trades |
| MA Crossover | 60% | 2.0R | 10 trades |
| VIX Fear | 80% | 1.0R | 5 trades |

## Benchmark Indices
| Benchmark | Purpose |
|-----------|---------|
| S&P 500 (SPY) | Beat this = we're doing well |
| 60/40 Portfolio | Beat this = risk-adjusted value add |
| Risk-Free Rate (~5%) | Absolute minimum acceptable |

## Strategy Retirement Criteria
A strategy should be paused for review if:
- Win rate drops 15% below target over 10+ trades
- Average R drops below 0.5R over 10+ trades
- 5 consecutive losses on same strategy
- Cumulative P&L turns negative after 15+ trades

## Strategy Promotion Criteria
A strategy earns more allocation if:
- Win rate exceeds target by 10%+ over 15+ trades
- Average R exceeds target by 0.5R+ over 15+ trades
- No losing streak > 3 trades

## Monthly Comparison Template
| Metric | Our System | S&P 500 | Notes |
|--------|-----------|---------|-------|
| Monthly Return | % | % | |
| Win Rate | % | N/A | |
| Max Drawdown | % | % | |
| Sharpe Ratio | | | |
| Trades Taken | | N/A | |
