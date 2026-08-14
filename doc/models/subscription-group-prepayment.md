
# Subscription Group Prepayment

## Structure

`SubscriptionGroupPrepayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Required | - |
| `details` | `str` | Required | - |
| `memo` | `str` | Required | - |
| `method` | [`SubscriptionGroupPrepaymentMethod`](../../doc/models/subscription-group-prepayment-method.md) | Required | - |

## Example

```python
from advancedbilling.models.subscription_group_prepayment import SubscriptionGroupPrepayment
from advancedbilling.models.subscription_group_prepayment_method import SubscriptionGroupPrepaymentMethod

subscription_group_prepayment = SubscriptionGroupPrepayment(
    amount=118,
    details='details8',
    memo='memo2',
    method=SubscriptionGroupPrepaymentMethod.CHECK
)
```

