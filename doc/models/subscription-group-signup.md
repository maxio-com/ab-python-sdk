
# Subscription Group Signup

## Structure

`SubscriptionGroupSignup`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_profile_id` | `int` | Optional | - |
| `payer_id` | `int` | Optional | - |
| `payer_reference` | `str` | Optional | - |
| `payment_collection_method` | [`CollectionMethod`](../../doc/models/collection-method.md) | Optional | The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options are - `invoice`, `automatic`. For current Relationship Invoicing Architecture valid options are - `remittance`, `automatic`, `prepaid`. |
| `payer_attributes` | [`PayerAttributes`](../../doc/models/payer-attributes.md) | Optional | - |
| `credit_card_attributes` | [`SubscriptionGroupCreditCard`](../../doc/models/subscription-group-credit-card.md) | Optional | - |
| `bank_account_attributes` | [`SubscriptionGroupBankAccount`](../../doc/models/subscription-group-bank-account.md) | Optional | - |
| `subscriptions` | [`List[SubscriptionGroupSignupItem]`](../../doc/models/subscription-group-signup-item.md) | Required | - |

## Example

```python
from advancedbilling.models.collection_method import CollectionMethod
from advancedbilling.models.payer_attributes import PayerAttributes
from advancedbilling.models.subscription_group_signup import SubscriptionGroupSignup
from advancedbilling.models.subscription_group_signup_item import SubscriptionGroupSignupItem

subscription_group_signup = SubscriptionGroupSignup(
    subscriptions=[
        SubscriptionGroupSignupItem(
            product_handle='product_handle8',
            product_id=144,
            product_price_point_id=68,
            product_price_point_handle='product_price_point_handle4',
            offer_id=40,
            metafields={
                'custom_field_name_1': 'custom_field_value_1',
                'custom_field_name_2': 'custom_field_value_2'
            }
        )
    ],
    payment_profile_id=232,
    payer_id=254,
    payer_reference='payer_reference2',
    payment_collection_method=CollectionMethod.PREPAID,
    payer_attributes=PayerAttributes(
        first_name='first_name2',
        last_name='last_name0',
        email='email4',
        cc_emails='cc_emails2',
        organization='organization6'
    )
)
```

