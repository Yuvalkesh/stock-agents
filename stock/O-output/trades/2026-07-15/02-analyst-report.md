# Technical Analysis Report — 2026-07-15

## Ticker: AMD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | DATA UNAVAILABLE |
| Day Change | DATA UNAVAILABLE |
| 20-Day Avg Volume | DATA UNAVAILABLE |
| Today's Volume | DATA UNAVAILABLE |
| Relative Volume | 0.72x |
| ATR(14) | DATA UNAVAILABLE |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $584.73 | DATA UNAVAILABLE |
| Support 1 | $495.35 | DATA UNAVAILABLE |
| 200 SMA | DATA UNAVAILABLE | DATA UNAVAILABLE |
| 50 EMA | $474.56 | DATA UNAVAILABLE |
| 10 EMA | $536.82 | DATA UNAVAILABLE |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=35.2 (threshold: <10), Price vs 200 SMA=BELOW | NO SETUP |
| MACD + RSI | INSUFFICIENT DATA | Unable to calculate MACD/histogram | NO SETUP |
| Bollinger Squeeze | INSUFFICIENT DATA | Unable to calculate bands | NO SETUP |
| MA Crossover | FAILED | 10 EMA=536.82 vs 50 EMA=474.56 (BULLISH), No recent crossover, Price data missing | NO SETUP |
| VIX Fear | N/A | Not applicable to single ticker | NO SETUP |

### Decision
**NO SETUP** — AMD lacks sufficient price data (current price and 200 SMA unavailable). Additionally, all strategies fail entry criteria: Connors RSI(2) at 35.2 exceeds threshold of <10, and MA Crossover shows no recent crossover signal despite bullish EMA alignment. Data quality insufficient for trade execution.

---

## Ticker: ABNB

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $146.54 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.81x |
| ATR(14) | $4.56 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $150.19 | +2.49% |
| Support 1 | $134.30 | -8.35% |
| 200 SMA | $130.87 | -10.68% |
| 50 EMA | $138.65 | -5.40% |
| 10 EMA | $146.11 | -0.29% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=43.9 (threshold: <10), Price above 200 SMA ✓ | NO SETUP |
| MACD + RSI | FAILED | MACD histogram=-0.0414 (bearish), RSI(14)=56.1 (in range ✓), Volume=0.81x (weak) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=9.3347 vs 6-month low=4.4917 (no squeeze), Breakout=NO, Volume=0.81x (weak) | NO SETUP |
| MA Crossover | SIGNAL PRESENT | 10 EMA=146.11 vs 50 EMA=140.0 (BULLISH ✓), Price at 10 EMA (pullback zone ✓), RSI(14)=56.1 ✓ | SETUP CONFIRMED |
| VIX Fear | N/A | Not applicable to single ticker | NO SETUP |

### Suggested Parameters (MA Crossover)
| Parameter | Value |
|-----------|-------|
| Entry | $146.54 |
| Stop Loss | $139.70 (1.5x ATR below entry) |
| Take Profit | $150.19 (resistance / exit on EMA bearish cross) |
| Risk/Share | $6.84 |
| Reward/Share | $3.65 |
| R:R Ratio | 0.53:1 |

### Analysis Notes
MA Crossover setup confirmed by technical criteria (bullish EMA alignment, price at pullback zone, RSI in healthy range). However, **R:R ratio of 0.53:1 FAILS minimum threshold of 1.5:1 required by strategy DNA.** Risk exceeds reward significantly — position offers poor risk-adjusted returns. **Trade parameters do not meet risk management standards.**

### Decision
**NO SETUP** — While MA Crossover technical setup is present (bullish EMA(10) vs EMA(50), pullback zone confirmed, RSI=56.1), the pre-computed trade parameters yield an unacceptable R:R ratio of 0.53:1 versus the required minimum of 1.5:1. **Entry risk ($6.84/share) far exceeds potential reward ($3.65/share). Trade is structurally unsound and fails risk-reward validation.**

---

## Ticker: ROKU

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $141.76 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.25x |
| ATR(14) | $3.32 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $145.88 | +2.91% |
| Support 1 | $134.36 | -5.18% |
| 200 SMA | $108.34 | -23.59% |
| 50 EMA | $130.26 | -8.12% |
| 10 EMA | $140.29 | -1.03% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=59.6 (threshold: <10), Price above 200 SMA ✓ | NO SETUP |
| MACD + RSI | FAILED | MACD histogram=-0.1635 (bearish), RSI(14)=61.9 (in range ✓), Volume=0.25x (very weak) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=7.5692 vs 6-month low=5.8768 (no squeeze), Breakout=NO, Volume=0.25x (critically weak) | NO SETUP |
| MA Crossover | SIGNAL PRESENT | 10 EMA=140.29 vs 50 EMA=130.26 (BULLISH ✓), Price at 10 EMA (pullback zone ✓), RSI(14)=61.9 ✓ | SETUP CONFIRMED |
| VIX Fear | N/A | Not applicable to single ticker | NO SETUP |

### Suggested Parameters (MA Crossover)
| Parameter | Value |
|-----------|-------|
| Entry | $141.76 |
| Stop Loss | $136.78 (1.5x ATR below entry) |
| Take Profit | $145.88 (resistance / exit on EMA bearish cross) |
| Risk/Share | $4.98 |
| Reward/Share | $4.12 |
| R:R Ratio | 0.83:1 |

### Analysis Notes
MA Crossover setup confirmed by technical criteria (bullish EMA alignment, price at pullback zone, RSI in healthy range). **However, R:R ratio of 0.83:1 FAILS minimum threshold of 1.5:1 required by strategy DNA.** Additionally, relative volume of 0.25x is critically weak—well below the 1.0x minimum for MA Crossover validation. Volume should be >1.0x on bounce confirmation; this setup lacks conviction.

### Decision
**NO SETUP** — While MA Crossover technical setup is present (bullish EMA(10) vs EMA(50), pullback zone confirmed, RSI=61.9), this trade fails on two critical fronts: (1) Pre-computed R:R ratio of 0.83:1 is grossly inadequate versus required minimum of 1.5:1, and (2) Relative volume of 0.25x is dangerously weak—less than one-quarter of average, indicating no buyer conviction. **This setup lacks both risk-reward alignment and volume confirmation. Trade is rejected.**

---

## Summary

| Ticker | Strategy | Decision |
|--------|----------|----------|
| AMD | All | NO SETUP — Insufficient data quality |
| ABNB | MA Crossover | NO SETUP — R:R ratio 0.53:1 fails 1.5:1 minimum |
| ROKU | MA Crossover | NO SETUP — R:R ratio 0.83:1 fails 1.5:1 minimum + volume 0.25x critically weak |

**No trades confirmed for 2026-07-15.** All three tickers fail entry criteria either due to data insufficiency (AMD), risk-reward misalignment (ABNB, ROKU), or inadequate volume confirmation (ROKU). The chart does not support execution today.