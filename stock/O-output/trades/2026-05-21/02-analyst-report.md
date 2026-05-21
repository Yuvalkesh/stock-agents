# Technical Analysis Report — 2026-05-21

## Ticker: TXN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $301.02 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.07x |
| ATR(14) | $9.48 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $310.29 | +3.1% |
| Support 1 | $262.90 | -12.6% |
| 200 SMA | $198.01 | -34.2% |
| 50 EMA | $238.89 | -20.6% |
| 10 EMA | $298.23 | -0.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO | RSI(2)=30.7, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | NO | MACD histogram=−1.43, RSI(14)=70.0, Volume=0.07x | NO SETUP |
| Bollinger Squeeze | NO | Bandwidth=18.90 (6m low=5.41), RSI(14)=70.0, Volume=0.07x | NO SETUP |
| MA Crossover | YES (technical) | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES, Price above 10 EMA=YES | REJECTED |
| VIX Fear | — | Not applicable | N/A |

### Decision
**NO SETUP**

**Rationale:** TXN triggers MA Crossover on technical parameters (bullish EMA alignment, pullback zone confirmed), but the pre-computed R:R ratio is **0.65:1**, which fails the minimum 1.5:1 threshold for this strategy. Additionally, relative volume of 0.07x is critically weak — well below the 1.0x preference. The setup lacks sufficient reward-to-risk geometry and volume confirmation to justify execution.

---

## Ticker: AMD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $440.29 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.15x |
| ATR(14) | $24.01 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $469.22 | +6.6% |
| Support 1 | $310.00 | -29.6% |
| 200 SMA | $229.31 | -47.9% |
| 50 EMA | $297.61 | -32.4% |
| 10 EMA | $426.48 | -3.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO | RSI(2)=60.4, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | NO | MACD histogram=−2.88, RSI(14)=67.1, Volume=0.15x | NO SETUP |
| Bollinger Squeeze | NO | Bandwidth=47.45 (6m low=9.53), RSI(14)=67.1, Volume=0.15x | NO SETUP |
| MA Crossover | NO | 10 EMA vs 50 EMA=BULLISH, Pullback zone=NO, Price above 10 EMA=YES | NO SETUP |
| VIX Fear | — | Not applicable | N/A |

### Decision
**NO SETUP**

**Rationale:** AMD shows bullish EMA alignment (10 EMA $426.48 > 50 EMA $297.61), but price ($440.29) is trading **above** the 10 EMA pullback zone. The MA Crossover strategy requires a pullback to touch the 10 EMA for better entry geometry. No other strategy triggers. Relative volume remains weak at 0.15x.

---

## Ticker: QCOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $208.25 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.17x |
| ATR(14) | $13.57 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $247.90 | +19.0% |
| Support 1 | $143.58 | -31.1% |
| 200 SMA | $158.88 | -23.7% |
| 50 EMA | $154.32 | -25.9% |
| 10 EMA | $201.51 | -3.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO | RSI(2)=78.7, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | NO | MACD histogram=−1.14, RSI(14)=63.2, Volume=0.17x | NO SETUP |
| Bollinger Squeeze | NO | Bandwidth=51.40 (6m low=5.85), RSI(14)=63.2, Volume=0.17x | NO SETUP |
| MA Crossover | NO | 10 EMA vs 50 EMA=BULLISH, Pullback zone=NO, Price above 10 EMA=YES | NO SETUP |
| VIX Fear | — | Not applicable | N/A |

### Decision
**NO SETUP**

**Rationale:** QCOM exhibits bullish EMA structure but fails MA Crossover entry: price is trading above the 10 EMA ($201.51) without a pullback to establish entry in the pullback zone. RSI(2) at 78.7 shows short-term exhaustion. Relative volume weak at 0.17x. No alternative strategy triggers.

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $418.46 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.23x |
| ATR(14) | $11.11 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $432.70 | +3.4% |
| Support 1 | $398.01 | -4.9% |
| 200 SMA | $459.77 | +9.9% |
| 50 EMA | $400.09 | -4.4% |
| 10 EMA | $417.07 | -0.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO | RSI(2)=41.0, Price vs 200 SMA=BELOW | NO SETUP |
| MACD + RSI | NO | MACD histogram=−0.36, RSI(14)=54.4, Volume=0.23x | NO SETUP |
| Bollinger Squeeze | NO | Bandwidth=6.34 (6m low=4.08), RSI(14)=54.4, Volume=0.23x | NO SETUP |
| MA Crossover | YES (technical) | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES, Price above 10 EMA=YES | REJECTED |
| VIX Fear | — | Not applicable | N/A |

### Decision
**NO SETUP**

