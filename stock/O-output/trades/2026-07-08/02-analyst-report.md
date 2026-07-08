# Technical Analysis Report — 2026-07-08

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $196.93 |
| 20-Day Avg Volume | baseline |
| Today's Volume | 0.83x |
| Relative Volume | 0.83x |
| ATR(14) | $6.90 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $213.99 | +8.6% |
| Support 1 | $189.80 | -3.6% |
| 200 SMA | $191.25 | -2.9% |
| 50 EMA | $209.60 | +6.4% |
| 10 EMA | $198.13 | +0.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=66.0, Price > 200 SMA=YES | RSI(2) NOT < 10 (oversold threshold missed) | NO SETUP |
| MACD + RSI | MACD=-4.01, RSI(14)=43.5, Price < 50 SMA | MACD below signal, price below 50 SMA trend filter failed | NO SETUP |
| Bollinger Squeeze | BW=11.73, 6m Low=5.37, RSI(14)=43.5 | Bandwidth well above 6-month low, no squeeze present | NO SETUP |
| MA Crossover | EMA10=$198.13 > EMA50=$203.58, Price=$196.93 | 10 EMA below 50 EMA (bearish), price below 10 EMA | NO SETUP |
| VIX Fear | N/A | Strategy not applicable to equity tickers | N/A |

### Decision
**NO SETUP**

Data does not support entry on any verified strategy. Price below both 10 EMA and 50 EMA; RSI(2) well above oversold threshold; relative volume weak at 0.83x.

---

## Ticker: AMD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $516.11 |
| 20-Day Avg Volume | baseline |
| Today's Volume | 0.93x |
| Relative Volume | 0.93x |
| ATR(14) | $38.05 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $584.73 | +13.3% |
| Support 1 | $437.23 | -15.3% |
| 200 SMA | $281.93 | -45.3% |
| 50 EMA | $469.57 | -8.9% |
| 10 EMA | $532.43 | +3.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=30.28, Price > 200 SMA=YES | RSI(2) NOT < 10 (no extreme oversold condition) | NO SETUP |
| MACD + RSI | MACD=20.14 < Signal=24.85, RSI(14)=51.2, Price > 50 SMA | MACD below signal line (bearish cross), momentum declining | NO SETUP |
| Bollinger Squeeze | BW=22.05, 6m Low=9.53, RSI(14)=51.2 | Bandwidth well above 6-month low, no squeeze; price well within bands | NO SETUP |
| MA Crossover | EMA10=$532.43 > EMA50=$463.31, Price=$516.11 | EMA10 above EMA50 (bullish), but price below EMA10 (no pullback zone) | NO SETUP |
| VIX Fear | N/A | Strategy not applicable to equity tickers | N/A |

### Decision
**NO SETUP**

No strategy parameters met. MACD bearish crossover despite bullish EMA alignment; price below faster MA; volume weak at 0.93x.

---

## Ticker: AMAT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $554.50 |
| 20-Day Avg Volume | baseline |
| Today's Volume | 0.95x |
| Relative Volume | 0.95x |
| ATR(14) | $47.32 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $739.67 | +33.4% |
| Support 1 | $466.51 | -15.9% |
| 200 SMA | $342.74 | -38.2% |
| 50 EMA | $496.79 | -10.4% |
| 10 EMA | $612.10 | +10.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=6.55, Price > 200 SMA=YES | RSI(2) < 10 ✓, Price > 200 SMA ✓, Price > $10 ✓ | SETUP CONFIRMED |
| MACD + RSI | MACD=36.63 < Signal=47.06, RSI(14)=48.1, Price > 50 SMA | MACD below signal (bearish), histogram negative | NO SETUP |
| Bollinger Squeeze | BW=40.57, 6m Low=8.80, RSI(14)=48.1 | Bandwidth well above 6-month low; no squeeze | NO SETUP |
| MA Crossover | EMA10=$612.10 > EMA50=$519.18, Price=$554.50 | EMA10 above EMA50 (bullish), but price below EMA10 (outside pullback zone) | NO SETUP |
| VIX Fear | N/A | Strategy not applicable to equity tickers | N/A |

