
# Invoice Payer

## Structure

`InvoicePayer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chargify_id` | `int` | Optional | - |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `organization` | `str` | Optional | - |
| `email` | `str` | Optional | - |
| `vat_number` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_payer import InvoicePayer

invoice_payer = InvoicePayer(
    chargify_id=108,
    first_name='first_name2',
    last_name='last_name0',
    organization='organization4',
    email='email4'
)
```

