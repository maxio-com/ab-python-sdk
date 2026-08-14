
# Invoice Discount Breakout

## Structure

`InvoiceDiscountBreakout`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `eligible_amount` | `str` | Optional | - |
| `discount_amount` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_discount_breakout import InvoiceDiscountBreakout

invoice_discount_breakout = InvoiceDiscountBreakout(
    uid='uid2',
    eligible_amount='eligible_amount4',
    discount_amount='discount_amount6'
)
```

