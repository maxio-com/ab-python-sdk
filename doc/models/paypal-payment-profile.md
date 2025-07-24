
# Paypal Payment Profile

## Structure

`PaypalPaymentProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The Chargify-assigned ID of the stored PayPal payment profile. |
| `first_name` | `str` | Optional | The first name of the PayPal account holder |
| `last_name` | `str` | Optional | The last name of the PayPal account holder |
| `customer_id` | `int` | Optional | The Chargify-assigned id for the customer record to which the PayPal account belongs |
| `current_vault` | [`PayPalVault`](../../doc/models/pay-pal-vault.md) | Optional | The vault that stores the payment profile with the provided vault_token. |
| `vault_token` | `str` | Optional | The “token” provided by your vault storage for an already stored payment profile |
| `billing_address` | `str` | Optional | The current billing street address for the PayPal account |
| `billing_city` | `str` | Optional | The current billing address city for the PayPal account |
| `billing_state` | `str` | Optional | The current billing address state for the PayPal account |
| `billing_zip` | `str` | Optional | The current billing address zip code for the PayPal account |
| `billing_country` | `str` | Optional | The current billing address country for the PayPal account |
| `customer_vault_token` | `str` | Optional | - |
| `billing_address_2` | `str` | Optional | The current billing street address, second line, for the PayPal account |
| `payment_type` | [`PaymentType`](../../doc/models/payment-type.md) | Required | **Default**: `'paypal_account'` |
| `site_gateway_setting_id` | `int` | Optional | - |
| `gateway_handle` | `str` | Optional | - |
| `paypal_email` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | A timestamp indicating when this payment profile was created |
| `updated_at` | `datetime` | Optional | A timestamp indicating when this payment profile was last updated |

## Example (as JSON)

```json
{
  "payment_type": "paypal_account",
  "id": 10,
  "first_name": "first_name0",
  "last_name": "last_name8",
  "customer_id": 48,
  "current_vault": "moduslink"
}
```

