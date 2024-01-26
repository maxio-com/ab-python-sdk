
# Credit Card Payment Profile

## Structure

`CreditCardPaymentProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The Chargify-assigned ID of the stored card. This value can be used as an input to payment_profile_id when creating a subscription, in order to re-use a stored payment profile for the same customer. |
| `first_name` | `str` | Optional | The first name of the card holder. |
| `last_name` | `str` | Optional | The last name of the card holder. |
| `masked_card_number` | `str` | Required | A string representation of the credit card number with all but the last 4 digits masked with X’s (i.e. ‘XXXX-XXXX-XXXX-1234’). |
| `card_type` | [`CardType`](../../doc/models/card-type.md) | Optional | The type of card used. |
| `expiration_month` | `int` | Optional | An integer representing the expiration month of the card(1 – 12). |
| `expiration_year` | `int` | Optional | An integer representing the 4-digit expiration year of the card(i.e. ‘2012’). |
| `customer_id` | `int` | Optional | The Chargify-assigned id for the customer record to which the card belongs. |
| `current_vault` | [`CurrentVault`](../../doc/models/current-vault.md) | Optional | The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for testing. |
| `vault_token` | `str` | Optional | The “token” provided by your vault storage for an already stored payment profile. |
| `billing_address` | `str` | Optional | The current billing street address for the card. |
| `billing_city` | `str` | Optional | The current billing address city for the card. |
| `billing_state` | `str` | Optional | The current billing address state for the card. |
| `billing_zip` | `str` | Optional | The current billing address zip code for the card. |
| `billing_country` | `str` | Optional | The current billing address country for the card. |
| `customer_vault_token` | `str` | Optional | (only for Authorize.Net CIM storage): the customerProfileId for the owner of the customerPaymentProfileId provided as the vault_token. |
| `billing_address_2` | `str` | Optional | The current billing street address, second line, for the card. |
| `payment_type` | [`PaymentType`](../../doc/models/payment-type.md) | Optional | **Default**: `'credit_card'` |
| `disabled` | `bool` | Optional | - |
| `chargify_token` | `str` | Optional | Token received after sending billing information using chargify.js. This token will only be received if passed as a sole attribute of credit_card_attributes (i.e. tok_9g6hw85pnpt6knmskpwp4ttt) |
| `site_gateway_setting_id` | `int` | Optional | - |
| `gateway_handle` | `str` | Optional | An identifier of connected gateway. |

## Example (as JSON)

```json
{
  "id": 10088716,
  "first_name": "Test",
  "last_name": "Subscription",
  "masked_card_number": "XXXX-XXXX-XXXX-1",
  "card_type": "bogus",
  "expiration_month": 1,
  "expiration_year": 2022,
  "customer_id": 14543792,
  "current_vault": "bogus",
  "vault_token": "1",
  "billing_address": "123 Montana Way",
  "billing_city": "Billings",
  "billing_state": "MT",
  "billing_zip": "59101",
  "billing_country": "US",
  "customer_vault_token": null,
  "billing_address_2": "",
  "payment_type": "credit_card",
  "site_gateway_setting_id": 1,
  "gateway_handle": null
}
```

