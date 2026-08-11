
# Invoice Payment Method Type

The type of payment method used. Defaults to other.

## Enumeration

`InvoicePaymentMethodType`

## Fields

| Name |
|  --- |
| `CREDIT_CARD` |
| `CHECK` |
| `CASH` |
| `MONEY_ORDER` |
| `ACH` |
| `OTHER` |

## Example

```python
from advancedbilling.models.invoice_payment_method_type import InvoicePaymentMethodType

invoice_payment_method_type = InvoicePaymentMethodType.CREDIT_CARD
```

