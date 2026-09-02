# Technical Analysis Report — 2026-09-02

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $498.30 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.18x |
| ATR(14) | $11.19 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $517.78 | +3.91% |
| Support 1 | $476.25 | -4.42% |
| 200 SMA | $429.38 | -13.82% |
| 50 EMA | $437.73 | -12.16% |
| 10 EMA | $497.81 | -0.10% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=20.03, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD=-2.13, RSI(14)=62.15, Price vs 50 SMA=ABOVE, RVol=0.18x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=7.74 (6m low=5.20), Price vs Upper Band=BELOW, RVol=0.18x | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA > 50 EMA (BULLISH), Price near 10 EMA, RSI(14)=62.15 | SETUP FAILED (R:R < min) |
| VIX Fear | N/A | Strategy not applicable to equity tickers | N/A |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $498.30 |
| Stop Loss | $481.51 |
| Take Profit | $517.78 |
| Risk/Share | $16.79 |
| Reward/Share | $19.48 |
| R:R Ratio | 1.16:1 |
| **Min R:R Required** | **1.5:1** |

### Decision
**NO SETUP** — MA Crossover setup detected but R:R Ratio (1.16:1) fails minimum requirement of 1.5:1. Weak volume (0.18x) also disconfirms. Pass.

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $336.84 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.33x |
| ATR(14) | $8.30 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $364.13 | +8.10% |
| Support 1 | $332.82 | -1.19% |
| 200 SMA | $335.11 | -0.51% |
| 50 EMA | $348.45 | +3.43% |
| 10 EMA | $341.35 | +1.34% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=38.05, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD=-3.19, RSI(14)=42.90, Price vs 50 SMA=BELOW | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=6.73 (6m low=5.06), Price vs Bands=NEUTRAL, RVol=0.33x | NO SETUP |
| MA Crossover | FAIL | 10 EMA < 50 EMA (BEARISH), Price below 10 EMA | NO SETUP |
| VIX Fear | N/A | Strategy not applicable to equity tickers | N/A |

### Decision
**NO SETUP** — No strategy conditions met. 10 EMA bearish vs 50 EMA. MACD negative. Price below 50 EMA. All indicators neutral-to-bearish. Pass.

---

## Ticker: AMZN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $255.37 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.23x |
| ATR(14) | $6.93 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $280.14 | +9.71% |
| Support 1 | $251.93 | -1.35% |
| 200 SMA | $238.88 | -6.43% |
| 50 EMA | $252.83 | -1.00% |
| 10 EMA | $259.43 | +1.58% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=28.45, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD=0.60, MACD Signal=2.16, Histogram=-1.56 (NO CROSS), RVol=0.23x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=9.59 (6m low=5.81), Price below middle band, RVol=0.23x | NO SETUP |
| MA Crossover | FAIL | 10 EMA > 50 EMA (BULLISH) but Price BELOW 10 EMA | NO SETUP |
| VIX Fear | N/A | Strategy not applicable to equity tickers | N/A |

### Decision
**NO SETUP** — MA Crossover shows bullish 10 EMA > 50 EMA, but price is below 10 EMA without confirmation bounce. Pullback zone exists but price not above EMA10. No other strategy triggered. Pass.

---

## Ticker: JPM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $360.95 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.21x |
| ATR(14) | $5.69 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $366.50 | +1.54% |
| Support 1 | $350.37 | -2.94% |
| 200 SMA | $315.72 | -12.53% |
| 50 EMA | $347.30 | -3.79% |
| 10 EMA | $357.08 | -1.07% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=85.45 (overbought), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD=2.24, MACD Signal=3.08, Histogram=-0.84 (NO CROSS), RVol=0.21x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=4.22 (6m low=3.17), No breakout, RVol=0.21x | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA > 50 EMA (BULLISH), Price near 10 EMA, RSI(14)=58.78 | SETUP FAILED (R:R < min) |
| VIX Fear | N/A | Strategy not applicable to equity tickers | N/A |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $360.95 |
| Stop Loss | $352.41 |
| Take Profit | $366.50 |
| Risk/Share | $8.54 |
| Reward/Share | $5.55 |
| R:R Ratio | 0.65:1 |
| **Min R:R Required** | **1.5:1** |

### Decision
**NO SETUP** — MA Crossover setup detected but R:R Ratio (0.65:1) severely fails minimum requirement of 1.5:1. Tight resistance only 1.54% above entry. Poor risk/reward. Pass.

---

## Ticker: XOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $163.30 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.20x |
| ATR(14) | $3.39 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $168.64 | +3.27% |
| Support 1 | $150.56 | -7.80% |
| 200 SMA | $142.62 | -12.67% |
| 50 EMA | $151.29 | -7.35% |
| 10 EMA | $161.23 | -1.27% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=65.87, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD=2.56, MACD Signal=2.97, Histogram=-0.41 (NO CROSS), RVol=0.20x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=9.76 (6m low=5.21), No breakout, RVol=0.20x | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA > 50 EMA (BULLISH), Price near 10 EMA, RSI(14)=59.64 | SETUP FAILED (R:R < min) |
| VIX Fear | N/A | Strategy not applicable to equity tickers | N/A |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $163.30 |
| Stop Loss | $158.22 |
| Take Profit | $168.64 |
| Risk/Share | $5.08 |
| Reward/Share | $5.34 |
| R:R Ratio | 1.05:1 |
| **Min R:R Required** | **1.5:1** |

### Decision
**NO SETUP** — MA Crossover setup detected but R:R Ratio (1.05:1) fails minimum requirement of 1.5:1. Limited upside to resistance. Weak volume (0.20x) disconfirms. Pass.

---

## Ticker: SLB

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $57.64 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.24x |
| ATR(14) | $1.87 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $60.46 | +4.89% |
| Support 1 | $50.28 |