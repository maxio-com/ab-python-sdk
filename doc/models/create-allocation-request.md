
# Create Allocation Request

## Structure

`CreateAllocationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allocation` | [`CreateAllocation`](../../doc/models/create-allocation.md) | Required | - |

## Example

```python
from advancedbilling.models.create_allocation import CreateAllocation
from advancedbilling.models.create_allocation_request import CreateAllocationRequest

create_allocation_request = CreateAllocationRequest(
    allocation=CreateAllocation(
        quantity=228.94,
        decimal_quantity='decimal_quantity6',
        previous_quantity=254.04,
        decimal_previous_quantity='decimal_previous_quantity8',
        component_id=8,
        memo='memo2'
    )
)
```

