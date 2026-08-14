
# Create Subscription Group

## Structure

`CreateSubscriptionGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Required | - |
| `member_ids` | `List[int]` | Optional | - |

## Example

```python
from advancedbilling.models.create_subscription_group import CreateSubscriptionGroup

create_subscription_group = CreateSubscriptionGroup(
    subscription_id=130,
    member_ids=[
        230
    ]
)
```

