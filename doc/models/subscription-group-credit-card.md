
# Subscription Group Credit Card

## Structure

`SubscriptionGroupCreditCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `full_number` | str \| int \| None | Optional | This is a container for one-of cases. |
| `expiration_month` | str \| int \| None | Optional | This is a container for one-of cases. |
| `expiration_year` | str \| int \| None | Optional | This is a container for one-of cases. |
| `chargify_token` | `str` | Optional | - |
| `vault_token` | `str` | Optional | - |
| `current_vault` | [`CurrentVault`](../../doc/models/current-vault.md) | Optional | The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for testing. |
| `gateway_handle` | `str` | Optional | - |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `billing_address` | `str` | Optional | - |
| `billing_address_2` | `str` | Optional | - |
| `billing_city` | `str` | Optional | - |
| `billing_state` | `str` | Optional | - |
| `billing_zip` | `str` | Optional | - |
| `billing_country` | `str` | Optional | - |
| `last_four` | `str` | Optional | - |
| `card_type` | `str` | Optional | - |
| `customer_vault_token` | `str` | Optional | - |
| `cvv` | `str` | Optional | - |
| `payment_type` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "full_number": 4111111111111111,
  "chargify_token": "tok_592nf92ng0sjd4300p",
  "card_type": "visa",
  "expiration_month": "String1",
  "expiration_year": "String5",
  "vault_token": "vault_token6"
}
```

