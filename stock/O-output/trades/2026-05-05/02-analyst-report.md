# Technical Analysis Report — 2026-05-05

## Ticker: AAPL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $276.83 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.0x |
| ATR(14) | $6.54 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $287.22 | +3.8% |
| Support 1 | $245.70 | -11.2% |
| 200 SMA | $255.24 | -7.8% |
| 50 EMA | $261.46 | -5.5% |
| 10 EMA | $272.21 | -1.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=58.2, Price above 200 SMA | NO SETUP |
| MACD + RSI | NO SETUP | MACD=4.56, Signal=3.68, RSI(14)=61.8, No crossover | NO SETUP |
| Bollinger Squeeze | NO SETUP | Bandwidth=10.2, 6M Low=3.2 (no squeeze), Volume=1.0x | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA vs 50 EMA bullish, Price in pullback zone, RSI(14)=61.8 | SETUP FAILS R:R |
| VIX Fear | — | VIX data unavailable | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $276.83 |
| Stop Loss | $267.02 (1.5x ATR below entry) |
| Take Profit | $287.22 (resistance) |
| Risk/Share | $9.81 |
| Reward/Share | $10.39 |
| R:R Ratio | 1.06:1 |
| **Status** | **FAILS minimum 1.5:1 requirement** |

### Decision
**NO SETUP** — MA Crossover strategy triggers pullback + bounce conditions, but R:R ratio of 1.06:1 fails the 1.5:1 minimum threshold for this strategy. Risk exceeds reward. Trade rejected.

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $413.62 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.79x |
| ATR(14) | $11.12 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $433.70 | +4.9% |
| Support 1 | $366.56 | -11.4% |
| 200 SMA | $466.16 | +12.7% |
| 50 EMA | $396.44 | -4.1% |
| 10 EMA | $416.08 | +0.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=39.9, Price below 200 SMA (fails trend filter) | NO SETUP |
| MACD + RSI | NO SETUP | MACD=7.74, Signal=7.97 (no crossover), RSI(14)=54.0, Volume=0.79x weak | NO SETUP |
| Bollinger Squeeze | NO SETUP | Bandwidth=20.3, 6M Low=4.1 (no squeeze), Volume=0.79x weak | NO SETUP |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA bullish, Crossover YES, but Price=$413.62 below 10 EMA=$416.08 | NO SETUP |
| VIX Fear | — | VIX data unavailable | N/A |

### Decision
**NO SETUP** — MA Crossover shows bullish crossover and price in pullback zone, but price has NOT bounced above 10 EMA as required. All other strategies fail parameter checks. No actionable setup.

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $383.25 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.96x |
| ATR(14) | $9.84 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $387.38 | +1.1% |
| Support 1 | $297.72 | -22.3% |
| 200 SMA | $281.87 | -26.4% |
| 50 EMA | $316.83 | -17.3% |
| 10 EMA | $360.75 | -5.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=79.2 (strong, not oversold), Price above 200 SMA | NO SETUP |
| MACD + RSI | NO SETUP | MACD=17.88, Signal=13.02 (no crossover), RSI(14)=80.0 (overbought, >75) | NO SETUP |
| Bollinger Squeeze | NO SETUP | Bandwidth=25.5, 6M Low=5.1 (no squeeze), RSI(14)=80.0 overbought | NO SETUP |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA bullish, but Price NOT in pullback zone (3.7% above 10 EMA) | NO SETUP |
| VIX Fear | — | VIX data unavailable | N/A |

### Decision
**NO SETUP** — Stock is overbought across multiple indicators (RSI(14)=80, RSI(2)=79.2). Price too extended above pullback zone for MA Crossover entry. No valid setup.

---

## Ticker: AMZN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $272.05 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.96x |
| ATR(14) | $7.51 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $276.10 | +1.5% |
| Support 1 | $209.08 | -23.2% |
| 200 SMA | $227.62 | -16.3% |
| 50 EMA | $226.04 | -16.9% |
| 10 EMA | $261.20 | -4.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=97.3 (extreme overbought, not oversold) | NO SETUP |
| MACD + RSI | NO SETUP | MACD=12.85, Signal=11.68 (no crossover), RSI(14)=79.9 (overbought, >75) | NO SETUP |
| Bollinger Squeeze | NO SETUP | Bandwidth=23.5, 6M Low=6.0 (no squeeze), RSI(14)=79.9 overbought | NO SETUP |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA bullish, but Price NOT in pullback zone (4.0% above 10 EMA) | NO SETUP |
| VIX Fear | — | VIX data unavailable | N/A |

### Decision
**NO SETUP** — Stock is severely overbought (RSI(2)=97.3, RSI(14)=79.9). Price extended well beyond pullback zone for MA Crossover. No valid setup. Risk/reward unfavorable.

