
# Invoice Address

## Structure

`InvoiceAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `str` | Optional | - |
| `line_2` | `str` | Optional | - |
| `city` | `str` | Optional | - |
| `state` | `str` | Optional | - |
| `zip` | `str` | Optional | - |
| `country` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_address import InvoiceAddress

invoice_address = InvoiceAddress(
    street='street8',
    line_2='line22',
    city='city8',
    state='state4',
    zip='zip2'
)
```

