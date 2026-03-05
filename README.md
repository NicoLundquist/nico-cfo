# Nico CFO

**AI-powered personal and business finance command center.**

Nico CFO aggregates financial data from multiple bank accounts, credit cards, and payment platforms into a single encrypted dashboard — providing real-time visibility into cash flow, spending patterns, and financial health.

![Dashboard Preview](docs/dashboard-preview.png)

---

## Features

### Multi-Account Aggregation
Connect checking, savings, credit cards, PayPal, and crypto accounts through Plaid's secure banking API. View all balances in one place with a unified net position calculation.

### AI-Powered Financial Analysis
Uses AI to analyze transactions and surface actionable insights:
- Automatic transaction categorization
- Recurring charge and subscription detection
- Spending trend analysis and anomaly flagging
- Budget vs. actual comparisons
- Cash flow forecasting

### Real-Time Dashboard
HUD-style command center dashboard with:
- Net position and account balance gauges
- Monthly income vs. expense tracking
- Spending breakdown by category (interactive donut chart)
- 6-month cash flow trend visualization
- Recent transactions feed with search and filtering
- Burn rate calculation and runway estimation

### Business Revenue Tracking
Tag incoming payments by client to track:
- Revenue per client over any time period
- Payment frequency and consistency
- Total business income vs. personal income
- Client-level profitability insights

### Conversational CFO
Query your finances in natural language through MCP (Model Context Protocol) integration:
- "What did I spend on software this month?"
- "What's my burn rate?"
- "Show me all recurring charges"
- "How much has Three Crowns paid me this year?"

---

## Architecture

```
Bank Accounts ──┐
Credit Cards ───┤
PayPal ─────────┼──▶ Plaid API ──▶ Encrypted DB ──▶ AI Analysis ──▶ Dashboard
Coinbase ───────┤     (read-only)   (SQLCipher)      (Claude MCP)    (Chart.js)
Savings ────────┘
```

### Tech Stack

| Component | Technology |
|-----------|-----------|
| Data Aggregation | Plaid API (Transactions, Balances) |
| Database | SQLCipher (AES-256 encrypted SQLite) |
| Credential Storage | macOS Keychain |
| Account Linking | Flask (localhost only) |
| Dashboard | HTML5, Chart.js, CSS3 |
| AI Integration | MCP (Model Context Protocol) via FastMCP |
| Language | Python 3.13 |

---

## Security

Nico CFO is designed with security as a first principle:

- **Encrypted at rest** — All financial data stored in AES-256 encrypted SQLite database (SQLCipher)
- **Keychain credentials** — API keys and tokens stored in macOS Keychain, never in config files
- **Read-only access** — Plaid connection cannot initiate transfers or modify accounts
- **No open ports** — MCP server communicates via stdio, no HTTP endpoints exposed
- **Local only** — All data stays on the local machine, no cloud storage or third-party transmission
- **Minimal scope** — Only requests Transactions product (includes balances), no identity or auth data

---

## Products Used

| Plaid Product | Purpose |
|---------------|---------|
| **Transactions** | Pull transaction history for categorization, trend analysis, and spending reports |
| **Balances** | Real-time account balance monitoring across all connected institutions |

---

## How Plaid Data Is Used

1. **Account Linking** — Users authenticate with their financial institution through Plaid Link (OAuth). Access tokens are stored in macOS Keychain.

2. **Transaction Sync** — Transactions are pulled via Plaid's cursor-based sync API and stored in an encrypted local database. Plaid's automatic categorization is preserved and enhanced with custom tagging.

3. **Balance Monitoring** — Current and available balances are synced daily and stored as snapshots to track balance trends over time.

4. **Analysis & Reporting** — Transaction data is analyzed locally to generate spending reports, detect recurring charges, calculate burn rate, and produce cash flow visualizations. All analysis happens on-device.

5. **No Data Sharing** — Financial data is never transmitted to third parties, stored in cloud services, or used for any purpose other than the account holder's personal financial analysis.

---

## Data Flow

```
Plaid API ──▶ Local Sync Engine ──▶ Encrypted Database (SQLCipher)
                                           │
                                           ├──▶ Dashboard Generator ──▶ HTML Dashboard
                                           │
                                           └──▶ MCP Server ──▶ AI Analysis (local only)
```

---

## License

MIT
