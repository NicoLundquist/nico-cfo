# Architecture

## System Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                        NICO CFO SYSTEM                           │
│                                                                  │
│  ┌─────────────┐    ┌──────────────┐    ┌───────────────────┐   │
│  │  Plaid API   │───▶│  Sync Engine  │───▶│  Encrypted DB     │   │
│  │  (read-only) │    │  (sync.py)    │    │  (SQLCipher)      │   │
│  └─────────────┘    └──────────────┘    └─────────┬─────────┘   │
│                                                     │             │
│                              ┌──────────────────────┼───────┐    │
│                              │                      │       │    │
│                     ┌────────▼───────┐    ┌────────▼──────┐│    │
│                     │  MCP Server     │    │  Dashboard    ││    │
│                     │  (mcp_server.py)│    │  (dashboard.py││    │
│                     │  9 CFO tools    │    │   + Chart.js) ││    │
│                     └────────────────┘    └───────────────┘│    │
│                              │                              │    │
│                     ┌────────▼───────┐    ┌───────────────┐│    │
│                     │  Claude AI      │    │  Browser       ││    │
│                     │  (conversational│    │  (visual       ││    │
│                     │   CFO queries)  │    │   dashboard)   ││    │
│                     └────────────────┘    └───────────────┘│    │
│                                                             │    │
└──────────────────────────────────────────────────────────────────┘
```

## Components

### 1. Account Linking (`link_server.py`)
- Flask server running on `127.0.0.1:5555`
- Serves Plaid Link UI for OAuth bank authentication
- Ephemeral — only runs during account setup
- Stores access tokens in macOS Keychain

### 2. Sync Engine (`sync.py`)
- Pulls transactions via Plaid's cursor-based sync API
- Syncs account balances and saves daily snapshots
- Supports incremental sync (only fetches new/modified/removed transactions)
- Stores all data in encrypted SQLite database

### 3. Encrypted Database (`db.py`)
- SQLCipher-encrypted SQLite database
- Tables: accounts, transactions, balance_snapshots, sync_cursors, client_tags
- Indexed for fast queries on date, category, account, and client tag
- Supports transaction tagging for business revenue tracking

### 4. MCP Server (`mcp_server.py`)
- FastMCP server exposing 9 financial query tools
- Communicates via stdio (no network exposure)
- Tools: get_balances, get_transactions, spending_by_category, monthly_summary,
  recurring_charges, tag_client_revenue, client_revenue_report, cash_flow_trend, sync_now

### 5. Dashboard Generator (`dashboard.py`)
- Generates standalone HTML dashboard from database
- Chart.js visualizations: line charts, bar charts, donut charts, gauges
- HUD-style command center interface
- Auto-refreshes by re-running the generator

## Data Flow

1. User authenticates with bank via Plaid Link (one-time)
2. Access token stored in macOS Keychain
3. Sync engine pulls transactions and balances via Plaid API
4. Data stored in encrypted local database
5. Dashboard generator reads DB and produces HTML visualization
6. MCP server reads DB and responds to AI queries

## Security Layers

| Layer | Implementation |
|-------|---------------|
| Transport | TLS (Plaid API), stdio (MCP) |
| Credentials | macOS Keychain |
| Data at rest | SQLCipher AES-256 |
| File permissions | chmod 600 on database |
| Network exposure | None (localhost only, ephemeral) |
| Access scope | Read-only (Transactions + Balances) |
