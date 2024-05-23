
# List Invoice Events Response

## Structure

`ListInvoiceEventsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `events` | List[[Apply Credit Note Event](../../doc/models/apply-credit-note-event.md) \| [Apply Debit Note Event](../../doc/models/apply-debit-note-event.md) \| [Apply Payment Event](../../doc/models/apply-payment-event.md) \| [Backport Invoice Event](../../doc/models/backport-invoice-event.md) \| [Change Chargeback Status Event](../../doc/models/change-chargeback-status-event.md) \| [Change Invoice Collection Method Event](../../doc/models/change-invoice-collection-method-event.md) \| [Change Invoice Status Event](../../doc/models/change-invoice-status-event.md) \| [Create Credit Note Event](../../doc/models/create-credit-note-event.md) \| [Create Debit Note Event](../../doc/models/create-debit-note-event.md) \| [Failed Payment Event](../../doc/models/failed-payment-event.md) \| [Issue Invoice Event](../../doc/models/issue-invoice-event.md) \| [Refund Invoice Event](../../doc/models/refund-invoice-event.md) \| [Remove Payment Event](../../doc/models/remove-payment-event.md) \| [Void Invoice Event](../../doc/models/void-invoice-event.md) \| [Void Remainder Event](../../doc/models/void-remainder-event.md)] \| None | Optional | - |
| `page` | `int` | Optional | - |
| `per_page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "events": [
    {
      "event_type": "apply_credit_note",
      "id": 214,
      "timestamp": "2016-03-13T12:52:32.123Z",
      "invoice": {
        "id": 166,
        "uid": "uid6",
        "site_id": 92,
        "customer_id": 204,
        "subscription_id": 20
      },
      "event_data": {
        "uid": "uid6",
        "credit_note_number": "credit_note_number0",
        "credit_note_uid": "credit_note_uid0",
        "original_amount": "original_amount0",
        "applied_amount": "applied_amount2",
        "transaction_time": "2016-03-13T12:52:32.123Z",
        "memo": "memo0",
        "role": "role0",
        "consolidated_invoice": false,
        "applied_credit_notes": [
          {
            "uid": "uid4",
            "number": "number8"
          },
          {
            "uid": "uid4",
            "number": "number8"
          },
          {
            "uid": "uid4",
            "number": "number8"
          }
        ]
      }
    }
  ],
  "page": 184,
  "per_page": 96,
  "total_pages": 194
}
```

