
# Subscription Group Members Array Error

## Structure

`SubscriptionGroupMembersArrayError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `members` | `List[str]` | Required | - |

## Example

```python
from advancedbilling.models.subscription_group_members_array_error import SubscriptionGroupMembersArrayError

subscription_group_members_array_error = SubscriptionGroupMembersArrayError(
    members=[
        'members2'
    ]
)
```

