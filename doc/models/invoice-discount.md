
# Invoice Discount

## Structure

`InvoiceDiscount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `code` | `str` | Optional | - |
| `source_type` | [`InvoiceDiscountSourceType`](../../doc/models/invoice-discount-source-type.md) | Optional | - |
| `source_id` | `int` | Optional | - |
| `discount_type` | [`InvoiceDiscountType`](../../doc/models/invoice-discount-type.md) | Optional | - |
| `percentage` | `str` | Optional | - |
| `eligible_amount` | `str` | Optional | - |
| `discount_amount` | `str` | Optional | - |
| `transaction_id` | `int` | Optional | - |
| `line_item_breakouts` | [`List[InvoiceDiscountBreakout]`](../../doc/models/invoice-discount-breakout.md) | Optional | - |

## Example (as JSON)

```json
{
  "uid": "uid0",
  "title": "title4",
  "description": "description0",
  "code": "code8",
  "source_type": "Coupon"
}
```

