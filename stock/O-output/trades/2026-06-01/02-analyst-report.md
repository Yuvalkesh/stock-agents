# Technical Analysis Report — 2026-06-01

## Ticker: AI

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $11.61 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 1.17x |
| ATR(14) | $0.56 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $11.72 | +0.9% |
| Support 1 | $8.32 | -28.3% |
| 200 SMA | $13.12 | +12.9% |
| 50 EMA | $9.01 | -22.5% |
| 10 EMA | $10.03 | -13.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=99.86, Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAILED | RSI(14)=76.28 (out of range 35-75), MACD not crossed | NO SETUP |
| Bollinger Squeeze | FAILED | BW=30.02 (not squeeze), Vol=weak 1.17x, RSI=76.28 (overbought) | NO SETUP |
| MA Crossover | FAILED | EMA10 (10.03) > EMA50 (9.48) bullish, but price not in pullback zone | NO SETUP |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Decision
**NO SETUP**

All strategies rejected. AI shows extreme overbought conditions (RSI(2)=99.86, RSI(14)=76.28) with price below long-term 200 SMA trend filter. No valid entry point.

---

## Ticker: QCOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $231.22 |
| Relative Volume | 0.42x |
| ATR(14) | $16.97 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $259.92 | +12.4% |
| Support 1 | $164.79 | -28.8% |
| 200 SMA | $161.72 | -30.1% |
| 50 EMA | $183.86 | -20.5% |
| 10 EMA | $229.12 | -0.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=26.90 (not < 10), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD not crossed, RSI(14)=60.34 (in range), Volume WEAK 0.42x | NO SETUP |
| Bollinger Squeeze | FAILED | BW=40.91 (no squeeze), No breakout, Volume WEAK 0.42x | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA (229.12) > 50 EMA (183.86) bullish, Price in pullback zone, RSI=60.34 OK | SETUP FLAGGED |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Suggested Parameters (MA Crossover — REJECTED)
| Parameter | Value |
|-----------|-------|
| Entry | $231.22 |
| Stop Loss | $205.76 |
| Target | $259.92 |
| R:R Ratio | 1.13:1 |

**Verdict Rationale:** MA Crossover parameters fail min R:R threshold (1.13:1 < required 1.5:1). Additionally, relative volume at 0.42x is weak for entry confirmation. **REJECTED.**

### Decision
**NO SETUP**

---

## Ticker: AMAT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $459.46 |
| Relative Volume | 0.36x |
| ATR(14) | $18.38 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $462.40 | +0.6% |
| Support 1 | $385.17 | -16.1% |
| 200 SMA | $293.21 | -36.2% |
| 50 EMA | $398.88 | -13.2% |
| 10 EMA | $442.60 | -3.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=92.81 (not < 10), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD not crossed, RSI(14)=64.74 (in range), Volume WEAK 0.36x | NO SETUP |
| Bollinger Squeeze | FAILED | BW=16.23 (no squeeze), No breakout, Volume WEAK 0.36x, RSI=64.74 | NO SETUP |
| MA Crossover | FAILED | No crossover, EMA10 (442.60) < EMA50 (398.88) bullish, Price not in pullback zone | NO SETUP |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Decision
**NO SETUP**

All strategies rejected. Price near upper resistance with weak volume (0.36x) provides no entry confirmation.

---

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $317.29 |
| Relative Volume | 0.47x |
| ATR(14) | $13.74 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $333.33 | +5.1% |
| Support 1 | $254.95 | -19.7% |
| 200 SMA | $193.67 | -39.0% |
| 50 EMA | $265.37 | -16.4% |
| 10 EMA | $308.38 | -2.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=49.09 (not < 10), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD not crossed, RSI(14)=65.45 (in range), Volume WEAK 0.47x | NO SETUP |
| Bollinger Squeeze | FAILED | BW=22.87 (no squeeze), No breakout, Volume WEAK 0.47x | NO SETUP |
| MA Crossover | FAILED | No crossover, EMA10 (308.38) > EMA50 (272.45) bullish, Price not in pullback zone | NO SETUP |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Decision
**NO SETUP**

Weak volume (0.47x) across all strategies. No pullback to 10 EMA for MA Crossover entry.

---

