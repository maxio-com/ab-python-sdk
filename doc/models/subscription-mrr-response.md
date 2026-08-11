
# Subscription MRR Response

## Structure

`SubscriptionMRRResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscriptions_mrr` | [`List[SubscriptionMRR]`](../../doc/models/subscription-mrr.md) | Required | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example

```python
from advancedbilling.models.subscription_mrr import SubscriptionMRR
from advancedbilling.models.subscription_mrr_breakout import SubscriptionMRRBreakout
from advancedbilling.models.subscription_mrr_response import SubscriptionMRRResponse

subscription_mrr_response = SubscriptionMRRResponse(
    subscriptions_mrr=[
        SubscriptionMRR(
            subscription_id=0,
            mrr_amount_in_cents=0,
            breakouts=SubscriptionMRRBreakout(
                plan_amount_in_cents=0,
                usage_amount_in_cents=0
            )
        )
    ]
)
```

