# Workflows

## Daily Trading Workflow

### Morning Scan (6:00 AM EST)
1. Data fetcher pulls overnight news, pre-market data, macro indicators
2. Agent 1 assesses market regime → PROCEED or STAND DOWN
3. If PROCEED: Agent 2 runs technicals on recommended tickers
4. Agent 3 merges news + technicals
5. Agent 4 scores and decides
6. Agent 5 final risk check
7. Approved trades queued for execution

### Market Open (9:30 AM EST)
1. Execute all approved trades as bracket orders
2. Log orders to `P-portfolio/pending-orders.md`
3. Update `P-portfolio/current-positions.md`

### Position Monitoring (10 AM - 3 PM EST, hourly)
1. Check all open positions vs current prices
2. Update unrealized P&L
3. Check if stops or targets have been hit
4. Update portfolio files
5. Log any fills

### Post-Market Review (4:30 PM EST)
1. Record all closed trades with final P&L
2. Generate trade journal entries
3. Update learning log with new patterns
4. Update strategy performance logs
5. Copy notable trades to best/worst references
6. Commit all vault changes to git

## Weekly Workflow

### Friday Post-Market
1. Review weekly performance
2. Assess strategy performance by type
3. Check if any strategies need adjustment
4. Update watchlist based on next week's catalysts
5. Review rejected trades — were they correctly rejected?

## Monthly Workflow

### End of Month
1. Generate monthly review in `M-memory/monthly-reviews/`
2. Compare actual vs target performance
3. Compare against S&P 500 benchmark
4. Identify best and worst strategies
5. Identify recurring patterns in wins and losses
6. Update monthly targets for next month
7. Consider strategy parameter adjustments

## Trade Lifecycle

```
1. CANDIDATE    → Ticker appears in Agent 1 brief
2. ANALYZED     → Agent 2 confirms/denies setup
3. MERGED       → Agent 3 produces unified report
4. DECIDED      → Agent 4 scores 8/10+ (BUY/SHORT)
5. APPROVED     → Agent 5 passes all 14 checks (GO)
6. EXECUTED     → Bracket order placed on Alpaca
7. ACTIVE       → Position open, monitored hourly
8. CLOSED       → Stop/target hit or manual exit
9. POST-MORTEM  → Trade journal + learning log updated
```

## Error Recovery

| Error | Action |
|-------|--------|
| Data fetch fails | Retry once, then STAND DOWN for the day |
| Claude API fails | Retry once, then STAND DOWN |
| Alpaca API fails | Retry once, then alert via log |
| Agent output unparseable | Retry once, then skip ticker |
| GitHub Action fails | Check logs, manual trigger available |