## Ticker: JPM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $295.76 |
| Relative Volume | 0.31x |
| ATR(14) | $5.96 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $316.30 | +6.9% |
| Support 1 | $293.67 | -0.7% |
| 200 SMA | $303.61 | +2.6% |
| 50 EMA | $302.67 | +2.3% |
| 10 EMA | $300.19 | +1.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=22.47 (not < 10), Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD not crossed, RSI(14)=42.36 (in range), Price BELOW 50 SMA | NO SETUP |
| Bollinger Squeeze | FAILED | BW=6.41 (no squeeze), No breakout, Volume WEAK 0.31x | NO SETUP |
| MA Crossover | FAILED | No crossover, 10 EMA (300.19) < 50 EMA (302.67) BEARISH crossover | NO SETUP |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Decision
**NO SETUP**

Bearish MA configuration with price below both 50 EMA and 200 SMA. Weakest relative volume (0.31x). No valid entry.

---

## Ticker: XOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $149.05 |
| Relative Volume | 0.41x |
| ATR(14) | $4.25 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $163.68 | +9.8% |
| Support 1 | $142.95 | -4.1% |
| 200 SMA | $130.49 | -12.5% |
| 50 EMA | $153.86 | +3.2% |
| 10 EMA | $150.35 | +0.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=68.91 (not < 10), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD not crossed, RSI(14)=46.15 (in range), Price BELOW 50 SMA | NO SETUP |
| Bollinger Squeeze | FAILED | BW=13.27 (no squeeze), No breakout, Volume WEAK 0.41x | NO SETUP |
| MA Crossover | FAILED | No crossover, 10 EMA (150.35) < 50 EMA (151.05) BEARISH, Price below EMA10 | NO SETUP |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Decision
**NO SETUP**

Bearish MA alignment with price dipping below 10 EMA. No pullback setup. Weak volume (0.41x).

---

## Ticker: CVX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $187.00 |
| Relative Volume | 0.41x |
| ATR(14) | $4.61 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $198.87 | +6.3% |
| Support 1 | $177.90 | -4.8% |
| 200 SMA | $166.98 | -10.7% |
| 50 EMA | $186.96 | -0.02% |
| 10 EMA | $186.31 | -0.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=81.92 (not < 10), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD not crossed, RSI(14)=49.56 (in range), Price BELOW 50 SMA | NO SETUP |
| Bollinger Squeeze | FAILED | BW=10.08 (no squeeze), No breakout, Volume WEAK 0.41x | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA (186.31) < 50 EMA (186.96) BEARISH, Price in pullback zone, RSI=49.56 | SETUP FLAGGED |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Suggested Parameters (MA Crossover — REJECTED)
| Parameter | Value |
|-----------|-------|
| Entry | $187.00 |
| Stop Loss | $180.09 |
| Target | $198.87 |
| R:R Ratio | 1.72:1 |

**Verdict Rationale:** MA Crossover shows **BEARISH** configuration (10 EMA < 50 EMA). This is a **bearish crossover setup**, which violates the bullish entry condition. While R:R ratio of 1.72:1 passes minimum threshold of 1.5:1, the fundamental MA structure is in downtrend mode. **REJECTED — Conflicting signal.**

### Decision
**NO SETUP**

MA configuration is BEARISH (10 EMA below 50 EMA), opposite of required bullish crossover. Trade parameter sheet shows the position would be short-biased.

---

## Ticker: QQQ

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $741.80 |
| Relative Volume | 0.46x |
| ATR(14) | $10.06 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $742.28 | +0.06% |
| Support 1 | $668.90 | -9.8% |
| 200 SMA | $617.64 | -16.7% |
| 50 EMA | $655.89 | -11.6% |
| 10 EMA | $725.98 | -2.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=98.17 (not < 10), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD crossed, RSI(14)=78.19 (out of range 35-75), OVERBOUGHT | NO SETUP |
| Bollinger Squeeze | FAILED | BW=9.78 (no squeeze), No breakout, Volume WEAK 0.46x, RSI=78.19 | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA (725.98) > 50 EMA (674.18) bullish, Price in pullback zone, RSI=78.19 OVERBOUGHT | SETUP FLAGGED |
| VIX Fear | FAILED | VIX=16.11, 10d SMA=16.60, Spike=-2.96% (< 20% threshold) | NO SETUP |

### Suggested Parameters (MA Crossover — REJECTED)
| Parameter | Value |
|-----------|-------|
| Entry | $741.80 |
| Stop Loss | $726.71 |
| Target | $742.28 |
| R:R Ratio | 0.03:1 |

**Verdict Rationale:** MA Crossover parameters fail catastrophically on R:R ratio (0.03:1 << required 1.5:1). Target ($742.28) is only $0.48 above entry — essentially resistance is at current price. This is not a viable trade setup. Additionally, RSI(14)=78.19 signals overbought extremes. **REJECTED.**

### Decision
**NO SETUP**

Extreme overbought conditions (RS