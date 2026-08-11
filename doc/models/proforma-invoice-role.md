
# Proforma Invoice Role

'proforma' value is deprecated in favor of proforma_adhoc and proforma_automatic.

## Enumeration

`ProformaInvoiceRole`

## Fields

| Name |
|  --- |
| `UNSET` |
| `PROFORMA` |
| `PROFORMA_ADHOC` |
| `PROFORMA_AUTOMATIC` |

## Example

```python
from advancedbilling.models.proforma_invoice_role import ProformaInvoiceRole

proforma_invoice_role = ProformaInvoiceRole.PROFORMA_ADHOC
```

