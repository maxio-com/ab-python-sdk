
# Component Price Point Assignment

## Structure

`ComponentPricePointAssignment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Optional | - |
| `price_point` | str \| int \| None | Optional | This is a container for one-of cases. |

## Example

```python
from advancedbilling.models.component_price_point_assignment import ComponentPricePointAssignment

component_price_point_assignment = ComponentPricePointAssignment(
    component_id=122,
    price_point='String5'
)
```

