
# Cancel Grouped Subscriptions Request

## Structure

`CancelGroupedSubscriptionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `charge_unbilled_usage` | `bool` | Optional | - |

## Example

```python
from advancedbilling.models.cancel_grouped_subscriptions_request import CancelGroupedSubscriptionsRequest

cancel_grouped_subscriptions_request = CancelGroupedSubscriptionsRequest(
    charge_unbilled_usage=False
)
```

