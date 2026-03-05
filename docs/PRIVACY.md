# Privacy Policy

## Data Collection

Nico CFO collects the following data from connected financial institutions via the Plaid API:

- **Account information**: Account name, type, subtype, mask (last 4 digits), and current/available balances
- **Transaction data**: Date, amount, merchant name, category, and pending status

No identity information, social security numbers, account numbers, routing numbers, or authentication credentials are collected or stored.

## Data Storage

All financial data is stored exclusively on the user's local machine in an AES-256 encrypted SQLite database (SQLCipher). Encryption keys are stored in macOS Keychain.

No data is transmitted to cloud services, third-party analytics, or external storage systems.

## Data Usage

Financial data is used solely for:
- Displaying account balances and transaction history
- Generating spending categorization and trend reports
- Detecting recurring charges and subscriptions
- Calculating cash flow, burn rate, and financial projections
- Responding to user queries through the AI integration

## Data Sharing

Financial data is never shared with third parties. All analysis occurs locally on the user's device.

## Data Retention

Data is retained in the local encrypted database until the user deletes it. Users can delete their database file at any time to remove all stored financial data.

## Plaid Integration

This application uses Plaid to connect to financial institutions. Plaid's privacy policy is available at https://plaid.com/legal/#end-user-privacy-policy.

## Contact

For questions about data handling, contact the repository owner.
