
# Subscription Group Signup Error

## Structure

`SubscriptionGroupSignupError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscriptions` | [`Dict[str, SubscriptionGroupSubscriptionError]`](../../doc/models/subscription-group-subscription-error.md) | Optional | Object that as key have subscription position in request subscriptions array and as value subscription errors object. |
| `payer_reference` | `str` | Optional | - |
| `payer` | [`PayerError`](../../doc/models/payer-error.md) | Optional | - |
| `subscription_group` | `List[str]` | Optional | - |
| `payment_profile_id` | `str` | Optional | - |
| `payer_id` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.payer_error import PayerError
from advancedbilling.models.subscription_group_signup_error import SubscriptionGroupSignupError
from advancedbilling.models.subscription_group_subscription_error import SubscriptionGroupSubscriptionError

subscription_group_signup_error = SubscriptionGroupSignupError(
    subscriptions={
        'key0': SubscriptionGroupSubscriptionError(
            product=[
                'product9'
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
        ),
        'key1': SubscriptionGroupSubscriptionError(
            product=[
                'product9'
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
    },
    payer_reference='payer_reference6',
    payer=PayerError(
        last_name=[
            'last_name5',
            'last_name6'
        ],
        first_name=[
            'first_name8'
        ],
        email=[
            'email0',
            'email9'
        ]
    ),
    subscription_group=[
        'subscription_group7',
        'subscription_group8'
    ],
    payment_profile_id='payment_profile_id8'
)
```

