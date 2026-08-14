
# Prepaid Usage Allocation Detail

## Structure

`PrepaidUsageAllocationDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allocation_id` | `int` | Optional | - |
| `charge_id` | `int` | Optional | - |
| `usage_quantity` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.prepaid_usage_allocation_detail import PrepaidUsageAllocationDetail

prepaid_usage_allocation_detail = PrepaidUsageAllocationDetail(
    allocation_id=18,
    charge_id=84,
    usage_quantity=10
)
```

