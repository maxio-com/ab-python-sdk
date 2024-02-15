
# Reactivate Subscription Group Response

## Structure

`ReactivateSubscriptionGroupResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `scheme` | `int` | Optional | - |
| `customer_id` | `int` | Optional | - |
| `payment_profile_id` | `int` | Optional | - |
| `subscription_ids` | `List[int]` | Optional | - |
| `primary_subscription_id` | `int` | Optional | - |
| `next_assessment_at` | `datetime` | Optional | - |
| `state` | `str` | Optional | - |
| `cancel_at_end_of_period` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "uid": "uid4",
  "scheme": 66,
  "customer_id": 86,
  "payment_profile_id": 250,
  "subscription_ids": [
    196,
    197
  ]
}
```

