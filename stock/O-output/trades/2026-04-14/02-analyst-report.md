# Technical Analysis Report — 2026-04-14

## Ticker: AI

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $8.47 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.04x |
| ATR(14) | $0.49 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $9.31 | +9.9% |
| Support 1 | $7.68 | -9.3% |
| 200 SMA | $15.77 | +86.1% |
| 50 EMA | $9.40 | +10.9% |
| 10 EMA | $8.51 | +0.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=50.3, Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAIL | No MACD cross, MACD=-0.27, RSI(14)=44.2, Price BELOW 50 SMA | NO SETUP |
| Bollinger Squeeze | FAIL | BW=13.90 (above 6m low=7.95), No breakout, Volume weak | NO SETUP |
| MA Crossover | FAIL | No crossover, 10 EMA ($8.51) below 50 EMA ($9.40), Price below 10 EMA | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

Price deeply underwater vs. 200 SMA (+86% gap). All moving averages bearish. No technical catalyst present.

---

## Ticker: JPM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $313.68 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.82x |
| ATR(14) | $7.05 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $313.74 | +0.02% |
| Support 1 | $280.32 | -10.6% |
| 200 SMA | $300.33 | -4.3% |
| 50 EMA | $298.21 | -4.9% |
| 10 EMA | $302.40 | -3.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=95.9 (extremely overbought), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAIL | No MACD cross, MACD=3.85, RSI(14)=69.3 (elevated), Volume weak (0.82x) | NO SETUP |
| Bollinger Squeeze | FAIL | BW=12.99 (above 6m low=4.52), Breakout triggered but volume weak | NO SETUP |
| MA Crossover | FAIL | Crossover present but price already extended above 10 EMA, no pullback zone, volume weak | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

Price at resistance ($313.74). RSI(2) extreme overbought (95.9). Volume confirmation lacking (0.82x). Risk/reward asymmetric to downside.

---

## Ticker: GS

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $890.79 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 2.03x |
| ATR(14) | $27.96 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $918.12 | +3.1% |
| Support 1 | $790.00 | -11.4% |
| 200 SMA | $809.55 | -9.1% |
| 50 EMA | $863.12 | -3.1% |
| 10 EMA | $876.13 | -1.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=30.2, Price above 200 SMA | NO SETUP |
| MACD + RSI | FAIL | No MACD cross, MACD=11.57, RSI(14)=59.2, Price above 50 SMA, Volume confirms (2.03x) | NO SETUP |
| Bollinger Squeeze | FAIL | BW=17.17 (above 6m low=5.29), No breakout, RSI(14)=59.2 | NO SETUP |
| MA Crossover | **CONFIRMED** | Crossover YES, EMA10 ($876.13) bullish vs EMA50 ($863.12), Pullback zone YES, Price above 10 EMA, RSI(14)=59.2, Volume confirms (2.03x) | **SETUP** |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $890.79 |
| Stop Loss | $848.85 |
| Take Profit | $918.12 |
| R:R Ratio | 0.65:1 |
| **R:R Assessment** | **BELOW MIN THRESHOLD (1.5:1 required)** |

### Decision
**SETUP CONFIRMED [MA Crossover] — BUT REJECTED FOR EXECUTION**

**Reason:** While MA Crossover strategy parameters are technically met (bullish crossover, pullback zone confirmed, strong volume), the risk-to-reward ratio of **0.65:1 fails the minimum requirement of 1.5:1**. The $27.33 reward does not justify the $41.94 risk. **Do not trade this setup.**

---

## Ticker: JNJ

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $237.96 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.02x |
| ATR(14) | $4.20 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $247.21 | +3.9% |
| Support 1 | $232.24 | -2.4% |
| 200 SMA | $199.37 | -16.2% |
| 50 EMA | $240.47 | +1.1% |
| 10 EMA | $240.07 | +0.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=14.8, Price above 200 SMA (but condition allows RSI < 10 only) | NO SETUP |
| MACD + RSI | FAIL | No MACD cross, MACD=0.21, RSI(14)=45.6, Price below 50 EMA ($240.47) | NO SETUP |
| Bollinger Squeeze | FAIL | BW=4.67 (above 6m low=3.91), No breakout, Volume weak | NO SETUP |
| MA Crossover | FAIL | No crossover, 10 EMA above 50 EMA (bullish) but price below 10 EMA, no pullback bounce | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

