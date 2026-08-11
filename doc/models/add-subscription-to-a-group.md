
# Add Subscription to a Group

## Structure

`AddSubscriptionToAGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group` | [`GroupSettings`](../../doc/models/group-settings.md) | Optional | - |

## Example

```python
from advancedbilling.models.add_subscription_to_a_group import AddSubscriptionToAGroup
from advancedbilling.models.group_billing import GroupBilling
from advancedbilling.models.group_settings import GroupSettings
from advancedbilling.models.group_target import GroupTarget
from advancedbilling.models.group_target_type import GroupTargetType

add_subscription_to_a_group = AddSubscriptionToAGroup(
    group=GroupSettings(
        target=GroupTarget(
            mtype=GroupTargetType.PARENT,
            id=236
        ),
        billing=GroupBilling(
            accrue=False,
            align_date=False,
            prorate=False
        )
    )
)
```

