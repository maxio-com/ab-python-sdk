
# Subscription Group Subscription Error

Object which contains subscription errors.

## Structure

`SubscriptionGroupSubscriptionError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product` | `List[str]` | Optional | - |
| `product_price_point_id` | `List[str]` | Optional | - |
| `payment_profile` | `List[str]` | Optional | - |
| `payment_profile_chargify_token` | `List[str]` | Optional | - |
| `base` | `List[str]` | Optional | - |
| `payment_profile_expiration_month` | `List[str]` | Optional | - |
| `payment_profile_expiration_year` | `List[str]` | Optional | - |
| `payment_profile_full_number` | `List[str]` | Optional | - |

## Example (as JSON)

```json
{
  "product": [
    "product7",
    "product6"
  ],
  "product_price_point_id": [
    "product_price_point_id9",
    "product_price_point_id0"
  ],
  "payment_profile": [
    "payment_profile4",
    "payment_profile5"
  ],
  "payment_profile.chargify_token": [
    "payment_profile.chargify_token8",
    "payment_profile.chargify_token9"
  ],
  "base": [
    "base7",
    "base8",
    "base9"
  ]
}
```

