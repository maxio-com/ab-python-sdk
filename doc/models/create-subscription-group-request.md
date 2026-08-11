
# Create Subscription Group Request

## Structure

`CreateSubscriptionGroupRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_group` | [`CreateSubscriptionGroup`](../../doc/models/create-subscription-group.md) | Required | - |

## Example

```python
from advancedbilling.models.create_subscription_group import CreateSubscriptionGroup
from advancedbilling.models.create_subscription_group_request import CreateSubscriptionGroupRequest

create_subscription_group_request = CreateSubscriptionGroupRequest(
    subscription_group=CreateSubscriptionGroup(
        subscription_id=36,
        member_ids=[
            164,
            165
        ]
    )
)
```

