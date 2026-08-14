
# Create Subscription Request

## Structure

`CreateSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription` | [`CreateSubscription`](../../doc/models/create-subscription.md) | Required | - |

## Example

```python
from advancedbilling.models.create_subscription import CreateSubscription
from advancedbilling.models.create_subscription_request import CreateSubscriptionRequest
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.subscription_custom_price import SubscriptionCustomPrice

create_subscription_request = CreateSubscriptionRequest(
    subscription=CreateSubscription(
        product_handle='product_handle6',
        product_id=206,
        product_price_point_handle='product_price_point_handle2',
        product_price_point_id=130,
        custom_price=SubscriptionCustomPrice(
            price_in_cents='String3',
            interval='String3',
            interval_unit=IntervalUnit.DAY,
            name='name4',
            handle='handle0',
            trial_price_in_cents='String3',
            trial_interval='String5',
            trial_interval_unit=IntervalUnit.DAY
        ),
        defer_signup=False,
        metafields={
            'custom_field_name_1': 'custom_field_value_1',
            'custom_field_name_2': 'custom_field_value_2'
        },
        dunning_communication_delay_enabled=False,
        dunning_communication_delay_time_zone='"Eastern Time (US & Canada)"'
    )
)
```

