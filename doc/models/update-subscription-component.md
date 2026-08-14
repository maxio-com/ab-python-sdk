
# Update Subscription Component

## Structure

`UpdateSubscriptionComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Optional | - |
| `custom_price` | [`ComponentCustomPrice`](../../doc/models/component-custom-price.md) | Optional | Create or update custom pricing unique to the subscription. Used in place of `price_point_id`. |

## Example

```python
from advancedbilling.models.component_custom_price import ComponentCustomPrice
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.update_subscription_component import UpdateSubscriptionComponent

update_subscription_component = UpdateSubscriptionComponent(
    component_id=76,
    custom_price=ComponentCustomPrice(
        prices=[
            Price(
                starting_quantity=242,
                unit_price=23.26,
                ending_quantity=40
            ),
            Price(
                starting_quantity=242,
                unit_price=23.26,
                ending_quantity=40
            )
        ],
        tax_included=False,
        pricing_scheme=PricingScheme.STAIRSTEP,
        interval=66,
        interval_unit=IntervalUnit.DAY,
        list_price_point_id=174
    )
)
```

