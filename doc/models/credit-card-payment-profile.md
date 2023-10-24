
# Credit Card Payment Profile

## Structure

`CreditCardPaymentProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `masked_card_number` | `str` | Required | - |
| `card_type` | [`CardTypeCreditCardPaymentProfile`](../../doc/models/card-type-credit-card-payment-profile.md) | Optional | - |
| `expiration_month` | `int` | Optional | - |
| `expiration_year` | `int` | Optional | - |
| `customer_id` | `int` | Optional | - |
| `current_vault` | [`CurrentVault`](../../doc/models/current-vault.md) | Optional | The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for testing. |
| `vault_token` | `str` | Optional | - |
| `billing_address` | `str` | Optional | - |
| `billing_city` | `str` | Optional | - |
| `billing_state` | `str` | Optional | - |
| `billing_zip` | `str` | Optional | - |
| `billing_country` | `str` | Optional | - |
| `customer_vault_token` | `str` | Optional | - |
| `billing_address_2` | `str` | Optional | - |
| `payment_type` | `str` | Optional | - |
| `disabled` | `bool` | Optional | - |
| `site_gateway_setting_id` | `int` | Optional | - |
| `gateway_handle` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "id": 252,
  "first_name": "first_name0",
  "last_name": "last_name8",
  "masked_card_number": "masked_card_number8",
  "card_type": "synchrony",
  "expiration_month": 170
}
```

