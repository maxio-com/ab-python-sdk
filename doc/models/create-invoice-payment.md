
# Create Invoice Payment

## Structure

`CreateInvoicePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | str \| float \| None | Optional | This is a container for one-of cases. |
| `memo` | `str` | Optional | A description to be attached to the payment. Applicable only to `external` payments. |
| `method` | [`InvoicePaymentMethodType`](../../doc/models/invoice-payment-method-type.md) | Optional | The type of payment method used. Defaults to other. |
| `details` | `str` | Optional | Additional information related to the payment method (eg. Check #). Applicable only to `external` payments. |
| `payment_profile_id` | `int` | Optional | The ID of the payment profile to be used for the payment. |
| `received_on` | `date` | Optional | Date reflecting when the payment was received from a customer. Must be in the past. Applicable only to<br>`external` payments. |

## Example

```python
from advancedbilling.models.create_invoice_payment import CreateInvoicePayment
from advancedbilling.models.invoice_payment_method_type import InvoicePaymentMethodType

create_invoice_payment = CreateInvoicePayment(
    amount='String7',
    memo='memo8',
    method=InvoicePaymentMethodType.CREDIT_CARD,
    details='details4',
    payment_profile_id=210
)
```

