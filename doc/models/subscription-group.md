
# Subscription Group

## Structure

`SubscriptionGroup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `customer_id` | `int` | Optional | - |
| `payment_profile` | [`SubscriptionGroupPaymentProfile`](../../doc/models/subscription-group-payment-profile.md) | Optional | - |
| `payment_collection_method` | [`CollectionMethod`](../../doc/models/collection-method.md) | Optional | The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options are - `invoice`, `automatic`. For current Relationship Invoicing Architecture valid options are - `remittance`, `automatic`, `prepaid`. |
| `subscription_ids` | `List[int]` | Optional | - |
| `created_at` | `datetime` | Optional | - |

## Example

```python
from advancedbilling.models.collection_method import CollectionMethod
from advancedbilling.models.subscription_group import SubscriptionGroup
from advancedbilling.models.subscription_group_payment_profile import SubscriptionGroupPaymentProfile

subscription_group = SubscriptionGroup(
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
```

