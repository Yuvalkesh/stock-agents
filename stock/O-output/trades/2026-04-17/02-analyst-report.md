# Technical Analysis Report — 2026-04-17

## Ticker: AI

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $9.32 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.45x |
| ATR(14) | $0.56 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $9.94 | +6.65% |
| Support 1 | $7.68 | -17.60% |
| 200 SMA | $15.54 | +66.74% |
| 50 EMA | $9.29 | -0.32% |
| 10 EMA | $8.79 | -5.68% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECT | RSI(2)=70.7, Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | REJECT | MACD cross=NO, RSI(14)=56.2, MACD=-0.09 | NO SETUP |
| Bollinger Squeeze | REJECT | BW=18.88 (not 6m low), Breakout=NO | NO SETUP |
| MA Crossover | REJECT | EMA10(8.79) BELOW EMA50(9.58), Bearish | NO SETUP |
| VIX Fear | N/A | Single stock, strategy applies to SPY/QQQ only | N/A |

### Decision
**NO SETUP**

Data Summary: AI is below its 200 SMA, eliminating mean-reversion trades. The 10 EMA is bearish to the 50 EMA. RSI(2) is elevated at 70.7, indicating recent strength without oversold conditions. No technical setup confirmed.

---

## Ticker: AMD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $278.26 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.82x |
| ATR(14) | $10.44 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $279.34 | +0.39% |
| Support 1 | $192.83 | -30.75% |
| 200 SMA | $201.74 | -27.53% |
| 50 EMA | $210.57 | -24.32% |
| 10 EMA | $244.87 | -12.01% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECT | RSI(2)=100.0, Extreme overbought | NO SETUP |
| MACD + RSI | REJECT | RSI(14)=80.2 (outside 35-75 range), Overbought | NO SETUP |
| Bollinger Squeeze | REJECT | No squeeze (BW=40.64, 6m low=9.53), Breakout=YES but RSI overbought | NO SETUP |
| MA Crossover | REJECT | Crossover=YES but price NOT in pullback zone, RSI overbought at 80.2 | NO SETUP |
| VIX Fear | N/A | Single stock, strategy applies to SPY/QQQ only | N/A |

### Decision
**NO SETUP**

Data Summary: AMD is deeply overbought (RSI(2)=100, RSI(14)=80.2). Although price is above both moving averages and momentum is positive, the extreme overbought conditions violate MACD+RSI entry parameters (RSI must be 35-75). MA Crossover requires pullback to 10 EMA — price at $278.26 is well above the 10 EMA at $244.87. No valid entry.

---

## Ticker: AMAT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $389.90 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.79x |
| ATR(14) | $15.42 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $407.29 | +4.45% |
| Support 1 | $320.69 | -17.77% |
| 200 SMA | $257.69 | -33.84% |
| 50 EMA | $356.28 | -8.63% |
| 10 EMA | $383.00 | -1.79% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECT | RSI(2)=15.6 (not <10), Price ABOVE 200 SMA but no extreme dip | NO SETUP |
| MACD + RSI | REJECT | MACD cross=NO, Histogram positive but signal line above, Volume=WEAK (0.79x) | NO SETUP |
| Bollinger Squeeze | REJECT | No squeeze (BW=25.23, 6m low=7.41), Breakout=NO, Volume WEAK | NO SETUP |
| MA Crossover | CONDITIONAL | EMA10(383.00) vs EMA50(352.63) BULLISH, Price within 1.79% of EMA10, RSI(14)=61.0 VALID, but Volume=0.79x (WEAK) | SETUP CONDITIONAL |
| VIX Fear | N/A | Single stock, strategy applies to SPY/QQQ only | N/A |

### Detailed MA Crossover Assessment
The system reports **Setup=YES** for MA Crossover, but **Pre-Computed Trade Parameters indicate R:R Ratio of 0.75:1, which FAILS the minimum 1.5:1 requirement** for this strategy. 

Entry price ($389.90) is within 1.0% of 10 EMA ($383.00). RSI(14)=61.0 is valid. However:
- Risk/Share: $23.13 (1.5x ATR = 1.5 × $15.42)
- Reward/Share: $17.39 (to resistance at $407.29)
- R:R Ratio: 0.75:1 — **UNACCEPTABLE**

Additionally, relative volume at 0.79x is below the 1.0x confirmation threshold.

### Decision
**NO SETUP**

Data Summary: Although MA Crossover conditions are technically present (bullish EMA cross, price in pullback zone, valid RSI), the risk-reward ratio of 0.75:1 is insufficient for the strategy's 1.5:1 minimum threshold. Volume confirmation is also weak. Trade rejected.

