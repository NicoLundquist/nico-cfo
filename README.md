# Nico CFO

AI-powered personal and business finance command center.

## What It Does

Nico CFO aggregates financial data from multiple bank accounts, credit cards, and payment platforms into a single encrypted dashboard. It uses AI to:

- **Analyze spending patterns** — categorize transactions automatically and identify where money is going
- **Track cash flow** — visualize income vs. expenses over time with trend analysis
- **Detect recurring charges** — surface subscriptions and recurring payments across all accounts
- **Monitor burn rate** — calculate monthly spend rate and financial runway
- **Generate financial reports** — monthly summaries, category breakdowns, and year-over-year comparisons
- **Track business revenue** — tag incoming payments by client and generate revenue reports

## How It Works

Nico CFO connects to financial institutions through the [Plaid API](https://plaid.com/) to securely pull account balances and transaction history. Data is stored in an encrypted local database (SQLCipher) and analyzed using AI to surface insights, trends, and anomalies.

### Architecture

```
Bank Accounts ──┐
Credit Cards ───┤
PayPal ─────────┼──▶ Plaid API ──▶ Encrypted DB ──▶ AI Analysis ──▶ Dashboard
Coinbase ───────┤                   (SQLCipher)      (Claude)        (Chart.js)
Savings ────────┘
```

### Security

- All financial data stored in an AES-256 encrypted SQLite database
- API credentials stored in macOS Keychain (not in config files)
- Read-only access to financial institutions (cannot initiate transfers)
- No open network ports — runs entirely on localhost
- No cloud storage — all data stays on the local machine

## Tech Stack

- **Python** — Core application
- **Plaid API** — Financial data aggregation
- **SQLCipher** — Encrypted database
- **Flask** — Account connection flow
- **Chart.js** — Dashboard visualizations
- **MCP (Model Context Protocol)** — AI integration layer

## Features

| Feature | Description |
|---------|-------------|
| Multi-account aggregation | Connect checking, savings, credit cards, PayPal, and crypto accounts |
| Automated categorization | Transactions automatically categorized by Plaid + custom rules |
| HUD-style dashboard | Real-time visual dashboard with charts, gauges, and trend analysis |
| Conversational CFO | Query your finances in natural language through AI integration |
| Client revenue tracking | Tag incoming payments to business clients for revenue reporting |
| Recurring charge detection | Automatically surface subscriptions and recurring payments |
| Cash flow forecasting | Burn rate calculation and runway estimation |

## License

MIT
