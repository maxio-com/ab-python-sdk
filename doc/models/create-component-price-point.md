
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
| `use_site_exchange_rate` | `bool` | Optional | Whether to use the site level exchange rate or define your own prices for each currency if you have multiple currencies defined on the site. Setting not supported when creating price points in bulk.<br><br>**Default**: `True` |
| `tax_included` | `bool` | Optional | Whether or not the price point includes tax. Setting not supported when creating price points in bulk. |
| `interval` | `int` | Optional | The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this price point would renew every 30 days. This property is only available for sites with Multifrequency enabled. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the interval unit for this price point, either month or day. This property is only available for sites with Multifrequency enabled. |

## Example

```python
from advancedbilling.models.create_component_price_point import CreateComponentPricePoint
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme

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
    use_site_exchange_rate=True,
    tax_included=False,
    interval=70,
    interval_unit=IntervalUnit.DAY
)
```

