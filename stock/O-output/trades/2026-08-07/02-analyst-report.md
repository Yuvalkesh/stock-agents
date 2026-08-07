# Technical Analysis Report — 2026-08-07

## Ticker: SNOW

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $318.00 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 1.19x |
| ATR(14) | $14.74 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $323.10 | +1.6% |
| Support 1 | $253.59 | -20.2% |
| 200 SMA | $212.00 | -33.3% |
| 50 EMA | $259.10 | -18.5% |
| 10 EMA | $299.34 | -5.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=94.82 (overbought), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD histogram=3.29 (no cross), RSI(14)=77.47 (overbought) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=26.30 (far from 6m low=8.14), RSI(14)=77.47 (overbought) | NO SETUP |
| MA Crossover | FAILED | 10 EMA=$299.34 vs 50 EMA=$256.17 (bullish but NO pullback to 10 EMA), price above both | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Analysis
SNOW is in an extended rally with elevated momentum (RSI(2)=94.82, RSI(14)=77.47). Price is $18.66 above the 10 EMA with no meaningful pullback zone. All mean-reversion and momentum strategies are negated by overbought conditions. The stock is trading near resistance ($323.10) with limited upside confirmation.

### Decision
**NO SETUP** — All strategies rejected. Stock is overbought with no valid entry conditions. Wait for pullback to 10 EMA or consolidation.

---

## Ticker: MA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $575.95 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 1.00x |
| ATR(14) | $12.12 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $583.71 | +1.3% |
| Support 1 | $519.65 | -9.8% |
| 200 SMA | $526.62 | -8.6% |
| 50 EMA | $519.63 | -9.8% |
| 10 EMA | $565.14 | -1.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=87.78 (overbought), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD histogram=1.23 (minimal momentum), RSI(14)=69.46 (in range) but no crossover | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=12.12 (far from 6m low=3.35), no breakout | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA=$565.14 vs 50 EMA=$531.79 (bullish), price within 1.9% of 10 EMA (pullback zone YES), RSI(14)=69.46 | SETUP SIGNALED |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $575.95 |
| Stop Loss | $557.77 (1.5x ATR below entry) |
| Take Profit | $583.71 (resistance / EMA bearish cross) |
| Risk/Share | $18.18 |
| Reward/Share | $7.76 |
| R:R Ratio | 0.43:1 |

### Analysis
MA Crossover strategy signals a setup: 10 EMA bullish vs 50 EMA, price in pullback zone. However, **Risk/Reward ratio is 0.43:1, FAR below the 1.5:1 minimum required for this strategy**. The reward ($7.76/share) is insufficient relative to risk ($18.18/share). This violates position sizing discipline.

### Decision
**NO SETUP** — MA Crossover signals structure but FAILS risk/reward validation (0.43:1 vs required 1.5:1). Trade violates position sizing rules. REJECT.

---

## Ticker: BMY

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $64.15 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.72x |
| ATR(14) | $1.93 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $68.10 | +6.2% |
| Support 1 | $56.78 | -11.5% |
| 200 SMA | $55.00 | -14.3% |
| 50 EMA | $59.75 | -6.9% |
| 10 EMA | $63.79 | -0.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=39.41 (not < 10), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD histogram=0.12 (minimal momentum), RSI(14)=61.80 (in range) but no crossover | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=16.50 (far from 6m low=5.05), no breakout, Volume=WEAK (0.72x) | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA=$63.79 vs 50 EMA=$59.75 (bullish), price within 0.6% of 10 EMA (pullback zone YES), RSI(14)=61.80 | SETUP SIGNALED |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $64.15 |
| Stop Loss | $61.26 (1.5x ATR below entry) |
| Take Profit | $68.10 (resistance / EMA bearish cross) |
| Risk/Share | $2.89 |
| Reward/Share | $3.95 |
| R:R Ratio | 1.37:1 |

### Analysis
BMY Crossover strategy signals structure: 10 EMA bullish vs 50 EMA, price at pullback zone (within 0.6%). However, **Risk/Reward ratio is 1.37:1, below the 1.5:1 minimum required for this strategy**. Additionally, relative volume is WEAK at 0.72x (below 1.0x threshold). The setup barely fails R:R validation and lacks volume confirmation.

### Decision
**NO SETUP** — MA Crossover signals structure but FAILS risk/reward validation (1.37:1 vs required 1.5:1) and volume confirmation (0.72x). REJECT.

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $499.86 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.92x |
| ATR(14) | $16.54 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $501.56 | +0.3% |
| Support 1 | $377.39 | -24.5% |
| 200 SMA | $431.90 | -13.6% |
| 50 EMA | $405.27 | -18.9% |
| 10 EMA | $456.87 | -8.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=87.63 (overbought), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD histogram=12.01 (large positive but no crossover), RSI(14)=78.12 (overbought) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=40.47 (expanded, far from 6m low=5.20), no squeeze condition | NO SETUP |
| MA Crossover | FAILED | 10 EMA=$456.87 vs 50 EMA=$412.87 (bullish crossover occurred within 10 days), but NO pullback to 10 EMA zone — price already $43 above 10 EMA, outside entry zone | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Analysis
MSFT crossed 10 EMA above 50 EMA recently, but the crossover is too old or the rally has extended too far. Price at $499.86 is $43 above the 10 EMA ($456.87), well outside the 1.0% pullback entry zone. RSI(14)=78.12 is overbought. MACD shows momentum but is diverging from RSI extremes, not confirming. No valid entry.

### Decision
**NO SETUP** — MA Crossover: crossover occurred but price too extended from 10 EMA pullback zone. All other strategies negated by overbought conditions. Wait for consolidation or pullback.

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $357.75 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.78x |
| ATR(14) | $13.45 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $384.48 | +7.5% |
| Support 1 | $314.90 | -12.0% |
| 200 SMA | $328.34 | -8.2% |
| 50 EMA | $357.16 | -0.2% |
| 10 EMA | $354.63 | -0.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=27.66 (not < 10), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD histogram=3.73 (positive but no crossover signal), MACD=0.95 vs Signal=-2.78 (just crossed), RSI(14)=52.38 (in range) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=18.93 (far from 6m low=5.06), no squeeze condition | NO SETUP |
| MA Crossover |