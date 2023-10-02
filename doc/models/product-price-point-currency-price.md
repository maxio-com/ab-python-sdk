
# Product Price Point Currency Price

object Product Price Point Currency Price:

## Structure

`ProductPricePointCurrencyPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `currency` | `str` | Optional | - |
| `price` | `int` | Optional | - |
| `formatted_price` | `str` | Optional | - |
| `product_price_point_id` | `int` | Optional | - |
| `role` | [`CurrencyPriceRoleEnum`](../../doc/models/currency-price-role-enum.md) | Optional | Role for the price. |

## Example (as JSON)

```json
{
  "id": 254,
  "currency": "currency2",
  "price": 130,
  "formatted_price": "formatted_price0",
  "product_price_point_id": 120
}
```

