
# Invoice Tax Breakout

## Structure

`InvoiceTaxBreakout`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `taxable_amount` | `str` | Optional | - |
| `tax_amount` | `str` | Optional | - |
| `tax_exempt_amount` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_tax_breakout import InvoiceTaxBreakout

invoice_tax_breakout = InvoiceTaxBreakout(
    uid='uid2',
    taxable_amount='taxable_amount6',
    tax_amount='tax_amount4',
    tax_exempt_amount='tax_exempt_amount2'
)
```

