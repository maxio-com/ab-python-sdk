
# Component Price

## Structure

`ComponentPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `component_id` | `int` | Optional | - |
| `starting_quantity` | `int` | Optional | - |
| `ending_quantity` | `int` | Optional | - |
| `unit_price` | `str` | Optional | - |
| `price_point_id` | `int` | Optional | - |
| `formatted_unit_price` | `str` | Optional | - |
| `segment_id` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.component_price import ComponentPrice

component_price = ComponentPrice(
    id=38,
    component_id=148,
    starting_quantity=44,
    ending_quantity=18,
    unit_price='unit_price8'
)
```

