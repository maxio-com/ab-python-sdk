
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
| `secondary_pricing` | [`UpdateSecondaryPricing`](../../doc/models/update-secondary-pricing.md) | Optional | Hybrid Pricing only. Changes the secondary pricing model of an existing hybrid price point. Send `pricing_scheme` (or the top-level `secondary_pricing_scheme`) every time you send this block; a block without a scheme returns `422`. Brackets sent without an `id` are added to the existing ones rather than replacing them, so to change a bracket set, update existing brackets by `id` and remove the ones you no longer want with `_destroy: true`. See [Hybrid Pricing](page:introduction/basic-concepts/hybrid-pricing). |
| `secondary_pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Optional | Hybrid Pricing only. Alternative to `secondary_pricing.pricing_scheme`; when both are sent, `secondary_pricing.pricing_scheme` is used. |

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

