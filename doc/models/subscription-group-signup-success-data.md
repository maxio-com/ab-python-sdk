
# Subscription Group Signup Success Data

## Structure

`SubscriptionGroupSignupSuccessData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Required | - |
| `scheme` | `int` | Required | - |
| `customer_id` | `int` | Required | - |
| `payment_profile_id` | `int` | Required | - |
| `subscription_ids` | `List[int]` | Required | - |
| `primary_subscription_id` | `int` | Required | - |
| `next_assessment_at` | `str` | Required | - |
| `state` | `str` | Required | - |
| `cancel_at_end_of_period` | `bool` | Required | - |

## Example (as JSON)

```json
{
  "uid": "uid8",
  "scheme": 154,
  "customer_id": 174,
  "payment_profile_id": 82,
  "subscription_ids": [
    28,
    29
  ],
  "primary_subscription_id": 102,
  "next_assessment_at": "next_assessment_at2",
  "state": "state4",
  "cancel_at_end_of_period": false
}
```

