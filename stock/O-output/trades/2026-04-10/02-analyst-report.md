# Technical Analysis Report — 2026-04-10

## Ticker: AI

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $8.58 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.8x |
| ATR(14) | $0.48 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $9.31 | +8.5% |
| Support 1 | $7.68 | -10.5% |
| 200 SMA | $15.93 | +85.6% |
| 50 EMA | $9.57 | +11.5% |
| 10 EMA | $8.57 | -0.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=23.1, Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, Price BELOW 50 SMA, Rel Vol=0.8x | NO SETUP |
| Bollinger Squeeze | FAILED | BW=14.7 (not at 6m low of 7.9), Breakout=NO | NO SETUP |
| MA Crossover | FAILED | 10 EMA vs 50 EMA=BEARISH | NO SETUP |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Decision
**NO SETUP**

Price is severely underwater relative to long-term trend (200 SMA at $15.93). All mean-reversion and momentum indicators rejected. Relative volume weak at 0.8x. No actionable setup on 2026-04-10.

---

## Ticker: GS

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $903.72 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.85x |
| ATR(14) | $27.84 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $918.12 | +1.6% |
| Support 1 | $780.50 | -13.6% |
| 200 SMA | $807.11 | -10.7% |
| 50 EMA | $871.06 | -3.6% |
| 10 EMA | $865.12 | -4.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=89.5 (>= 10), extremely overbought | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=64.6 (in range but no cross), Rel Vol=0.85x | NO SETUP |
| Bollinger Squeeze | FAILED | BW=16.8 (NOT at 6m low of 4.7), Breakout=YES but squeeze condition failed | NO SETUP |
| MA Crossover | FAILED | 10 EMA=865.12, 50 EMA=860.12 (crossover YES), but price NOT in pullback zone, already extended | NO SETUP |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Decision
**NO SETUP**

RSI(2) at 99.5 indicates extreme overbought condition on short-term basis. While MA crossover occurred, price is already well above pullback zone (required within 1.0% of 10 EMA). No volatility squeeze to confirm breakout. Relative volume weak. No valid setup.

---

## Ticker: JPM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $310.33 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.63x |
| ATR(14) | $7.21 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $311.26 | +0.3% |
| Support 1 | $277.68 | -10.5% |
| 200 SMA | $299.98 | -3.3% |
| 50 EMA | $297.82 | -4.0% |
| 10 EMA | $297.68 | -4.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=98.97 (>= 10), extremely overbought | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=67.2 (in range but no cross signal), Rel Vol=0.63x (weak) | NO SETUP |
| Bollinger Squeeze | FAILED | BW=10.8 (NOT at 6m low of 3.96), Breakout=YES but squeeze condition failed | NO SETUP |
| MA Crossover | FAILED | 10 EMA=297.68, 50 EMA=297.03 (crossover YES), but price already extended well above pullback zone | NO SETUP |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Decision
**NO SETUP**

RSI(2) at 99.0 signals extreme overbought on short-term basis. Price has already moved well beyond 10 EMA pullback zone despite recent crossover. Relative volume critically weak at 0.63x. No valid entry conditions met.

---

## Ticker: JNJ

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $241.31 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.83x |
| ATR(14) | $4.26 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $247.21 | +2.4% |
| Support 1 | $232.24 | -3.8% |
| 200 SMA | $198.48 | -17.7% |
| 50 EMA | $236.06 | -2.2% |
| 10 EMA | $241.00 | -0.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=60.7 (>= 10), not in oversold territory | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=52.7 (in range but no cross), Rel Vol=0.83x | NO SETUP |
| Bollinger Squeeze | FAILED | BW=4.68 (near 6m low of 3.91 but NOT below it), Breakout=NO | NO SETUP |
| MA Crossover | TRIGGERED | 10 EMA=241.00, 50 EMA=236.06 (BULLISH), Price in pullback zone (within 0.1%), RSI(14)=52.7 (in range) | **SETUP CONFIRMED** |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Suggested Parameters (MA Crossover)
| Parameter | Value |
|-----------|-------|
| Entry | $241.31 |
| Stop Loss | $234.92 |
| Take Profit | $247.21 |
| Risk/Share | $6.39 |
| Reward/Share | $5.90 |
| R:R Ratio | 0.92:1 |

### Decision
**SETUP CONFIRMED — MA Crossover (CONDITIONAL)**

