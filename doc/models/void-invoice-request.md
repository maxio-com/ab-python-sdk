
# Void Invoice Request

## Structure

`VoidInvoiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `void` | [`VoidInvoice`](../../doc/models/void-invoice.md) | Required | - |

## Example

```python
from advancedbilling.models.void_invoice import VoidInvoice
from advancedbilling.models.void_invoice_request import VoidInvoiceRequest

void_invoice_request = VoidInvoiceRequest(
    void=VoidInvoice(
        reason='reason6'
    )
)
```

