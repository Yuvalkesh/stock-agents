# Technical Analysis Report — 2026-06-19

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $389.04 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 2.01x |
| ATR(14) | $22.35 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $401.00 | +3.1% |
| Support 1 | $291.59 | -25.0% |
| 200 SMA | $209.70 | -46.1% |
| 50 EMA | $297.96 | -23.4% |
| 10 EMA | $360.30 | -7.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=81.2, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD histogram=4.25, RSI(14)=68.6, Price vs 50 SMA=ABOVE | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=32.4, Min=11.0, Squeeze=NO | NO SETUP |
| MA Crossover | FAIL | 10 EMA=360.3 vs 50 EMA=304.7, No pullback | NO SETUP |
| VIX Fear | N/A | Not applicable | N/A |

### Analysis Notes
RSI(2) is extremely elevated at 81.2, indicating overbought conditions rather than mean reversion setup. Price is well above 200 SMA but offers no pullback entry. MACD is positive but histogram is small and RSI is elevated, reducing momentum setup probability. No volatility squeeze present. No moving average crossover signal active.

### Decision
**NO SETUP**

---

## Ticker: MRVL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $310.58 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 3.54x |
| ATR(14) | $28.54 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $329.88 | +6.2% |
| Support 1 | $188.20 | -39.4% |
| 200 SMA | $113.00 | -63.6% |
| 50 EMA | $197.94 | -36.2% |
| 10 EMA | $282.95 | -8.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=79.3, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | TRIGGER | MACD cross=YES, RSI(14)=64.6, Price vs 50 SMA=ABOVE, Volume=3.54x | SETUP CONFIRMED |
| Bollinger Squeeze | FAIL | Bandwidth=66.5, Min=10.1, Squeeze=NO | NO SETUP |
| MA Crossover | FAIL | 10 EMA=282.95 vs 50 EMA=209.57, No pullback | NO SETUP |
| VIX Fear | N/A | Not applicable | N/A |

### Suggested Parameters (Pre-Computed Trade Parameters)
| Parameter | Value |
|-----------|-------|
| Entry | $310.58 |
| Stop Loss | $267.77 (1.5x ATR(14) below entry) |
| Target | $329.88 (resistance, exit on MACD bearish cross or RSI>80) |
| Risk/Share | $42.81 |
| Reward/Share | $19.30 |
| R:R Ratio | 0.45:1 |

### Analysis Notes
MACD line has crossed above signal line with positive histogram (0.63). RSI(14) is in ideal momentum range at 64.6 (not overbought). Price well above 50 SMA at $197.94. Volume confirmation strong at 3.54x average. However, **R:R ratio of 0.45:1 falls below strategy minimum of 1.0:1**. Risk ($42.81) exceeds reward ($19.30) by 2.2x — unfavorable risk/reward geometry.

### Decision
**SETUP CONFIRMED [MACD + RSI MOMENTUM] — BUT REJECTED ON RISK/REWARD**
Trade setup is technically valid, but pre-computed parameters show insufficient reward relative to risk. Recommend skipping this trade per position management rules.

---

## Ticker: CDNS

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $387.39 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 2.63x |
| ATR(14) | $15.98 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $416.69 | +7.6% |
| Support 1 | $347.56 | -10.3% |
| 200 SMA | $326.32 | -15.8% |
| 50 EMA | $353.71 | -8.7% |
| 10 EMA | $388.55 | +0.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=35.1, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD histogram=-2.86, RSI(14)=55.3, Price vs 50 SMA=ABOVE | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=15.3, Min=6.8, Squeeze=NO | NO SETUP |
| MA Crossover | FAIL | 10 EMA=388.55 vs 50 EMA=359.73, Price below 10 EMA, Pullback zone=YES | NO SETUP |
| VIX Fear | N/A | Not applicable | N/A |

### Analysis Notes
MACD histogram is negative (-2.86), indicating bearish momentum. Price is only $1.16 below 10 EMA, still within pullback zone but has not bounced decisively above. MA Crossover condition requires price to bounce (close above 10 EMA) after pullback — current price is below EMA. RSI(14) is neutral at 55.3. No clear momentum or mean reversion signal present.

### Decision
**NO SETUP**

---

## Ticker: ROKU

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $138.07 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 3.96x |
| ATR(14) | $6.01 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $148.88 | +7.9% |
| Support 1 | $115.00 | -16.7% |
| 200 SMA | $105.04 | -23.9% |
| 50 EMA | $122.44 | -11.3% |
| 10 EMA | $132.98 | -3.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=61.2, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD histogram=1.12, RSI(14)=61.8, Price vs 50 SMA=ABOVE | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=22.7, Min=5.9, Squeeze=NO | NO SETUP |
| MA Crossover | FAIL | 10 EMA=132.98 vs 50 EMA=122.15, No pullback | NO SETUP |
| VIX Fear | N/A | Not applicable | N/A |

### Analysis Notes
RSI(2) at 61.2 shows neither deep oversold nor overbought conditions. MACD histogram is positive but small (1.12), and RSI(14) is in momentum range but not showing strong conviction. No pullback to 10 EMA for MA Crossover entry. Price is extended above 10 EMA, making a mean reversion setup unlikely. High relative volume (3.96x) but no clear directional signal to execute.

### Decision
**NO SETUP**

---

## Ticker: META

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $577.22 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.50x |
| ATR(14) | $20.11 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $642.40 | +11.3% |
| Support 1 | $556.49 | -3.6% |
| 200 SMA | $653.70 | +13.3% |
| 50 EMA | $621.37 | +7.7% |
| 10 EMA | $584.76 | +1.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=46.7, Price vs 200 SMA=BELOW | NO SETUP |
| MACD + RSI | FAIL | MACD histogram=-1.53, RSI(14)=43.0, Price vs 50 SMA=BELOW | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=15.0, Min=4.1, Squeeze=NO | NO SETUP |
| MA Crossover | FAIL | 10 EMA=584.76 vs 50 EMA=608.98, Bearish crossover signal, Price below both EMAs | NO SETUP |
| VIX Fear | N/A | Not applicable | N/A |

### Analysis Notes
Price is below 200 SMA ($653.70) and below 50 EMA ($621.37), indicating bearish trend. MACD is negative with negative histogram (-1.53). RSI(14) is at 43.0, approaching oversold but not yet a reversal signal. 10 EMA is below 50 EMA, confirming bearish structure. Price is in a pullback zone but in a downtrend — not suitable for long entry strategies. No bullish setup present.

### Decision
**NO SETUP**

---

## Ticker: GE

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $357.64 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.58x |
| ATR(14) | $10.48 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $364.70 | +2.0% |
| Support 1 |