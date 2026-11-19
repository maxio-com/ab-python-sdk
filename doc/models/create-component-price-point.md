
# Create Component Price Point

## Structure

`CreateComponentPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `handle` | `str` | Optional | - |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Required | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `prices` | [`List[Price]`](../../doc/models/price.md) | Required | - |
| `secondary_pricing` | [`SecondaryPricing`](../../doc/models/secondary-pricing.md) | Optional | Hybrid Pricing only. The secondary pricing model that takes over once usage passes the primary model's included threshold. Applies to Quantity-Based and Metered Components on Sites with Hybrid Pricing enabled; ignored otherwise. Its `prices` brackets start at `1`, not at the primary model's highest `ending_quantity`. See [Hybrid Pricing](page:introduction/basic-concepts/hybrid-pricing). |
| `secondary_pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Optional | Hybrid Pricing only. Alternative to `secondary_pricing.pricing_scheme`; when both are sent, `secondary_pricing.pricing_scheme` is used. Setting not supported when creating price points in bulk. |
| `use_site_exchange_rate` | `bool` | Optional | Whether to use the site level exchange rate or define your own prices for each currency if you have multiple currencies defined on the site. Setting not supported when creating price points in bulk.<br><br>**Default**: `True` |
| `tax_included` | `bool` | Optional | Whether or not the price point includes tax. Setting not supported when creating price points in bulk. |
| `interval` | `int` | Optional | The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this price point would renew every 30 days. This property is only available for sites with Multifrequency enabled. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the interval unit for this price point, either month or day. This property is only available for sites with Multifrequency enabled. |

## Example

```python
from advancedbilling.models.create_component_price_point import CreateComponentPricePoint
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.secondary_pricing import SecondaryPricing

create_component_price_point = CreateComponentPricePoint(
    name='name4',
    pricing_scheme=PricingScheme.STAIRSTEP,
    prices=[
        Price(
            starting_quantity=242,
            unit_price=23.26,
            ending_quantity=40
        )
    ],
    handle='handle0',
    secondary_pricing=SecondaryPricing(
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
        ]
    ),
    secondary_pricing_scheme=PricingScheme.PER_UNIT,
    use_site_exchange_rate=True,
    tax_included=False
)
```

