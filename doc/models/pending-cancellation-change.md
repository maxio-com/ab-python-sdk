
# Pending Cancellation Change

## Structure

`PendingCancellationChange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cancellation_state` | `str` | Required | - |
| `cancels_at` | `datetime` | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.pending_cancellation_change import PendingCancellationChange

pending_cancellation_change = PendingCancellationChange(
    cancellation_state='cancellation_state2',
    cancels_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

