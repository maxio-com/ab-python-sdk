
# Invoice Debit

## Structure

`InvoiceDebit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `debit_note_number` | `str` | Optional | - |
| `debit_note_uid` | `str` | Optional | - |
| `role` | [`DebitNoteRole`](../../doc/models/debit-note-role.md) | Optional | The role of the debit note. |
| `transaction_time` | `datetime` | Optional | - |
| `memo` | `str` | Optional | - |
| `original_amount` | `str` | Optional | - |
| `applied_amount` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "uid": "uid2",
  "debit_note_number": "debit_note_number2",
  "debit_note_uid": "debit_note_uid8",
  "role": "chargeback",
  "transaction_time": "2016-03-13T12:52:32.123Z"
}
```

