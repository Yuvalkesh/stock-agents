# Technical Analysis Report — 2026-07-16

## Ticker: AMD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $529.14 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.95x |
| ATR(14) | $37.08 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $584.73 | +10.5% |
| Support 1 | $495.35 | -6.4% |
| 200 SMA | $293.31 | -44.6% |
| 50 EMA | $493.09 | -6.8% |
| 10 EMA | $537.10 | +1.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=29.0, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=51.7, Vol=0.95x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=13.47, 6M Low=9.53, Squeeze=NO | NO SETUP |
| MA Crossover | FAIL | 10 EMA > 50 EMA=YES, Price < 10 EMA, RSI=51.7 | NO SETUP |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### Decision
**NO SETUP**

AMD shows no valid entry signal across all five strategies. Connors RSI(2) fails the oversold threshold (29.0 vs required <10). MACD shows no crossover signal. Bollinger Bandwidth is elevated, not at squeeze levels. MA Crossover is bullish directionally but price is below the 10 EMA (outside pullback zone). Volume is weak at 0.95x. Hold monitoring.

---

## Ticker: ABNB

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $148.38 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.99x |
| ATR(14) | $4.53 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $150.75 | +1.6% |
| Support 1 | $137.91 | -7.0% |
| 200 SMA | $131.00 | -11.7% |
| 50 EMA | $138.79 | -6.5% |
| 10 EMA | $146.52 | -1.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=76.0, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=58.5, Vol=0.99x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=8.94, 6M Low=4.49, Squeeze=NO | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA > 50 EMA=YES, Pullback=YES, Above 10 EMA=YES, RSI=58.5 | SETUP CONDITIONAL |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### MA Crossover Setup Analysis
**Entry Condition Status:**
- 10 EMA (146.52) > 50 EMA (138.79): ✓ BULLISH
- Price (148.38) in pullback zone (within 1% of 10 EMA): ✓ YES
- Price above 10 EMA: ✓ YES
- RSI(14) = 58.5 (> 45): ✓ YES
- Volume = 0.99x: ✗ WEAK (requires 1.0x minimum for confirmation)

**Pre-Computed Trade Parameters:**
| Parameter | Value |
|-----------|-------|
| Entry | $148.38 |
| Stop Loss | $141.59 (1.5x ATR below entry) |
| Take Profit | $150.75 (resistance) |
| Risk/Share | $6.79 |
| Reward/Share | $2.37 |
| R:R Ratio | 0.35:1 |
| Minimum R:R for MA Crossover | 1.5:1 |

### Decision
**NO SETUP — R:R RATIO FAILS MINIMUM THRESHOLD**

ABNB shows a technical MA Crossover crossover pattern with 10 EMA > 50 EMA, price in pullback zone, and RSI in valid range. However, the pre-computed risk/reward ratio of 0.35:1 severely falls short of the required 1.5:1 minimum for this strategy. The target ($150.75) is only 1.6% away while stop-loss is 4.6% away. Unfavorable asymmetry. **REJECT.**

---

## Ticker: V

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $355.14 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.9x |
| ATR(14) | $8.22 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $365.02 | +2.8% |
| Support 1 | $324.38 | -8.7% |
| 200 SMA | $328.43 | -7.5% |
| 50 EMA | $331.53 | -6.7% |
| 10 EMA | $351.10 | -1.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=54.4, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=63.6, Vol=0.9x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=13.39, 6M Low=3.23, Squeeze=NO | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA > 50 EMA=YES, Pullback=YES, Above 10 EMA=YES, RSI=63.6 | SETUP CONDITIONAL |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### MA Crossover Setup Analysis
**Entry Condition Status:**
- 10 EMA (351.10) > 50 EMA (334.27): ✓ BULLISH
- Price (355.14) in pullback zone (within 1% of 10 EMA): ✓ YES
- Price above 10 EMA: ✓ YES
- RSI(14) = 63.6 (> 45): ✓ YES
- Volume = 0.9x: ✗ WEAK (requires 1.0x minimum for confirmation)

**Pre-Computed Trade Parameters:**
| Parameter | Value |
|-----------|-------|
| Entry | $355.14 |
| Stop Loss | $342.81 (1.5x ATR below entry) |
| Take Profit | $365.02 (resistance) |
| Risk/Share | $12.33 |
| Reward/Share | $9.88 |
| R:R Ratio | 0.8:1 |
| Minimum R:R for MA Crossover | 1.5:1 |

### Decision
**NO SETUP — R:R RATIO FAILS MINIMUM THRESHOLD**

V displays a valid MA Crossover pattern: 10 EMA > 50 EMA with price in the pullback zone and RSI in the 45-75 sweet spot. However, the risk/reward ratio of 0.8:1 falls well short of the required 1.5:1 minimum. Stop-loss is $12.33 away while target is only $9.88 away—insufficient margin of safety. Volume is also soft at 0.9x. **REJECT.**

---

## Ticker: ROKU

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $143.32 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.5x |
| ATR(14) | $3.22 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $143.56 | +0.2% |
| Support 1 | $134.36 | -6.2% |
| 200 SMA | $108.57 | -24.2% |
| 50 EMA | $131.53 | -8.2% |
| 10 EMA | $140.84 | -1.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=85.1, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=64.3, Vol=0.5x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=7.98, 6M Low=5.88, Squeeze=NO | NO SETUP |
| MA Crossover | CONDITIONAL | 10 EMA > 50 EMA=YES, Pullback=YES, Above 10 EMA=YES, RSI=64.3 | SETUP CONDITIONAL |
| VIX Fear | N/A | Not applicable (single stock) | N/A |

### MA Crossover Setup Analysis
**Entry Condition Status:**
- 10 EMA (140.84) > 50 EMA (130.77): ✓ BULLISH
- Price (143.32) in pullback zone (within 1% of 10 EMA): ✓ YES
- Price above 10 EMA: ✓ YES
- RSI(14) = 64.3 (> 45): ✓ YES
- Volume = 0.5x: ✗ CRITICALLY WEAK (requires 1.0x minimum for confirmation)

**Pre-Computed Trade Parameters:**
| Parameter | Value |
|-----------|-------|
| Entry | $143.32 |
| Stop Loss | $138.49 (1.5x ATR below entry) |
| Take Profit | $143.56 (resistance) |
| Risk/Share | $4.83 |
| Reward/Share | $0.24 |
| R:R Ratio | 0.05:1 |
| Minimum R:R for MA Crossover | 1.5:1 |

### Decision
**NO SETUP — R:R RATIO AND VOLUME CRITICALLY FAIL**

ROKU triggers MA Crossover directionally (10 EMA > 50 EMA, price in zone, RSI valid) but is disqualified on two critical fronts: (1) R:R ratio of 0.05:1 is essentially a coin flip—reward is only $0.24 vs risk of $4.83, and (2) relative volume of 0.5x is half the