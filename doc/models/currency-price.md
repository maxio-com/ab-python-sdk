
# Currency Price

## Structure

`CurrencyPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `currency` | `str` | Optional | - |
| `price` | `float` | Optional | - |
| `formatted_price` | `str` | Optional | - |
| `product_price_point_id` | `int` | Optional | - |
| `role` | [`CurrencyPriceRole`](../../doc/models/currency-price-role.md) | Optional | Role for the price. |

## Example (as JSON)

```json
{
  "id": 88,
  "currency": "currency6",
  "price": 41.36,
  "formatted_price": "formatted_price4",
  "product_price_point_id": 210
}
```

