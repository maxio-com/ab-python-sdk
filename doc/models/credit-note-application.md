
# Credit Note Application

## Structure

`CreditNoteApplication`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `transaction_time` | `datetime` | Optional | - |
| `invoice_uid` | `str` | Optional | - |
| `memo` | `str` | Optional | - |
| `applied_amount` | `str` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.credit_note_application import CreditNoteApplication

credit_note_application = CreditNoteApplication(
    uid='uid0',
    transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice_uid='invoice_uid0',
    memo='memo4',
    applied_amount='applied_amount2'
)
```

