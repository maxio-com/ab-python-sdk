
# Update Component Price Point

## Structure

`UpdateComponentPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `handle` | `str` | Optional | - |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Optional | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `use_site_exchange_rate` | `bool` | Optional | Whether to use the site level exchange rate or define your own prices for each currency if you have multiple currencies defined on the site. |
| `tax_included` | `bool` | Optional | Whether or not the price point includes tax |
| `interval` | `int` | Optional | The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this component price point would renew every 30 days. This property is only available for sites with Multifrequency enabled. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the interval unit for this component price point, either month or day. This property is only available for sites with Multifrequency enabled. |
| `prices` | [`List[UpdatePrice]`](../../doc/models/update-price.md) | Optional | - |

## Example

```python
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.update_component_price_point import UpdateComponentPricePoint

update_component_price_point = UpdateComponentPricePoint(
    name='name2',
    handle='handle8',
    pricing_scheme=PricingScheme.PER_UNIT,
    use_site_exchange_rate=False,
    tax_included=False
)
```

