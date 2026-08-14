
# Subscription Group Signup Component

## Structure

`SubscriptionGroupSignupComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `allocated_quantity` | str \| int \| None | Optional | This is a container for one-of cases. |
| `unit_balance` | str \| int \| None | Optional | This is a container for one-of cases. |
| `price_point_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `custom_price` | [`SubscriptionGroupComponentCustomPrice`](../../doc/models/subscription-group-component-custom-price.md) | Optional | Used in place of `price_point_id` to define a custom price point unique to the subscription. You still need to provide `component_id`. |

## Example

```python
from advancedbilling.models.component_custom_price import ComponentCustomPrice
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.subscription_group_component_custom_price import SubscriptionGroupComponentCustomPrice
from advancedbilling.models.subscription_group_signup_component import SubscriptionGroupSignupComponent

subscription_group_signup_component = SubscriptionGroupSignupComponent(
    component_id='String9',
    allocated_quantity='String3',
    unit_balance='String7',
    price_point_id='String9',
    custom_price=SubscriptionGroupComponentCustomPrice(
        pricing_scheme=PricingScheme.STAIRSTEP,
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
        overage_pricing=[
            ComponentCustomPrice(
                prices=[
                    Price(
                        starting_quantity=242,
                        unit_price=23.26,
                        ending_quantity=40
                    )
                ],
                tax_included=False,
                pricing_scheme=PricingScheme.STAIRSTEP,
                interval=230,
                interval_unit=IntervalUnit.DAY,
                list_price_point_id=10
            ),
            ComponentCustomPrice(
                prices=[
                    Price(
                        starting_quantity=242,
                        unit_price=23.26,
                        ending_quantity=40
                    )
                ],
                tax_included=False,
                pricing_scheme=PricingScheme.STAIRSTEP,
                interval=230,
                interval_unit=IntervalUnit.DAY,
                list_price_point_id=10
            ),
            ComponentCustomPrice(
                prices=[
                    Price(
                        starting_quantity=242,
                        unit_price=23.26,
                        ending_quantity=40
                    )
                ],
                tax_included=False,
                pricing_scheme=PricingScheme.STAIRSTEP,
                interval=230,
                interval_unit=IntervalUnit.DAY,
                list_price_point_id=10
            )
        ]
    )
)
```

