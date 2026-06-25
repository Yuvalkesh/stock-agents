# Technical Analysis Report — 2026-06-25

## Ticker: KLAC

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $240.48 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.85x |
| ATR(14) | $15.29 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $269.90 | +12.2% |
| Support 1 | $188.60 | -21.6% |
| 200 SMA | $146.58 | -39.1% |
| 50 EMA | $198.23 | -17.6% |
| 10 EMA | $241.78 | +0.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | ❌ FAIL | RSI(2)=23.98, Price/200 SMA=ABOVE | NO SETUP |
| MACD + RSI | ❌ FAIL | MACD=17.2, Signal=15.87, Histogram=1.32 (no cross), RSI(14)=57.95 | NO SETUP |
| Bollinger Squeeze | ❌ FAIL | Bandwidth=44.37 (6m min=8.90, NO squeeze), Volume=WEAK (0.85x) | NO SETUP |
| MA Crossover | ❌ FAIL | 10 EMA=241.78, 50 EMA=203.39 (bullish), Price=240.48 (BELOW 10 EMA) | NO SETUP |
| VIX Fear | N/A | Strategy does not apply to individual stocks | N/A |

### Decision
**NO SETUP**

All five strategies rejected. RSI(2) is too high (23.98, threshold < 10), no MACD crossover present, no Bollinger Squeeze detected, and price has not pulled back to the 10 EMA for entry. Relative volume weak at 0.85x. No actionable setup.

---

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $374.80 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.99x |
| ATR(14) | $23.22 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $409.75 | +9.3% |
| Support 1 | $302.53 | -19.3% |
| 200 SMA | $213.98 | -42.9% |
| 50 EMA | $305.29 | -18.6% |
| 10 EMA | $370.57 | -1.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | ❌ FAIL | RSI(2)=36.46, Price/200 SMA=ABOVE | NO SETUP |
| MACD + RSI | ❌ FAIL | MACD=24.24, Signal=22.56, Histogram=1.68 (no cross), RSI(14)=59.46 | NO SETUP |
| Bollinger Squeeze | ❌ FAIL | Bandwidth=34.24 (6m min=11.03, NO squeeze), Volume=WEAK (0.99x) | NO SETUP |
| MA Crossover | ⚠️ CONDITIONAL | 10 EMA=370.57, 50 EMA=313.77 (bullish), Price=374.80 (ABOVE 10 EMA), RSI(14)=59.46 | SETUP DETECTED BUT R:R FAILS |
| VIX Fear | N/A | Strategy does not apply to individual stocks | N/A |

### Suggested Parameters (Pre-Computed, NOT USED — R:R fails threshold)
| Parameter | Value |
|-----------|-------|
| Entry | $374.80 |
| Stop Loss | $339.97 |
| Take Profit | $409.75 |
| Risk/Share | $34.83 |
| Reward/Share | $34.95 |
| R:R Ratio | 1.0:1 |
| **Min R:R Required** | **1.5:1** |
| **Result** | **FAIL** |

### Decision
**NO SETUP**

MA Crossover strategy technically triggers (bullish EMA arrangement, price above 10 EMA, RSI in range, relative volume adequate at 0.99x), but the pre-computed R:R ratio of 1.0:1 **fails the minimum 1.5:1 threshold** required by strategy rules. Risk equals reward — insufficient profit potential. Trade rejected.

---

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $199.00 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.89x |
| ATR(14) | $7.41 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $232.01 | +16.6% |
| Support 1 | $196.58 | -1.2% |
| 200 SMA | $190.18 | -4.4% |
| 50 EMA | $210.05 | +5.5% |
| 10 EMA | $205.67 | +3.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | ❌ FAIL | RSI(2)=12.55 (threshold < 10 fails by 2.55), Price/200 SMA=ABOVE | NO SETUP |
| MACD + RSI | ❌ FAIL | MACD=-2.2, Signal=-0.85 (bearish), Histogram=-1.35, Price BELOW 50 EMA | NO SETUP |
| Bollinger Squeeze | ❌ FAIL | Bandwidth=12.84 (6m min=5.37, NO squeeze), Volume=WEAK (0.89x) | NO SETUP |
| MA Crossover | ❌ FAIL | 10 EMA=205.67, 50 EMA=206.27 (bearish arrangement, EMA10 below EMA50), Price BELOW both | NO SETUP |
| VIX Fear | N/A | Strategy does not apply to individual stocks | N/A |

### Decision
**NO SETUP**

All strategies rejected. NVDA is in a downtrend: price below both 10 EMA and 50 EMA, MACD bearish (signal line above MACD), and no meaningful support near current levels. RSI(2) just barely fails mean-reversion threshold. Relative volume weak. No trade setup.

---

## Ticker: AAPL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $293.08 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.99x |
| ATR(14) | $7.00 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $317.40 | +8.3% |
| Support 1 | $287.38 | -1.9% |
| 200 SMA | $268.64 | -8.3% |
| 50 EMA | $290.73 | -0.8% |
| 10 EMA | $296.51 | +1.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | ❌ FAIL | RSI(2)=12.66 (threshold < 10 fails by 2.66), Price/200 SMA=ABOVE | NO SETUP |
| MACD + RSI | ❌ FAIL | MACD=0.19, Signal=1.93 (MACD below signal), Histogram=-1.74 (bearish), RSI(14)=45.84 | NO SETUP |
| Bollinger Squeeze | ❌ FAIL | Bandwidth=10.75 (6m min=4.27, NO squeeze), Volume=WEAK (0.99x) | NO SETUP |
| MA Crossover | ❌ FAIL | 10 EMA=296.51, 50 EMA=290.80 (bullish), Price=293.08 (BELOW 10 EMA, not in pullback zone) | NO SETUP |
| VIX Fear | N/A | Strategy does not apply to individual stocks | N/A |

### Decision
**NO SETUP**

All strategies rejected. AAPL price sits between the EMAs but has not pulled back to the 10 EMA to trigger the MA Crossover entry. MACD histogram is negative (bearish divergence). RSI(2) just above oversold but fails the < 10 threshold. No clear setup.

---

## Ticker: ABNB

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $144.40 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.03x |
| ATR(14) | $4.58 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $147.27 | +2.0% |
| Support 1 | $127.23 | -11.9% |
| 200 SMA | $129.40 | -10.4% |
| 50 EMA | $137.15 | -5.1% |
| 10 EMA | $138.98 | -3.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | ❌ FAIL | RSI(2)=85.37 (overbought, >> 10 threshold), Price/200 SMA=ABOVE | NO SETUP |
| MACD + RSI | ❌ FAIL | MACD=1.70, Signal=0.64, Histogram=1.06 (MACD above signal but NO cross), RSI(14)=63.36 | NO SETUP |
| Bollinger Squeeze | ❌ FAIL | Bandwidth=12.24 (6m min=4.49, NO squeeze), Breakout=YES but Volume=WEAK (1.03x, below 1.5x threshold), RSI=63.36 | NO SETUP |
| MA Crossover | ❌ FAIL | 10 EMA=138.98, 50 EMA=135.63 (bullish), Crossover=YES but Price ABOVE 10 EMA (no pullback zone hit) | NO SETUP |
| VIX Fear | N/A | Strategy does not apply to individual stocks | N/A |

### Decision
**NO SETUP**

All strategies rejected. ABNB is extended: RSI(2)=85.37 (extreme overbought, no mean-reversion dip), price already above both EMAs with no