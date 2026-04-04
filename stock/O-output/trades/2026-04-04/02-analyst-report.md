# Technical Analysis Report — 2026-04-04

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $373.46 |
| 20-Day Avg Volume | Not provided |
| Today's Volume | Not provided |
| Relative Volume | 0.74x |
| ATR(14) | $8.92 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $413.05 | +10.6% |
| Support 1 | $356.28 | -4.6% |
| 200 SMA | $475.26 | +27.3% |
| 50 EMA | $403.24 | +8.0% |
| 10 EMA | $372.87 | -0.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=85.04, Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, Price BELOW 50 SMA, Volume=0.74x | NO SETUP |
| Bollinger Squeeze | FAIL | BW=17.48 (not at 6m low of 3.65), Breakout=NO, Volume=0.74x | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BEARISH, Price BELOW 50 EMA | NO SETUP |
| VIX Fear | N/A | Not applicable for single ticker | N/A |

### Decision
**NO SETUP**

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $295.77 |
| 20-Day Avg Volume | Not provided |
| Today's Volume | Not provided |
| Relative Volume | 0.73x |
| ATR(14) | $8.49 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $312.47 | +5.6% |
| Support 1 | $272.11 | -8.0% |
| 200 SMA | $264.69 | -10.5% |
| 50 EMA | $310.28 | +4.9% |
| 10 EMA | $291.40 | -1.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=76.78 (>= 10 threshold), Price ABOVE 200 SMA | NO SETUP |
| MACD + RSI | FAIL | MACD cross=YES, Price BELOW 50 SMA, Volume=0.73x (weak) | NO SETUP |
| Bollinger Squeeze | FAIL | BW=14.76 (not at 6m low of 5.06), Breakout=NO, Volume=0.73x | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BEARISH, Price BELOW 50 EMA | NO SETUP |
| VIX Fear | N/A | Not applicable for single ticker | N/A |

### Decision
**NO SETUP**

---

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $177.39 |
| 20-Day Avg Volume | Not provided |
| Today's Volume | Not provided |
| Relative Volume | 0.80x |
| ATR(14) | $5.67 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $188.88 | +6.5% |
| Support 1 | $164.27 | -7.4% |
| 200 SMA | $179.80 | +1.4% |
| 50 EMA | $182.64 | +2.9% |
| 10 EMA | $174.70 | -1.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=85.79 (>= 10 threshold), Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAIL | MACD cross=YES, Price BELOW 50 SMA, Volume=0.80x (weak) | NO SETUP |
| Bollinger Squeeze | FAIL | BW=12.23 (not at 6m low of 5.37), Breakout=NO, Volume=0.80x | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BEARISH, Price BELOW 50 EMA | NO SETUP |
| VIX Fear | N/A | Not applicable for single ticker | N/A |

### Decision
**NO SETUP**

---

## Ticker: COP

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $130.52 |
| 20-Day Avg Volume | Not provided |
| Today's Volume | Not provided |
| Relative Volume | 0.64x |
| ATR(14) | $3.81 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $135.87 | +4.1% |
| Support 1 | $112.93 | -13.4% |
| 200 SMA | $97.17 | -25.6% |
| 50 EMA | $114.68 | -12.1% |
| 10 EMA | $129.40 | -0.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=52.0 (>= 10 threshold), Price ABOVE 200 SMA | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, Price ABOVE 50 SMA, Volume=0.64x (weak) | NO SETUP |
| Bollinger Squeeze | FAIL | BW=18.91 (not at 6m low of 4.53), Breakout=NO, Volume=0.64x | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA(129.40) vs 50 EMA(116.63)=BULLISH, Pullback=YES, Price ABOVE EMA10, RSI(14)=66.4 | **REJECTED** |
| VIX Fear | N/A | Not applicable for single ticker | N/A |

### Suggested Parameters (MA Crossover — REJECTED)
| Parameter | Value | Reason |
|-----------|-------|--------|
| Entry | $130.52 | Pre-computed |
| Stop Loss | $124.81 | 1.5x ATR(14) below entry |
| Target | $135.87 | Resistance level |
| R:R Ratio | 0.94:1 | **FAILS minimum 1.5:1 requirement** |

### Decision
**NO SETUP** — MA Crossover setup triggered on technicals (10 EMA > 50 EMA, price in pullback zone, RSI in range), BUT risk-reward ratio of 0.94:1 is **below the minimum 1.5:1 threshold** for this strategy. Trade REJECTED.

---

