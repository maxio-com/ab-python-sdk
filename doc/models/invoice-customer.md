
# Invoice Customer

Information about the customer who is owner or recipient of the invoiced subscription.

## Structure

`InvoiceCustomer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chargify_id` | `int` | Optional | - |
| `first_name` | `str` | Optional | - |
| `last_name` | `str` | Optional | - |
| `organization` | `str` | Optional | - |
| `email` | `str` | Optional | - |
| `vat_number` | `str` | Optional | - |
| `reference` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_customer import InvoiceCustomer

invoice_customer = InvoiceCustomer(
    chargify_id=52,
    first_name='first_name0',
    last_name='last_name8',
    organization='organization4',
    email='email6'
)
```

