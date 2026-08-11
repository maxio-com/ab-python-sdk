
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
| `price_id` | `int` | Optional | - |
| `price_point_id` | `int` | Optional | - |
| `product_price_point_id` | `int` | Optional | - |
| `role` | [`CurrencyPriceRole`](../../doc/models/currency-price-role.md) | Optional | Role for the price. |

## Example

```python
from advancedbilling.models.currency_price import CurrencyPrice

currency_price = CurrencyPrice(
    id=254,
    currency='currency6',
    price=247.06,
    formatted_price='formatted_price4',
    price_id=168
)
```

