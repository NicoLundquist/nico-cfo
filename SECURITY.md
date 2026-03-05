# Security Policy

## Architecture

Nico CFO is designed with a security-first architecture for handling sensitive financial data.

### Data Storage
- All financial data is stored in a locally encrypted SQLite database using SQLCipher (AES-256)
- Database encryption keys are stored in macOS Keychain, not in configuration files
- No financial data is transmitted to cloud services or third-party storage

### Credential Management
- Plaid API credentials are stored exclusively in macOS Keychain
- No `.env` files or plaintext credential storage
- Access tokens for financial institutions are stored in Keychain, keyed by item ID

### Network Security
- The MCP server communicates via stdio (standard input/output) — no network ports are opened
- The Plaid Link server runs on `127.0.0.1` only and is ephemeral (only active during account setup)
- All Plaid API communication uses TLS-encrypted HTTPS
- Plaid access is read-only — the application cannot initiate transfers or modify accounts

### Access Scope
- Only the Plaid Transactions product is used (includes balances)
- No identity, authentication, or income data is requested
- Plaid tokens can be revoked at any time from the Plaid dashboard

## Reporting a Vulnerability

If you discover a security vulnerability, please report it by opening a private issue or contacting the repository owner directly.
