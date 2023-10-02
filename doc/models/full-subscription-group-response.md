
# Full Subscription Group Response

## Structure

`FullSubscriptionGroupResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `scheme` | `int` | Optional | - |
| `customer_id` | `int` | Optional | - |
| `payment_profile_id` | `int` | Optional | - |
| `subscription_ids` | `List[int]` | Optional | - |
| `primary_subscription_id` | `int` | Optional | - |
| `next_assessment_at` | `str` | Optional | - |
| `state` | `str` | Optional | - |
| `cancel_at_end_of_period` | `bool` | Optional | - |
| `current_billing_amount_in_cents` | `int` | Optional | - |
| `customer` | [`SubscriptionGroupCustomer`](../../doc/models/subscription-group-customer.md) | Optional | - |
| `account_balances` | [`SubscriptionGroupBalances`](../../doc/models/subscription-group-balances.md) | Optional | - |

## Example (as JSON)

```json
{
  "uid": "uid8",
  "scheme": 90,
  "customer_id": 110,
  "payment_profile_id": 18,
  "subscription_ids": [
    220,
    221,
    222
  ]
}
```

