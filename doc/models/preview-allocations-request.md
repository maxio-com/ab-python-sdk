
# Preview Allocations Request

## Structure

`PreviewAllocationsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allocations` | [`List[CreateAllocation]`](../../doc/models/create-allocation.md) | Required | - |
| `effective_proration_date` | `date` | Optional | To calculate proration amounts for a future time. Only within a current subscription period. Only ISO8601 format is supported. |
| `upgrade_charge` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided. |
| `downgrade_credit` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided. |

## Example

```python
import dateutil.parser

from advancedbilling.models.create_allocation import CreateAllocation
from advancedbilling.models.credit_type import CreditType
from advancedbilling.models.preview_allocations_request import PreviewAllocationsRequest

preview_allocations_request = PreviewAllocationsRequest(
    allocations=[
        CreateAllocation(
            quantity=26.48,
            decimal_quantity='decimal_quantity8',
            previous_quantity=55.5,
            decimal_previous_quantity='decimal_previous_quantity2',
            component_id=242,
            memo='memo6'
        )
    ],
    effective_proration_date=dateutil.parser.parse('2023-12-01').date(),
    upgrade_charge=CreditType.FULL,
    downgrade_credit=CreditType.FULL
)
```

