
# Component Allocation Error Item

## Structure

`ComponentAllocationErrorItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Optional | - |
| `message` | `str` | Optional | - |
| `kind` | `str` | Optional | - |
| `on` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.component_allocation_error_item import ComponentAllocationErrorItem

component_allocation_error_item = ComponentAllocationErrorItem(
    component_id=238,
    message='message8',
    kind='kind6',
    on='on8'
)
```

