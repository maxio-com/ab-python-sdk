
# Billing Manifest

## Structure

`BillingManifest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `line_items` | [`List[BillingManifestItem]`](../../doc/models/billing-manifest-item.md) | Optional | - |
| `total_in_cents` | `int` | Optional | - |
| `total_discount_in_cents` | `int` | Optional | - |
| `total_tax_in_cents` | `int` | Optional | - |
| `subtotal_in_cents` | `int` | Optional | - |
| `start_date` | `datetime` | Optional | - |
| `end_date` | `datetime` | Optional | - |
| `period_type` | `str` | Optional | - |
| `existing_balance_in_cents` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.billing_manifest import BillingManifest
from advancedbilling.models.billing_manifest_item import BillingManifestItem
from advancedbilling.models.billing_manifest_line_item_kind import BillingManifestLineItemKind
from advancedbilling.models.line_item_transaction_type import LineItemTransactionType

billing_manifest = BillingManifest(
    line_items=[
        BillingManifestItem(
            transaction_type=LineItemTransactionType.CREDIT,
            kind=BillingManifestLineItemKind.COMPONENT,
            amount_in_cents=24,
            memo='memo2',
            discount_amount_in_cents=172
        ),
        BillingManifestItem(
            transaction_type=LineItemTransactionType.CREDIT,
            kind=BillingManifestLineItemKind.COMPONENT,
            amount_in_cents=24,
            memo='memo2',
            discount_amount_in_cents=172
        ),
        BillingManifestItem(
            transaction_type=LineItemTransactionType.CREDIT,
            kind=BillingManifestLineItemKind.COMPONENT,
            amount_in_cents=24,
            memo='memo2',
            discount_amount_in_cents=172
        )
    ],
    total_in_cents=6,
    total_discount_in_cents=8,
    total_tax_in_cents=242,
    subtotal_in_cents=118
)
```

