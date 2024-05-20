
# Invoice Event

## Structure

`InvoiceEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Optional | Invoice Event Type |
| `event_data` | [Apply Credit Note Event Data](../../doc/models/apply-credit-note-event-data.md) \| [Apply Debit Note Event Data](../../doc/models/apply-debit-note-event-data.md) \| [Apply Payment Event Data](../../doc/models/apply-payment-event-data.md) \| [Change Invoice Collection Method Event Data](../../doc/models/change-invoice-collection-method-event-data.md) \| [Issue Invoice Event Data](../../doc/models/issue-invoice-event-data.md) \| [Refund Invoice Event Data](../../doc/models/refund-invoice-event-data.md) \| [Remove Payment Event Data](../../doc/models/remove-payment-event-data.md) \| [Void Invoice Event Data](../../doc/models/void-invoice-event-data.md) \| [Void Remainder Event Data](../../doc/models/void-remainder-event-data.md) \| [Invoice](../../doc/models/invoice.md) \| [Change Invoice Status Event Data](../../doc/models/change-invoice-status-event-data.md) \| [Failed Payment Event Data](../../doc/models/failed-payment-event-data.md) \| [Debit Note](../../doc/models/debit-note.md) \| [Credit Note](../../doc/models/credit-note.md) \| [Change Chargeback Status Event Data](../../doc/models/change-chargeback-status-event-data.md) \| None | Optional | This is a container for any-of cases. |
| `timestamp` | `datetime` | Optional | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": 78,
  "event_type": "create_debit_note",
  "event_data": {
    "uid": "uid2",
    "credit_note_number": "credit_note_number4",
    "credit_note_uid": "credit_note_uid4",
    "original_amount": "original_amount6",
    "applied_amount": "applied_amount6",
    "transaction_time": "2016-03-13T12:52:32.123Z",
    "memo": "memo6",
    "role": "role4",
    "consolidated_invoice": false,
    "applied_credit_notes": [
      {
        "uid": "uid4",
        "number": "number8"
      },
      {
        "uid": "uid4",
        "number": "number8"
      }
    ]
  },
  "timestamp": "2016-03-13T12:52:32.123Z",
  "invoice": {
    "id": 166,
    "uid": "uid6",
    "site_id": 92,
    "customer_id": 204,
    "subscription_id": 20
  }
}
```

