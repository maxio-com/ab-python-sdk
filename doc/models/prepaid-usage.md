
# Prepaid Usage

## Structure

`PrepaidUsage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `previous_unit_balance` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `previous_overage_unit_balance` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `new_unit_balance` | int \| str | Required | This is a container for one-of cases. |
| `new_overage_unit_balance` | int \| str | Required | This is a container for one-of cases. |
| `usage_quantity` | `int` | Required | - |
| `overage_usage_quantity` | `int` | Required | - |
| `component_id` | `int` | Required | - |
| `component_handle` | `str` | Required | - |
| `memo` | `str` | Required | - |
| `allocation_details` | [`List[PrepaidUsageAllocationDetail]`](../../doc/models/prepaid-usage-allocation-detail.md) | Required | - |

## Example

```python
from advancedbilling.models.prepaid_usage import PrepaidUsage
from advancedbilling.models.prepaid_usage_allocation_detail import PrepaidUsageAllocationDetail

prepaid_usage = PrepaidUsage(
    previous_unit_balance='previous_unit_balance2',
    previous_overage_unit_balance='previous_overage_unit_balance2',
    new_unit_balance=180,
    new_overage_unit_balance=204,
    usage_quantity=220,
    overage_usage_quantity=144,
    component_id=182,
    component_handle='component_handle2',
    memo='memo6',
    allocation_details=[
        PrepaidUsageAllocationDetail(
            allocation_id=18,
            charge_id=84,
            usage_quantity=10
        )
    ]
)
```

