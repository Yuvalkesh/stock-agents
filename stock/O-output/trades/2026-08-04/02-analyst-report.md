# Technical Analysis Report — 2026-08-04

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $206.64 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.99x |
| ATR(14) | $7.79 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $214.39 | +3.7% |
| Support 1 | $190.01 | -8.1% |
| 200 SMA | $193.06 | -6.6% |
| 50 EMA | $205.79 | -0.4% |
| 10 EMA | $201.33 | -2.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=88.9, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=53.1, Volume=0.99x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=12.03, 6m Low=6.82, Breakout=NO | NO SETUP |
| MA Crossover | FAIL | 10 EMA < 50 EMA (bearish), No crossover | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

---

## Ticker: META

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $590.24 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.33x |
| ATR(14) | $26.30 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $686.08 | +16.2% |
| Support 1 | $524.49 | -11.2% |
| 200 SMA | $633.00 | +7.2% |
| 50 EMA | $601.71 | +1.9% |
| 10 EMA | $590.06 | -0.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=76.4, Price < 200 SMA (downtrend) | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=47.0, Price < 50 SMA | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=24.31, 6m Low=5.03, No squeeze | NO SETUP |
| MA Crossover | FAIL | 10 EMA < 50 EMA (bearish), No crossover | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $487.65 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.76x |
| ATR(14) | $16.79 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $491.65 | +0.8% |
| Support 1 | $373.35 | -23.4% |
| 200 SMA | $432.14 | -11.4% |
| 50 EMA | $400.74 | -17.8% |
| 10 EMA | $426.30 | -12.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=99.0, Extreme overbought | NO SETUP |
| MACD + RSI | FAIL | RSI(14)=78.3 (>75, out of range) | NO SETUP |
| Bollinger Squeeze | FAIL | Price broke above upper band BUT RSI(14)=78.3 (overbought) | NO SETUP |
| MA Crossover | FAIL | Crossover exists but price NOT in pullback zone (far above 10 EMA) | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

---

## Ticker: AMZN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $284.02 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.88x |
| ATR(14) | $9.95 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $287.20 | +1.1% |
| Support 1 | $226.16 | -20.4% |
| 200 SMA | $235.35 | -17.1% |
| 50 EMA | $247.01 | -13.0% |
| 10 EMA | $250.22 | -11.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=97.9 (>= 10, not extreme oversold) | NO SETUP |
| MACD + RSI | SIGNAL | MACD cross=YES, RSI(14)=72.2 (in range), Volume=1.88x, Price > 50 SMA | SETUP CONFIRMED |
| Bollinger Squeeze | FAIL | No squeeze present, bandwidth=21.52 vs 6m low=5.81 | NO SETUP |
| MA Crossover | FAIL | Crossover exists but price NOT in pullback zone | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Suggested Parameters (MACD + RSI)
| Parameter | Value |
|-----------|-------|
| Entry | $284.02 |
| Stop Loss | $269.09 |
| Take Profit | $287.20 |
| Risk/Share | $14.93 |
| Reward/Share | $3.18 |
| R:R Ratio | 0.21:1 |

### ⚠️ RISK ASSESSMENT
**R:R RATIO FAILS MINIMUM THRESHOLD**: This setup has a 0.21:1 risk/reward ratio, but the MACD + RSI strategy requires a minimum 1.0:1 ratio. **Reward is insufficient relative to risk. Trade is NOT recommended.**

### Decision
**MACD + RSI SETUP IDENTIFIED — REJECTED DUE TO INADEQUATE RISK/REWARD**

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $373.51 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.26x |
| ATR(14) | $12.86 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $376.69 | +0.9% |
| Support 1 | $314.90 | -15.7% |
| 200 SMA | $326.62 | -12.5% |
| 50 EMA | $358.38 | -4.1% |
| 10 EMA | $346.35 | -7.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=96.8 (>= 10, not extreme oversold) | NO SETUP |
| MACD + RSI | SIGNAL | MACD cross=YES, RSI(14)=61.1 (in range), Volume=1.26x, Price > 50 SMA | SETUP CONFIRMED |
| Bollinger Squeeze | FAIL | No squeeze present, bandwidth=18.08 vs 6m low=5.06 | NO SETUP |
| MA Crossover | FAIL | 10 EMA < 50 EMA (bearish), no crossover | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Suggested Parameters (MACD + RSI)
| Parameter | Value |
|-----------|-------|
| Entry | $373.51 |
| Stop Loss | $354.22 |
| Take Profit | $376.69 |
| Risk/Share | $19.29 |
| Reward/Share | $3.18 |
| R:R Ratio | 0.16:1 |

### ⚠️ RISK ASSESSMENT
**R:R RATIO FAILS MINIMUM THRESHOLD**: This setup has a 0.16:1 risk/reward ratio, but the MACD + RSI strategy requires a minimum 1.0:1 ratio. **Reward is severely insufficient relative to risk. Trade is NOT recommended.**

### Decision
**MACD + RSI SETUP IDENTIFIED — REJECTED DUE TO INADEQUATE RISK/REWARD**

---

## Ticker: SNOW

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $307.53 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.63x |
| ATR(14) | $14.69 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $315.42 | +2.6% |
| Support 1 | $253.00 | -17.7% |
| 200 SMA | $210.85 | -31.4% |
| 50 EMA | $250.37 | -18.6% |
| 10 EMA | $284.51 | -7.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=88.4 (>= 10, not extreme oversold) | NO SETUP |
| MACD + RSI | SIGNAL | MACD cross=YES, RSI(14)=74.5 (in range), Volume=1.63x, Price > 50 SMA | SETUP CONFIRMED |
| Bollinger Squeeze | FAIL | No squeeze present, bandwidth=17.56 vs 6m low=8.14 | NO SETUP |
| MA Crossover | FAIL | Crossover does not exist (EMA10 > EMA50 but no recent cross) | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Suggested Parameters (MACD + RSI)
| Parameter | Value |
|-----------|-------|
| Entry | $307.53 |
| Stop Loss | $285.49 |
| Take Profit | $315.42 |
| Risk/Share | $22.04 |
| Reward/Share | $7.89 |
| R:R Ratio | 0.36:1 |

### ⚠️ RISK ASSESSMENT