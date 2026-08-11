
# Address Change

## Structure

`AddressChange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `before` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Required | - |
| `after` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Required | - |

## Example

```python
from advancedbilling.models.address_change import AddressChange
from advancedbilling.models.invoice_address import InvoiceAddress

address_change = AddressChange(
    before=InvoiceAddress(
        street='street0',
        line_2='line24',
        city='city0',
        state='state6',
        zip='zip4'
    ),
    after=InvoiceAddress(
        street='street2',
        line_2='line26',
        city='city8',
        state='state2',
        zip='zip4'
    )
)
```

