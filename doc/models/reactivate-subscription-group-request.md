
# Reactivate Subscription Group Request

## Structure

`ReactivateSubscriptionGroupRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `resume` | `bool` | Optional | - |
| `resume_members` | `bool` | Optional | - |

## Example

```python
from advancedbilling.models.reactivate_subscription_group_request import ReactivateSubscriptionGroupRequest

reactivate_subscription_group_request = ReactivateSubscriptionGroupRequest(
    resume=False,
    resume_members=False
)
```

