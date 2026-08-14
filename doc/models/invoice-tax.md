
# Invoice Tax

## Structure

`InvoiceTax`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `source_type` | [`ProformaInvoiceTaxSourceType`](../../doc/models/proforma-invoice-tax-source-type.md) | Optional | - |
| `source_id` | `int` | Optional | - |
| `percentage` | `str` | Optional | - |
| `taxable_amount` | `str` | Optional | - |
| `tax_amount` | `str` | Optional | - |
| `transaction_id` | `int` | Optional | - |
| `line_item_breakouts` | [`List[InvoiceTaxBreakout]`](../../doc/models/invoice-tax-breakout.md) | Optional | - |
| `tax_component_breakouts` | [`List[InvoiceTaxComponentBreakout]`](../../doc/models/invoice-tax-component-breakout.md) | Optional | - |
| `eu_vat` | `bool` | Optional | - |
| `mtype` | `str` | Optional | - |
| `tax_exempt_amount` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_tax import InvoiceTax
from advancedbilling.models.proforma_invoice_tax_source_type import ProformaInvoiceTaxSourceType

invoice_tax = InvoiceTax(
    uid='uid0',
    title='title4',
    description='description0',
    source_type=ProformaInvoiceTaxSourceType.TAX,
    source_id=216
)
```

