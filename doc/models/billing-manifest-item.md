
# Billing Manifest Item

## Structure

`BillingManifestItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_type` | [`LineItemTransactionType`](../../doc/models/line-item-transaction-type.md) | Optional | A handle for the line item transaction type |
| `kind` | [`BillingManifestLineItemKind`](../../doc/models/billing-manifest-line-item-kind.md) | Optional | A handle for the billing manifest line item kind |
| `amount_in_cents` | `int` | Optional | - |
| `memo` | `str` | Optional | - |
| `discount_amount_in_cents` | `int` | Optional | - |
| `taxable_amount_in_cents` | `int` | Optional | - |
| `component_id` | `int` | Optional | - |
| `component_handle` | `str` | Optional | - |
| `component_name` | `str` | Optional | - |
| `product_id` | `int` | Optional | - |
| `product_handle` | `str` | Optional | - |
| `product_name` | `str` | Optional | - |
| `period_range_start` | `str` | Optional | - |
| `period_range_end` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.billing_manifest_item import BillingManifestItem
from advancedbilling.models.billing_manifest_line_item_kind import BillingManifestLineItemKind
from advancedbilling.models.line_item_transaction_type import LineItemTransactionType

billing_manifest_item = BillingManifestItem(
    transaction_type=LineItemTransactionType.PAYMENT_AUTHORIZATION,
    kind=BillingManifestLineItemKind.BASELINE,
    amount_in_cents=152,
    memo='memo0',
    discount_amount_in_cents=92
)
```

