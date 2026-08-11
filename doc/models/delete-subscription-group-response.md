
# Delete Subscription Group Response

## Structure

`DeleteSubscriptionGroupResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `deleted` | `bool` | Optional | - |

## Example

```python
from advancedbilling.models.delete_subscription_group_response import DeleteSubscriptionGroupResponse

delete_subscription_group_response = DeleteSubscriptionGroupResponse(
    uid='uid8',
    deleted=False
)
```

