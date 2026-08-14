
# List Proforma Invoices Meta

## Structure

`ListProformaInvoicesMeta`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_count` | `int` | Optional | - |
| `current_page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `status_code` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.list_proforma_invoices_meta import ListProformaInvoicesMeta

list_proforma_invoices_meta = ListProformaInvoicesMeta(
    total_count=84,
    current_page=60,
    total_pages=72,
    status_code=102
)
```

