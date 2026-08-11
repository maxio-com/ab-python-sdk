
# Price

## Structure

`Price`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `starting_quantity` | int \| str | Required | This is a container for one-of cases. |
| `ending_quantity` | int \| str \| None | Optional | This is a container for one-of cases. |
| `unit_price` | float \| str | Required | This is a container for one-of cases. |

## Example

```python
from advancedbilling.models.price import Price

price = Price(
    starting_quantity=132,
    unit_price=70.44,
    ending_quantity=6
)
```

