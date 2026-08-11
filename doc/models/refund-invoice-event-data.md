
# Refund Invoice Event Data

Example schema for an `refund_invoice` event

## Structure

`RefundInvoiceEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `apply_credit` | `bool` | Required | If true, credit was created and applied it to the invoice. |
| `consolidation_level` | [`InvoiceConsolidationLevel`](../../doc/models/invoice-consolidation-level.md) | Optional | Consolidation level of the invoice, which is applicable to invoice consolidation. It will hold one of the following values:<br><br>* "none": A normal invoice with no consolidation.<br>* "child": An invoice segment which has been combined into a consolidated invoice.<br>* "parent": A consolidated invoice, whose contents are composed of invoice segments.<br><br>"Parent" invoices do not have lines of their own, but they have subtotals and totals which aggregate the member invoice segments.<br><br>See also the [invoice consolidation documentation](https://maxio.zendesk.com/hc/en-us/articles/24252269909389-Invoice-Consolidation). |
| `credit_note_attributes` | [`CreditNote`](../../doc/models/credit-note.md) | Required | - |
| `memo` | `str` | Optional | The refund memo. |
| `original_amount` | `str` | Optional | The full, original amount of the refund. |
| `payment_id` | `int` | Required | The ID of the payment transaction to be refunded. |
| `refund_amount` | `str` | Required | The amount of the refund. |
| `refund_id` | `int` | Required | The ID of the refund transaction. |
| `transaction_time` | `datetime` | Required | The time the refund was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" |

## Example

```python
import dateutil.parser

from advancedbilling.models.credit_note import CreditNote
from advancedbilling.models.invoice_consolidation_level import InvoiceConsolidationLevel
from advancedbilling.models.refund_invoice_event_data import RefundInvoiceEventData

refund_invoice_event_data = RefundInvoiceEventData(
    apply_credit=False,
    credit_note_attributes=CreditNote(
        uid='uid2',
        site_id=72,
        customer_id=184,
        subscription_id=0,
        number='number0'
    ),
    payment_id=150,
    refund_amount='refund_amount0',
    refund_id=194,
    transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    consolidation_level=InvoiceConsolidationLevel.NONE,
    memo='memo8',
    original_amount='original_amount8'
)
```

