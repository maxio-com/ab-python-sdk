
# Renewal Preview Line Item

## Structure

`RenewalPreviewLineItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_type` | [`LineItemTransactionType`](../../doc/models/line-item-transaction-type.md) | Optional | A handle for the line item transaction type |
| `kind` | [`LineItemKind`](../../doc/models/line-item-kind.md) | Optional | A handle for the line item kind |
| `amount_in_cents` | `int` | Optional | - |
| `memo` | `str` | Optional | - |
| `discount_amount_in_cents` | `int` | Optional | - |
| `taxable_amount_in_cents` | `int` | Optional | - |
| `product_id` | `int` | Optional | - |
| `product_name` | `str` | Optional | - |
| `component_id` | `int` | Optional | - |
| `component_handle` | `str` | Optional | - |
| `component_name` | `str` | Optional | - |
| `product_handle` | `str` | Optional | - |
| `period_range_start` | `str` | Optional | - |
| `period_range_end` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.line_item_kind import LineItemKind
from advancedbilling.models.line_item_transaction_type import LineItemTransactionType
from advancedbilling.models.renewal_preview_line_item import RenewalPreviewLineItem

renewal_preview_line_item = RenewalPreviewLineItem(
    transaction_type=LineItemTransactionType.CREDIT,
    kind=LineItemKind.TRIAL,
    amount_in_cents=254,
    memo='memo8',
    discount_amount_in_cents=194
)
```

