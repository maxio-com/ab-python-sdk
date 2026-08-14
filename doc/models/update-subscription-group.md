
# Update Subscription Group

## Structure

`UpdateSubscriptionGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `member_ids` | `List[int]` | Optional | - |

## Example

```python
from advancedbilling.models.update_subscription_group import UpdateSubscriptionGroup

update_subscription_group = UpdateSubscriptionGroup(
    member_ids=[
        54,
        55
    ]
)
```