Price caught between moving averages. No crossover signal. MACD bearish (histogram negative). Relative volume minimal (1.02x). Consolidation pattern — no edge.

---

## Ticker: TSLA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $352.42 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.83x |
| ATR(14) | $14.26 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $403.73 | +14.6% |
| Support 1 | $337.24 | -4.3% |
| 200 SMA | $397.48 | +12.8% |
| 50 EMA | $393.02 | +11.5% |
| 10 EMA | $355.99 | +1.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=80.7, Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAIL | No MACD cross, MACD=-13.95 (bearish), RSI(14)=39.2, Price below 50 EMA | NO SETUP |
| Bollinger Squeeze | FAIL | BW=18.88 (above 6m low=7.04), No breakout, Volume weak | NO SETUP |
| MA Crossover | FAIL | No crossover, 10 EMA above 50 EMA but both above price, bearish configuration | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

Price significantly below both 50 EMA and 200 SMA (downtrend). MACD deeply negative. Volume weak (0.83x). No mean reversion setup (RSI not oversold). Avoid until trend reversal confirmed.

---

## Ticker: EV

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | N/A |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | N/A |
| ATR(14) | N/A |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | N/A | N/A |
| Support 1 | N/A | N/A |
| 200 SMA | N/A | N/A |
| 50 EMA | N/A | N/A |
| 10 EMA | N/A | N/A |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | SKIP | No data | N/A |
| MACD + RSI | SKIP | No data | N/A |
| Bollinger Squeeze | SKIP | No data | N/A |
| MA Crossover | SKIP | No data | N/A |
| VIX Fear | SKIP | No data | N/A |

### Decision
**NO DATA — CANNOT ANALYZE**

Ticker EV: No price, volume, or technical data available. Possible delisting, data feed error, or invalid ticker. Exclude from analysis.

---

## Ticker: TXN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $216.71 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.78x |
| ATR(14) | $5.84 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $217.32 | +0.3% |
| Support 1 | $184.90 | -14.7% |
| 200 SMA | $188.63 | -13.0% |
| 50 EMA | $206.64 | -4.6% |
| 10 EMA | $205.86 | -5.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=96.8 (extremely overbought), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAIL | No MACD cross, MACD=3.06, RSI(14)=67.9 (elevated), Volume weak (0.78x) | NO SETUP |
| Bollinger Squeeze | FAIL | BW=18.50 (above 6m low=5.41), Breakout triggered but volume weak | NO SETUP |
| MA Crossover | FAIL | Crossover present but price already extended above 10 EMA, no pullback zone present, volume weak | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

Price at resistance ($217.32). RSI(2) extreme overbought (96.8). No pullback into 10 EMA for safe entry. Volume weak (0.78x). High risk of immediate pullback with minimal upside.

---

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $267.32 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.85x |
| ATR(14) | $12.10 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $268.23 | +0.3% |
| Support 1 | $198.60 | -25.7% |
| 200 SMA | $162.58 | -39.2% |
| 50 EMA | $228.46 | -14.6% |
| 10 EMA | $242.44 | -9.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=99.3 (extreme overbought), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAIL | No MACD cross, MACD=8.20, RSI(14)=68.1 (elevated), Volume weak (0.85x) | NO SETUP |
| Bollinger Squeeze | FAIL | BW=30.31 (above 6m low=15.05), Breakout triggered but volume weak | NO SETUP |
| MA Crossover | FAIL | No crossover, 10 EMA ($242.44) below price (bullish) but no pullback zone, volume weak | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP**

Price at resistance ($268.23). RSI(2) extreme overbought (99.3). Extended above both 10 EMA and 50 EMA with no pullback. Volume weak (0.85x). High probability of correction without confirmed setup for long entry.

---

## Summary — 2026-04-14

| Ticker | Strategy | Verdict | Reason |
|--------|----------|---------|--------|
| AI | Any | NO SETUP | Price below 200 SMA; no bullish indicator alignment |
| JPM |