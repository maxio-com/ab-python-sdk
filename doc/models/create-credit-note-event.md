
# Create Credit Note Event

## Structure

`CreateCreditNoteEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `'create_credit_note'` |
| `event_data` | [`CreditNote`](../../doc/models/credit-note.md) | Required | Example schema for an `create_credit_note` event |

## Example (as JSON)

```json
{
  "id": 28,
  "timestamp": "2016-03-13T12:52:32.123Z",
  "invoice": {
    "issue_date": "2024-01-01",
    "due_date": "2024-01-01",
    "paid_date": "2024-01-01",
    "public_url_expires_on": "2024-01-21",
    "id": 166,
    "uid": "uid6",
    "site_id": 92,
    "customer_id": 204,
    "subscription_id": 20
  },
  "event_type": "create_credit_note",
  "event_data": {
    "uid": "uid6",
    "site_id": 132,
    "customer_id": 244,
    "subscription_id": 60,
    "number": "number6"
  }
}
```

