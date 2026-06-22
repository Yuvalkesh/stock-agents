# Technical Analysis Report — 2026-06-22

## Ticker: KLAC

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $266.11 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.28x |
| ATR(14) | $14.68 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $269.90 | +1.4% |
| Support 1 | $186.17 | -30.1% |
| 200 SMA | $145.03 | -45.5% |
| 50 EMA | $195.47 | -26.5% |
| 10 EMA | $240.98 | -9.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | OVERBOUGHT | RSI(2)=88.39, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | MOMENTUM WANING | MACD=19.04, Signal=14.78, RSI(14)=71.85 | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | Bandwidth=45.91 (6m low=8.90), RSI=71.85 | NO SETUP |
| MA Crossover | BULLISH BUT EXTENDED | 10 EMA=240.98, 50 EMA=195.47, Price above both | NO SETUP |
| VIX Fear | N/A | Not applicable | N/A |

### Decision
**NO SETUP**

**Rationale:** KLAC is extended across all timeframes. RSI(2) at 88.39 signals extreme overbought conditions unsuitable for mean reversion. No MACD crossover confirmed. Bollinger Bandwidth (45.91) far exceeds 6-month low (8.90), indicating high expansion—not squeeze setup. Relative volume at 0.28x is weak and insufficient for confirmation. Price is well above 10 EMA and 50 EMA with no pullback zone forming. All five strategies reject this setup.

---

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $394.48 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.30x |
| ATR(14) | $21.68 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $402.00 | +1.9% |
| Support 1 | $302.53 | -23.3% |
| 200 SMA | $211.19 | -46.4% |
| 50 EMA | $300.68 | -23.8% |
| 10 EMA | $366.51 | -7.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | OVERBOUGHT | RSI(2)=86.63, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | MOMENTUM WANING | MACD=25.53, Signal=21.10, RSI(14)=69.68 | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | Bandwidth=33.71 (6m low=11.03), RSI=69.68 | NO SETUP |
| MA Crossover | BULLISH BUT EXTENDED | 10 EMA=366.51, 50 EMA=308.23, Price above both | NO SETUP |
| VIX Fear | N/A | Not applicable | N/A |

### Decision
**NO SETUP**

**Rationale:** LRCX mirrors KLAC conditions—extended momentum across all moving averages with no pullback trigger. RSI(2) at 86.63 confirms overbought extremes. MACD histogram (4.44) shows weakening momentum with no bearish crossover. Bollinger Bandwidth (33.71) is inflated relative to 6-month low (11.03). Relative volume at 0.30x fails to validate any breakout. Price sits 7.1% above 10 EMA with no reversion zone. No setup warranted.

---

## Ticker: MRVL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $301.55 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.34x |
| ATR(14) | $27.60 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $329.88 | +9.4% |
| Support 1 | $192.22 | -36.3% |
| 200 SMA | $114.19 | -62.1% |
| 50 EMA | $201.57 | -33.1% |
| 10 EMA | $286.34 | -5.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NEUTRAL | RSI(2)=54.34, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | CROSSOVER CONFIRMED | MACD=30.46, Signal=30.29, RSI(14)=62.05 | SETUP CONFIRMED |
| Bollinger Squeeze | NO SQUEEZE | Bandwidth=62.24 (6m low=10.06), RSI=62.05 | NO SETUP |
| MA Crossover | BULLISH BUT EXTENDED | 10 EMA=286.34, 50 EMA=213.18, Price above both | NO SETUP |
| VIX Fear | N/A | Not applicable | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $301.55 |
| Stop Loss | $260.15 |
| Take Profit | $329.88 |
| R:R Ratio | 0.68:1 |

### Decision
**SETUP CONFIRMED — MACD + RSI, BUT R:R RATIO FAILS MINIMUM REQUIREMENT**

**Rationale:** MACD crossover confirmed with histogram = 0.16 (positive and rising). MACD (30.46) crossing above Signal (30.29). RSI(14) at 62.05 is in optimal range (35-75). Price above 50 EMA ($201.57). However, **pre-computed R:R ratio of 0.68:1 fails the strategy minimum of 1.0:1**. Risk per share ($41.40) exceeds reward per share ($28.33). This setup is **REJECTED for execution** due to insufficient risk/reward geometry, despite technical confirmation. Do not trade.

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $370.74 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.41x |
| ATR(14) | $11.86 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $466.32 | +25.7% |
| Support 1 | $370.41 | -0.1% |
| 200 SMA | $448.90 | +21.1% |
| 50 EMA | $412.41 | +11.2% |
| 10 EMA | $391.43 | +5.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | OVERSOLD BUT BEARISH | RSI(2)=5.81 (< 10), Price < 200 SMA | NO SETUP |
| MACD + RSI | BEARISH DIVERGENCE | MACD=-10.01, Signal=-4.69, RSI(14)=32.0 (out of range) | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | Bandwidth=22.83 (6m low=4.08), RSI=32.0 | NO SETUP |
| MA Crossover | BEARISH CROSSOVER | 10 EMA=391.43, 50 EMA=407.90, Price below both | NO SETUP |
| VIX Fear | N/A | Not applicable | N/A |

### Decision
**NO SETUP**

**Rationale:** MSFT is in clear downtrend. Price ($370.74) is below 200 SMA ($448.90), 50 EMA ($412.41), and 10 EMA ($391.43). RSI(2) at 5.81 signals oversold, but Connors RSI(2) strategy requires price > 200 SMA for long-term uptrend confirmation—this is absent. MACD is deeply negative (-10.01 vs Signal -4.69) with negative histogram, confirming bearish momentum. No MA crossover. EMA10 is below EMA50. Relative volume at 0.41x is weak. This is a downtrend environment; no setup is valid.

---

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $209.83 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.33x |
| ATR(14) | $7.44 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $232.01 | +10.5% |
| Support 1 | $199.34 | -4.9% |
| 200 SMA | $189.88 | -9.5% |
| 50 EMA | $209.64 | -0.1% |
| 10 EMA | $208.95 | -0.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NEUTRAL | RSI(2)=61.21, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | MOMENTUM WANING | MACD=-0.88, Signal=-0.22, RSI(14)=49.76 | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | Bandwidth=11.24 (6m low=5.37), RSI=49.76 | NO SETUP |
| MA Crossover | PULLBACK ZONE ACTIVE | 10 EMA=208.95, 50 EMA=206.88, Price above both, RSI=49.76 | SETUP CONFIRMED |
| VIX Fear | N/A | Not applicable | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $209.83 |
| Stop Loss | $198.67 |
| Take Profit | $232.01 |
| R:R Ratio | 1.99:1 |

### Decision
**SETUP CONFIRMED — MA CROSSOVER**

**Rationale:** MA Crossover setup validated. 10 EMA ($208.95) crossed above 50 EMA ($206.88) within recent period. Price ($209.83) is within pullback zone (within 1.0% of 10 EMA = 0.4% distance). Price bounced and closed above 10 EMA.