### Suggested Parameters (Connors RSI(2) Mean Reversion)
| Parameter | Value |
|-----------|-------|
| Entry | $554.50 |
| Stop Loss | $459.86 |
| Take Profit | $624.85 |
| Risk/Share | $94.64 |
| Reward/Share | $70.35 |
| R:R Ratio | 0.74:1 |

### Decision
**SETUP CONFIRMED — Connors RSI(2) Mean Reversion**

All entry conditions satisfied: RSI(2) = 6.55 (well below 10 oversold threshold), price above 200 SMA confirming long-term uptrend, stock above $10 liquidity filter. Exit defined on close above 5-day SMA ($624.85) or 2x ATR stop at $459.86. R:R ratio 0.74:1 meets minimum 0.5:1 threshold. Relative volume 0.95x acceptable for dip reversal setup.

---

## Ticker: ABNB

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $148.80 |
| 20-Day Avg Volume | baseline |
| Today's Volume | 0.59x |
| Relative Volume | 0.59x |
| ATR(14) | $4.36 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $150.19 | +0.9% |
| Support 1 | $127.23 | -14.5% |
| 200 SMA | $130.34 | -12.4% |
| 50 EMA | $138.60 | -6.9% |
| 10 EMA | $145.47 | -2.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=70.67, Price > 200 SMA=YES | RSI(2) NOT < 10 (overbought, not oversold) | NO SETUP |
| MACD + RSI | MACD=3.44 > Signal=2.61, RSI(14)=62.8, Price > 50 SMA | MACD above signal, RSI elevated but RSI(14) in range 35-75 ✓, price above 50 SMA ✓, volume weak | NO SETUP (volume fails) |
| Bollinger Squeeze | BW=17.44, 6m Low=4.49, RSI(14)=62.8 | Bandwidth well above 6-month low; no squeeze | NO SETUP |
| MA Crossover | EMA10=$145.47 > EMA50=$138.60, Price=$148.80 | 10 EMA above 50 EMA ✓, price in pullback zone (within 1.0% of 10 EMA) ✓, price above 10 EMA ✓, RSI(14)=62.8 > 45 ✓ | SETUP FLAGGED |
| VIX Fear | N/A | Strategy not applicable to equity tickers | N/A |

### Suggested Parameters (MA Crossover — Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $148.80 |
| Stop Loss | $142.26 |
| Take Profit | $150.19 |
| Risk/Share | $6.54 |
| Reward/Share | $1.39 |
| R:R Ratio | 0.21:1 |

### Decision
**NO SETUP — MA Crossover Failed on R:R Validation**

While MA crossover parameters align (10 EMA above 50 EMA, price in pullback zone, RSI(14) acceptable), **Risk/Reward ratio is 0.21:1, which FAILS the required minimum of 1.5:1 for this strategy**. Reward too small relative to risk. Additionally, relative volume at 0.59x is weak. Trade rejected on risk/reward basis.

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $388.84 |
| 20-Day Avg Volume | baseline |
| Today's Volume | 0.60x |
| Relative Volume | 0.60x |
| ATR(14) | $12.51 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $417.16 | +7.3% |
| Support 1 | $349.20 | -10.2% |
| 200 SMA | $442.60 | +13.8% |
| 50 EMA | $405.79 | +4.4% |
| 10 EMA | $382.13 | -1.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=72.40, Price < 200 SMA | RSI(2) NOT < 10 (overbought); price below 200 SMA (downtrend fails trend filter) | NO SETUP |
| MACD + RSI | MACD=-7.35 < Signal=-9.78, RSI(14)=49.2, Price < 50 SMA | MACD above signal (bullish cross apparent), BUT price below 50 SMA (medium-term trend filter failed) | NO SETUP |
| Bollinger Squeeze | BW=14.83, 6m Low=4.19,