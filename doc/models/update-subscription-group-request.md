
# Update Subscription Group Request

## Structure

`UpdateSubscriptionGroupRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_group` | [`UpdateSubscriptionGroup`](../../doc/models/update-subscription-group.md) | Required | - |

## Example

```python
from advancedbilling.models.update_subscription_group import UpdateSubscriptionGroup
from advancedbilling.models.update_subscription_group_request import UpdateSubscriptionGroupRequest

update_subscription_group_request = UpdateSubscriptionGroupRequest(
    subscription_group=UpdateSubscriptionGroup(
        member_ids=[
            164,
            165
        ]
    )
)
```

