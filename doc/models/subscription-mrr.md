
# Subscription MRR

## Structure

`SubscriptionMRR`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Required | - |
| `mrr_amount_in_cents` | `int` | Required | - |
| `breakouts` | [`SubscriptionMRRBreakout`](../../doc/models/subscription-mrr-breakout.md) | Optional | - |

## Example

```python
from advancedbilling.models.subscription_mrr import SubscriptionMRR
from advancedbilling.models.subscription_mrr_breakout import SubscriptionMRRBreakout

subscription_mrr = SubscriptionMRR(
    subscription_id=186,
    mrr_amount_in_cents=204,
    breakouts=SubscriptionMRRBreakout(
        plan_amount_in_cents=254,
        usage_amount_in_cents=106
    )
)
```

