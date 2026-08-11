
# Create Invoice Payment Application

## Structure

`CreateInvoicePaymentApplication`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_uid` | `str` | Required | Unique identifier for the invoice. It has the prefix "inv_" followed by alphanumeric characters. |
| `amount` | `str` | Required | Dollar amount of the invoice payment (eg. "10.50" => $10.50). |

## Example

```python
from advancedbilling.models.create_invoice_payment_application import CreateInvoicePaymentApplication

create_invoice_payment_application = CreateInvoicePaymentApplication(
    invoice_uid='invoice_uid8',
    amount='amount0'
)
```

