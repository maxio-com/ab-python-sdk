
# List Subscription Group Prepayment Response

## Structure

`ListSubscriptionGroupPrepaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `prepayments` | [`List[ListSubscriptionGroupPrepayment]`](../../doc/models/list-subscription-group-prepayment.md) | Required | - |

## Example

```python
from advancedbilling.models.list_subscription_group_prepayment import ListSubscriptionGroupPrepayment
from advancedbilling.models.list_subscription_group_prepayment_item import ListSubscriptionGroupPrepaymentItem
from advancedbilling.models.list_subscription_group_prepayment_response import ListSubscriptionGroupPrepaymentResponse

list_subscription_group_prepayment_response = ListSubscriptionGroupPrepaymentResponse(
    prepayments=[
        ListSubscriptionGroupPrepayment(
            prepayment=ListSubscriptionGroupPrepaymentItem(
                id=38,
                subscription_group_uid='subscription_group_uid2',
                amount_in_cents=124,
                remaining_amount_in_cents=182,
                details='details8'
            )
        )
    ]
)
```

