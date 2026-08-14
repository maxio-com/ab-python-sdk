
# Bank Account Vault

The vault that stores the payment profile with the provided vault_token. Use `bogus` for testing.

## Enumeration

`BankAccountVault`

## Fields

| Name |
|  --- |
| `AUTHORIZENET` |
| `BLUE_SNAP` |
| `BOGUS` |
| `FORTE` |
| `GOCARDLESS` |
| `MAXIO_PAYMENTS` |
| `MAXP` |
| `STRIPE_CONNECT` |

## Example

```python
from advancedbilling.models.bank_account_vault import BankAccountVault

bank_account_vault = BankAccountVault.BOGUS
```

