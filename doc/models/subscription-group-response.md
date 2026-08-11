
# Subscription Group Response

## Structure

`SubscriptionGroupResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_group` | [`SubscriptionGroup`](../../doc/models/subscription-group.md) | Required | - |

## Example

```python
from advancedbilling.models.collection_method import CollectionMethod
from advancedbilling.models.subscription_group import SubscriptionGroup
from advancedbilling.models.subscription_group_payment_profile import SubscriptionGroupPaymentProfile
from advancedbilling.models.subscription_group_response import SubscriptionGroupResponse

subscription_group_response = SubscriptionGroupResponse(
    subscription_group=SubscriptionGroup(
        uid='uid8',
        customer_id=220,
        payment_profile=SubscriptionGroupPaymentProfile(
            id=44,
            first_name='first_name4',
            last_name='last_name2',
            masked_card_number='masked_card_number2'
        ),
        payment_collection_method=CollectionMethod.PREPAID,
        subscription_ids=[
            74,
            75
        ]
    )
)
```

