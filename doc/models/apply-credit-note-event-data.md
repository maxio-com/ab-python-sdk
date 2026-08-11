
# Apply Credit Note Event Data

Example schema for an `apply_credit_note` event

## Structure

`ApplyCreditNoteEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Required | Unique identifier for the credit note application. It is generated automatically by Chargify and has the prefix "cdt_" followed by alphanumeric characters. |
| `credit_note_number` | `str` | Required | A unique, identifying string that appears on the credit note and in places it is referenced. |
| `credit_note_uid` | `str` | Required | Unique identifier for the credit note. It is generated automatically by Chargify and has the prefix "cn_" followed by alphanumeric characters. |
| `original_amount` | `str` | Required | The full, original amount of the credit note. |
| `applied_amount` | `str` | Required | The amount of the credit note applied to invoice. |
| `transaction_time` | `datetime` | Optional | The time the credit note was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" |
| `memo` | `str` | Optional | The credit note memo. |
| `role` | `str` | Optional | The role of the credit note (e.g. 'general') |
| `consolidated_invoice` | `bool` | Optional | Shows whether it was applied to consolidated invoice or not. |
| `applied_credit_notes` | [`List[AppliedCreditNoteData]`](../../doc/models/applied-credit-note-data.md) | Optional | List of credit notes applied to children invoices (if consolidated invoice) |

## Example

```python
import dateutil.parser

from advancedbilling.models.applied_credit_note_data import AppliedCreditNoteData
from advancedbilling.models.apply_credit_note_event_data import ApplyCreditNoteEventData

apply_credit_note_event_data = ApplyCreditNoteEventData(
    uid='uid8',
    credit_note_number='credit_note_number8',
    credit_note_uid='credit_note_uid8',
    original_amount='original_amount2',
    applied_amount='applied_amount0',
    transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    memo='memo2',
    role='role8',
    consolidated_invoice=False,
    applied_credit_notes=[
        AppliedCreditNoteData(
            uid='uid4',
            number='number8'
        ),
        AppliedCreditNoteData(
            uid='uid4',
            number='number8'
        ),
        AppliedCreditNoteData(
            uid='uid4',
            number='number8'
        )
    ]
)
```

