
# Apply Debit Note Event Data

Example schema for an `apply_debit_note` event

## Structure

`ApplyDebitNoteEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `debit_note_number` | `str` | Required | A unique, identifying string that appears on the debit note and in places it is referenced. |
| `debit_note_uid` | `str` | Required | Unique identifier for the debit note. It is generated automatically by Chargify and has the prefix "db_" followed by alphanumeric characters. |
| `original_amount` | `str` | Required | The full, original amount of the debit note. |
| `applied_amount` | `str` | Required | The amount of the debit note applied to invoice. |
| `memo` | `str` | Optional | The debit note memo. |
| `transaction_time` | `datetime` | Optional | The time the debit note was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" |

## Example (as JSON)

```json
{
  "debit_note_number": "debit_note_number0",
  "debit_note_uid": "debit_note_uid6",
  "original_amount": "original_amount4",
  "applied_amount": "applied_amount8",
  "memo": "memo4",
  "transaction_time": "2016-03-13T12:52:32.123Z"
}
```

