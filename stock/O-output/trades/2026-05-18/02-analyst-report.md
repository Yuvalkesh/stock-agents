# Technical Analysis Report — 2026-05-18

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $222.85 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.3x |
| ATR(14) | $7.47 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $236.54 | +6.1% |
| Support 1 | $194.74 | -12.6% |
| 200 SMA | $186.18 | -16.5% |
| 50 EMA | $193.97 | -13.0% |
| 10 EMA | $219.65 | -1.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=31.01, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=62.17, Volume=0.3x | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=20.72, BW 6mo low=5.37, Volume=0.3x | NO SETUP |
| MA Crossover | TRIGGERED | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES, Above 10 EMA=YES | SETUP CONFIRMED |
| VIX Fear | N/A | N/A | NO SETUP |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $222.85 |
| Stop Loss | $211.64 (1.5x ATR below entry) |
| Take Profit | $236.54 (resistance) |
| Risk/Share | $11.21 |
| Reward/Share | $13.69 |
| R:R Ratio | 1.22:1 |

### Decision
**NO SETUP**

**Rationale:** MA Crossover setup technically confirmed (EMA10 > EMA50, pullback zone active, price above 10 EMA, RSI in acceptable range). However, **R:R Ratio of 1.22:1 FAILS minimum threshold of 1.5:1 required for this strategy**. Risk-reward imbalance disqualifies this trade. Additionally, relative volume of 0.3x is below preferred 0.8x minimum, reducing setup reliability. **PASS on NVDA.**

---

## Ticker: AMD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $417.81 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.19x |
| ATR(14) | $23.01 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $469.22 | +12.3% |
| Support 1 | $276.62 | -33.8% |
| 200 SMA | $225.40 | -46.0% |
| 50 EMA | $283.72 | -32.1% |
| 10 EMA | $418.36 | +0.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | TRIGGERED | RSI(2)=9.76 (<10 oversold), Price vs 200 SMA=ABOVE | SETUP CONFIRMED |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=65.18, Volume=0.19x | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=59.44, BW 6mo low=9.53, Volume=0.19x | NO SETUP |
| MA Crossover | FAILED | Pullback zone=YES, Above 10 EMA=NO (Price=417.81 vs EMA10=418.36) | NO SETUP |
| VIX Fear | N/A | N/A | NO SETUP |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $417.81 |
| Stop Loss | $371.79 (2x ATR below entry) |
| Take Profit | $437.08 (close above 5-day SMA) |
| Risk/Share | $46.02 |
| Reward/Share | $19.27 |
| R:R Ratio | 0.42:1 |

### Decision
**NO SETUP**

**Rationale:** Connors RSI(2) setup triggered (RSI(2)=9.76 clearly <10, price well above 200 SMA at $225.40). However, **R:R Ratio of 0.42:1 FAILS minimum threshold of 0.5:1 required for this strategy**. Stop loss is too wide relative to potential reward — risk of $46.02 per share for only $19.27 reward is unfavorable. Additionally, relative volume of 0.19x is critically weak. **PASS on AMD.**

---

