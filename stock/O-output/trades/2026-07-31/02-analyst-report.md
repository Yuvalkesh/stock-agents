# Technical Analysis Report — 2026-07-31

## Ticker: AAPL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $333.43 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.45x |
| ATR(14) | $8.06 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $344.57 | +3.3% |
| Support 1 | $293.68 | -12.0% |
| 200 SMA | $277.35 | -16.8% |
| 50 EMA | $309.30 | -7.2% |
| 10 EMA | $331.31 | -0.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=25.4 | Price above 200 SMA, RSI not < 10 | NO SETUP |
| MACD + RSI | MACD=9.24, Signal=8.60 | No crossover, RSI in range, price above 50 SMA | NO SETUP |
| Bollinger Squeeze | BW=12.13, Min=5.83 | No squeeze (BW > 6m low), no breakout | NO SETUP |
| MA Crossover | EMA10=331.31, EMA50=309.91 | Bullish MA alignment, pullback zone, RSI=61.7 | **SETUP CONFIRMED** |
| VIX Fear | N/A | Not applicable | — |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $333.43 |
| Stop Loss | $321.34 (1.5x ATR(14) below entry) |
| Target | $344.57 |
| R:R Ratio | 0.92:1 |

### Decision
**NO SETUP — R:R Ratio 0.92:1 fails minimum 1.5:1 threshold for MA Crossover strategy**

The MA Crossover setup is technically confirmed (bullish EMA alignment, pullback zone achieved, RSI in acceptable range), but the reward-to-risk ratio is insufficient at 0.92:1. Strategy requires minimum 1.5:1. **TRADE REJECTED ON RISK MANAGEMENT GROUNDS.**

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $451.10 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 3.12x |
| ATR(14) | $15.90 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $458.69 | +1.7% |
| Support 1 | $373.35 | -17.3% |
| 200 SMA | $432.49 | -4.1% |
| 50 EMA | $398.42 | -11.7% |
| 10 EMA | $401.10 | -11.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=97.1 | Overbought, RSI >> 10, price above 200 SMA | NO SETUP |
| MACD + RSI | MACD=4.43, Signal=-0.00 | No crossover signal, RSI=71.8 in range, price above 50 SMA | NO SETUP |
| Bollinger Squeeze | BW=14.75, Min=5.20 | No squeeze, breakout=YES, volume 3.12x, RSI=71.8 | NO SETUP |
| MA Crossover | EMA10=401.10, EMA50=396.44 | Bullish crossover=YES, but price NOT in pullback zone (price >> EMA10) | NO SETUP |
| VIX Fear | N/A | Not applicable | — |

### Decision
**NO SETUP**

MSFT is extended beyond entry zones for all strategies. MA Crossover crossover occurred recently (YES), but price has already moved significantly above the 10 EMA ($401.10 vs $451.10 = +12.5%), violating the pullback zone requirement. All other strategies lack confirmatory signals. **NO TRADE.**

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $333.66 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.04x |
| ATR(14) | $11.29 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $375.27 | +12.4% |
| Support 1 | $314.90 | -5.6% |
| 200 SMA | $325.41 | -2.5% |
| 50 EMA | $359.31 | +7.7% |
| 10 EMA | $336.80 | +1.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=52.0 | Neutral, price above 200 SMA | NO SETUP |
| MACD + RSI | MACD=-8.15, Signal=-6.73 | Bearish histogram (-1.42), price below 50 EMA | NO SETUP |
| Bollinger Squeeze | BW=17.66, Min=5.06 | No squeeze, no breakout, volume WEAK (1.04x) | NO SETUP |
| MA Crossover | EMA10=336.80, EMA50=351.28 | Bearish crossover (EMA10 < EMA50), price below EMA10 | NO SETUP |
| VIX Fear | N/A | Not applicable | — |

### Decision
**NO SETUP**

GOOGL shows weakness: price is below both 50 EMA ($359.31) and in pullback below 10 EMA. MACD is negative with bearish histogram. No strategy triggers. **NO TRADE.**

---

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $195.04 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.0x |
| ATR(14) | $7.51 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $214.39 | +9.9% |
| Support 1 | $190.01 | -2.6% |
| 200 SMA | $192.86 | -1.1% |
| 50 EMA | $206.52 | +5.9% |
| 10 EMA | $200.01 | +2.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=51.1 | Neutral, price above 200 SMA | NO SETUP |
| MACD + RSI | MACD=-2.11, Signal=-0.74 | Bearish histogram (-1.37), price below 50 EMA | NO SETUP |
| Bollinger Squeeze | BW=12.99, Min=6.53 | No squeeze, no breakout, volume WEAK (1.0x) | NO SETUP |
| MA Crossover | EMA10=200.01, EMA50=206.52 | Bearish crossover (EMA10 < EMA50), price below EMA10 | NO SETUP |
| VIX Fear | N/A | Not applicable | — |

### Decision
**NO SETUP**

NVDA is correcting: price below both 50 EMA and 10 EMA. MACD is negative. Volume at 1.0x relative confirms weak action. No strategy triggers. **NO TRADE.**

---

## Ticker: META

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $539.03 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 2.23x |
| ATR(14) | $25.63 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $686.08 | +27.2% |
| Support 1 | $524.49 | -2.7% |
| 200 SMA | $634.37 | +17.7% |
| 50 EMA | $602.90 | +11.9% |
| 10 EMA | $597.43 | +10.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=0.03 | **Extreme oversold (<10)**, but price below 200 SMA | NO SETUP |
| MACD + RSI | MACD=-6.44, Signal=4.44 | Bearish histogram, RSI=32.1 below 35 (out of range), price below 50 EMA | NO SETUP |
| Bollinger Squeeze | BW=22.83, Min=5.03 | No squeeze, no breakout, price far below bands | NO SETUP |
| MA Crossover | EMA10=597.43, EMA50=608.88 | Bearish crossover (EMA10 < EMA50), price far below both | NO SETUP |
| VIX Fear | N/A | Not applicable | — |

### Decision
**NO SETUP**

META is in a downtrend: price is below 200 SMA ($634.37), below 50 EMA, below 10 EMA. Although RSI(2) is extreme oversold (0.03), Connors RSI strategy requires price **above** 200 SMA for entry—this is a long-term trend filter and META fails it. MACD is bearish. **NO TRADE.**

---

## Ticker: V

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $366.27 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.07x |
| ATR(14) | $8.30 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $373.97 | +2.1% |
| Support 1 | $344.42 | -6.0% |
| 200 SMA | $329.34 | -10.1% |
| 50 EMA | $339.72 | -7.2% |
| 10 EMA | $361.16 | -1.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=55.2 | Neutral, price above 200 SMA | NO SETUP |
| MACD + RSI | MACD=7.20, Signal=7.01 | **Bullish crossover=YES**, RSI=