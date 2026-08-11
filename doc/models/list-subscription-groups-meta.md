
# List Subscription Groups Meta

## Structure

`ListSubscriptionGroupsMeta`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `current_page` | `int` | Optional | - |
| `total_count` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.list_subscription_groups_meta import ListSubscriptionGroupsMeta

list_subscription_groups_meta = ListSubscriptionGroupsMeta(
    current_page=110,
    total_count=134
)
```

