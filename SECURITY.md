# Information Security Policy

**Organization:** Amplify AI Solutions
**Application:** Nico CFO
**Policy Owner:** Nico Lundquist, Owner
**Last Reviewed:** March 5, 2026
**Review Cadence:** Quarterly

---

## 1. Purpose

This document establishes the information security policies, procedures, and controls for the Nico CFO application. These policies are designed to protect the confidentiality, integrity, and availability of financial data processed by the application. This policy is continuously reviewed and matured as the application evolves.

## 2. Scope

This policy covers all components of the Nico CFO application, including:
- Financial data aggregation via the Plaid API
- Local data storage and encryption
- Credential and secret management
- Network communications
- Access controls
- Incident response

## 3. Data Classification

| Classification | Description | Examples |
|---------------|-------------|----------|
| **Confidential** | Financial data requiring encryption at rest and in transit | Transaction history, account balances, merchant data |
| **Secret** | Credentials and keys that must never be stored in plaintext | Plaid API keys, access tokens, database encryption keys |
| **Internal** | Application configuration and operational data | Sync cursors, category mappings, dashboard templates |

## 4. Encryption and Data Protection

### 4.1 Encryption at Rest
- All financial data is stored in a SQLCipher-encrypted SQLite database using **AES-256 encryption**
- Database encryption keys are 64-character hex strings generated using Python's `secrets` module (cryptographically secure random number generator)
- Encryption keys are stored in **macOS Keychain**, which is itself protected by the user's system login credentials

### 4.2 Encryption in Transit
- All communication with the Plaid API uses **TLS 1.2+** via HTTPS
- No unencrypted network communication occurs at any point in the application

### 4.3 Data Minimization
- Only the minimum required Plaid products are requested (Transactions, which includes Balances)
- No identity, authentication, income, or liability data is collected
- Account numbers and routing numbers are never stored — only masked identifiers (last 4 digits)

## 5. Credential and Secret Management

### 5.1 Storage
- All API credentials (Plaid client ID, secret, access tokens) are stored exclusively in **macOS Keychain**
- No credentials are stored in environment files, configuration files, or source code
- The `.gitignore` file explicitly excludes all sensitive file types (`.env`, `*.db`, credential files)

### 5.2 Access Control
- Keychain access requires the user's macOS login password or biometric authentication
- Credentials are scoped to the application service name (`nico-cfo`) in Keychain

### 5.3 Rotation and Revocation
- Plaid access tokens can be revoked at any time through the Plaid dashboard
- Database encryption keys can be rotated by generating a new key and re-encrypting the database
- The `keychain_setup.py` utility manages credential lifecycle (creation, retrieval, deletion)

## 6. Network Security

### 6.1 No Persistent Network Services
- The MCP server communicates via **stdio** (standard input/output pipes) — no TCP/UDP ports are opened
- The Plaid Link server is **ephemeral** — it runs on `127.0.0.1:5555` only during account setup and is shut down immediately after

### 6.2 Firewall and Exposure
- No inbound network connections are accepted during normal operation
- The application has zero attack surface from external networks
- The only outbound connections are HTTPS calls to the Plaid API (`*.plaid.com`)

### 6.3 Read-Only Access
- The Plaid integration is configured with **read-only scope** — it cannot initiate transfers, modify accounts, or perform any write operations against connected financial institutions

## 7. Access Controls

### 7.1 Application Access
- The application runs as a single-user local process under the operating system user's account
- No multi-user access, no authentication layer required (single-user, local-only)
- File permissions on the database are set to `chmod 600` (owner read/write only)

### 7.2 Third-Party Access
- No financial data is shared with, transmitted to, or accessible by any third party
- No cloud services, analytics platforms, or external APIs receive financial data
- All data processing occurs entirely on the local machine

## 8. Secure Development Practices

### 8.1 Dependency Management
- Dependencies are pinned to minimum versions in `requirements.txt`
- Only well-maintained, reputable packages are used (Plaid official SDK, Flask, SQLCipher)

### 8.2 Code Security
- No credentials are hardcoded in source code
- Input validation is performed on all user-supplied parameters (date ranges, search queries)
- SQL queries use parameterized statements to prevent SQL injection

### 8.3 Source Code Management
- Application source code is not published to public repositories
- The public GitHub repository contains documentation only (README, security policy, architecture)

## 9. Data Retention and Disposal

### 9.1 Retention
- Financial data is retained in the local encrypted database for as long as the user requires it for analysis
- No automatic data retention limits are imposed — the user controls their own data

### 9.2 Disposal
- Users can delete the encrypted database file (`cfo.db`) at any time to permanently remove all financial data
- Plaid access tokens can be revoked through the Plaid dashboard, which immediately terminates the application's ability to pull new data
- Keychain entries can be removed using macOS Keychain Access utility

## 10. Incident Response

### 10.1 Detection
- Plaid provides webhook notifications for suspicious activity on connected items
- Users can review transaction history through the dashboard to identify unauthorized transactions

### 10.2 Response Procedure
1. **Identify** — Determine the scope and nature of the incident
2. **Contain** — Revoke affected Plaid access tokens immediately via the Plaid dashboard
3. **Eradicate** — Rotate database encryption key and regenerate all credentials
4. **Recover** — Re-authenticate with financial institutions using new tokens
5. **Review** — Document the incident and update security controls as needed

### 10.3 Contact
- Security incidents should be reported to the application owner immediately
- Plaid security incidents can be reported to Plaid's security team at security@plaid.com

## 11. Monitoring and Review

### 11.1 Continuous Monitoring
- Transaction sync logs are reviewed for API errors or unexpected behavior
- Plaid dashboard provides visibility into API call usage and connected item status

### 11.2 Policy Review
- This security policy is reviewed **quarterly** and updated as the application evolves
- Changes to the security architecture trigger an immediate policy review
- All policy updates are documented with revision dates

---

**Document History:**

| Date | Version | Change |
|------|---------|--------|
| March 5, 2026 | 1.0 | Initial security policy |
