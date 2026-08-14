
# Update Allocation Expiration Date

## Structure

`UpdateAllocationExpirationDate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allocation` | [`AllocationExpirationDate`](../../doc/models/allocation-expiration-date.md) | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.allocation_expiration_date import AllocationExpirationDate
from advancedbilling.models.update_allocation_expiration_date import UpdateAllocationExpirationDate

update_allocation_expiration_date = UpdateAllocationExpirationDate(
    allocation=AllocationExpirationDate(
        expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

