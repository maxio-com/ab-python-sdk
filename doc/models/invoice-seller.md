
# Invoice Seller

Information about the seller (merchant) listed on the masthead of the invoice.

## Structure

`InvoiceSeller`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `address` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Optional | - |
| `phone` | `str` | Optional | - |
| `logo_url` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_address import InvoiceAddress
from advancedbilling.models.invoice_seller import InvoiceSeller

invoice_seller = InvoiceSeller(
    name='name2',
    address=InvoiceAddress(
        street='street6',
        line_2='line20',
        city='city6',
        state='state2',
        zip='zip0'
    ),
    phone='phone2',
    logo_url='logo_url2'
)
```

