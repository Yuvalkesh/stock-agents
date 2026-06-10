# Technical Analysis Report — 2026-06-10

## Ticker: AMAT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $525.36 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.31x |
| ATR(14) | $27.24 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $532.53 | +1.4% |
| Support 1 | $396.88 | -24.5% |
| 200 SMA | $304.76 | -42.0% |
| 50 SMA | $418.94 | -20.3% |
| 10 EMA | $484.36 | -7.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=86.9, Price vs 200 SMA=ABOVE | RSI(2) ≥ 10 — not oversold |
| MACD + RSI | NO SETUP | MACD cross=NO, RSI(14)=68.5, Rel Vol=0.31x | No MACD crossover; volume weak |
| Bollinger Squeeze | NO SETUP | Bandwidth=28.35, 6m low=8.80, RSI(14)=68.5 | No squeeze condition (BW above minimum) |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA=BULLISH, Price=above 10 EMA, RSI(14)=68.5 | No pullback to 10 EMA; already extended |
| VIX Fear | N/A | N/A | Not applicable (sector stock) |

### Decision
**NO SETUP**

Data does not support entry. RSI(2) overbought at 86.9; price extended above all key moving averages; volume weak at 0.31x. No strategy meets entry criteria.

---

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $342.68 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.31x |
| ATR(14) | $19.09 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $349.09 | +1.9% |
| Support 1 | $263.71 | -23.0% |
| 200 SMA | $201.73 | -41.1% |
| 50 SMA | $280.47 | -18.1% |
| 10 EMA | $324.91 | -5.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=83.14, Price vs 200 SMA=ABOVE | RSI(2) ≥ 10 — not oversold |
| MACD + RSI | **SETUP CONFIRMED** | MACD cross=YES, RSI(14)=63.78, Price vs 50 SMA=ABOVE | MACD bullish crossover; RSI in range 35-75 |
| Bollinger Squeeze | NO SETUP | Bandwidth=25.87, 6m low=11.03, RSI(14)=63.8 | No squeeze; no breakout |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA=BULLISH, Price above 10 EMA, RSI(14)=63.8 | No pullback to 10 EMA |
| VIX Fear | N/A | N/A | Not applicable (sector stock) |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $342.68 |
| Stop Loss | $314.05 (1.5x ATR below entry) |
| Take Profit | $349.09 (resistance) |
| Risk/Share | $28.63 |
| Reward/Share | $6.41 |
| R:R Ratio | 0.22:1 |

### Risk Assessment
**⚠️ WARNING: R:R Ratio 0.22:1 FAILS minimum strategy requirement of 1.0:1**

Setup confirmed on MACD + RSI mechanics, but reward-to-risk is severely unfavorable. Risk is 4.5x the potential reward. Volume is weak (0.31x). **Trade is NOT recommended despite setup confirmation.**

### Decision
**SETUP CONFIRMED [MACD + RSI] — BUT REJECTED FOR EXECUTION**

Mechanics align (MACD cross, RSI 63.78 in sweet spot), but risk/reward geometry is broken. Entry $342.68 vs take profit $349.09 is only $6.41 upside against $28.63 downside risk. Do not trade this setup. Await better entry or exit signal.

---

## Ticker: MRVL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $263.67 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.27x |
| ATR(14) | $25.69 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $324.20 | +22.9% |
| Support 1 | $162.85 | -38.2% |
| 200 SMA | $106.44 | -59.6% |
| 50 SMA | $176.12 | -33.2% |
| 10 EMA | $259.48 | -1.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=29.84, Price vs 200 SMA=ABOVE | RSI(2) ≥ 10 — not extreme oversold |
| MACD + RSI | NO SETUP | MACD cross=NO, RSI(14)=61.31, Price vs 50 SMA=ABOVE | No MACD crossover; histogram positive but no cross |
| Bollinger Squeeze | NO SETUP | Bandwidth=84.12, 6m low=10.06, RSI(14)=61.3 | No squeeze; wide bands |
| MA Crossover | **SETUP CONFIRMED** | 10 EMA vs 50 EMA=BULLISH, Price in pullback zone (1.6% below 10 EMA), RSI(14)=61.31 | Price near 10 EMA; bullish EMA alignment |
| VIX Fear | N/A | N/A | Not applicable (sector stock) |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $263.67 |
| Stop Loss | $225.14 (1.5x ATR below entry) |
| Take Profit | $324.20 (resistance) |
| Risk/Share | $38.53 |
| Reward/Share | $60.53 |
| R:R Ratio | 1.57:1 |

### Risk Assessment
**✓ PASS: R:R Ratio 1.57:1 exceeds minimum strategy requirement of 1.5:1**

Clean MA crossover setup. 10 EMA (259.48) bullish above 50 EMA (187.69). Price touching pullback zone just 1.6% below 10 EMA. RSI 61.31 confirms momentum without overbought extremes. R:R 1.57:1 valid. Volume weak (0.27x) is noted but acceptable for MA crossover strategy.

### Decision
**SETUP CONFIRMED [MA Crossover (10 EMA / 50 EMA)]**

Price at $263.67 represents pullback entry into established 10/50 EMA bullish crossover. Stop at $225.14 gives 38.53 risk per share. Target $324.20 (resistance) offers 60.53 reward. Setup geometry meets all criteria. Proceed with trade execution.

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $402.79 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.20x |
| ATR(14) | $12.28 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $466.32 | +15.8% |
| Support 1 | $397.47 | -1.3% |
| 200 SMA | $452.99 | +12.5% |
| 50 SMA | $410.44 | +1.9% |
| 10 EMA | $417.95 | +3.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=2.89 (OVERSOLD), Price vs 200 SMA=BELOW | RSI(2) < 10 but price BELOW 200 SMA — no uptrend |
| MACD + RSI | NO SETUP | MACD cross=NO, RSI(14)=41.70, Price vs 50 SMA=BELOW | MACD bearish (histogram -3.82); price below 50 SMA |
| Bollinger Squeeze | NO SETUP | Bandwidth=13.85, 6m low=4.08, RSI(14)=41.7 | No squeeze; bandwidth above minimum |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA=BULLISH, Price below 10 EMA, RSI(14)=41.7 | Price $402.79 below both 10 EMA ($417.95) and 50 SMA ($410.44) |
| VIX Fear | N/A | N/A | Not applicable (covered under equity strategy) |

### Decision
**NO SETUP**

Price below 200 SMA ($452.99) and below both 10 EMA and 50 SMA. MACD bearish with negative histogram. RSI(2) oversold but trend filter (200 SMA) negates Connors signal. Volume weak (0.20x). Stock in correction; no confirmation for entry. Wait for recovery above 50 SMA.

---

## Ticker: QCOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $198.68 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.15x |
| ATR(14) | $17.09 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $258.96 | +30.4% |
| Support 1 | $190.32 | -4.2% |
| 200 SMA | $163.58 | -17.7% |
| 50 SMA | $180.42 | -9.2% |
| 10 EMA | $220.08 | +10.8% |

### Strategy Scorecard
|