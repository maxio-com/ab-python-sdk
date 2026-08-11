
# Customer Payer Change

## Structure

`CustomerPayerChange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `before` | [`InvoicePayerChange`](../../doc/models/invoice-payer-change.md) | Required | - |
| `after` | [`InvoicePayerChange`](../../doc/models/invoice-payer-change.md) | Required | - |

## Example

```python
from advancedbilling.models.customer_payer_change import CustomerPayerChange
from advancedbilling.models.invoice_payer_change import InvoicePayerChange

customer_payer_change = CustomerPayerChange(
    before=InvoicePayerChange(
        first_name='first_name0',
        last_name='last_name8',
        organization='organization4',
        email='email6'
    ),
    after=InvoicePayerChange(
        first_name='first_name2',
        last_name='last_name0',
        organization='organization4',
        email='email4'
    )
)
```

