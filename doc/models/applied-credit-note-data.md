
# Applied Credit Note Data

## Structure

`AppliedCreditNoteData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | The UID of the credit note |
| `number` | `str` | Optional | The number of the credit note |

## Example

```python
from advancedbilling.models.applied_credit_note_data import AppliedCreditNoteData

applied_credit_note_data = AppliedCreditNoteData(
    uid='uid2',
    number='number0'
)
```

