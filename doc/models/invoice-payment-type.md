
# Invoice Payment Type

The type of payment to be applied to an Invoice. Defaults to external.

## Enumeration

`InvoicePaymentType`

## Fields

| Name |
|  --- |
| `EXTERNAL` |
| `PREPAYMENT` |
| `SERVICE_CREDIT` |
| `PAYMENT` |

## Example

```python
from advancedbilling.models.invoice_payment_type import InvoicePaymentType

invoice_payment_type = InvoicePaymentType.EXTERNAL
```

