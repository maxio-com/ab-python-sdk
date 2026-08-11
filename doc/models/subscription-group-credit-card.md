
# Subscription Group Credit Card

## Structure

`SubscriptionGroupCreditCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chargify_token` | `str` | Optional | - |
| `vault_token` | `str` | Optional | - |
| `current_vault` | [`CreditCardVault`](../../doc/models/credit-card-vault.md) | Optional | The vault that stores the payment profile with the provided `vault_token`. Use `bogus` for testing. |
| `gateway_handle` | `str` | Optional | - |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `billing_address` | `str` | Optional | - |
| `billing_address_2` | `str` | Optional | - |
| `billing_city` | `str` | Optional | - |
| `billing_state` | `str` | Optional | - |
| `billing_zip` | `str` | Optional | - |
| `billing_country` | `str` | Optional | - |
| `full_number` | str \| int \| None | Optional | This is a container for one-of cases. |
| `expiration_month` | str \| int \| None | Optional | This is a container for one-of cases. |
| `expiration_year` | str \| int \| None | Optional | This is a container for one-of cases. |
| `last_four` | `str` | Optional | - |
| `card_type` | [`CardType`](../../doc/models/card-type.md) | Optional | The type of card used. |
| `customer_vault_token` | `str` | Optional | - |
| `cvv` | `str` | Optional | - |
| `payment_type` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.credit_card_vault import CreditCardVault
from advancedbilling.models.subscription_group_credit_card import SubscriptionGroupCreditCard

subscription_group_credit_card = SubscriptionGroupCreditCard(
    chargify_token='tok_592nf92ng0sjd4300p',
    vault_token='vault_token8',
    current_vault=CreditCardVault.PAYMILL,
    gateway_handle='gateway_handle2',
    first_name='first_name6',
    full_number=4111111111111111
)
```

