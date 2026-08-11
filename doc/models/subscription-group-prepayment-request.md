
# Subscription Group Prepayment Request

## Structure

`SubscriptionGroupPrepaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `prepayment` | [`SubscriptionGroupPrepayment`](../../doc/models/subscription-group-prepayment.md) | Required | - |

## Example

```python
from advancedbilling.models.subscription_group_prepayment import SubscriptionGroupPrepayment
from advancedbilling.models.subscription_group_prepayment_method import SubscriptionGroupPrepaymentMethod
from advancedbilling.models.subscription_group_prepayment_request import SubscriptionGroupPrepaymentRequest

subscription_group_prepayment_request = SubscriptionGroupPrepaymentRequest(
    prepayment=SubscriptionGroupPrepayment(
        amount=136,
        details='details8',
        memo='memo2',
        method=SubscriptionGroupPrepaymentMethod.PAYPAL_ACCOUNT
    )
)
```

