
# Invoice Status

The current status of the invoice. See [Invoice Statuses](https://docs.maxio.com/billing/invoicing/overview/understand-how-invoices-are-generated#invoice-statuses) for more.

## Enumeration

`InvoiceStatus`

## Fields

| Name |
|  --- |
| `DRAFT` |
| `OPEN` |
| `PAID` |
| `PENDING` |
| `VOIDED` |
| `CANCELED` |
| `PROCESSING` |

## Example

```python
from advancedbilling.models.invoice_status import InvoiceStatus

invoice_status = InvoiceStatus.PROCESSING
```

