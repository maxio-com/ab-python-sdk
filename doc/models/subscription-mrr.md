
# Subscription MRR

## Structure

`SubscriptionMRR`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Required | - |
| `mrr_amount_in_cents` | `int` | Required | - |
| `breakouts` | [`SubscriptionMRRBreakout`](../../doc/models/subscription-mrr-breakout.md) | Optional | - |

## Example (as JSON)

```json
{
  "subscription_id": 4,
  "mrr_amount_in_cents": 22,
  "breakouts": {
    "plan_amount_in_cents": 254,
    "usage_amount_in_cents": 106
  }
}
```

