
# Group Settings

## Structure

`GroupSettings`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `target` | [`GroupTarget`](../../doc/models/group-target.md) | Required | Attributes of the target customer who will be the responsible payer of the created subscription. Required. |
| `billing` | [`GroupBilling`](../../doc/models/group-billing.md) | Optional | (Optional) Attributes related to billing date and accrual. Note: Only applicable for new subscriptions. |

## Example

```python
from advancedbilling.models.group_billing import GroupBilling
from advancedbilling.models.group_settings import GroupSettings
from advancedbilling.models.group_target import GroupTarget
from advancedbilling.models.group_target_type import GroupTargetType

group_settings = GroupSettings(
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
```

