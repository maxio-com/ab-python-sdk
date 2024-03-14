
# List Subscription Groups Item

## Structure

`ListSubscriptionGroupsItem`

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
| `account_balances` | [`SubscriptionGroupBalances`](../../doc/models/subscription-group-balances.md) | Optional | - |
| `group_type` | [`GroupType`](../../doc/models/group-type.md) | Optional | - |

## Example (as JSON)

```json
{
  "uid": "uid0",
  "scheme": 124,
  "customer_id": 144,
  "payment_profile_id": 52,
  "subscription_ids": [
    254
  ]
}
```

