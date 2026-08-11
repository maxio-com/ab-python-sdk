
# Allocation Response

## Structure

`AllocationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allocation` | [`Allocation`](../../doc/models/allocation.md) | Optional | - |

## Example

```python
from advancedbilling.models.allocation import Allocation
from advancedbilling.models.allocation_response import AllocationResponse

allocation_response = AllocationResponse(
    allocation=Allocation(
        allocation_id=238,
        component_id=8,
        component_handle='component_handle8',
        subscription_id=8,
        quantity=32
    )
)
```

