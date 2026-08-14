
# Invoice Payer Change

## Structure

`InvoicePayerChange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `organization` | `str` | Optional | - |
| `email` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_payer_change import InvoicePayerChange

invoice_payer_change = InvoicePayerChange(
    first_name='first_name0',
    last_name='last_name8',
    organization='organization4',
    email='email6'
)
```

