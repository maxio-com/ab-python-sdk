
# Subscription Group Signup Failure Data

## Structure

`SubscriptionGroupSignupFailureData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payer_id` | `int` | Optional | - |
| `payer_reference` | `str` | Optional | - |
| `payment_profile_id` | `int` | Optional | - |
| `payment_collection_method` | `str` | Optional | - |
| `payer_attributes` | [`PayerAttributes`](../../doc/models/payer-attributes.md) | Optional | - |
| `credit_card_attributes` | [`SubscriptionGroupCreditCard`](../../doc/models/subscription-group-credit-card.md) | Optional | - |
| `bank_account_attributes` | [`SubscriptionGroupBankAccount`](../../doc/models/subscription-group-bank-account.md) | Optional | - |
| `subscriptions` | [`List[SubscriptionGroupSignupItem]`](../../doc/models/subscription-group-signup-item.md) | Optional | - |

## Example

```python
from advancedbilling.models.payer_attributes import PayerAttributes
from advancedbilling.models.subscription_group_signup_failure_data import SubscriptionGroupSignupFailureData

subscription_group_signup_failure_data = SubscriptionGroupSignupFailureData(
    payer_id=218,
    payer_reference='payer_reference2',
    payment_profile_id=196,
    payment_collection_method='payment_collection_method0',
    payer_attributes=PayerAttributes(
        first_name='first_name2',
        last_name='last_name0',
        email='email4',
        cc_emails='cc_emails2',
        organization='organization6'
    )
)
```

