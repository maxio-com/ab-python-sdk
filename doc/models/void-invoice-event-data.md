
# Void Invoice Event Data

Example schema for an `void_invoice` event

## Structure

`VoidInvoiceEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credit_note_attributes` | [Credit Note](../../doc/models/credit-note.md) \| None | Required | This is a container for one-of cases. |
| `memo` | `str` | Required | The memo provided during invoice voiding. |
| `applied_amount` | `str` | Required | The amount of the void. |
| `transaction_time` | `datetime` | Required | The time the refund was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" |
| `is_advance_invoice` | `bool` | Required | If true, the invoice is an advance invoice. |
| `reason` | `str` | Required | The reason for the void. |

## Example (as JSON)

```json
{
  "credit_note_attributes": {
    "uid": "uid2",
    "site_id": 218,
    "customer_id": 74,
    "subscription_id": 146,
    "number": "number0"
  },
  "memo": "memo6",
  "applied_amount": "applied_amount6",
  "transaction_time": "2016-03-13T12:52:32.123Z",
  "is_advance_invoice": false,
  "reason": "reason8"
}
```

