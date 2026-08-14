
# Refund Invoice Request

## Structure

`RefundInvoiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `refund` | [Refund Invoice](../../doc/models/refund-invoice.md) \| [Refund Consolidated Invoice](../../doc/models/refund-consolidated-invoice.md) | Required | This is a container for any-of cases. |

## Example

```python
from advancedbilling.models.refund_invoice import RefundInvoice
from advancedbilling.models.refund_invoice_request import RefundInvoiceRequest

refund_invoice_request = RefundInvoiceRequest(
    refund=RefundInvoice(
        amount='amount8',
        memo='memo0',
        payment_id=0,
        external=False,
        apply_credit=False,
        void_invoice=False
    )
)
```

