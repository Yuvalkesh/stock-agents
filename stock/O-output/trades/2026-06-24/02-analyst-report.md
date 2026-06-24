# Technical Analysis Report — 2026-06-24

## Ticker: WMT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $119.42 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.92x |
| ATR(14) | $2.85 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $122.94 | +3.0% |
| Support 1 | $112.73 | -5.6% |
| 200 SMA | $116.23 | -2.7% |
| 50 EMA | $124.62 | +4.4% |
| 10 EMA | $119.01 | -0.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=78.83, Price > 200 SMA (ABOVE) | NO SETUP |
| MACD + RSI | FAIL | MACD=-1.61, Signal=-1.87, Histogram=+0.26, RSI(14)=45.82, Price < 50 SMA | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=7.11 (min 6m=4.79), No squeeze, Volume=0.92x | NO SETUP |
| MA Crossover | FAIL | 10 EMA < 50 EMA (bearish), Price above 10 EMA | NO SETUP |
| VIX Fear | N/A | Not applicable for individual equity | N/A |

### Decision
**NO SETUP** — All five strategies fail entry criteria. RSI(2) is elevated (78.83, well above 10 threshold). Price below 50 EMA with no MACD confirmation. Bollinger Bandwidth not in squeeze. MA configuration bearish (10 EMA below 50 EMA). Relative volume weak at 0.92x. Data does not support entry on any strategy.

---

## Ticker: HD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $324.45 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.90x |
| ATR(14) | $8.51 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $341.15 | +5.2% |
| Support 1 | $304.83 | -6.0% |
| 200 SMA | $352.98 | +8.8% |
| 50 EMA | $320.63 | -1.2% |
| 10 EMA | $325.76 | +0.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=24.3, Price < 200 SMA (BELOW) | NO SETUP |
| MACD + RSI | FAIL | MACD=3.73, Signal=2.30, Histogram=1.43 (positive), RSI(14)=52.86, Volume=0.90x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=11.32 (min 6m=4.43), No squeeze active, Volume=0.90x | NO SETUP |
| MA Crossover | FAIL | 10 EMA > 50 EMA (bullish crossover), but price below 10 EMA (pullback zone not confirmed) | NO SETUP |
| VIX Fear | N/A | Not applicable for individual equity | N/A |

### Decision
**NO SETUP** — Price significantly below 200 SMA (8.8% gap), disqualifying Connors RSI strategy. MACD histogram positive but no fresh crossover signal confirmed. MA Crossover shows bullish EMA configuration but price has not bounced above 10 EMA as required. Volume weak at 0.90x. No actionable setup confirmed.

---

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $200.04 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.89x |
| ATR(14) | $7.59 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $232.01 | +16.0% |
| Support 1 | $199.34 | -0.4% |
| 200 SMA | $190.02 | -5.0% |
| 50 EMA | $209.85 | +4.9% |
| 10 EMA | $207.16 | +3.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=14.71 (above 10 threshold), Price > 200 SMA | NO SETUP |
| MACD + RSI | FAIL | MACD=-1.62, Signal=-0.52, Histogram=-1.11 (negative), RSI(14)=42.56, Price < 50 EMA | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=12.06 (min 6m=5.37), No squeeze, Price below upper band, Volume=0.89x | NO SETUP |
| MA Crossover | FAIL | 10 EMA > 50 EMA (bullish), but price below 10 EMA (no pullback zone entry), RSI(14)=42.56 | NO SETUP |
| VIX Fear | N/A | Not applicable for individual equity | N/A |

### Decision
**NO SETUP** — RSI(2) at 14.71 fails threshold. MACD negative with price below both 10 and 50 EMAs. Price clearly below short-term moving averages despite positive SMA structure. Volume weak at 0.89x. No strategy parameters satisfied. Data does not support trade entry.

---

## Ticker: ABNB

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $138.85 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.88x |
| ATR(14) | $4.28 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $143.80 | +3.6% |
| Support 1 | $127.23 | -8.4% |
| 200 SMA | $129.29 | -7.0% |
| 50 EMA | $136.87 | -1.4% |
| 10 EMA | $137.78 | -0.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=29.41 (above 10 threshold), Price > 200 SMA | NO SETUP |
| MACD + RSI | FAIL | MACD=1.23, Signal=0.38, Histogram=0.85 (positive), No crossover, RSI(14)=55.39, Volume=0.88x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=10.97 (min 6m=4.49), No squeeze, Volume=0.88x | NO SETUP |
| MA Crossover | PASS | 10 EMA=137.78 < 50 EMA=135.27 (bullish crossover), Price=138.85 > 10 EMA (pullback zone satisfied, bounce confirmed), RSI(14)=55.39 | SETUP DETECTED |
| VIX Fear | N/A | Not applicable for individual equity | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $138.85 |
| Stop Loss | $132.43 |
| Take Profit | $143.80 |
| R:R Ratio | 0.77:1 |

### Decision
**NO SETUP** — MA Crossover setup technically triggered (10 EMA > 50 EMA, price above 10 EMA, RSI in range), however **R:R ratio of 0.77:1 FAILS minimum requirement of 1.5:1**. Risk/reward asymmetry ($6.42 risk vs $4.95 reward) makes position unfavorable. Strategy rules require 1.5:1 minimum. Entry rejected despite technical confirmation.

---

## Ticker: ROKU

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $135.05 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.97x |
| ATR(14) | $5.49 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $148.88 | +10.2% |
| Support 1 | $115.00 | -14.8% |
| 200 SMA | $105.41 | -22.0% |
| 50 EMA | $123.15 | -8.9% |
| 10 EMA | $133.69 | -1.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=23.28 (above 10 threshold), Price > 200 SMA | NO SETUP |
| MACD + RSI | FAIL | MACD=3.96, Signal=3.36, Histogram=0.60 (positive), No crossover, RSI(14)=57.80, Volume=0.97x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=22.86 (min 6m=5.88), No squeeze, Volume=0.97x | NO SETUP |
| MA Crossover | PASS | 10 EMA=133.69 > 50 EMA=123.15 (bullish structure maintained), Price=135.05 > 10 EMA (pullback zone satisfied), RSI(14)=57.80 | SETUP DETECTED |
| VIX Fear | N/A | Not applicable for individual equity | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $135.05 |
| Stop Loss | $126.82 |
| Take Profit | $148.88 |
| Risk/Share | $8.23 |
| Reward/Share | $13.83 |
| R:R Ratio | 1.68:1 |

### Decision
**SETUP CONFIRMED [MA Crossover]** — 10 EMA clearly above 50 EMA in bullish configuration. Price trading above 10 EMA within pullback zone. RSI(14)=57.80 confirms bullish bias without overbought condition. R:R ratio of 1.68:1 **PASSES** minimum requirement of 1.5:1. Relative volume at 0.97x is acceptable. **Entry at $135.05, Stop at $126.82, Target $148.88. Trade approved.**

---

## Ticker: KLAC

### Price Data
| Metric | Value |