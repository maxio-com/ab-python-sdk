
# List Subscription Groups Item

## Structure

`ListSubscriptionGroupsItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `scheme` | `int` | Optional | - |
| `customer_id` | `int` | Optional | - |
| `payment_profile_id` | `int` | Optional | - |
| `subscription_ids` | `List[int]` | Optional | - |
| `primary_subscription_id` | `int` | Optional | - |
| `next_assessment_at` | `datetime` | Optional | - |
| `state` | `str` | Optional | - |
| `cancel_at_end_of_period` | `bool` | Optional | - |
| `account_balances` | [`SubscriptionGroupBalances`](../../doc/models/subscription-group-balances.md) | Optional | - |
| `group_type` | [`GroupType`](../../doc/models/group-type.md) | Optional | - |

## Example

```python
from advancedbilling.models.list_subscription_groups_item import ListSubscriptionGroupsItem

list_subscription_groups_item = ListSubscriptionGroupsItem(
    uid='uid0',
    scheme=62,
    customer_id=82,
    payment_profile_id=246,
    subscription_ids=[
        192,
        193,
        194
    ]
)
```

