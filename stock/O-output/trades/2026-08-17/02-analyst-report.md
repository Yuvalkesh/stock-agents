# Technical Analysis Report — 2026-08-17

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $225.16 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.63x |
| ATR(14) | $6.93 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $227.49 | +1.04% |
| Support 1 | $190.01 | -15.63% |
| 200 SMA | $194.75 | -13.48% |
| 50 EMA | $206.52 | -8.26% |
| 10 EMA | $218.59 | -2.94% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=81.92, Price vs 200 SMA=ABOVE | NO SETUP — RSI(2) overbought (>10) |
| MACD + RSI | NO SETUP | MACD cross=NO, RSI(14)=63.04, Histogram=2.05 | NO SETUP — No MACD crossover, weak volume |
| Bollinger Squeeze | NO SETUP | Bandwidth=20.28, 6m-low=7.76, RSI(14)=63.04 | NO SETUP — No squeeze condition, no breakout |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA=BULLISH, Pullback zone=NO | NO SETUP — Price too far above 10 EMA, weak volume |
| VIX Fear | N/A | N/A | N/A — Not applicable for single stock |

### Decision
**NO SETUP** — All five strategies fail entry criteria. RSI(2) is severely overbought at 81.92. MACD shows no crossover signal. Bollinger Bands show no squeeze and price is not breaking out. MA Crossover triggered but price is elevated above the 10 EMA pullback zone. Volume is weak at 0.63x average. No trade.

---

## Ticker: META

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $589.85 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.55x |
| ATR(14) | $21.62 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $655.88 | +11.20% |
| Support 1 | $524.49 | -11.07% |
| 200 SMA | $626.83 | +6.27% |
| 50 EMA | $597.06 | +1.21% |
| 10 EMA | $590.68 | +0.14% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=46.65, Price vs 200 SMA=BELOW | NO SETUP — Price below 200 SMA (trend filter failed) |
| MACD + RSI | NO SETUP | MACD cross=YES, RSI(14)=47.63, Price vs 50 SMA=BELOW | NO SETUP — Price below 50 SMA despite MACD cross, weak volume |
| Bollinger Squeeze | NO SETUP | Bandwidth=15.96, 6m-low=5.03, RSI(14)=47.63 | NO SETUP — No squeeze, no breakout, weak volume |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA=BEARISH, Pullback zone=YES | NO SETUP — 10 EMA below 50 EMA (bearish crossover), price below 10 EMA |
| VIX Fear | N/A | N/A | N/A — Not applicable for single stock |

### Decision
**NO SETUP** — Price is below both the 200 SMA and 50 EMA, failing all long-bias trend filters. MA Crossover shows bearish alignment (10 EMA < 50 EMA). MACD histogram turned positive but price fails the 50 SMA confirmation. Relative volume is critically weak at 0.55x. No trade.

---

## Ticker: XOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $160.10 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.73x |
| ATR(14) | $3.65 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $161.67 | +1.00% |
| Support 1 | $146.23 | -8.70% |
| 200 SMA | $140.32 | -12.40% |
| 50 EMA | $147.57 | -7.80% |
| 10 EMA | $157.41 | -1.68% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=74.74, Price vs 200 SMA=ABOVE | NO SETUP — RSI(2) overbought (>10) |
| MACD + RSI | NO SETUP | MACD cross=NO, RSI(14)=64.33, Histogram=0.23 | NO SETUP — No MACD crossover, weak volume |
| Bollinger Squeeze | NO SETUP | Bandwidth=7.93, 6m-low=5.21, RSI(14)=64.33 | NO SETUP — No squeeze, no breakout, weak volume |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES | NO SETUP — Setup exists but R:R ratio 0.29:1 fails min threshold 1.5:1 |
| VIX Fear | N/A | N/A | N/A — Not applicable for single stock |

### Suggested Parameters (MA Crossover — Rejected)
| Parameter | Value |
|-----------|-------|
| Entry | $160.10 |
| Stop Loss | $154.62 (1.5x ATR(14) below entry) |
| Take Profit | $161.67 (resistance) |
| Risk/Share | $5.48 |
| Reward/Share | $1.57 |
| R:R Ratio | 0.29:1 (FAILS minimum 1.5:1) |

### Decision
**NO SETUP** — MA Crossover strategy triggers (10 EMA above 50 EMA, price in pullback zone at 10 EMA), but the risk-reward ratio of 0.29:1 is severely unfavorable, falling far short of the required 1.5:1 minimum. The reward ($1.57) is too small relative to risk ($5.48). RSI(2) is overbought. No trade.

---

## Ticker: CVX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $200.00 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 1.00x |
| ATR(14) | $4.39 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $201.63 | +0.82% |
| Support 1 | $185.87 | -7.07% |
| 200 SMA | $175.54 | -12.23% |
| 50 EMA | $183.99 | -8.00% |
| 10 EMA | $194.64 | -2.68% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=96.09, Price vs 200 SMA=ABOVE | NO SETUP — RSI(2) extremely overbought (>10) |
| MACD + RSI | NO SETUP | MACD cross=NO, RSI(14)=64.53, Histogram=0.51, Volume=CONFIRMS | NO SETUP — No MACD crossover despite good volume |
| Bollinger Squeeze | NO SETUP | Bandwidth=7.76, 6m-low=6.50, RSI(14)=64.53 | NO SETUP — No squeeze, no breakout |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA=BULLISH, Pullback zone=NO | NO SETUP — Price above 10 EMA, not in pullback zone, weak volume |
| VIX Fear | N/A | N/A | N/A — Not applicable for single stock |

### Decision
**NO SETUP** — RSI(2) at 96.09 indicates extreme overbought condition, disqualifying Connors strategy. MACD shows no crossover. Bollinger Bands show no squeeze. MA Crossover shows bullish alignment but price is not in the pullback zone (price above 10 EMA by 2.68%). Volume is at parity (1.0x) but insufficient for breakout confirmation. No trade.

---

## Ticker: JPM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $362.84 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.77x |
| ATR(14) | $6.34 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $366.50 | +0.91% |
| Support 1 | $337.30 | -7.04% |
| 200 SMA | $312.51 | -13.86% |
| 50 EMA | $338.79 | -6.64% |
| 10 EMA | $359.63 | -0.88% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO SETUP | RSI(2)=48.69, Price vs 200 SMA=ABOVE | NO SETUP — RSI(2) not in oversold range (<10) |
| MACD + RSI | NO SETUP | MACD cross=YES, RSI(14)=65.31, Price vs 50 SMA=ABOVE, Volume=WEAK | NO SETUP — Setup exists but R:R ratio 0.38:1 fails min threshold 1.0:1 |
| Bollinger Squeeze | NO SETUP | Bandwidth=7.61, 6m-low=3.17, RSI(14)=65.31 | NO SETUP — No squeeze, no breakout, weak volume |
| MA Crossover | NO SETUP | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES, RSI(14)=65.31 | NO SETUP — Setup exists but R:R ratio 0.38:1 fails min threshold 1.5:1 |
| VIX Fear | N/A | N/A | N/A — Not applicable for single stock |

### Suggested Parameters (Both Strategies — Rejected)
| Parameter | MACD+RSI | MA Crossover |
|-----------|----------|-------------|
| Entry | $362.84 | $362.84 |
| Stop Loss | $353.33 (1.5x ATR) | $353.33 (1.5x ATR) |
| Take