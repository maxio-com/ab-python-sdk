
# Subscription Response

## Structure

`SubscriptionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription` | [`Subscription`](../../doc/models/subscription.md) | Optional | - |

## Example

```python
from advancedbilling.models.subscription import Subscription
from advancedbilling.models.subscription_response import SubscriptionResponse
from advancedbilling.models.subscription_state import SubscriptionState

subscription_response = SubscriptionResponse(
    subscription=Subscription(
        id=8,
        state=SubscriptionState.PAUSED,
        balance_in_cents=124,
        total_revenue_in_cents=48,
        product_price_in_cents=238
    )
)
```

