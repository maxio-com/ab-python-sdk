
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

