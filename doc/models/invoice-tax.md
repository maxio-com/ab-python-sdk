
# Invoice Tax

## Structure

`InvoiceTax`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `source_type` | `str` | Optional | - |
| `source_id` | `int` | Optional | - |
| `percentage` | `str` | Optional | - |
| `taxable_amount` | `str` | Optional | - |
| `tax_amount` | `str` | Optional | - |
| `transaction_id` | `int` | Optional | - |
| `line_item_breakouts` | [`List[InvoiceTaxBreakout]`](../../doc/models/invoice-tax-breakout.md) | Optional | - |
| `tax_component_breakouts` | [`List[InvoiceTaxComponentBreakout]`](../../doc/models/invoice-tax-component-breakout.md) | Optional | - |

## Example (as JSON)

```json
{
  "uid": "uid8",
  "title": "title6",
  "description": "description2",
  "source_type": "source_type8",
  "source_id": 164
}
```

