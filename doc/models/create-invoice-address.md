
# Create Invoice Address

Overrides the default address.

## Structure

`CreateInvoiceAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `phone` | `str` | Optional | - |
| `address` | `str` | Optional | - |
| `address_2` | `str` | Optional | - |
| `city` | `str` | Optional | - |
| `state` | `str` | Optional | - |
| `zip` | `str` | Optional | - |
| `country` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.create_invoice_address import CreateInvoiceAddress

create_invoice_address = CreateInvoiceAddress(
    first_name='first_name8',
    last_name='last_name6',
    phone='phone2',
    address='address4',
    address_2='address_22'
)
```

