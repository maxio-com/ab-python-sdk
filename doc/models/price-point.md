
# Price Point

## Structure

`PricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `handle` | `str` | Optional | - |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Optional | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `prices` | [`List[Price]`](../../doc/models/price.md) | Optional | - |
| `use_site_exchange_rate` | `bool` | Optional | Whether to use the site level exchange rate or define your own prices for each currency if you have multiple currencies defined on the site.<br>**Default**: `True` |
| `tax_included` | `bool` | Optional | Whether or not the price point includes tax |
| `interval` | `int` | Optional | The numerical interval. i.e. an interval of ‘30’ coupled with an interval_unit of day would mean this price point would renew every 30 days. This property is only available for sites with Multifrequency enabled. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the interval unit for this price point, either month or day. This property is only available for sites with Multifrequency enabled. |
| `overage_pricing` | [`OveragePricing`](../../doc/models/overage-pricing.md) | Optional | - |
| `rollover_prepaid_remainder` | `bool` | Optional | Boolean which controls whether or not remaining units should be rolled over to the next period |
| `renew_prepaid_allocation` | `bool` | Optional | Boolean which controls whether or not the allocated quantity should be renewed at the beginning of each period |
| `expiration_interval` | `float` | Optional | (only for prepaid usage components where rollover_prepaid_remainder is true) The number of `expiration_interval_unit`s after which rollover amounts should expire |
| `expiration_interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | - |

## Example (as JSON)

```json
{
  "use_site_exchange_rate": true,
  "name": "name0",
  "handle": "handle6",
  "pricing_scheme": "per_unit",
  "prices": [
    {
      "starting_quantity": 242,
      "ending_quantity": 40,
      "unit_price": 23.26
    }
  ]
}
```

