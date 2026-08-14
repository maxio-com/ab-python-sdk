
# Create Multi Invoice Payment

## Structure

`CreateMultiInvoicePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `memo` | `str` | Optional | A description to be attached to the payment. |
| `details` | `str` | Optional | Additional information related to the payment method (eg. Check #). |
| `method` | [`InvoicePaymentMethodType`](../../doc/models/invoice-payment-method-type.md) | Optional | The type of payment method used. Defaults to other. |
| `amount` | str \| float | Required | This is a container for one-of cases. |
| `received_on` | `str` | Optional | Date reflecting when the payment was received from a customer. Must be in the past. |
| `applications` | [`List[CreateInvoicePaymentApplication]`](../../doc/models/create-invoice-payment-application.md) | Required | - |

## Example

```python
from advancedbilling.models.create_invoice_payment_application import CreateInvoicePaymentApplication
from advancedbilling.models.create_multi_invoice_payment import CreateMultiInvoicePayment
from advancedbilling.models.invoice_payment_method_type import InvoicePaymentMethodType

create_multi_invoice_payment = CreateMultiInvoicePayment(
    amount='String5',
    applications=[
        CreateInvoicePaymentApplication(
            invoice_uid='invoice_uid8',
            amount='amount0'
        )
    ],
    memo='memo6',
    details='details2',
    method=InvoicePaymentMethodType.ACH,
    received_on='received_on4'
)
```

