
# Allocation Expiration Date

## Structure

`AllocationExpirationDate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expires_at` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.allocation_expiration_date import AllocationExpirationDate

allocation_expiration_date = AllocationExpirationDate(
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

