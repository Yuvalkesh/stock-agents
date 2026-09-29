# Technical Analysis Report — 2026-09-29

## Ticker: AMD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $611.47 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.44x |
| ATR(14) | $24.77 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $639.00 | +4.49% |
| Support 1 | $440.50 | -27.96% |
| 200 SMA | $368.64 | -39.75% |
| 50 EMA | $509.11 | -16.74% |
| 10 EMA | $592.97 | -3.01% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=37.51, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD histogram=8.84, RSI(14)=66.2, No crossover | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=45.59 (not at 6m low of 11.36), No breakout | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BULLISH, No pullback to 10 EMA zone | NO SETUP |
| VIX Fear | N/A | Not applicable to individual ticker | N/A |

### Decision
**NO SETUP**

All five strategies fail entry criteria. Price is extended above 10 EMA with weak relative volume (0.44x). No mean reversion opportunity. No MACD crossover. No volatility squeeze. No pullback to moving average. Data does not support entry.

---

## Ticker: MRVL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $262.01 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.50x |
| ATR(14) | $13.40 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $267.48 | +2.08% |
| Support 1 | $200.62 | -23.42% |
| 200 SMA | $164.13 | -37.34% |
| 50 EMA | $223.18 | -14.84% |
| 10 EMA | $252.27 | -3.74% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=67.83, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD histogram=2.35, RSI(14)=61.12, No crossover | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=31.82 (not at 6m low of 18.23), No breakout | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BULLISH, No pullback to 10 EMA zone | NO SETUP |
| VIX Fear | N/A | Not applicable to individual ticker | N/A |

### Decision
**NO SETUP**

All five strategies fail entry criteria. RSI(2) is elevated at 67.83 (no mean reversion). No MACD crossover signal. No volatility squeeze. Price is extended above 10 EMA with weak volume (0.50x). No pullback opportunity. Data does not support entry.

---

## Ticker: NET

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $351.49 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.25x |
| ATR(14) | $17.25 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $367.43 | +4.53% |
| Support 1 | $269.30 | -23.36% |
| 200 SMA | $233.00 | -33.69% |
| 50 EMA | $302.84 | -13.80% |
| 10 EMA | $343.90 | -2.14% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=42.97, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD histogram=2.33, RSI(14)=62.35, No crossover | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=34.92 (not at 6m low of 9.13), No breakout | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA vs 50 EMA=BULLISH, In pullback zone (within 1.0% of 10 EMA), RSI(14)=62.35 | SETUP MEETS CRITERIA |
| VIX Fear | N/A | Not applicable to individual ticker | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $351.49 |
| Stop Loss | $325.62 (1.5x ATR below entry) |
| Take Profit | $367.43 (Resistance / EMA bearish cross exit) |
| Risk/Share | $25.87 |
| Reward/Share | $15.94 |
| R:R Ratio | 0.62:1 |

### Decision
**NO SETUP — MA CROSSOVER FAILS MINIMUM R:R REQUIREMENT**

MA Crossover strategy meets technical entry criteria (10 EMA/50 EMA bullish, pullback to 10 EMA zone, RSI 62.35 in range). However, pre-computed risk/reward analysis shows R:R Ratio of 0.62:1, which FAILS the strategy minimum requirement of 1.5:1. Risk of $25.87 exceeds reward of $15.94 by a significant margin. Trade is unfavorable on a risk-adjusted basis. **NO ENTRY.**

---

## Ticker: DDOG

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $264.11 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.39x |
| ATR(14) | $12.71 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $280.70 | +6.28% |
| Support 1 | $203.24 | -23.05% |
| 200 SMA | $182.86 | -30.76% |
| 50 EMA | $242.92 | -8.01% |
| 10 EMA | $252.56 | -4.35% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=48.41, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD histogram=5.12, RSI(14)=63.58, No crossover | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=31.72 (not at 6m low of 10.99), No breakout | NO SETUP |
| MA Crossover | FAIL | Crossover=YES (recent), Price NOT in pullback zone (4.35% above 10 EMA) | NO SETUP |
| VIX Fear | N/A | Not applicable to individual ticker | N/A |

### Decision
**NO SETUP**

MA Crossover crossover occurred recently (within 10 days), but price has already moved 4.35% above the 10 EMA and is outside the pullback zone (>1.0% tolerance). Price is extended from entry point. Relative volume is weak (0.39x). Other four strategies fail entirely. Data does not support entry.

---

## Ticker: ORCL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $137.94 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.88x |
| ATR(14) | $7.28 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $170.70 | +23.76% |
| Support 1 | $131.58 | -4.63% |
| 200 SMA | $162.96 | +18.15% |
| 50 EMA | $142.70 | +3.45% |
| 10 EMA | $141.68 | +2.71% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=58.68, Price vs 200 SMA=BELOW (bearish filter) | NO SETUP |
| MACD + RSI | FAIL | MACD histogram=-1.81, Price vs 50 SMA=BELOW (bearish filter) | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=21.54 (not at 6m low of 10.51), No breakout, Volume weak | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BEARISH, Price BELOW 10 EMA | NO SETUP |
| VIX Fear | N/A | Not applicable to individual ticker | N/A |

### Decision
**NO SETUP**

Price is below 200 SMA ($162.96), below 50 EMA ($142.70), and below 10 EMA ($141.68). All trend filters are bearish. MACD histogram is negative. 10 EMA / 50 EMA are in bearish crossover configuration. This is a downtrend. No long entry signals qualify. Data does not support entry.

---

## Ticker: LUMN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $5.53 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.25x |
| ATR(14) | $0.32 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $7.27 | +31.46% |
| Support 1 | $5.49 | -0.72% |
| 200 SMA | $7.59 | +37.25% |
| 50 EMA | $6.35 | +14.83% |
| 10 EMA | $6.01 | +8.66% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=0.55 (oversold), Price vs 200 SMA=BELOW (bearish filter) | NO SETUP |
| MACD + RSI | FAIL | RSI(14)=30.73 (out of range <35), Price vs 50 SMA=BELOW