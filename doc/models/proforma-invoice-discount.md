
# Proforma Invoice Discount

## Structure

`ProformaInvoiceDiscount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `title` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `code` | `str` | Optional | - |
| `source_type` | [`ProformaInvoiceDiscountSourceType`](../../doc/models/proforma-invoice-discount-source-type.md) | Optional | - |
| `discount_type` | [`InvoiceDiscountType`](../../doc/models/invoice-discount-type.md) | Optional | - |
| `eligible_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `discount_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `line_item_breakouts` | [`List[InvoiceDiscountBreakout]`](../../doc/models/invoice-discount-breakout.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |

## Example (as JSON)

```json
{
  "uid": "uid2",
  "title": "title8",
  "code": "code0",
  "source_type": "Coupon",
  "discount_type": "percentage"
}
```