## Ticker: TXN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $301.25 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.1x |
| ATR(14) | $9.48 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $310.29 | +3.0% |
| Support 1 | $229.47 | -23.8% |
| 200 SMA | $196.16 | -34.9% |
| 50 EMA | $232.52 | -22.8% |
| 10 EMA | $294.71 | -2.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=33.81 (>=10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=73.23 (overbought edge), Volume=0.1x | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=28.59, BW 6mo low=5.41, Volume=0.1x | NO SETUP |
| MA Crossover | TRIGGERED | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES, Above 10 EMA=YES | SETUP CONFIRMED |
| VIX Fear | N/A | N/A | NO SETUP |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $301.25 |
| Stop Loss | $287.03 (1.5x ATR below entry) |
| Take Profit | $310.29 (resistance) |
| Risk/Share | $14.22 |
| Reward/Share | $9.04 |
| R:R Ratio | 0.64:1 |

### Decision
**NO SETUP**

**Rationale:** MA Crossover setup technically triggered (EMA10 > EMA50, price in pullback zone, above 10 EMA, RSI=73.23 acceptable). However, **R:R Ratio of 0.64:1 FAILS minimum threshold of 1.5:1 required for this strategy**. Reward of $9.04 per share is insufficient against risk of $14.22. Target resistance is too tight relative to entry risk. Additionally, relative volume of 0.1x is extremely weak, and RSI at 73.23 suggests price is getting toppy. **PASS on TXN.**

---

## Ticker: QCOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $196.93 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.19x |
| ATR(14) | $14.08 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $247.90 | +25.8% |
| Support 1 | $132.05 | -32.9% |
| 200 SMA | $157.99 | -19.8% |
| 50 EMA | $150.21 | -23.7% |
| 10 EMA | $199.10 | +1.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=17.63 (>=10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=59.76, Volume=0.19x | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=67.14, BW 6mo low=5.85, Volume=0.19x | NO SETUP |
| MA Crossover | FAILED | Pullback zone=YES, Above 10 EMA=NO (Price=196.93 vs EMA10=199.10) | NO SETUP |
| VIX Fear | N/A | N/A | NO SETUP |

### Decision
**NO SETUP**

**Rationale:** No strategy setup confirmed. MA Crossover is bullish directionally (EMA10 > EMA50), but price is currently below 10 EMA, failing entry condition. RSI(2) at 17.63 does not trigger Connors. MACD shows no crossover. All setups lack sufficient confluent conditions. Relative volume of 0.19x is weak. **PASS on QCOM.**

---

## Ticker: XOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $157.48 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.18x |
| ATR(14) | $4.05 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $158.00 | +0.3% |
| Support 1 | $142.95 | -9.2% |
| 200 SMA | $128.30 | -18.6% |
| 50 EMA | $154.08 | -2.2% |
| 10 EMA | $152.32 | -3.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=87.80 (>=10, overbought), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=59.83, Price vs 50 SMA=ABOVE, Volume=0.18x | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=9.54, BW 6mo low=4.27, Volume=0.18x | NO SETUP |
| MA Crossover | FAILED | Crossover=YES (recent), Pullback zone=NO (price above both EMAs), Above 10 EMA=YES | NO SETUP |
| VIX Fear | N/A | N/A | NO SETUP |

### Decision
**NO SETUP**

**Rationale:** MA Crossover triggered (10 EMA recently crossed above 50 EMA), but **pullback condition FAILED** — price is already extended above 10 EMA ($152.32) without pulling back into the optimal entry zone. This is a late-stage entry signal after a move has already begun. RSI(2) overbought at 87.80 disqualifies Connors. Resistance is extremely tight at $158.00 (+0.3%), offering minimal reward potential. Relative volume 0.18x is weak. **PASS on XOM.**

---

## Ticker: CVX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $191.85 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.17x |
| ATR(14) | $4.36 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $194.13 | +1.2% |
| Support 1 | $179.53 | -6.4% |
| 200 SMA | $166.64 | -13.1% |
| 50 EMA | $193.08 | +0.6% |
| 10 EMA | $188.11 | -2.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=98.08 (>>10, extreme overbought), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAILED | MACD cross=YES (bullish), RSI(14)=55.16, **Price vs 50 SMA=BELOW** | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=7.39, BW 6mo low=3.60, Volume=0.17x | NO SETUP |
| MA Crossover | FAILED | 10 EMA vs 50 EMA=BEARISH, Pullback zone=YES, Above 10 EMA=YES | NO SETUP |
| VIX Fear | N/A | N/A | NO SETUP |

### Decision
**NO SETUP**

**Rationale:** All strategies fail. Connors RSI(2) severely overbought at 98.08 — no setup. MACD shows bullish crossover but **price is BELOW 50 EMA ($193.08 vs $191.85)**, violating the trend filter requirement. MA Crossover shows bearish EMA arrangement (10 EMA < 50 EMA). Chart structure is unclear and lacks directional conviction. Resistance is minimal at +1.2%. Relative volume 0.17x is critically weak. **PASS on CVX.**

---

## Ticker: UNH

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $385.86 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.29x |
| ATR(14) | $9.38 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $404.15 | +4.7% |
| Support 1 | $345.23 | -10.5% |
| 200 SMA | $318.08 | -17.6% |
| 50 EMA | $322.27 | -16.5% |
| 10 EMA | $384.83 | -0.03% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=13.09 (>10 threshold), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RS