**Rationale:** MSFT qualifies on MA Crossover technical conditions (price in pullback zone near 10 EMA, above 50 EMA), but pre-computed R:R is **0.85:1**, failing the 1.5:1 minimum. Critical concern: price is **below** 200 SMA ($459.77), indicating we are outside a long-term uptrend. Additionally, Connors RSI(2) requires price above 200 SMA; MSFT does not qualify. Setup rejected on risk geometry and trend filter.

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $383.92 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.13x |
| ATR(14) | $9.85 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $408.61 | +6.4% |
| Support 1 | $335.39 | -12.6% |
| 200 SMA | $295.00 | -23.2% |
| 50 EMA | $339.48 | -11.6% |
| 10 EMA | $389.45 | +1.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO | RSI(2)=10.4, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | NO | MACD histogram=−3.08, RSI(14)=58.5, Volume=0.13x | NO SETUP |
| Bollinger Squeeze | NO | Bandwidth=19.19 (6m low=5.06), RSI(14)=58.5, Volume=0.13x | NO SETUP |
| MA Crossover | NO | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES, Price above 10 EMA=NO | NO SETUP |
| VIX Fear | — | Not applicable | N/A |

### Decision
**NO SETUP**

**Rationale:** GOOGL fails MA Crossover despite pullback zone confirmation. Price ($383.92) is **below** the 10 EMA ($389.45), which violates the entry requirement ("closes above 10 EMA after the pullback"). Connors RSI(2) at 10.4 is borderline (just at threshold) but price is within pullback territory, not establishing a clear mean reversion bottom. No setup confirmed.

---

## Ticker: XLE

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $59.99 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.23x |
| ATR(14) | $1.35 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $61.70 | +2.8% |
| Support 1 | $55.13 | -8.1% |
| 200 SMA | $49.12 | -18.1% |
| 50 EMA | $58.35 | -2.7% |
| 10 EMA | $59.24 | -0.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO | RSI(2)=45.3, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | NO | MACD histogram=+0.30, RSI(14)=58.1, Volume=0.23x | NO SETUP |
| Bollinger Squeeze | NO | Bandwidth=10.45 (6m low=4.67), RSI(14)=58.1, Volume=0.23x | NO SETUP |
| MA Crossover | YES (technical) | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES, Price above 10 EMA=YES | REJECTED |
| VIX Fear | — | Not applicable | N/A |

### Decision
**NO SETUP**

**Rationale:** XLE technically qualifies for MA Crossover (bullish EMA structure, price in pullback zone, above 10 EMA), but pre-computed R:R is **0.85:1**, failing the mandatory 1.5:1 minimum. Reward potential ($1.71/share) does not justify risk ($2.02/share). The setup lacks sufficient asymmetry to warrant execution despite technical alignment.

---

## Ticker: XOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $157.09 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.24x |
| ATR(14) | $4.40 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $163.68 | +4.2% |
| Support 1 | $142.95 | -8.9% |
| 200 SMA | $129.13 | -17.8% |
| 50 EMA | $154.72 | -1.5% |
| 10 EMA | $155.32 | -1.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO | RSI(2)=40.2, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | NO | MACD histogram=+1.19, RSI(14)=55.9, Volume=0.24x | NO SETUP |
| Bollinger Squeeze | NO | Bandwidth=12.69 (6m low=4.27), RSI(14)=55.9, Volume=0.24x | NO SETUP |
| MA Crossover | YES (technical) | 10 EMA vs 50 EMA=BULLISH, Pullback zone=YES, Crossover=YES, Price above 10 EMA=YES | REJECTED |
| VIX Fear | — | Not applicable | N/A |

### Decision
**NO SETUP**

**Rationale:** XOM shows the strongest technical setup: bullish 10 EMA / 50 EMA crossover confirmed, price above both moving averages, pullback zone confirmed, RSI(14)=55.9 neutral. However, pre-computed R:R is **1.0:1**, failing the 1.5:1 threshold. Risk ($6.60/share) equals reward ($6.59/share), offering insufficient edge for strategy execution. The setup is mathematically underwater on asymmetry grounds despite solid technical alignment.

---

## Ticker: CVX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $192.53 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.24x |
| ATR(14) | $4.68 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $198.87 | +3.3% |
| Support 1 | $177.90 | -7.6% |
| 200 SMA | $165.87 | -13.8% |
| 50 EMA | $187.53 | -2.6% |
| 10 EMA | $189.99 | -1.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO | RSI(2)=49.2, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | NO | MACD histogram=+1.21, RSI(14)=55.6, Volume=0.24x | NO SETUP |
| Bollinger Squeeze | NO | Bandwidth=9.92 (6