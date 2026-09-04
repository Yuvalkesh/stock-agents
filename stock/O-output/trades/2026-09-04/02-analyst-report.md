# Technical Analysis Report — 2026-09-04

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $501.98 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.19x |
| ATR(14) | $11.68 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $517.78 | +3.16% |
| Support 1 | $476.25 | -5.14% |
| 200 SMA | $429.38 | -14.50% |
| 50 EMA | $443.61 | -11.58% |
| 10 EMA | $500.22 | -0.35% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=40.71, Price vs 200 SMA=ABOVE | RSI(2) >= 10 (fails threshold) | NO SETUP |
| MACD + RSI | MACD cross=NO, RSI(14)=61.0, Volume=0.19x | Histogram negative (-2.21), weak volume | NO SETUP |
| Bollinger Squeeze | BW=8.21, 6m low=5.20 | No squeeze, no breakout, weak volume | NO SETUP |
| MA Crossover | EMA10 vs EMA50=BULLISH, Pullback=YES | Price above 10 EMA, RSI(14)=61.0 | **SETUP (Technical)** |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $501.98 |
| Stop Loss | $484.46 |
| Take Profit | $517.78 |
| Risk/Share | $17.52 |
| Reward/Share | $15.80 |
| R:R Ratio | 0.9:1 |

### Decision
**NO SETUP** — MA Crossover setup is technically present (bullish EMA10/EMA50, price in pullback zone), but **R:R ratio of 0.9:1 fails minimum threshold of 1.5:1**. Risk-to-reward is unfavorable. Strategy disqualified.

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $338.86 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.26x |
| ATR(14) | $8.08 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $357.61 | +5.54% |
| Support 1 | $332.82 | -1.79% |
| 200 SMA | $335.71 | -0.93% |
| 50 EMA | $348.58 | +2.86% |
| 10 EMA | $341.10 | +0.66% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=42.09, Price vs 200 SMA=ABOVE | RSI(2) >= 10 (fails threshold) | NO SETUP |
| MACD + RSI | MACD cross=NO, Price vs 50 SMA=BELOW, Volume=0.26x | Price below 50 EMA, histogram negative | NO SETUP |
| Bollinger Squeeze | BW=5.38, 6m low=5.06 | Near squeeze but no breakout, weak volume | NO SETUP |
| MA Crossover | EMA10 vs EMA50=BEARISH, Pullback=YES, Price Above EMA10=NO | EMA10 < EMA50, price below 10 EMA | NO SETUP |

### Decision
**NO SETUP** — No strategies qualify. Price below 50 EMA, EMA10 in bearish configuration, weak volume (0.26x). Market structure unfavorable for entry.

---

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $233.48 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.42x |
| ATR(14) | $7.38 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $234.76 | +0.55% |
| Support 1 | $207.25 | -11.21% |
| 200 SMA | $196.54 | -15.82% |
| 50 EMA | $210.63 | -9.78% |
| 10 EMA | $223.02 | -4.47% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=92.21, Price vs 200 SMA=ABOVE | RSI(2) >> 10 (extreme overbought), fails threshold | NO SETUP |
| MACD + RSI | MACD cross=YES, RSI(14)=62.18, Volume=0.42x | Histogram positive (1.04), price above 50 SMA | **SETUP (Technical)** |
| Bollinger Squeeze | BW=11.41, 6m low=7.76 | Breakout=YES, but weak volume, BW not at extreme | NO SETUP |
| MA Crossover | EMA10 vs EMA50=BULLISH, Pullback zone=NO | Price well above 10 EMA, no pullback entry zone | NO SETUP |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $233.48 |
| Stop Loss | $222.41 |
| Take Profit | $234.76 |
| Risk/Share | $11.07 |
| Reward/Share | $1.28 |
| R:R Ratio | 0.12:1 |

### Decision
**NO SETUP** — MACD + RSI setup is technically present (bullish MACD cross, RSI in range), but **R:R ratio of 0.12:1 catastrophically fails minimum threshold of 1.0:1**. Reward is only 11.5% of risk. Setup disqualified due to severely unfavorable risk-to-reward.

---

## Ticker: SLB

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $56.66 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.17x |
| ATR(14) | $1.87 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $60.15 | +6.16% |
| Support 1 | $50.41 | -11.06% |
| 200 SMA | $48.55 | -14.37% |
| 50 EMA | $50.53 | -10.81% |
| 10 EMA | $56.25 | -0.72% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=28.44, Price vs 200 SMA=ABOVE | RSI(2) >= 10 (fails threshold) | NO SETUP |
| MACD + RSI | MACD cross=NO, RSI(14)=59.53, Volume=0.17x | Histogram positive (0.23), but no crossover | NO SETUP |
| Bollinger Squeeze | BW=15.91, 6m low=6.56 | Wide bands, no squeeze, weak volume | NO SETUP |
| MA Crossover | EMA10 vs EMA50=BULLISH, Pullback=YES, Above EMA10=YES | Price in pullback zone, RSI(14)=59.5 | **SETUP (Technical)** |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $56.66 |
| Stop Loss | $53.85 |
| Take Profit | $60.15 |
| Risk/Share | $2.81 |
| Reward/Share | $3.49 |
| R:R Ratio | 1.24:1 |

### Decision
**NO SETUP** — MA Crossover setup is technically present (bullish EMA configuration, price in pullback zone), but **R:R ratio of 1.24:1 fails minimum threshold of 1.5:1**. Insufficient reward-to-risk margin. Setup disqualified.

---

## Ticker: CRWD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $215.43 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.20x |
| ATR(14) | $12.34 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $233.88 | +8.57% |
| Support 1 | $181.24 | -15.85% |
| 200 SMA | $142.50 | -33.87% |
| 50 EMA | $200.86 | -6.73% |
| 10 EMA | $211.60 | -1.78% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=59.39, Price vs 200 SMA=ABOVE | RSI(2) >= 10 (fails threshold) | NO SETUP |
| MACD + RSI | MACD cross=NO, RSI(14)=54.16, Volume=0.20x | Histogram positive (0.32), but no crossover | NO SETUP |
| Bollinger Squeeze | BW=26.74, 6m low=15.44 | Wide bands, no squeeze, weak volume | NO SETUP |
| MA Crossover | EMA10 vs EMA50=BULLISH, Pullback=YES, Above EMA10=YES | Price in pullback zone, RSI(14)=54.2 | **SETUP (Technical)** |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $215.43 |
| Stop Loss | $196.92 |
| Take Profit | $233.88 |
| Risk/Share | $18.51 |
| Reward/Share | $18.45 |
| R:R Ratio | 1.0:1 |

### Decision
**NO SETUP** — MA Crossover setup is technically present (bullish EMA configuration, price in pullback zone), but **R:R ratio of 1.0:1 fails minimum threshold of 1.5:1**. Insufficient reward-to-risk ratio. Setup disqualified.

---

## Ticker: JPM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $357.82 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.18x |
| ATR(14) | $5.85 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $366.