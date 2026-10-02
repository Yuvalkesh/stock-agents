# Technical Analysis Report — 2026-10-02

## Ticker: AMD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $631.92 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.53x |
| ATR(14) | $24.21 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $645.46 | 2.1% |
| Support 1 | $458.00 | -27.5% |
| 200 SMA | $374.71 | -40.8% |
| 50 EMA | $513.49 | -18.8% |
| 10 EMA | $605.34 | -4.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=92.77 (>10), Price > 200 SMA (YES) | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=69.76, Rel Vol=0.53x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=39.00 (6m low=11.36), Vol=0.53x | NO SETUP |
| MA Crossover | FAIL | 10 EMA > 50 EMA (YES), No pullback zone | NO SETUP |
| VIX Fear | N/A | Equity ticker only | N/A |

### Decision
**NO SETUP**

All strategies rejected. RSI(2) is overbought (92.77). Volume is weak across all setups (0.53x). No meaningful pullback or momentum setup available.

---

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $236.35 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.76x |
| ATR(14) | $5.90 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $237.87 | 0.6% |
| Support 1 | $208.93 | -11.6% |
| 200 SMA | $200.39 | -15.2% |
| 50 EMA | $218.17 | -7.7% |
| 10 EMA | $228.23 | -3.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=96.72 (>10), Price > 200 SMA (YES) | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=64.92, Rel Vol=0.76x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=11.52 (6m low=9.27), Vol=0.76x | NO SETUP |
| MA Crossover | FAIL | 10 EMA > 50 EMA (YES), No pullback zone | NO SETUP |
| VIX Fear | N/A | Equity ticker only | N/A |

### Decision
**NO SETUP**

All strategies rejected. RSI(2) is overbought (96.72). Price is touching upper resistance. No pullback zone detected. Volume weak.

---

## Ticker: DDOG

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $279.36 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.26x |
| ATR(14) | $11.85 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $281.99 | 0.9% |
| Support 1 | $203.24 | -27.2% |
| 200 SMA | $184.84 | -33.9% |
| 50 EMA | $244.70 | -12.4% |
| 10 EMA | $264.02 | -5.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=99.61 (>10), Price > 200 SMA (YES) | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=71.44, Rel Vol=0.26x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=35.73 (6m low=10.99), Vol=0.26x | NO SETUP |
| MA Crossover | FAIL | 10 EMA > 50 EMA (YES), No pullback zone, Rel Vol=0.26x | NO SETUP |
| VIX Fear | N/A | Equity ticker only | N/A |

### Decision
**NO SETUP**

All strategies rejected. RSI(2) is overbought (99.61). Volume critically weak (0.26x). No pullback zone. Price near resistance.

---

## Ticker: NET

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $351.54 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.45x |
| ATR(14) | $15.98 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $367.43 | 4.5% |
| Support 1 | $271.72 | -22.7% |
| 200 SMA | $235.22 | -33.1% |
| 50 EMA | $307.78 | -12.4% |
| 10 EMA | $346.83 | -1.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=61.69 (>10), Price > 200 SMA (YES) | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=61.60, Rel Vol=0.45x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=27.87 (6m low=9.13), Vol=0.45x | NO SETUP |
| MA Crossover | TRIGGER | 10 EMA > 50 EMA (YES), Pullback zone (YES) | TRIGGERED |
| VIX Fear | N/A | Equity ticker only | N/A |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $351.54 |
| Stop Loss | $327.57 |
| Take Profit | $367.43 |
| Risk/Share | $23.97 |
| Reward/Share | $15.89 |
| R:R Ratio | 0.66:1 |

### Decision
**NO SETUP**

MA Crossover triggered but **R:R ratio FAILS validation**. Minimum required 1.5:1; actual ratio is 0.66:1. Risk is 1.5x reward — unfavorable risk/reward structure. Entry parameters are sound, but asymmetric payoff rejects this setup per strategy rules.

---

## Ticker: MRVL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $275.46 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.52x |
| ATR(14) | $13.01 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $280.00 | 1.6% |
| Support 1 | $210.87 | -23.4% |
| 200 SMA | $166.88 | -39.4% |
| 50 EMA | $226.79 | -17.6% |
| 10 EMA | $260.42 | -5.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=94.32 (>10), Price > 200 SMA (YES) | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=66.11, Rel Vol=0.52x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=28.57 (6m low=18.23), Vol=0.52x | NO SETUP |
| MA Crossover | FAIL | 10 EMA > 50 EMA (YES), No pullback zone | NO SETUP |
| VIX Fear | N/A | Equity ticker only | N/A |

### Decision
**NO SETUP**

All strategies rejected. RSI(2) overbought (94.32). No pullback zone. Volume weak. Price near resistance.

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $342.96 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.46x |
| ATR(14) | $9.00 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $364.17 | 6.2% |
| Support 1 | $327.74 | -4.4% |
| 200 SMA | $338.54 | -1.3% |
| 50 EMA | $344.22 | 0.4% |
| 10 EMA | $342.72 | -0.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=62.81 (>10), Price > 200 SMA (YES) | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=49.58, Price < 50 SMA | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=6.87 (6m low=4.07), Vol=0.46x | NO SETUP |
| MA Crossover | TRIGGER | 10 EMA < 50 EMA (BEARISH), Pullback zone (YES) | TRIGGERED |
| VIX Fear | N/A | Equity ticker only | N/A |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $342.96 |
| Stop Loss | $329.46 |
| Take Profit | $364.17 |
| Risk/Share | $13.50 |
| Reward/Share | $21.21 |
| R:R Ratio | 1.57:1 |

### Decision
**SETUP CONFIRMED [MA Crossover]**

MA Crossover setup triggered with valid R:R ratio (1.57:1