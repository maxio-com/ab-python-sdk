
# Bank Account

## Structure

`BankAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `customer_id` | `int` | Optional | - |
| `current_vault` | [`BankAccountVault`](../../doc/models/bank-account-vault.md) | Optional | The vault that stores the payment profile with the provided vault_token. |
| `vault_token` | `str` | Optional | - |
| `billing_address` | `str` | Optional | - |
| `billing_city` | `str` | Optional | - |
| `billing_state` | `str` | Optional | - |
| `billing_zip` | `str` | Optional | - |
| `billing_country` | `str` | Optional | - |
| `customer_vault_token` | `str` | Optional | - |
| `billing_address_2` | `str` | Optional | - |
| `bank_name` | `str` | Optional | - |
| `masked_bank_routing_number` | `str` | Optional | - |
| `masked_bank_account_number` | `str` | Optional | - |
| `bank_account_type` | `str` | Optional | - |
| `bank_account_holder_type` | `str` | Optional | - |
| `payment_type` | `str` | Optional | - |
| `verified` | `bool` | Optional | denotes whether a bank account has been verified by providing the amounts of two small deposits made into the account<br>**Default**: `False` |
| `site_gateway_setting_id` | `int` | Optional | - |
| `gateway_handle` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "verified": false,
  "id": 190,
  "first_name": "first_name2",
  "last_name": "last_name0",
  "customer_id": 228,
  "current_vault": "stripe_connect"
}
```

