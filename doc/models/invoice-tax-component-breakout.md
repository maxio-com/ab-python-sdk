
# Invoice Tax Component Breakout

## Structure

`InvoiceTaxComponentBreakout`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_rule_id` | `int` | Optional | - |
| `percentage` | `str` | Optional | - |
| `country_code` | `str` | Optional | - |
| `subdivision_code` | `str` | Optional | - |
| `tax_amount` | `str` | Optional | - |
| `taxable_amount` | `str` | Optional | - |
| `tax_exempt_amount` | `str` | Optional | - |
| `non_taxable_amount` | `str` | Optional | - |
| `tax_name` | `str` | Optional | - |
| `tax_type` | `str` | Optional | - |
| `rate_type` | `str` | Optional | - |
| `tax_authority_type` | `int` | Optional | - |
| `state_assigned_no` | `str` | Optional | - |
| `tax_sub_type` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_tax_component_breakout import InvoiceTaxComponentBreakout

invoice_tax_component_breakout = InvoiceTaxComponentBreakout(
    tax_rule_id=4,
    percentage='percentage0',
    country_code='country_code2',
    subdivision_code='subdivision_code4',
    tax_amount='tax_amount6'
)
```

