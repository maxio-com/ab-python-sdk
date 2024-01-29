
# Subscription Group Signup Response

## Structure

`SubscriptionGroupSignupResponse`

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
| `subscriptions` | [`List[SubscriptionGroupItem]`](../../doc/models/subscription-group-item.md) | Optional | - |
| `payment_collection_method` | [`CollectionMethod`](../../doc/models/collection-method.md) | Optional | The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options are - `invoice`, `automatic`. For current Relationship Invoicing Architecture valid options are - `remittance`, `automatic`, `prepaid`.<br>**Default**: `'automatic'` |

## Example (as JSON)

```json
{
  "payment_collection_method": "automatic",
  "uid": "uid8",
  "scheme": 28,
  "customer_id": 48,
  "payment_profile_id": 44,
  "subscription_ids": [
    158,
    159,
    160
  ]
}
```

