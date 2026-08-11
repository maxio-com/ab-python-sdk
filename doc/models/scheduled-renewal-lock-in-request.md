
# Scheduled Renewal Lock in Request

## Structure

`ScheduledRenewalLockInRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `lock_in_at` | `date` | Required | Date to lock in the renewal. |

## Example

```python
import dateutil.parser

from advancedbilling.models.scheduled_renewal_lock_in_request import ScheduledRenewalLockInRequest

scheduled_renewal_lock_in_request = ScheduledRenewalLockInRequest(
    lock_in_at=dateutil.parser.parse('2016-03-13').date()
)
```

