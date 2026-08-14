
# List Subscription Group Prepayment Item

## Structure

`ListSubscriptionGroupPrepaymentItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `subscription_group_uid` | `str` | Optional | - |
| `amount_in_cents` | `int` | Optional | - |
| `remaining_amount_in_cents` | `int` | Optional | - |
| `details` | `str` | Optional | - |
| `external` | `bool` | Optional | - |
| `memo` | `str` | Optional | - |
| `payment_type` | [`PrepaymentMethod`](../../doc/models/prepayment-method.md) | Optional | - |
| `created_at` | `datetime` | Optional | - |

## Example

```python
from advancedbilling.models.list_subscription_group_prepayment_item import ListSubscriptionGroupPrepaymentItem

list_subscription_group_prepayment_item = ListSubscriptionGroupPrepaymentItem(
    id=96,
    subscription_group_uid='subscription_group_uid6',
    amount_in_cents=74,
    remaining_amount_in_cents=240,
    details='details2'
)
```

