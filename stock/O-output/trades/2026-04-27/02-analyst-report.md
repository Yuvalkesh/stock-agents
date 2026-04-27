# Technical Analysis Report — 2026-04-27

## Ticker: SPY

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $713.94 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.66x |
| ATR(14) | $8.64 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $714.47 | +0.07% |
| Support 1 | $629.28 | -11.85% |
| 200 SMA | $665.52 | -6.76% |
| 50 EMA | $676.07 | -5.30% |
| 10 EMA | $701.73 | -1.70% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | OVERBOUGHT | RSI(2)=78.89, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | MOMENTUM WEAK | MACD=12.51, Signal=8.71, RSI(14)=70.45, Vol=0.66x | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | Bandwidth=15.39 vs 6m Low=2.37, RSI(14)=70.45 | NO SETUP |
| MA Crossover | CONFIRMED | 10 EMA=701.73 vs 50 EMA=680.66, Price=713.94 in pullback zone | **SETUP CONFIRMED** |
| VIX Fear | NO SPIKE | VIX=18.97 vs 10d SMA=18.62, Spike=1.9% (<20%) | NO SETUP |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $713.94 |
| Stop Loss | $700.98 |
| Take Profit | $714.47 |
| Risk/Share | $12.96 |
| Reward/Share | $0.53 |
| R:R Ratio | 0.04:1 |
| Min Required | 1.5:1 |

### Decision
**NO SETUP — R:R RATIO FAILS MINIMUM THRESHOLD**

The MA Crossover setup is confirmed technically (10 EMA crossed above 50 EMA, price in pullback zone), but the risk-reward ratio of 0.04:1 is catastrophically below the 1.5:1 minimum required for this strategy. Take profit is only $0.53 above entry while risk is $12.96. Trade is not viable.

---

## Ticker: QQQ

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $663.88 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.88x |
| ATR(14) | $10.70 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $664.51 | +0.09% |
| Support 1 | $555.60 | -16.33% |
| 200 SMA | $600.09 | -9.60% |
| 50 EMA | $606.02 | -8.72% |
| 10 EMA | $642.24 | -3.26% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | EXTREME OVERBOUGHT | RSI(2)=87.24, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | MOMENTUM WEAK | MACD=16.58, Signal=11.28, RSI(14)=74.92, Vol=0.88x | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | Bandwidth=20.78 vs 6m Low=2.88, RSI(14)=74.92 | NO SETUP |
| MA Crossover | CROSSOVER YES | 10 EMA=642.24 vs 50 EMA=613.64, but NO pullback zone (price too high) | NO SETUP |
| VIX Fear | NO SPIKE | VIX=18.97 vs 10d SMA=18.62, Spike=1.9% (<20%) | NO SETUP |

### Decision
**NO SETUP**

Crossover conditions are met (10 EMA > 50 EMA bullishly established), but price has already moved too far above the 10 EMA ($663.88 vs $642.24 = 3.4% gap). No pullback zone available for entry. Market is overextended; wait for pullback before considering entry.

---

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $267.78 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.34x |
| ATR(14) | $11.83 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $275.84 | +3.02% |
| Support 1 | $198.60 | -25.78% |
| 200 SMA | $170.08 | -36.49% |
| 50 EMA | $235.17 | -12.18% |
| 10 EMA | $260.33 | -2.78% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | OVERBOUGHT | RSI(2)=71.49, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | HISTOGRAM FLATTENING | MACD=10.69, Signal=9.93, Histogram=0.77 (weak), RSI(14)=61.21 | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | Bandwidth=38.01 vs 6m Low=15.05, Price within bands | NO SETUP |
| MA Crossover | NO CROSSOVER | 10 EMA=260.33 vs 50 EMA=236.41, No recent crossover signal | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

No strategy triggers on LRCX. Good relative volume (1.34x) and RSI in moderate territory, but momentum indicators show convergence (MACD histogram narrowing). No clear directional setup present.

---

## Ticker: AMAT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $417.04 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.12x |
| ATR(14) | $14.29 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $420.50 | +0.83% |
| Support 1 | $320.69 | -23.13% |
| 200 SMA | $264.03 | -36.68% |
| 50 EMA | $366.00 | -12.24% |
| 10 EMA | $397.55 | -4.67% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | EXTREME OVERBOUGHT | RSI(2)=97.48, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | HISTOGRAM WEAK | MACD=14.38, Signal=12.11, Histogram=2.28, RSI(14)=69.34 | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | Bandwidth=28.17 vs 6m Low=7.41, Price above middle band | NO SETUP |
| MA Crossover | NO CROSSOVER | 10 EMA=397.55 vs 50 EMA=363.10, No recent crossover | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

