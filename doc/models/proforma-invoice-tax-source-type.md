
# Proforma Invoice Tax Source Type

The source of the tax. `Tax` is a tax configured in Advanced Billing. The other values identify the tax service that calculated the tax.

## Enumeration

`ProformaInvoiceTaxSourceType`

## Fields

| Name |
|  --- |
| `TAX` |
| `AVALARA` |
| `ANROK` |
| `TAXJAR` |
| `NUMERAL` |
| `SPHERE` |
| `TAXWIRE` |

## Example

```python
from advancedbilling.models.proforma_invoice_tax_source_type import ProformaInvoiceTaxSourceType

proforma_invoice_tax_source_type = ProformaInvoiceTaxSourceType.ANROK
```

