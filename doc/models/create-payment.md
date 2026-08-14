
# Create Payment

## Structure

`CreatePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `str` | Required | - |
| `memo` | `str` | Required | - |
| `payment_details` | `str` | Required | - |
| `payment_method` | [`InvoicePaymentMethodType`](../../doc/models/invoice-payment-method-type.md) | Required | The type of payment method used. Defaults to other. |

## Example

```python
from advancedbilling.models.create_payment import CreatePayment
from advancedbilling.models.invoice_payment_method_type import InvoicePaymentMethodType

create_payment = CreatePayment(
    amount='amount0',
    memo='memo2',
    payment_details='payment_details8',
    payment_method=InvoicePaymentMethodType.ACH
)
```

