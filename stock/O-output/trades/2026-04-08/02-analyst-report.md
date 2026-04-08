# Technical Analysis Report — 2026-04-08

## Ticker: AI

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $8.73 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.55x |
| ATR(14) | $0.48 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $9.42 | +7.9% |
| Support 1 | $7.68 | -12.0% |
| 200 SMA | $16.07 | +84.1% |
| 50 EMA | $9.73 | +11.5% |
| 10 EMA | $8.52 | -2.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=75.7, Price vs 200 SMA=BELOW | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=47.0, Price vs 50 SMA=BELOW, Volume=0.55x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=16.8 (min=7.9), Breakout=NO, Volume=0.55x, RSI(14)=47.0 | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BEARISH, Pullback zone=YES, Price above 10 EMA=YES, RSI(14)=47.0 | NO SETUP |
| VIX Fear | N/A | N/A | N/A |

### Analysis
AI fails all criteria across all strategies. Price is deeply below 200 SMA ($16.07 vs $8.73), disqualifying mean reversion. MACD shows no bullish crossover. Bollinger Bandwidth is elevated, not in squeeze. MA structure is bearish (10 EMA below 50 EMA). Critical constraint: relative volume at 0.55x is weak across all setups. This stock is in a downtrend with insufficient momentum confirmation.

### Decision
**NO SETUP**

---

## Ticker: GS

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $864.15 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.7x |
| ATR(14) | $26.97 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $873.21 | +1.0% |
| Support 1 | $780.50 | -9.7% |
| 200 SMA | $804.41 | -7.0% |
| 50 EMA | $871.91 | +0.9% |
| 10 EMA | $845.60 | -2.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=73.6, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=56.0, Price vs 50 SMA=BELOW, Volume=0.7x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=12.3 (min=4.7), Breakout=NO, Volume=0.7x, RSI(14)=56.0 | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BEARISH, Pullback zone=YES, Price above 10 EMA=YES, RSI(14)=56.0 | NO SETUP |
| VIX Fear | N/A | N/A | N/A |

### Analysis
GS is rejected across all strategies. RSI(2)=73.6 indicates overbought conditions, not mean reversion oversold. MACD shows no crossover signal; histogram is positive but signal line remains negative, indicating early-stage recovery, not confirmed momentum. Price sits below 50 EMA while above 200 SMA, creating a mixed structure. MA crossover is bearish (10 below 50). Relative volume at 0.7x is below preferred 1.0x threshold. No edge detected.

### Decision
**NO SETUP**

---

## Ticker: JNJ

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $238.41 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.84x |
| ATR(14) | $4.07 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $247.21 | +3.7% |
| Support 1 | $232.24 | -2.6% |
| 200 SMA | $197.55 | -17.1% |
| 50 EMA | $239.22 | +0.3% |
| 10 EMA | $240.85 | +1.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | PASS* | RSI(2)=5.39 (< 10 OVERSOLD), Price vs 200 SMA=ABOVE | SETUP DETECTED |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=46.5, Price vs 50 SMA=BELOW, Volume=0.84x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=4.9 (min=3.9), Breakout=NO, Volume=0.84x, RSI(14)=46.5 | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES, Price above 10 EMA=NO, RSI(14)=46.5 | NO SETUP |
| VIX Fear | N/A | N/A | N/A |

### Suggested Parameters (Pre-Computed)

**Strategy: Connors RSI(2) Mean Reversion**

| Parameter | Value |
|-----------|-------|
| Entry | $238.41 |
| Stop Loss | $230.27 (2x ATR(14) below entry) |
| Take Profit | $242.20 (close above 5-day SMA) |
| Risk/Share | $8.14 |
| Reward/Share | $3.79 |
| R:R Ratio | 0.47:1 |

### Analysis
JNJ triggers Connors RSI(2) with textbook precision: RSI(2)=5.39 is in extreme oversold territory (< 10), price is $238.41 well above 200 SMA ($197.55), confirming a long-term uptrend. The stock has pulled back sharply into a mean reversion setup. However, **this setup fails the minimum R:R requirement of 0.5:1**. The computed R:R is 0.47:1, with reward ($3.79) insufficient relative to risk ($8.14). The take profit target ($242.20 = close above 5-day SMA at $242.20) is only +1.6% above entry while the stop loss is -3.4% below entry, creating an unfavorable risk/reward structure. 

While the technical setup is mechanically valid, position sizing and risk management would require excessive risk to achieve acceptable return. This fails quantitative trade acceptance criteria.

### Decision
**NO SETUP** — *Connors RSI(2) triggered on technicals, but R:R ratio of 0.47:1 falls below strategy minimum of 0.5:1. Trade rejected on risk/reward basis.*

