
# Change Invoice Status Event

## Structure

`ChangeInvoiceStatusEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `'change_invoice_status'` |
| `event_data` | [`ChangeInvoiceStatusEventData`](../../doc/models/change-invoice-status-event-data.md) | Required | Example schema for an `change_invoice_status` event |

## Example (as JSON)

```json
{
  "id": 92,
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
  "event_type": "change_invoice_status",
  "event_data": {
    "gateway_trans_id": "gateway_trans_id2",
    "amount": "amount8",
    "from_status": "open",
    "to_status": "pending",
    "consolidation_level": "child"
  }
}
```

