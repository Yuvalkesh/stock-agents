# Quick Start Guide

## Prerequisites
1. Python 3.12+
2. API keys:
   - Anthropic API key (Claude)
   - Alpaca API key + secret (paper trading)
   - Finnhub API key (news)

## Setup

### 1. Clone and install
```bash
cd /Users/Yuval/Documents/stock-agents
pip install -r requirements.txt
```

### 2. Configure environment
```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Run manually
```bash
# Full pipeline (morning scan + analysis + trade decisions)
python src/main.py --mode scan

# Execute approved trades
python src/main.py --mode execute

# Monitor positions
python src/main.py --mode monitor

# Post-market review
python src/main.py --mode review

# Full run (all modes in sequence)
python src/main.py --mode full
```

### 4. Check outputs
Open the `stock/` folder in Obsidian. All agent outputs appear in `O-output/trades/{date}/`.

### 5. Deploy to GitHub Actions
1. Push repo to GitHub
2. Add secrets in Settings → Secrets → Actions:
   - `ANTHROPIC_API_KEY`
   - `ALPACA_API_KEY`
   - `ALPACA_SECRET_KEY`
   - `NEWS_API_KEY`
3. Enable the workflow in Actions tab
4. Bot runs Mon-Fri on schedule automatically

## Daily Workflow
| Time (EST) | What Happens |
|------------|-------------|
| 6:00 AM | Morning scan + agent pipeline |
| 9:30 AM | Execute approved trades |
| 10 AM - 3 PM | Hourly position checks |
| 4:30 PM | Post-market review + learning log update |

## Verification Checklist
- [ ] `python src/main.py --mode scan` completes without errors
- [ ] Agent outputs appear in `O-output/trades/{date}/`
- [ ] Obsidian can read all files
- [ ] Alpaca dashboard shows bracket orders (after execute mode)
- [ ] Trade journal updates after position closes
