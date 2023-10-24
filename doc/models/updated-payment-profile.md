
# Updated Payment Profile

## Structure

`UpdatedPaymentProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `card_type` | `str` | Optional | - |
| `expiration_month` | `int` | Optional | - |
| `expiration_year` | `int` | Optional | - |
| `customer_id` | `int` | Optional | - |
| `current_vault` | [`CurrentVault`](../../doc/models/current-vault.md) | Optional | The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for testing. |
| `vault_token` | `str` | Optional | - |
| `billing_address` | `str` | Optional | - |
| `billing_address_2` | `str` | Optional | - |
| `billing_city` | `str` | Optional | - |
| `billing_state` | `str` | Optional | - |
| `billing_zip` | `str` | Optional | - |
| `billing_country` | `str` | Optional | - |
| `payment_type` | `str` | Optional | - |
| `site_gateway_setting_id` | `int` | Optional | - |
| `gateway_handle` | `str` | Optional | - |
| `masked_card_number` | `str` | Optional | - |
| `customer_vault_token` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "id": 232,
  "first_name": "first_name0",
  "last_name": "last_name8",
  "card_type": "card_type4",
  "expiration_month": 150
}
```

