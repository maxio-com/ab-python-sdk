
# Invoice Credit

## Structure

`InvoiceCredit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `credit_note_number` | `str` | Optional | - |
| `credit_note_uid` | `str` | Optional | - |
| `transaction_time` | `datetime` | Optional | - |
| `memo` | `str` | Optional | - |
| `original_amount` | `str` | Optional | - |
| `applied_amount` | `str` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.invoice_credit import InvoiceCredit

invoice_credit = InvoiceCredit(
    uid='uid8',
    credit_note_number='credit_note_number8',
    credit_note_uid='credit_note_uid2',
    transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    memo='memo2'
)
```