**MA Crossover entry conditions met**: 10 EMA ($241.00) crossed above 50 EMA ($236.06), price touching 10 EMA within pullback zone, RSI(14) at neutral 52.7. 

**CRITICAL ISSUE**: R:R Ratio is **0.92:1**, which **FAILS the minimum 1.5:1 requirement** for MA Crossover strategy. Risk ($6.39) exceeds reward ($5.90). This setup does not meet portfolio risk management standards.

**RECOMMENDATION**: Do NOT trade. Wait for a better risk/reward setup or choose another ticker.

---

## Ticker: SPY

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $679.91 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.59x |
| ATR(14) | $10.36 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $681.16 | +0.2% |
| Support 1 | $629.28 | -7.4% |
| 200 SMA | $660.58 | -2.8% |
| 50 EMA | $673.27 | -1.0% |
| 10 EMA | $661.97 | -2.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=99.36 (>= 10), extremely overbought | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO (MACD=-1.87, Signal=-6.02), RSI(14)=60.8 (in range), Rel Vol=0.59x | NO SETUP |
| Bollinger Squeeze | FAILED | BW=7.00 (NOT at 6m low of 2.37), Breakout=NO, Rel Vol=0.59x (weak) | NO SETUP |
| MA Crossover | FAILED | 10 EMA vs 50 EMA=BEARISH (10 EMA below 50 EMA) | NO SETUP |
| VIX Fear | FAILED | VIX=19.31, 10d SMA=24.51, Spike=-21.2% (<20% threshold), S&P above 200 SMA | NO SETUP |

### Decision
**NO SETUP**

RSI(2) at 99.4 indicates extreme overbought condition. MA crossover is bearish (10 EMA below 50 EMA). VIX fear spike threshold not met (-21.2% vs required 20%+). Relative volume critically weak at 0.59x. No valid setup on any strategy.

---

## Ticker: QQQ

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $610.19 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.58x |
| ATR(14) | $11.47 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $610.50 | +0.1% |
| Support 1 | $555.60 | -8.9% |
| 200 SMA | $594.96 | -2.5% |
| 50 EMA | $600.52 | -1.6% |
| 10 EMA | $591.58 | -3.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=99.22 (>= 10), extremely overbought | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO (MACD=-1.56, Signal=-5.53), RSI(14)=60.25 (in range), Rel Vol=0.58x | NO SETUP |
| Bollinger Squeeze | FAILED | BW=8.68 (NOT at 6m low of 2.88), Breakout=NO, Rel Vol=0.58x (weak) | NO SETUP |
| MA Crossover | FAILED | 10 EMA vs 50 EMA=BEARISH (10 EMA below 50 EMA) | NO SETUP |
| VIX Fear | FAILED | VIX=19.31, 10d SMA=24.51, Spike=-21.2% (<20% threshold), S&P above 200 SMA | NO SETUP |

### Decision
**NO SETUP**

RSI(2) at 99.2 indicates extreme overbought condition. MA crossover is bearish (10 EMA below 50 EMA). VIX fear spike threshold not met (-21.2% vs required 20%+). Relative volume critically weak at 0.58x. No valid setup on any strategy.

---

## Ticker: AAPL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $260.49 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.68x |
| ATR(14) | $6.11 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $262.16 | +0.6% |
| Support 1 | $245.51 | -5.7% |
| 200 SMA | $250.00 | -4.2% |
| 50 EMA | $260.76 | +0.1% |
| 10 EMA | $255.87 | -1.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=77.92 (>= 10), not in oversold territory | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO (MACD=-0.6, Signal=-2.0), Price BELOW 50 SMA, Rel Vol=0.68x | NO SETUP |
| Bollinger Squeeze | FAILED | BW=5.83 (NOT at 6m low of 3.25), Breakout=YES but squeeze condition not met | NO SETUP |
| MA Crossover | FAILED | 10 EMA vs 50 EMA=BEARISH (10 EMA below 50 EMA) | NO SETUP |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Decision
**NO SETUP**

MA crossover is bearish (10 EMA at $255.87 below 50 EMA at $258.45). MACD shows negative histogram with price below 50 EMA. Relative volume weak at 0.68x. No valid setup on any strategy.

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $373.07 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.96x |
| ATR(14) | $8.69 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $406.12 | +8.9% |
| Support 1 | $356.28