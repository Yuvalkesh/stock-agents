# Risk Management Rules

## Hard Limits — Zero Tolerance

These rules are non-negotiable. The Gatekeeper (Agent 05) enforces every single one. If ANY rule is violated, the trade is rejected immediately.

### Position-Level Rules
| Rule | Limit | Rationale |
|------|-------|-----------|
| Max risk per trade | 1% of equity | A single bad trade can never hurt us badly |
| Max single position size | 15% of equity | No concentration risk |
| Stop loss required | ATR-based, always set | Every trade has a defined exit |
| Min R:R ratio | Strategy-specific (0.5-1.5) | Only take trades where upside justifies risk per strategy |
| Earnings buffer | No trade within 3 trading days of earnings | Binary events are gambling, not trading |

### Portfolio-Level Rules
| Rule | Limit | Rationale |
|------|-------|-----------|
| Max open positions | 6 | Focus on quality, not quantity |
| Max total exposure | 70% of equity | Always keep dry powder |
| Max correlated positions | 2 in same sector | Don't stack the same bet |
| Max daily loss | 3% of equity | Stop trading if we're bleeding |
| Max monthly drawdown | 10% of equity | Circuit breaker for bad months |
| Max quarterly drawdown | 20% of equity | Major circuit breaker |

### Daily Circuit Breakers
| Trigger | Action |
|---------|--------|
| Daily loss reaches 2% | Reduce position sizes by 50% |
| Daily loss reaches 3% | STOP all new trades for the day |
| 3 consecutive losing trades | Review all positions, no new entries for 24h |
| Monthly drawdown reaches 7% | Reduce to 2 max positions, half size |
| Monthly drawdown reaches 10% | STOP all trading for remainder of month |

## Position Sizing Formula

```
Risk Amount = Account Equity × 0.01 (1%)
Stop Distance = ATR(14) × multiplier (strategy-specific)
Shares = Risk Amount / Stop Distance
Position Value = Shares × Entry Price
```

### Position Size Validation
1. `Shares × Entry Price` must be <= 15% of equity
2. `Total exposure + new position` must be <= 70% of equity
3. `Risk Amount` must be <= 1% of equity
4. If any check fails, reduce shares until all pass

## Stop Loss Rules

### ATR-Based Stops (Primary Method)
| Strategy | Stop Distance |
|----------|--------------|
| Connors RSI(2) | 2.0 × ATR(14) |
| MACD + RSI | 1.5 × ATR(14) |
| Bollinger Squeeze | Lower BB at entry |
| MA Crossover | 1.5 × ATR(14) or below 50 EMA |
| VIX Fear | 3% (SPY) / 4% (QQQ) fixed |

### Stop Loss Non-Negotiables
- Every trade MUST have a stop loss set at order entry (bracket order)
- Stops are NEVER widened after entry
- Stops may be tightened (trailed) but never loosened
- Mental stops don't count — must be actual orders

## Trade Management Rules

### Adding to Positions
- NEVER add to a losing position
- May add to a winning position only if:
  - Original position is profitable by at least 1R
  - Total position stays within 15% limit
  - Stop is moved to breakeven on original position

### Scaling Out
- Optional: Take 50% profits at 1R, let rest ride to target
- Move stop to breakeven after taking partial profits

### Holding Period
- Minimum hold: 1 trading day (no same-day exits unless stopped out)
- Maximum hold: 15 trading days (reassess if still open)
- If a trade hasn't moved after 5 days, consider closing for opportunity cost

## What We DON'T Do
- No options trading
- No leverage / margin
- No penny stocks (minimum $10 price)
- No pre-market or after-hours trading
- No averaging down
- No revenge trading (chasing losses)
- No FOMO entries (if we missed it, we missed it)
- No trading during major news events we can't quantify
