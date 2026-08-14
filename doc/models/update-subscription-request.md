
# Update Subscription Request

## Structure

`UpdateSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription` | [`UpdateSubscription`](../../doc/models/update-subscription.md) | Required | - |

## Example

```python
from advancedbilling.models.credit_card_attributes import CreditCardAttributes
from advancedbilling.models.update_subscription import UpdateSubscription
from advancedbilling.models.update_subscription_request import UpdateSubscriptionRequest

update_subscription_request = UpdateSubscriptionRequest(
    subscription=UpdateSubscription(
        credit_card_attributes=CreditCardAttributes(
            full_number='full_number2',
            expiration_month='expiration_month6',
            expiration_year='expiration_year2'
        ),
        product_handle='product_handle6',
        product_id=206,
        product_change_delayed=False,
        next_product_id='next_product_id6',
        defer_signup=False,
        dunning_communication_delay_time_zone='"Eastern Time (US & Canada)"'
    )
)
```