---

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $260.96 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.78x |
| ATR(14) | $11.85 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $273.50 | +4.80% |
| Support 1 | $198.60 | -23.88% |
| 200 SMA | $165.12 | -36.74% |
| 50 EMA | $230.42 | -11.71% |
| 10 EMA | $252.84 | -3.08% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECT | RSI(2)=26.5 (not <10), No extreme oversold dip | NO SETUP |
| MACD + RSI | REJECT | MACD cross=NO, Histogram positive but Signal line above, Volume WEAK (0.78x) | NO SETUP |
| Bollinger Squeeze | REJECT | No squeeze (BW=36.18, 6m low=15.05), Breakout=NO, Volume WEAK | NO SETUP |
| MA Crossover | REJECT | Crossover=NO, EMA10 vs EMA50 BULLISH but price NOT in pullback zone (3.08% above EMA10), Volume WEAK | NO SETUP |
| VIX Fear | N/A | Single stock, strategy applies to SPY/QQQ only | N/A |

### Decision
**NO SETUP**

Data Summary: LRCX shows bullish trend structure (price above both moving averages, 50 EMA above 200 SMA) but lacks a specific MA Crossover pullback trigger. Price at $260.96 is already 3.08% above the 10 EMA, outside the 1.0% pullback zone. Volume is weak at 0.78x average. No setup.

---

## Ticker: KLAC

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $1734.85 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.89x |
| ATR(14) | $67.48 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $1798.00 | +3.64% |
| Support 1 | $1374.43 | -20.75% |
| 200 SMA | $1209.34 | -30.23% |
| 50 EMA | $1506.65 | -13.16% |
| 10 EMA | $1687.29 | -2.74% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECT | RSI(2)=29.1 (not <10), No extreme oversold | NO SETUP |
| MACD + RSI | REJECT | MACD cross=NO, MACD=77.37, Signal=54.41 (positive histogram but no cross), Volume WEAK (0.89x) | NO SETUP |
| Bollinger Squeeze | REJECT | No squeeze (BW=31.05, 6m low=8.90), Breakout=NO, Volume WEAK | NO SETUP |
| MA Crossover | REJECT | Crossover=NO, EMA10 vs EMA50 BULLISH, Price 2.74% above EMA10 (outside pullback zone), Volume WEAK | NO SETUP |
| VIX Fear | N/A | Single stock, strategy applies to SPY/QQQ only | N/A |

### Decision
**NO SETUP**

Data Summary: KLAC exhibits strong uptrend structure (price well above all moving averages, 10 EMA above 50 EMA) but shows no pullback or mean-reversion signal. Price is extended above the 10 EMA, eliminating the MA Crossover pullback entry. Volume is weak at 0.89x. No trade setup.

---

## Ticker: TSLA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $388.90 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.92x |
| ATR(14) | $15.36 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $396.23 | +1.88% |
| Support 1 | $337.24 | -13.27% |
| 200 SMA | $398.37 | +2.43% |
| 50 EMA | $390.44 | +0.40% |
| 10 EMA | $368.32 | -5.31% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECT | RSI(2)=84.5 (>= 10), Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | REJECT | MACD cross=YES (bullish) but Price BELOW 50 SMA ($390.44), violates trend filter | NO SETUP |
| Bollinger Squeeze | REJECT | No squeeze (BW=16.77, 6m low=7.04), Breakout=NO, Volume WEAK | NO SETUP |
| MA Crossover | REJECT | Crossover=NO, EMA10 BELOW EMA50 (bearish cross), Price above EMA10 but trend deteriorating | NO SETUP |
| VIX Fear | N/A | Single stock, strategy applies to SPY/QQQ only | N/A |

### Decision
**NO SETUP**

Data Summary: TSLA is caught between support and resistance, with price just below the 200 SMA and 50 EMA. The 10 EMA is bearish to the 50 EMA. Although MACD shows a bullish crossover, price is below the 50 SMA, violating the trend filter for MACD+RSI. RSI(2) at 84.5 rules out mean-reversion. No setup.

---

## Ticker: TXN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $223.10 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.10x |
| ATR(14) | $6.02 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $224.02 | +0.41% |
| Support 1 | $184.90 | -17.08% |
| 200 SMA | $188.88 | -15.34% |
| 50 EMA | $206.49 | -7.43% |
| 10 EMA | $212.13 | -4.89% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECT | RSI(2)=85.9 (>= 10), Extreme overbought | NO SETUP |
| MACD + RSI | REJECT | MACD cross=NO, RSI(14)=70.3 (in range), but no crossover signal, MACD hist=3.17 (small positive) | NO SETUP |
| Bollinger Squeeze | REJECT | No squeeze (BW=23.49, 6m low=5.41), Breakout=NO, Volume WEAK | NO SETUP |
| MA Crossover | REJECT | Crossover=YES but price NOT in pullback zone (4.89% above EMA10), RSI elevated at 70.3 | NO SETUP |
| VIX Fear | N/A | Single stock, strategy applies to SPY/QQQ only | N/A |

### Decision
**NO SETUP**

Data Summary: TXN shows a recent crossover (10 EMA above 50 EMA) with price above both moving averages, but the entry condition requires a pullback to the 10 EMA. Price at $223.10 is 4.89% above the 10 EMA at $212.13, well outside the 1.0% pullback zone. RSI(2) at 85.9 indicates extended momentum. Volume confirmation at 1.10x is marginal. No setup.

---

## Ticker: SPY

### Price Data
| Metric |