---

## Ticker: JPM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $297.40 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.74x |
| ATR(14) | $6.87 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $298.18 | +0.3% |
| Support 1 | $277.68 | -6.6% |
| 200 SMA | $299.60 | +0.7% |
| 50 EMA | $297.42 | +0.0% |
| 10 EMA | $291.95 | -1.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=91.7, Price vs 200 SMA=BELOW | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=56.4, Price vs 50 SMA=AT/BELOW, Volume=0.74x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=6.7 (min=4.0), Breakout=NO, Volume=0.74x, RSI(14)=56.4 | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BEARISH, Pullback zone=YES, Price above 10 EMA=YES, RSI(14)=56.4 | NO SETUP |
| VIX Fear | N/A | N/A | N/A |

### Analysis
JPM is overbought (RSI(2)=91.7) and near resistance. Price is below 200 SMA, failing trend filter for mean reversion. MACD shows no crossover. MA structure is bearish with 10 EMA below 50 EMA. Stock is compressed at 50 EMA ($297.42) with price at $297.40, but momentum is flat (RSI=56.4). Relative volume at 0.74x is weak. No actionable setup.

### Decision
**NO SETUP**

---

## Ticker: SPY

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $659.22 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.68x |
| ATR(14) | $10.03 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $681.50 | +3.4% |
| Support 1 | $629.28 | -4.5% |
| 200 SMA | $659.72 | +0.1% |
| 50 EMA | $673.84 | +2.2% |
| 10 EMA | $653.97 | -0.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=91.7, Price vs 200 SMA=BELOW | NO SETUP |
| MACD + RSI | FAIL | MACD cross=YES (histogram positive), RSI(14)=48.7, Price vs 50 SMA=BELOW, Volume=0.68x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=6.7 (min=2.4), Breakout=NO, Volume=0.68x, RSI(14)=48.7 | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BEARISH, Pullback zone=YES, Price above 10 EMA=YES, RSI(14)=48.7 | NO SETUP |
| VIX Fear | FAIL | VIX=20.33, 10d SMA=25.84, Spike=-21.3% (< 20%), S&P vs 200 SMA=BELOW | NO SETUP |

### Analysis
SPY is overbought (RSI(2)=91.7) with no mean reversion oversold. MACD histogram turned positive but price remains below 50 EMA ($673.84 vs $659.22), indicating crossover is in early/false stage—insufficient confirmation. MA structure is bearish (10 EMA at $653.97 below 50 EMA). Critical rejection for VIX Fear: while VIX=20.33 is near its 10-day SMA of 25.84, the spike is -21.3%, *below* the 20% threshold required. Additionally, S&P is below its 200 SMA, violating the systemic risk filter. Relative volume is weak at 0.68x. No edge.

### Decision
**NO SETUP**

---

## Ticker: QQQ

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $588.59 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.7x |
| ATR(14) | $11.04 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $612.52 | +4.1% |
| Support 1 | $555.60 | -5.6% |
| 200 SMA | $594.14 | +0.9% |
| 50 EMA | $601.29 | +2.2% |
| 10 EMA | $583.30 | -0.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=90.5, Price vs 200 SMA=BELOW | NO SETUP |
| MACD + RSI | FAIL | MACD cross=YES (histogram positive), RSI(14)=49.0, Price vs 50 SMA=BELOW, Volume=0.7x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=8.5 (min=2.9), Breakout=NO, Volume=0.7x, RSI(14)=49.0 | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BEARISH, Pullback zone=YES, Price above 10 EMA=YES, RSI(14)=49.0 | NO SETUP |
| VIX Fear | FAIL | VIX=20.33, 10d SMA=25.84, Spike=-21.3% (< 20%), S&P vs 200 SMA=BELOW | NO SETUP |

### Analysis
QQQ mirrors SPY rejection pattern. RSI(2)=90.5 is overbought, eliminating mean reversion. MACD histogram positive but price below 50 EMA ($601.29 vs $588.59), signaling early/false crossover without confirmation. MA structure is bearish (10 EMA below 50 EMA). VIX Fear fails: spike is -21.3%, below the 20% threshold, and S&P is below 200 SMA (systemic risk violation). Relative volume weak at 0.7x. No trade.

### Decision
**NO SETUP**

---

## Summary

| Ticker | Status | Notes |
|--------|--------|-------|
| AI | NO SETUP | Downtrend, price below 200 SMA, weak volume (0.55x) |
| GS | NO SETUP | Overbought RSI(2), no MACD cross, bearish MA structure, weak volume (0.7x) |
| JNJ | NO SETUP | Connors RSI(2) setup triggered but R:R 0.47: