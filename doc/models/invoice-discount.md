
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

## Example

```python
from advancedbilling.models.invoice_discount import InvoiceDiscount
from advancedbilling.models.invoice_discount_source_type import InvoiceDiscountSourceType

invoice_discount = InvoiceDiscount(
    uid='uid2',
    title='title2',
    description='description8',
    code='code0',
    source_type=InvoiceDiscountSourceType.REFERRAL
)
```

