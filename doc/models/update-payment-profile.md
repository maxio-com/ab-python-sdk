
# Update Payment Profile

## Structure

`UpdatePaymentProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | The first name of the card holder. |
| `last_name` | `str` | Optional | The last name of the card holder. |
| `full_number` | `str` | Optional | The full credit card number |
| `card_type` | [`CardType`](../../doc/models/card-type.md) | Optional | The type of card used. |
| `expiration_month` | `str` | Optional | (Optional when performing an Import via vault_token, required otherwise) The 1- or 2-digit credit card expiration month, as an integer or string, e.g., 5 |
| `expiration_year` | `str` | Optional | (Optional when performing an Import via vault_token, required otherwise) The 4-digit credit card expiration year, as an integer or string, e.g., 2012 |
| `current_vault` | [`AllVaults`](../../doc/models/all-vaults.md) | Optional | The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for testing. |
| `billing_address` | `str` | Optional | The credit card or bank account billing street address (e.g., 123 Main St.). This value is merely passed through to the payment gateway. |
| `billing_city` | `str` | Optional | The credit card or bank account billing address city (e.g., “Boston”). This value is merely passed through to the payment gateway. |
| `billing_state` | `str` | Optional | The credit card or bank account billing address state (e.g., MA). This value is merely passed through to the payment gateway. This must conform to the [ISO_3166-1](https://en.wikipedia.org/wiki/ISO_3166-1#Current_codes) in order to be valid for tax locale purposes. |
| `billing_zip` | `str` | Optional | The credit card or bank account billing address zip code (e.g., 12345). This value is merely passed through to the payment gateway. |
| `billing_country` | `str` | Optional | The credit card or bank account billing address country, required in [ISO_3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format (e.g., “US”). This value is merely passed through to the payment gateway. Some gateways require country codes in a specific format. Check your gateway’s documentation. If creating an ACH subscription, only US is supported at this time. |
| `billing_address_2` | `str` | Optional | Second line of the customer’s billing address, e.g., Apt. 100 |

## Example

```python
from advancedbilling.models.card_type import CardType
from advancedbilling.models.update_payment_profile import UpdatePaymentProfile

update_payment_profile = UpdatePaymentProfile(
    first_name='first_name0',
    last_name='last_name8',
    full_number='5424000000000015',
    card_type=CardType.BOGUS,
    expiration_month='expiration_month6'
)
```

