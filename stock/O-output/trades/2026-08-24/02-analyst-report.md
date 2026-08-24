# Technical Analysis Report — 2026-08-24

## Ticker: TMO

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $629.27 |
| 20-Day Avg Volume | — |
| Relative Volume | 0.82x |
| ATR(14) | $16.07 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $634.70 | +0.86% |
| Support 1 | $556.01 | -11.64% |
| 200 SMA | $533.09 | -15.28% |
| 50 EMA | $541.66 | -13.91% |
| 10 EMA | $604.54 | -3.93% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | OVERSOLD FAIL | RSI(2)=96.6 (needs <10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | SETUP CONFIRMED | MACD cross=YES, RSI(14)=74.6, Price vs 50 SMA=ABOVE | **SETUP CONFIRMED** |
| Bollinger Squeeze | NO SQUEEZE | BW=12.62 (6m low=5.98), Volume=0.82x | NO SETUP |
| MA Crossover | NO PULLBACK | 10 EMA vs 50 EMA=BULLISH but no pullback zone | NO SETUP |
| VIX Fear | N/A | N/A | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $629.27 |
| Stop Loss | $605.16 (1.5x ATR below entry) |
| Take Profit | $634.70 (resistance; exit on MACD bearish cross or RSI>80) |
| Risk/Share | $24.11 |
| Reward/Share | $5.43 |
| R:R Ratio | 0.23:1 |

### Decision
**NO SETUP** — While MACD + RSI technically confirms, the R:R ratio of 0.23:1 **fails the minimum 1.0:1 threshold** for this strategy. Risk ($24.11) far exceeds reward ($5.43). The tight target relative to stop loss makes this trade unfavorable on a risk-adjusted basis. Price is also at local extremes (RSI=74.6, near resistance), suggesting limited upside. **REJECT.**

---

## Ticker: BKNG

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $209.62 |
| 20-Day Avg Volume | — |
| Relative Volume | 0.75x |
| ATR(14) | $6.81 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $216.42 | +3.26% |
| Support 1 | $180.59 | -13.85% |
| 200 SMA | $185.11 | -11.71% |
| 50 EMA | $188.06 | -10.30% |
| 10 EMA | $208.84 | -0.37% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO OVERSOLD | RSI(2)=41.6 (needs <10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | NO CROSS | MACD cross=NO, RSI(14)=60.8, MACD histogram=-0.64 | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | BW=16.58 (6m low=6.85), No breakout, Volume=0.75x | NO SETUP |
| MA Crossover | SETUP CONFIRMED | Pullback zone=YES (within 1%), Price above 10 EMA=YES, RSI(14)=60.8 | **SETUP CONFIRMED** |
| VIX Fear | N/A | N/A | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $209.62 |
| Stop Loss | $199.41 (1.5x ATR below entry) |
| Take Profit | $216.42 (resistance; exit on EMA bearish cross) |
| Risk/Share | $10.21 |
| Reward/Share | $6.80 |
| R:R Ratio | 0.67:1 |

### Decision
**NO SETUP** — While MA Crossover technically confirms a pullback setup, the R:R ratio of 0.67:1 **fails the minimum 1.5:1 threshold** for this strategy. Risk ($10.21) exceeds reward ($6.80) unfavorably. Additionally, relative volume is weak (0.75x), which reduces confidence in the bounce confirmation. **REJECT.**

---

## Ticker: JPM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $351.58 |
| 20-Day Avg Volume | — |
| Relative Volume | 1.30x |
| ATR(14) | $6.23 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $366.50 | +4.24% |
| Support 1 | $343.78 | -2.21% |
| 200 SMA | $313.83 | -10.73% |
| 50 EMA | $343.50 | -2.29% |
| 10 EMA | $357.14 | +1.58% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | SETUP CONFIRMED | RSI(2)=7.3 (<10 OVERSOLD), Price vs 200 SMA=ABOVE | **SETUP CONFIRMED** |
| MACD + RSI | NO CROSS | MACD cross=NO, RSI(14)=48.6, MACD histogram=-1.92 | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | BW=5.75 (6m low=3.17), No breakout, Volume=1.3x | NO SETUP |
| MA Crossover | NO SETUP | Pullback zone=YES but price below 10 EMA | NO SETUP |
| VIX Fear | N/A | N/A | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $351.58 |
| Stop Loss | $339.12 (2x ATR below entry) |
| Take Profit | $356.92 (close above 5-day SMA) |
| Risk/Share | $12.46 |
| Reward/Share | $5.34 |
| R:R Ratio | 0.43:1 |

### Decision
**NO SETUP** — Connors RSI(2) technically confirms (RSI=7.3, price above 200 SMA), but the R:R ratio of 0.43:1 **fails the minimum 0.5:1 threshold** for this strategy by a narrow margin. Risk ($12.46) is 2.3x reward ($5.34), creating unfavorable odds. Mean reversion trades depend on favorable risk-reward; this setup does not meet it. Relative volume (1.3x) is the sole positive. **REJECT.**

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $344.82 |
| 20-Day Avg Volume | — |
| Relative Volume | 0.78x |
| ATR(14) | $9.34 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $384.48 | +11.50% |
| Support 1 | $324.44 | -5.90% |
| 200 SMA | $332.77 | -3.50% |
| 50 EMA | $351.77 | +2.03% |
| 10 EMA | $345.81 | +0.29% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO OVERSOLD | RSI(2)=66.2 (needs <10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | NO SETUP | MACD cross=NO, RSI(14)=47.2, Price vs 50 SMA=**BELOW** | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | BW=14.46 (6m low=5.06), No breakout, Volume=0.78x | NO SETUP |
| MA Crossover | BEARISH CROSS | 10 EMA vs 50 EMA=**BEARISH**, Price below 10 EMA | NO SETUP |
| VIX Fear | N/A | N/A | N/A |

### Decision
**NO SETUP** — All five strategies fail to confirm. MACD is below signal with price below 50 EMA (bearish). MA Crossover shows a bearish 10/50 cross, not bullish. RSI(2) is elevated at 66.2, not oversold. No Bollinger Squeeze present. Relative volume is weak (0.78x). **REJECT ALL STRATEGIES.**

---

## Summary

| Ticker | Setup Status | Strategy | Verdict |
|--------|--------------|----------|---------|
| TMO | REJECTED | MACD + RSI (R:R 0.23:1 fails min 1.0:1) | No trade |
| BKNG | REJECTED | MA Crossover (R:R 0.67:1 fails min 1.5:1) | No trade |
| JPM | REJECTED | Connors RSI(2) (R:R 0.43:1 fails min 0.5:1) | No trade |
| GOOGL | REJECTED | All strategies fail confirmation | No trade |

**Market Assessment:** Weak relative volume across all tickers (0.75x–1.3x). All confirmed setups fail risk-reward minimum thresholds. **No actionable trades identified for 2026-08-24.**