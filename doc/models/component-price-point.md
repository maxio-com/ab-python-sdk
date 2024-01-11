
# Component Price Point

## Structure

`ComponentPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `mtype` | [`PricePointType`](../../doc/models/price-point-type.md) | Optional | Price point type. We expose the following types:<br><br>1. **default**: a price point that is marked as a default price for a certain product.<br>2. **custom**: a custom price point.<br>3. **catalog**: a price point that is **not** marked as a default price for a certain product and is **not** a custom one. |
| `default` | `bool` | Optional | Note: Refer to type attribute instead |
| `name` | `str` | Optional | - |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Optional | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `component_id` | `int` | Optional | - |
| `handle` | `str` | Optional | - |
| `archived_at` | `str` | Optional | - |
| `created_at` | `str` | Optional | - |
| `updated_at` | `str` | Optional | - |
| `prices` | [`List[ComponentPricePointPrice]`](../../doc/models/component-price-point-price.md) | Optional | - |
| `use_site_exchange_rate` | `bool` | Optional | Whether to use the site level exchange rate or define your own prices for each currency if you have multiple currencies defined on the site.<br>**Default**: `True` |
| `subscription_id` | `int` | Optional | (only used for Custom Pricing - ie. when the price point's type is `custom`) The id of the subscription that the custom price point is for. |
| `tax_included` | `bool` | Optional | - |
| `interval` | `int` | Optional | The numerical interval. i.e. an interval of ‘30’ coupled with an interval_unit of day would mean this component price point would renew every 30 days. This property is only available for sites with Multifrequency enabled. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the interval unit for this component price point, either month or day. This property is only available for sites with Multifrequency enabled. |

## Example (as JSON)

```json
{
  "use_site_exchange_rate": true,
  "id": 190,
  "type": "custom",
  "default": false,
  "name": "name2",
  "pricing_scheme": "stairstep"
}
```

