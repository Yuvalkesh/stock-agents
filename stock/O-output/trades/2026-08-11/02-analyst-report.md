# Technical Analysis Report — 2026-08-11

## Ticker: XOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $159.79 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.35x |
| ATR(14) | $4.03 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $160.37 | +0.4% |
| Support 1 | $142.03 | -11.1% |
| 200 SMA | $139.39 | -12.8% |
| 50 EMA | $146.74 | -8.2% |
| 10 EMA | $154.75 | -3.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECTED | RSI(2)=85.33, Price ABOVE 200 SMA | NO SETUP |
| MACD + RSI | TRIGGERED | MACD=2.95, Signal=2.87, RSI(14)=65.09, Price ABOVE 50 SMA, RelVol=1.35x | SETUP CONFIRMED |
| Bollinger Squeeze | REJECTED | Bandwidth=11.21 (6m low=5.21, not squeezed), RSI(14)=65.09 | NO SETUP |
| MA Crossover | REJECTED | EMA10=154.75 ABOVE EMA50=149.39 (no recent cross), Price NOT in pullback zone | NO SETUP |
| VIX Fear | N/A | Strategy not applicable to equity ticker | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $159.79 |
| Stop Loss | $153.75 |
| Take Profit | $160.37 |
| Risk/Share | $6.04 |
| Reward/Share | $0.58 |
| R:R Ratio | 0.1:1 |

### Decision
**NO SETUP — R:R Ratio Insufficient**

*MACD + RSI strategy triggers on technical parameters, but the risk-reward ratio (0.1:1) falls significantly below the 1.0:1 minimum requirement for this strategy. The entry offers $6.04 of risk for only $0.58 of reward. Position geometry is unfavorable; entry is too close to resistance and stop loss is too wide relative to profit target. Trade rejected on risk management grounds.*

---

## Ticker: CVX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $194.91 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.74x |
| ATR(14) | $4.66 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $197.69 | +1.4% |
| Support 1 | $178.58 | -8.4% |
| 200 SMA | $174.60 | -10.4% |
| 50 EMA | $183.09 | -6.1% |
| 10 EMA | $190.46 | -2.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECTED | RSI(2)=81.10, Price ABOVE 200 SMA | NO SETUP |
| MACD + RSI | REJECTED | MACD=2.63, Signal=2.95, Histogram=-0.32 (bearish cross), RSI(14)=59.41 | NO SETUP |
| Bollinger Squeeze | REJECTED | Bandwidth=8.89 (6m low=6.50, not squeezed), Breakout=NO | NO SETUP |
| MA Crossover | TRIGGERED | EMA10=190.46 ABOVE EMA50=185.58 (bullish), Price=194.91 in pullback zone (within 1.0%), RSI(14)=59.41, RelVol=1.74x | SETUP CONFIRMED |
| VIX Fear | N/A | Strategy not applicable to equity ticker | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $194.91 |
| Stop Loss | $187.92 |
| Take Profit | $197.69 |
| Risk/Share | $6.99 |
| Reward/Share | $2.78 |
| R:R Ratio | 0.4:1 |

### Decision
**NO SETUP — R:R Ratio Insufficient**

*MA Crossover strategy triggers technically, but the risk-reward ratio (0.4:1) falls below the 1.5:1 minimum requirement for this strategy. Trade risk ($6.99) exceeds profit target reward ($2.78) by 2.5x. Position geometry is poor; insufficient edge to justify the setup.*

---

## Ticker: ABNB

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $184.70 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 2.18x |
| ATR(14) | $6.15 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $185.99 | +0.7% |
| Support 1 | $135.72 | -26.5% |
| 200 SMA | $133.63 | -27.6% |
| 50 EMA | $144.51 | -21.7% |
| 10 EMA | $160.51 | -13.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECTED | RSI(2)=98.52, Price ABOVE 200 SMA (oversold threshold broken) | NO SETUP |
| MACD + RSI | REJECTED | MACD=6.64, Signal=3.40, Histogram=+3.23 (bullish), RSI(14)=81.54 (OVERBOUGHT, >80 threshold) | NO SETUP |
| Bollinger Squeeze | REJECTED | Bandwidth=29.28 (6m low=4.49, not squeezed), Breakout=YES but RSI(14)=81.54 overbought | NO SETUP |
| MA Crossover | REJECTED | EMA10=160.51 ABOVE EMA50=144.94 (bullish), Price NOT in pullback zone (Price ABOVE EMA10), RSI(14)=81.54 overbought | NO SETUP |
| VIX Fear | N/A | Strategy not applicable to equity ticker | N/A |

### Decision
**NO SETUP**

*All strategies rejected. ABNB is extended and overbought across multiple timeframes. RSI(2)=98.52 and RSI(14)=81.54 indicate severe overextension. Price is disconnected from the 10 EMA by 13.1%, well outside any reasonable pullback zone. The Bollinger Squeeze breakout is rendered invalid by overbought RSI conditions. No edge available; risk of mean reversion to downside is elevated.*

---

## Ticker: AMGN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $417.20 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.72x |
| ATR(14) | $11.80 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $418.40 | +0.3% |
| Support 1 | $353.95 | -15.1% |
| 200 SMA | $344.00 | -17.5% |
| 50 EMA | $363.60 | -12.8% |
| 10 EMA | $397.73 | -4.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECTED | RSI(2)=92.45, Price ABOVE 200 SMA (oversold threshold broken) | NO SETUP |
| MACD + RSI | REJECTED | MACD=13.21, Signal=10.05, Histogram=+3.16 (bullish), RSI(14)=74.28, RelVol=0.72x (WEAK, <1.0x) | NO SETUP |
| Bollinger Squeeze | REJECTED | Bandwidth=18.40 (6m low=3.98, not squeezed), Breakout=YES, RelVol=0.72x (WEAK volume confirmation) | NO SETUP |
| MA Crossover | REJECTED | EMA10=397.73 ABOVE EMA50=369.67 (bullish), Price NOT in pullback zone, RSI(14)=74.28, RelVol=0.72x (WEAK) | NO SETUP |
| VIX Fear | N/A | Strategy not applicable to equity ticker | N/A |

### Decision
**NO SETUP**

*All strategies rejected. AMGN exhibits poor volume confirmation across all setups (RelVol=0.72x, below 1.0x minimum). RSI(2)=92.45 indicates overextension. MACD and Bollinger Squeeze breakout both fail on weak volume condition. While price structure remains above key moving averages, the lack of volume participation disqualifies all setups. No edge available.*

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $506.06 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.78x |
| ATR(14) | $15.67 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $513.73 | +1.5% |
| Support 1 | $377.39 | -25.4% |
| 200 SMA | $431.79 | -14.6% |
| 50 EMA | $408.59 | -19.3% |
| 10 EMA | $472.23 | -6.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECTED | RSI(2)=94.14, Price ABOVE 200 SMA (oversold threshold broken) | NO SETUP |
| MACD + RSI | REJECTED | MACD=29.40, Signal=18.91, Histogram=+10.49 (bullish), RSI(14)=79.15 (OUT OF RANGE, >75 threshold), RelVol=0.78x (WEAK) | NO SETUP |
| Bollinger Squeeze | REJECTED | Bandwidth=44.54 (6m low=5.20, not squeezed), Breakout=NO, RelVol=0.78x (WEAK) | NO SETUP |
| MA Crossover | REJECTED | EMA10=472.23 ABOVE EMA50=419.80 (bullish crossover YES), Price NOT in pullback zone (Price ABOVE EMA10), RSI(14)=79.15 overbought,