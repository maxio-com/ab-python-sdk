
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
| `allocated_quantity` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "previous_allocation": 94,
  "new_allocation": 102,
  "component_id": 88,
  "component_handle": "component_handle8",
  "memo": "memo2",
  "allocation_id": 158,
  "allocated_quantity": 182
}
```

