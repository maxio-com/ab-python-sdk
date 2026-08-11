
# Debit Note Status

Current status of the debit note.

## Enumeration

`DebitNoteStatus`

## Fields

| Name |
|  --- |
| `OPEN` |
| `APPLIED` |
| `BANISHED` |
| `PAID` |

## Example

```python
from advancedbilling.models.debit_note_status import DebitNoteStatus

debit_note_status = DebitNoteStatus.BANISHED
```