---

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $198.48 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.84x |
| ATR(14) | $6.33 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $216.83 | +9.3% |
| Support 1 | $173.66 | -12.5% |
| 200 SMA | $183.97 | -7.3% |
| 50 EMA | $187.33 | -5.6% |
| 10 EMA | $202.17 | +1.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=10.57 (marginally oversold at threshold), Price above 200 SMA | NO SETUP |
| MACD + RSI | NO SETUP | MACD=5.49, Signal=6.18 (no crossover, histogram negative), RSI(14)=53.0 | NO SETUP |
| Bollinger Squeeze | NO SETUP | Bandwidth=19.6, 6M Low=5.4 (no squeeze), Volume=0.84x weak | NO SETUP |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA bullish, Pullback zone YES, but Price=$198.48 below 10 EMA=$202.17 | NO SETUP |
| VIX Fear | — | VIX data unavailable | N/A |

### Decision
**NO SETUP** — RSI(2)=10.57 marginally above the strict <10 threshold (Connors standard). MA Crossover shows pullback zone but price has not bounced above 10 EMA. Volume weak at 0.84x. No confirmed setup.

---

## Ticker: HD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $312.42 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.71x |
| ATR(14) | $8.48 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $353.55 | +13.2% |
| Support 1 | $312.26 | -0.05% |
| 200 SMA | $366.91 | +17.5% |
| 50 EMA | $341.33 | +9.3% |
| 10 EMA | $328.09 | +5.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=9.09 (oversold <10), BUT Price below 200 SMA (fails trend filter) | NO SETUP |
| MACD + RSI | NO SETUP | MACD=-4.81, Signal=-2.78 (no crossover), RSI(14)=33.8 (below 35 range), Price below 50 EMA | NO SETUP |
| Bollinger Squeeze | NO SETUP | Bandwidth=11.5, 6M Low=4.4 (no squeeze), RSI(14)=33.8 (below 50 threshold) | NO SETUP |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA bearish (crossover to downside), Price below both MAs | NO SETUP |
| VIX Fear | — | VIX data unavailable | N/A |

### Decision
**NO SETUP** — Connors RSI(2) shows oversold condition but price is below 200 SMA (fails long-term uptrend requirement). MA Crossover shows bearish crossover (downtrend). RSI(14)=33.8 confirms weakness. Stock in downtrend despite elevated volume (1.71x). No valid entry setup.

---

## Ticker: AI

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $9.22 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.76x |
| ATR(14) | $0.49 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $9.94 | +7.8% |
| Support 1 | $7.90 | -14.3% |
| 200 SMA | $14.49 | +57.2% |
| 50 EMA | $9.36 | +1.5% |
| 10 EMA | $8.99 | -2.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=89.6 (extreme overbought, not oversold), Price below 200 SMA | NO SETUP |
| MACD + RSI | NO SETUP | MACD=0.03, Signal=-0.02 (no crossover), RSI(14)=54.6, Price above 50 EMA, Volume=0.76x weak | NO SETUP |
| Bollinger Squeeze | NO SETUP | Bandwidth=16.1, 6M Low=7.9 (no squeeze), Volume=0.76x weak | NO SETUP |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA bearish, Price above 10 EMA but trend is down, Volume=0.76x weak | NO SETUP |
| VIX Fear | — | VIX data unavailable | N/A |

### Decision
**NO SETUP** — Stock is overbought (RSI(2)=89.6), trading 57% below 200 SMA (long-term downtrend). MA Crossover shows bearish crossover. Volume weak at 0.76x. No valid setup. Stock fails liquidity requirement with price at $9.22 (marginal).

---

## Summary

| Ticker | Decision | Reason |
|--------|----------|--------|
| AAPL | NO SETUP | MA Crossover triggered but R:R 1.06:1 fails 1.5:1 minimum |
| MSFT | NO SETUP | No strategy parameters met; price below 10 EMA on MA Crossover attempt |
| GOOGL | NO SETUP | RSI(14)=80.0 overbought; price too extended from 10 EMA |
| AMZN | NO SETUP | Extreme overbought (RSI(2)=97.3, RSI(14)=79.9); price too extended |
| NVDA | NO SETUP | RSI(2) marginally above threshold; MA Crossover bounce not confirmed |
| HD | NO SETUP | Connors RSI(2) oversold but price below 200 SMA; in downtrend |
| AI | NO SETUP | Overbought; price 57% below 200 SMA; in long-term downtrend |

**Market Assessment (2026-05-05):** Weak environment across sample. Multiple mega-cap stocks (AAPL, GOOGL, AMZN) are overbought on RSI(14) (>75 range). HD and AI in clear downtrends.