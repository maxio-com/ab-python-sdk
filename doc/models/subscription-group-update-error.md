
# Subscription Group Update Error

## Structure

`SubscriptionGroupUpdateError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `members` | `List[str]` | Optional | - |

## Example

```python
from advancedbilling.models.subscription_group_update_error import SubscriptionGroupUpdateError

subscription_group_update_error = SubscriptionGroupUpdateError(
    members=[
        'members6',
        'members5',
        'members4'
    ]
)
```

