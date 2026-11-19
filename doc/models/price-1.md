
# Price 1

## Structure

`Price1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `starting_quantity` | `int` | Optional | - |
| `ending_quantity` | `int` | Optional | - |
| `unit_price` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.price_1 import Price1

price_1 = Price1(
    starting_quantity=20,
    ending_quantity=250,
    unit_price='unit_price2'
)
```

