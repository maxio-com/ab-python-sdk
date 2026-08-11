
# Get One Time Token Payment Profile

## Structure

`GetOneTimeTokenPaymentProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | - |
| `first_name` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `last_name` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `masked_card_number` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `card_type` | [`CardType`](../../doc/models/card-type.md) | Required | The type of card used. |
| `expiration_month` | `float` | Required | - |
| `expiration_year` | `float` | Required | - |
| `customer_id` | `str` | Optional | - |
| `current_vault` | [`CreditCardVault`](../../doc/models/credit-card-vault.md) | Required | The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for testing. |
| `vault_token` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `billing_address` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `billing_address_2` | `str` | Optional | - |
| `billing_city` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `billing_country` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `billing_state` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `billing_zip` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `payment_type` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `disabled` | `bool` | Required | - |
| `site_gateway_setting_id` | `int` | Required | - |
| `customer_vault_token` | `str` | Optional | - |
| `gateway_handle` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.card_type import CardType
from advancedbilling.models.credit_card_vault import CreditCardVault
from advancedbilling.models.get_one_time_token_payment_profile import GetOneTimeTokenPaymentProfile

get_one_time_token_payment_profile = GetOneTimeTokenPaymentProfile(
    first_name='first_name0',
    last_name='last_name8',
    masked_card_number='masked_card_number8',
    card_type=CardType.VISA,
    expiration_month=114.46,
    expiration_year=91.12,
    current_vault=CreditCardVault.ADYEN,
    vault_token='vault_token2',
    billing_address='billing_address2',
    billing_city='billing_city8',
    billing_country='billing_country4',
    billing_state='billing_state4',
    billing_zip='billing_zip8',
    payment_type='payment_type0',
    disabled=False,
    site_gateway_setting_id=68,
    id='id0',
    customer_id='customer_id8',
    billing_address_2='billing_address_22',
    customer_vault_token='customer_vault_token8',
    gateway_handle='gateway_handle2'
)
```

