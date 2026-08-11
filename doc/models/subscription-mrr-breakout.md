
# Subscription MRR Breakout

## Structure

`SubscriptionMRRBreakout`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_amount_in_cents` | `int` | Required | - |
| `usage_amount_in_cents` | `int` | Required | - |

## Example

```python
from advancedbilling.models.subscription_mrr_breakout import SubscriptionMRRBreakout

subscription_mrr_breakout = SubscriptionMRRBreakout(
    plan_amount_in_cents=214,
    usage_amount_in_cents=66
)
```

