
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

## Example

```python
from advancedbilling.models.subscription_group_subscription_error import SubscriptionGroupSubscriptionError

subscription_group_subscription_error = SubscriptionGroupSubscriptionError(
    product=[
        'product1'
    ],
    product_price_point_id=[
        'product_price_point_id7'
    ],
    payment_profile=[
        'payment_profile2'
    ],
    payment_profile_chargify_token=[
        'payment_profile.chargify_token6'
    ],
    base=[
        'base5',
        'base6'
    ]
)
```

