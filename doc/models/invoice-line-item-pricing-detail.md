
# Invoice Line Item Pricing Detail

## Structure

`InvoiceLineItemPricingDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `label` | `str` | Optional | - |
| `amount` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.invoice_line_item_pricing_detail import InvoiceLineItemPricingDetail

invoice_line_item_pricing_detail = InvoiceLineItemPricingDetail(
    label='label0',
    amount='amount2'
)
```

