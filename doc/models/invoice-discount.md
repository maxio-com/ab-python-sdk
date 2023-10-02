
# Invoice Discount

## Structure

`InvoiceDiscount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `code` | `str` | Optional | - |
| `source_type` | `str` | Optional | - |
| `source_id` | `int` | Optional | - |
| `discount_type` | `str` | Optional | - |
| `percentage` | `str` | Optional | - |
| `eligible_amount` | `str` | Optional | - |
| `discount_amount` | `str` | Optional | - |
| `line_item_breakouts` | [`List[InvoiceDiscountBreakout]`](../../doc/models/invoice-discount-breakout.md) | Optional | - |

## Example (as JSON)

```json
{
  "uid": "uid0",
  "title": "title4",
  "code": "code8",
  "source_type": "source_type0",
  "source_id": 66
}
```

