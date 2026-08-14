
# Subscription Group Component Custom Price

Used in place of `price_point_id` to define a custom price point unique to the subscription. You still need to provide `component_id`.

## Structure

`SubscriptionGroupComponentCustomPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Optional | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `prices` | [`List[Price]`](../../doc/models/price.md) | Optional | - |
| `overage_pricing` | [`List[ComponentCustomPrice]`](../../doc/models/component-custom-price.md) | Optional | - |

## Example

```python
from advancedbilling.models.component_custom_price import ComponentCustomPrice
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.subscription_group_component_custom_price import SubscriptionGroupComponentCustomPrice

subscription_group_component_custom_price = SubscriptionGroupComponentCustomPrice(
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
        )
    ]
)
```