AMAT shows strong relative volume (1.12x) but all technical indicators signal an exhausted move. RSI(2) at 97.48 is at extreme overbought levels. MACD histogram is flattening. No pullback to moving averages visible. Setup not confirmed.

---

## Ticker: AMD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $347.81 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 2.11x |
| ATR(14) | $13.82 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $352.99 | +1.49% |
| Support 1 | $192.87 | -44.55% |
| 200 SMA | $206.60 | -40.57% |
| 50 EMA | $221.57 | -36.27% |
| 10 EMA | $288.34 | -17.09% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | EXTREME OVERBOUGHT | RSI(2)=99.57, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | OVERBOUGHT | MACD=27.63, Signal=18.65, RSI(14)=88.94 (>>75), Histogram=8.98 | NO SETUP |
| Bollinger Squeeze | BREAKOUT OCCURRED | Bandwidth=63.03 vs 6m Low=9.53, Breakout=YES, Vol=2.11x, **but RSI=88.94 (overbought)** | NO SETUP |
| MA Crossover | NO CROSSOVER | 10 EMA=288.34 vs 50 EMA=236.76, No recent crossover | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

AMD shows a Bollinger Band breakout with exceptional volume (2.11x) and strong volume confirmation. However, RSI(14) at 88.94 is deep into overbought territory (>80 threshold), which disqualifies the Bollinger Squeeze setup. The move is exhausted. Wait for pullback or RSI mean reversion to 50-60 range before reconsidering.

---

## Ticker: AI

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $8.64 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.85x |
| ATR(14) | $0.54 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $9.94 | +15.05% |
| Support 1 | $7.68 | -11.11% |
| 200 SMA | $15.03 | +73.95% |
| 50 EMA | $9.04 | +4.63% |
| 10 EMA | $8.92 | +3.24% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | WEAK SIGNAL | RSI(2)=26.71, **Price vs 200 SMA=BELOW** (disqualifies) | NO SETUP |
| MACD + RSI | BEARISH | MACD=-0.01, Signal=-0.06, Price vs 50 SMA=BELOW, RSI(14)=45.93 | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | Bandwidth=22.37 vs 6m Low=7.95, Price near lower band | NO SETUP |
| MA Crossover | BEARISH | 10 EMA=8.92 vs 50 EMA=9.47 (10 EMA BELOW 50 EMA), Price below 10 EMA | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

AI is in a bearish structure. Price is 73.95% below 200 SMA and below both 10 EMA and 50 EMA. 10 EMA has crossed below 50 EMA (bearish). All trend filters fail. No setup confirmed. Stock does not meet minimum uptrend requirements for mean reversion strategies.

---

## Ticker: AAPL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $271.06 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.91x |
| ATR(14) | $5.88 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $275.77 | +1.75% |
| Support 1 | $245.51 | -9.40% |
| 200 SMA | $253.34 | -6.53% |
| 50 EMA | $261.65 | -3.43% |
| 10 EMA | $267.93 | -1.07% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NEUTRAL | RSI(2)=41.53, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | MOMENTUM EMERGING | MACD=4.02, Signal=2.49, Histogram=1.53, RSI(14)=59.71 | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | Bandwidth=11.99 vs 6m Low=3.25, Price above middle band | NO SETUP |
| MA Crossover | CONFIRMED | 10 EMA=267.93 vs 50 EMA=261.65, Price=271.06 in pullback zone, RSI(14)=59.71 | **SETUP CONFIRMED** |
| VIX Fear | NO SPIKE | VIX=18.97 vs 10d SMA=18.62, Spike=1.9% (<20%) | NO SETUP |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $271.06 |
| Stop Loss | $262.24 |
| Take Profit | $275.77 |
| Risk/Share | $8.82 |
| Reward/Share | $4.71 |
| R:R Ratio | 0.53:1 |
| Min Required | 1.5:1 |

### Decision
**NO SETUP — R:R RATIO FAILS MINIMUM THRESHOLD**

The MA Crossover setup is technically confirmed (10 EMA crossed above 50 EMA, price within pullback zone, RSI at healthy 59.71). However, the risk-reward ratio of 0.53:1 falls well below the required 1.5:1 minimum for this strategy. Risk of $8.82 per share vs reward of $4.71 per share represents unfavorable risk-on-reward geometry. Trade is not executable under risk management guidelines.

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $424.62 |
| 20-Day Avg Volume | N/A |
| Today's Volume