## Ticker: MRVL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $107.11 |
| 20-Day Avg Volume | Not provided |
| Today's Volume | Not provided |
| Relative Volume | 0.91x |
| ATR(14) | $5.72 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $107.84 | +0.7% |
| Support 1 | $83.40 | -22.1% |
| 200 SMA | $81.56 | -23.8% |
| 50 EMA | $84.95 | -20.7% |
| 10 EMA | $97.66 | -8.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=86.82 (>= 10 threshold), Price ABOVE 200 SMA | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, Price ABOVE 50 SMA, Volume=0.91x | NO SETUP |
| Bollinger Squeeze | FAIL | BW=24.68 (not at 6m low of 10.06), Breakout=YES but Volume=0.91x (weak), RSI(14)=67.5 | NO SETUP |
| MA Crossover | FAIL | 10 EMA(97.66) vs 50 EMA(88.19)=BULLISH, but Price NOT in pullback zone (107.11 >> 97.66) | NO SETUP |
| VIX Fear | N/A | Not applicable for single ticker | N/A |

### Decision
**NO SETUP**

---

## Ticker: HD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $321.63 |
| 20-Day Avg Volume | Not provided |
| Today's Volume | Not provided |
| Relative Volume | 0.88x |
| ATR(14) | $8.78 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $359.24 | +11.7% |
| Support 1 | $318.66 | -0.9% |
| 200 SMA | $369.23 | +14.8% |
| 50 EMA | $360.46 | +12.0% |
| 10 EMA | $328.51 | +2.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=18.88 (>= 10 threshold), Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAIL | MACD cross=YES, RSI(14)=33.7 (OUT of 35-75 range — too low), Price BELOW 50 SMA | NO SETUP |
| Bollinger Squeeze | FAIL | BW=12.79 (not at 6m low of 4.43), Breakout=NO, Volume=0.88x | NO SETUP |
| MA Crossover | FAIL | 10 EMA(328.51) vs 50 EMA(350.27)=BEARISH, Price BELOW 10 EMA | NO SETUP |
| VIX Fear | N/A | Not applicable for single ticker | N/A |

### Decision
**NO SETUP**

---

## Ticker: WMT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $125.79 |
| 20-Day Avg Volume | Not provided |
| Today's Volume | Not provided |
| Relative Volume | 0.58x |
| ATR(14) | $2.62 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $126.93 | +0.9% |
| Support 1 | $118.02 | -6.2% |
| 200 SMA | $108.88 | -13.4% |
| 50 EMA | $124.28 | -1.2% |
| 10 EMA | $123.79 | -1.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=97.97 (>= 10 threshold), Price ABOVE 200 SMA | NO SETUP |
| MACD + RSI | CONDITIONAL | MACD cross=YES, RSI(14)=56.4 (in 35-75 range), Price ABOVE 50 SMA | **REJECTED** |
| Bollinger Squeeze | FAIL | BW=6.01 (not at 6m low of 2.38), Breakout=NO, Volume=0.58x | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA(123.79) vs 50 EMA(122.56)=BULLISH, Pullback=YES, Price ABOVE EMA10, RSI(14)=56.4 | **REJECTED** |
| VIX Fear | N/A | Not applicable for single ticker | N/A |

### Suggested Parameters (MACD + RSI — REJECTED)
| Parameter | Value | Reason |
|-----------|-------|--------|
| Entry | $125.79 | Pre-computed |
| Stop Loss | $121.86 | 1.5x ATR(14) below entry |
| Target | $126.93 | Resistance (exit on MACD bearish cross or RSI > 80) |
| R:R Ratio | 0.29:1 | **FAILS minimum 1.0:1 requirement** |

### Suggested Parameters (MA Crossover — REJECTED)
| Parameter | Value | Reason |
|-----------|-------|--------|
| Entry | $125.79 | Pre-computed |
| Stop Loss | $121.86 | 1.5x ATR(14) below entry |
| Target | $126.93 | Resistance (exit on EMA bearish cross) |
| R:R Ratio | 0.29:1 | **FAILS minimum 1.5:1 requirement** |

### Decision
**NO SETUP** — Both MACD + RSI and MA Crossover setups triggered on technicals (MACD bullish cross, 10 EMA > 50 EMA, price in pullback zone, RSI in range), BUT risk-reward ratios (0.29:1 for both) are **critically below minimum thresholds** (1.0:1 for MACD, 1.5:1 for MA Crossover). The resistance level is too tight relative to stop loss distance. Trades REJECTED.

---

## Summary
**Total Confirmed Setups: 0 of 7 tickers**

All seven tickers fail technical criteria or risk-reward validation:
- **MSFT, GOOGL, NVDA**: Bearish MA crossovers, prices below key SMAs, weak volume
- **COP**: MA crossover fails R:R threshold (0.94:1 vs 1.5:1 minimum)
- **MRVL**: MA pullback zone not reached, MACD no cross signal
- **HD**: Bearish MA alignment, RSI too low (33.7), price below both 50 EMA and 200 SMA
- **WMT**: Both MACD+RSI and MA Crossover fail critical R:R ratios (0.29:1 vs 1.0:1 and 1.5:1 minimums respectively)

**Market Environment**: Weak overall. Most mega-caps trending down relative to 200 SMAs. Low relative volume (0.58x–0.91x) across all tickers indicates lack of conviction. No margin of safety on any setup.