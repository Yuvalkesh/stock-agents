# Technical Analysis Report — 2026-07-02

## Ticker: AMAT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $650.91 |
| 20-Day Avg Volume | — |
| Relative Volume | 1.25x |
| ATR(14) | $44.42 |
| 200 SMA | $336.59 |
| 50 SMA | $485.79 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $739.67 | +13.6% |
| Support 1 | $452.91 | -30.4% |
| 200 SMA | $336.59 | -48.3% |
| 50 EMA | $485.79 | -25.4% |
| 10 EMA | $638.48 | -1.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=31.86 (threshold: <10), Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=60.37 (in range), Price > 50 SMA=YES, Volume=1.25x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=49.84 (6m low=8.80), Breakout=NO, RSI(14)=60.37 | NO SETUP |
| MA Crossover | TRIGGERED | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES, Price above 10 EMA=YES, RSI(14)=60.37 | SETUP IDENTIFIED — R:R RATIO FAILS THRESHOLD |
| VIX Fear | N/A | Not applicable to individual equity | N/A |

### Suggested Parameters (Pre-Computed)

_MA Crossover Setup:_
| Parameter | Value |
|-----------|-------|
| Entry | $650.91 |
| Stop Loss | $584.28 (1.5x ATR below entry) |
| Take Profit | $739.67 (resistance / EMA bearish cross) |
| Risk/Share | $66.63 |
| Reward/Share | $88.76 |
| R:R Ratio | 1.33:1 |
| **Minimum R:R Requirement** | **1.5:1** |
| **Status** | **FAIL** |

### Decision
**NO SETUP**

*Rationale:* MA Crossover strategy triggers on technical setup (10 EMA > 50 EMA, price above 10 EMA, RSI in acceptable range). However, the computed R:R ratio of 1.33:1 falls short of the strategy's minimum threshold of 1.5:1. Risk-reward geometry does not justify entry. Pass.

---

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $391.26 |
| 20-Day Avg Volume | — |
| Relative Volume | 1.32x |
| ATR(14) | $27.28 |
| 200 SMA | $221.33 |
| 50 SMA | $319.05 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $438.50 | +12.1% |
| Support 1 | $302.53 | -22.7% |
| 200 SMA | $221.33 | -43.5% |
| 50 EMA | $330.04 | -15.7% |
| 10 EMA | $391.97 | +0.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=31.78 (threshold: <10), Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=56.36 (in range), Price > 50 SMA=YES, Volume=1.32x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=36.14 (6m low=11.03), Breakout=NO, RSI(14)=56.36 | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES, Price above 10 EMA=NO (price $391.26 < 10 EMA $391.97), RSI(14)=56.36 | NO SETUP |
| VIX Fear | N/A | Not applicable to individual equity | N/A |

### Decision
**NO SETUP**

*Rationale:* MA Crossover fails on price positioning. Price ($391.26) is below the 10 EMA ($391.97), violating the "Above EMA10=YES" requirement. The setup requires price to bounce above the 10 EMA after pullback; this has not occurred. No valid entry signal.

---

## Ticker: KLAC

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $266.19 |
| 20-Day Avg Volume | — |
| Relative Volume | 1.53x |
| ATR(14) | $19.34 |
| 200 SMA | $151.02 |
| 50 SMA | $207.58 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $307.37 | +15.4% |
| Support 1 | $192.77 | -27.6% |
| 200 SMA | $151.02 | -43.2% |
| 50 EMA | $215.70 | -19.0% |
| 10 EMA | $261.66 | -1.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=35.35 (threshold: <10), Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=58.11 (in range), Price > 50 SMA=YES, Volume=1.53x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=43.51 (6m low=8.90), Breakout=NO, RSI(14)=58.11 | NO SETUP |
| MA Crossover | TRIGGERED | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES, Price above 10 EMA=YES, RSI(14)=58.11 | SETUP IDENTIFIED — R:R RATIO FAILS THRESHOLD |
| VIX Fear | N/A | Not applicable to individual equity | N/A |

### Suggested Parameters (Pre-Computed)

_MA Crossover Setup:_
| Parameter | Value |
|-----------|-------|
| Entry | $266.19 |
| Stop Loss | $237.18 (1.5x ATR below entry) |
| Take Profit | $307.37 (resistance / EMA bearish cross) |
| Risk/Share | $29.01 |
| Reward/Share | $41.18 |
| R:R Ratio | 1.42:1 |
| **Minimum R:R Requirement** | **1.5:1** |
| **Status** | **FAIL** |

### Decision
**NO SETUP**

*Rationale:* MA Crossover strategy triggers on technical conditions (10 EMA bullish vs 50 EMA, price in pullback zone, price above 10 EMA, RSI acceptable). Computed R:R ratio of 1.42:1 fails to meet the strategy minimum of 1.5:1. Risk/reward does not justify trade entry. Pass.

---

## Ticker: ABNB

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $147.31 |
| 20-Day Avg Volume | — |
| Relative Volume | 0.82x |
| ATR(14) | $4.75 |
| 200 SMA | $129.94 |
| 50 SMA | $137.76 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $150.19 | +1.9% |
| Support 1 | $127.23 | -13.6% |
| 200 SMA | $129.94 | -11.8% |
| 50 EMA | $137.34 | -6.9% |
| 10 EMA | $143.00 | -3.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=70.28 (threshold: <10), Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=62.10 (in range), Price > 50 SMA=YES, Volume=0.82x (WEAK, <1.0x) | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=16.11 (6m low=4.49), Breakout=NO, Volume=0.82x (WEAK), RSI(14)=62.10 | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BULLISH, Pullback zone=NO (price $147.31 > 10 EMA $143.00, not within 1% touch zone), Price above 10 EMA=YES, RSI(14)=62.10 | NO SETUP |
| VIX Fear | N/A | Not applicable to individual equity | N/A |

### Decision
**NO SETUP**

*Rationale:* MA Crossover fails on pullback zone requirement. Price ($147.31) is above 10 EMA ($143.00) by +3.0%, exceeding the 1.0% pullback zone tolerance. Additionally, relative volume of 0.82x is below the 1.0x threshold across all strategies. No valid entry signal.

---

## Ticker: MO

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $71.54 |
| 20-Day Avg Volume | — |
| Relative Volume | 0.74x |
| ATR(14) | $1.59 |
| 200 SMA | $62.90 |
| 50 SMA | $70.06 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $74.15 | +3.6% |
| Support 1 | $68.07 | -4.8% |
| 200 SMA | $62.90 | -12.0% |
| 50 EMA | $70.06 | -2.1% |
| 10 EMA | $71.89 | +0.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=15.11 (threshold: <10), Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)