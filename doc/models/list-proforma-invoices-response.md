
# List Proforma Invoices Response

## Structure

`ListProformaInvoicesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `proforma_invoices` | [`List[ProformaInvoice]`](../../doc/models/proforma-invoice.md) | Optional | - |
| `meta` | [`ListProformaInvoicesMeta`](../../doc/models/list-proforma-invoices-meta.md) | Optional | - |

## Example

```python
from advancedbilling.models.list_proforma_invoices_meta import ListProformaInvoicesMeta
from advancedbilling.models.list_proforma_invoices_response import ListProformaInvoicesResponse
from advancedbilling.models.proforma_invoice import ProformaInvoice

list_proforma_invoices_response = ListProformaInvoicesResponse(
    proforma_invoices=[
        ProformaInvoice(
            uid='uid0',
            site_id=140,
            customer_id=252,
            subscription_id=68,
            number=56
        ),
        ProformaInvoice(
            uid='uid0',
            site_id=140,
            customer_id=252,
            subscription_id=68,
            number=56
        ),
        ProformaInvoice(
            uid='uid0',
            site_id=140,
            customer_id=252,
            subscription_id=68,
            number=56
        )
    ],
    meta=ListProformaInvoicesMeta(
        total_count=150,
        current_page=126,
        total_pages=138,
        status_code=168
    )
)
```

