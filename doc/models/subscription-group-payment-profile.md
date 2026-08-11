
# Subscription Group Payment Profile

## Structure

`SubscriptionGroupPaymentProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `masked_card_number` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.subscription_group_payment_profile import SubscriptionGroupPaymentProfile

subscription_group_payment_profile = SubscriptionGroupPaymentProfile(
    id=112,
    first_name='first_name8',
    last_name='last_name6',
    masked_card_number='masked_card_number6'
)
```

