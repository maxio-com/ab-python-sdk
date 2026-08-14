
# Component Allocation Change

## Structure

`ComponentAllocationChange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `previous_allocation` | `int` | Required | - |
| `new_allocation` | `int` | Required | - |
| `component_id` | `int` | Required | - |
| `component_handle` | `str` | Required | - |
| `memo` | `str` | Required | - |
| `allocation_id` | `int` | Required | - |
| `allocated_quantity` | int \| str \| None | Optional | This is a container for one-of cases. |

## Example

```python
from advancedbilling.models.component_allocation_change import ComponentAllocationChange

component_allocation_change = ComponentAllocationChange(
    previous_allocation=124,
    new_allocation=72,
    component_id=118,
    component_handle='component_handle0',
    memo='memo4',
    allocation_id=128,
    allocated_quantity=134
)
```

