# Technical Analysis Report — 2026-07-27

## Ticker: NET

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $269.09 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.02x |
| ATR(14) | $12.85 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $291.00 | +8.2% |
| Support 1 | $220.95 | -17.9% |
| 200 SMA | $211.99 | -21.2% |
| 50 EMA | $242.02 | -10.0% |
| 10 EMA | $268.46 | -0.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | Oversold Check Failed | RSI(2)=60.4, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | No Crossover | MACD=8.88, Signal=10.21, RSI(14)=57.4, Volume=0.02x | NO SETUP |
| Bollinger Squeeze | No Squeeze Active | Bandwidth=20.57 (6m low=12.63), Breakout=NO, RSI=57.4 | NO SETUP |
| MA Crossover | R:R Ratio Fails | 10 EMA=268.46 vs 50 EMA=246.16 (BULLISH), RSI=57.4 | NO SETUP |
| VIX Fear | Not Applicable | N/A | NO SETUP |

### Decision
**NO SETUP**

**Rationale:** NET shows bullish technicals (10 EMA > 50 EMA, price above 200 SMA), but the MA Crossover setup fails the minimum R:R threshold (1.14:1 vs. required 1.5:1). Volume is critically weak at 0.02x relative volume, which invalidates all entry confidence. No other strategy triggers. The setup is rejected.

---

## Ticker: SNOW

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $275.18 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.04x |
| ATR(14) | $13.19 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $279.49 | +1.6% |
| Support 1 | $222.45 | -19.2% |
| 200 SMA | $209.59 | -23.8% |
| 50 EMA | $235.24 | -14.5% |
| 10 EMA | $268.95 | -2.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | Overbought | RSI(2)=79.2 (threshold < 10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | No Crossover | MACD=10.65, Signal=12.29, RSI(14)=64.5, Volume=0.04x | NO SETUP |
| Bollinger Squeeze | Squeeze Active But No Breakout | Bandwidth=11.16 (at 6m low), Price=275.18 vs Upper=279.85, RSI=64.5 | NO SETUP |
| MA Crossover | R:R Ratio Fails | 10 EMA=268.95 vs 50 EMA=237.82 (BULLISH), RSI=64.5 | NO SETUP |
| VIX Fear | Not Applicable | N/A | NO SETUP |

### Decision
**NO SETUP**

**Rationale:** SNOW triggers MA Crossover conditions structurally (bullish EMA crossover, price in pullback zone, RSI neutral), but the R:R ratio is severely unfavorable at 0.22:1 (required minimum 1.5:1). The risk/reward is inverted: $19.78 risk for only $4.31 reward. Volume is extremely weak at 0.04x, providing no confirmation. Bollinger Squeeze shows active volatility compression at 6-month lows, but price has not broken above the upper band. The setup is rejected.

---

## Summary

**Date:** 2026-07-27  
**Tickers Analyzed:** 2  
**Confirmed Setups:** 0  
**Rejected Setups:** 2

### Key Observations
- Both NET and SNOW exhibit bullish technical alignment (price above 200 SMA, 10 EMA > 50 EMA), but neither meets entry criteria for viable trades.
- Volume is critically weak across both tickers (0.02x–0.04x relative), violating minimum volume thresholds for all strategies.
- MA Crossover setups on both tickers fail the R:R minimum threshold of 1.5:1, making risk/reward untenable.
- SNOW shows Bollinger Bandwidth at 6-month lows, indicating volatility compression, but no breakout has occurred yet.
- **No trades to execute on 2026-07-27.**