
# Offer Item

## Structure

`OfferItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Optional | - |
| `price_point_id` | `int` | Optional | - |
| `starting_quantity` | `str` | Optional | - |
| `editable` | `bool` | Optional | - |
| `component_unit_price` | `str` | Optional | - |
| `component_name` | `str` | Optional | - |
| `price_point_name` | `str` | Optional | - |
| `currency_prices` | [`List[CurrencyPrice]`](../../doc/models/currency-price.md) | Optional | - |
| `interval` | `int` | Optional | The numerical interval. i.e. an interval of '30' coupled with an interval_unit of day would mean this component price point would renew every 30 days. This property is only available for sites with Multifrequency enabled. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the interval unit for this component price point, either month or day. This property is only available for sites with Multifrequency enabled. |

## Example (as JSON)

```json
{
  "component_id": 216,
  "price_point_id": 16,
  "starting_quantity": "starting_quantity0",
  "editable": false,
  "component_unit_price": "component_unit_price8"
}
```

