# Technical Analysis Report — 2026-08-20

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $484.31 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.53x |
| ATR(14) | $13.28 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $513.73 | +6.1% |
| Support 1 | $377.39 | -22.1% |
| 200 SMA | $430.55 | -11.1% |
| 50 EMA | $416.57 | -14.0% |
| 10 EMA | $484.20 | -0.02% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=45.89, Price > 200 SMA | RSI above threshold (need <10), Price ABOVE 200 SMA | NO SETUP |
| MACD + RSI | MACD=-1.71, RSI(14)=63.53, Price > 50 SMA | No bullish crossover, volume weak (0.53x) | NO SETUP |
| Bollinger Squeeze | BW=39.33, 6m low=5.20, RSI(14)=63.53 | No squeeze (bandwidth too wide), no breakout | NO SETUP |
| MA Crossover | 10 EMA=$484.20, 50 EMA=$436.98, RSI(14)=63.53 | Bullish alignment, price at 10 EMA, in pullback zone | CONDITIONAL |
| VIX Fear | — | Not applicable (equity ticker) | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $484.31 |
| Stop Loss | $464.39 (1.5x ATR(14) below entry) |
| Take Profit | $513.73 (resistance) |
| Risk/Share | $19.92 |
| Reward/Share | $29.42 |
| R:R Ratio | 1.48:1 |

### Decision
**NO SETUP** — MA Crossover shows bullish EMA alignment, but R:R ratio of 1.48:1 **FAILS minimum threshold of 1.5:1** for this strategy. Trade rejected on risk/reward grounds. Volume confirmation weak (0.53x relative volume).

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $344.72 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.66x |
| ATR(14) | $9.88 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $384.48 | +11.5% |
| Support 1 | $314.90 | -8.7% |
| 200 SMA | $332.16 | -3.7% |
| 50 EMA | $352.47 | +2.2% |
| 10 EMA | $347.23 | +0.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=51.17, Price > 200 SMA | RSI well above threshold (need <10), no extreme oversold | NO SETUP |
| MACD + RSI | MACD=-0.56, RSI(14)=46.53, Price < 50 SMA | No bullish crossover, price below 50 EMA, volume weak (0.66x) | NO SETUP |
| Bollinger Squeeze | BW=17.82, 6m low=5.06, RSI(14)=46.53 | No squeeze, no breakout, volume weak | NO SETUP |
| MA Crossover | 10 EMA=$347.23, 50 EMA=$351.72, RSI(14)=46.53 | Bearish alignment (EMA10 < EMA50), price below 10 EMA | NO SETUP |
| VIX Fear | — | Not applicable (equity ticker) | N/A |

### Decision
**NO SETUP** — All strategies rejected. Price below 50 EMA, bearish MA alignment, MACD negative, RSI(2) neutral. No actionable setup.

---

## Ticker: META

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $546.03 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.97x |
| ATR(14) | $21.79 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $614.65 | +12.6% |
| Support 1 | $524.49 | -4.0% |
| 200 SMA | $624.30 | +14.3% |
| 50 EMA | $594.15 | +8.8% |
| 10 EMA | $572.93 | +4.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=15.37, Price < 200 SMA | RSI in extreme oversold range BUT price BELOW 200 SMA — trend filter FAILS | NO SETUP |
| MACD + RSI | MACD=-4.21, RSI(14)=37.06, Price < 50 SMA | Bearish MACD histogram, price below 50 EMA, volume weak (0.97x) | NO SETUP |
| Bollinger Squeeze | BW=13.29, 6m low=5.03, RSI(14)=37.06 | No squeeze, no breakout, volume weak | NO SETUP |
| MA Crossover | 10 EMA=$572.93, 50 EMA=$595.98, RSI(14)=37.06 | Bearish alignment (EMA10 < EMA50), price well below both, no pullback setup | NO SETUP |
| VIX Fear | — | Not applicable (equity ticker) | N/A |

### Decision
**NO SETUP** — All strategies rejected. Price is **below 200 SMA** and **below 50 EMA**, confirming downtrend. Connors RSI(2)=15.37 signals extreme oversold but trend filter is violated (price must be > 200 SMA). Market structure against longs.

---

## Ticker: JPM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $357.26 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.05x |
| ATR(14) | $6.20 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $366.50 | +2.6% |
| Support 1 | $343.78 | -3.7% |
| 200 SMA | $313.38 | -12.3% |
| 50 EMA | $341.82 | -4.3% |
| 10 EMA | $359.90 | +0.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=16.45, Price > 200 SMA | RSI near threshold but > 10, volume weak (no spike confirmation) | NO SETUP |
| MACD + RSI | MACD=-0.83, RSI(14)=55.52, Price > 50 SMA | No bullish crossover, MACD histogram negative, volume confirms but signal absent | NO SETUP |
| Bollinger Squeeze | BW=5.78, 6m low=3.17, RSI(14)=55.52 | No active squeeze (bandwidth >3.17), no breakout | NO SETUP |
| MA Crossover | 10 EMA=$359.90, 50 EMA=$343.09, RSI(14)=55.52 | Bullish alignment, but price is BELOW 10 EMA (not in pullback zone correctly) | NO SETUP |
| VIX Fear | — | Not applicable (equity ticker) | N/A |

### Decision
**NO SETUP** — All strategies rejected. Price below 50 EMA (downside risk), MACD negative, no clear bullish signals. Relative volume confirms (1.05x) but no entry trigger across any strategy.

---

## Ticker: ABNB

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $186.39 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.92x |
| ATR(14) | $6.04 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $189.20 | +1.5% |
| Support 1 | $135.72 | -27.2% |
| 200 SMA | $135.58 | -27.3% |
| 50 EMA | $151.36 | -18.8% |
| 10 EMA | $177.88 | -4.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=79.07, Price > 200 SMA | RSI(2) FAR above threshold (79.07 >> 10), showing overbought, not oversold | NO SETUP |
| MACD + RSI | MACD=1.93, RSI(14)=72.37, Price > 50 SMA | Positive MACD histogram but RSI(14)=72.37 near overbought zone (>75 threshold for exit), weak volume (0.92x) | NO SETUP |
| Bollinger Squeeze | BW=42.15, 6m low=4.49, RSI(14)=72.37 | No squeeze, no breakout, RSI overbought | NO SETUP |
| MA Crossover | 10 EMA=$177.88, 50 EMA=$151.36, RSI(14)=72.37 | Bullish alignment, price above 10 EMA, but NO pullback zone (price extended), RSI overbought | NO SETUP |
| VIX Fear | — | Not applicable (equity ticker) | N/A |

### Decision
**NO SETUP** — All strategies rejected. Stock is **extended and overbought** (RSI(2)=79.07, RSI(14)=72.37). No pullback to 10 EMA to establish entry. Price is $8.51 above resistance, risk/reward unfavorable.

---

## Ticker: DASH

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $220.22 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.03x |
| ATR(14) | $8.14 |

### Key Levels
| Level | Price | Distance |
|-------|----