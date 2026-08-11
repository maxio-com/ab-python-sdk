
# Component Price Point Error Item

## Structure

`ComponentPricePointErrorItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Optional | - |
| `message` | `str` | Optional | - |
| `price_point` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.component_price_point_error_item import ComponentPricePointErrorItem

component_price_point_error_item = ComponentPricePointErrorItem(
    component_id=152,
    message='message0',
    price_point=50
)
```

