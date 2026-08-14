
# Component Currency Price

## Structure

`ComponentCurrencyPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `currency` | `str` | Optional | - |
| `price` | `str` | Optional | - |
| `formatted_price` | `str` | Optional | - |
| `price_id` | `int` | Optional | - |
| `price_point_id` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.component_currency_price import ComponentCurrencyPrice

component_currency_price = ComponentCurrencyPrice(
    id=170,
    currency='currency2',
    price='price4',
    formatted_price='formatted_price6',
    price_id=252
)
```

