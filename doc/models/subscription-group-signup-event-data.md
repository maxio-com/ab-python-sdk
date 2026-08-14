
# Subscription Group Signup Event Data

## Structure

`SubscriptionGroupSignupEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_group` | [`SubscriptionGroupSignupFailureData`](../../doc/models/subscription-group-signup-failure-data.md) | Required | - |
| `customer` | [`Customer`](../../doc/models/customer.md) | Required | - |

## Example

```python
from advancedbilling.models.customer import Customer
from advancedbilling.models.payer_attributes import PayerAttributes
from advancedbilling.models.subscription_group_signup_event_data import SubscriptionGroupSignupEventData
from advancedbilling.models.subscription_group_signup_failure_data import SubscriptionGroupSignupFailureData

subscription_group_signup_event_data = SubscriptionGroupSignupEventData(
    subscription_group=SubscriptionGroupSignupFailureData(
        payer_id=150,
        payer_reference='payer_reference6',
        payment_profile_id=128,
        payment_collection_method='payment_collection_method8',
        payer_attributes=PayerAttributes(
            first_name='first_name2',
            last_name='last_name0',
            email='email4',
            cc_emails='cc_emails2',
            organization='organization6'
        )
    ),
    customer=Customer(
        first_name='first_name0',
        last_name='last_name8',
        email='email6',
        cc_emails='cc_emails0',
        organization='organization6'
    )
)
```

