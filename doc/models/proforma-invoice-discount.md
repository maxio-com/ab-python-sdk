
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

## Example

```python
from advancedbilling.models.invoice_discount_type import InvoiceDiscountType
from advancedbilling.models.proforma_invoice_discount import ProformaInvoiceDiscount
from advancedbilling.models.proforma_invoice_discount_source_type import ProformaInvoiceDiscountSourceType

proforma_invoice_discount = ProformaInvoiceDiscount(
    uid='uid0',
    title='title6',
    code='code8',
    source_type=ProformaInvoiceDiscountSourceType.COUPON,
    discount_type=InvoiceDiscountType.ROLLOVER
)
```

