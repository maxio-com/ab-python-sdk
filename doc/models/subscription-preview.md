
# Subscription Preview

## Structure

`SubscriptionPreview`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `current_billing_manifest` | [`BillingManifest`](../../doc/models/billing-manifest.md) | Optional | - |
| `next_billing_manifest` | [`BillingManifest`](../../doc/models/billing-manifest.md) | Optional | - |

## Example

```python
from advancedbilling.models.billing_manifest import BillingManifest
from advancedbilling.models.billing_manifest_item import BillingManifestItem
from advancedbilling.models.billing_manifest_line_item_kind import BillingManifestLineItemKind
from advancedbilling.models.line_item_transaction_type import LineItemTransactionType
from advancedbilling.models.subscription_preview import SubscriptionPreview

subscription_preview = SubscriptionPreview(
    current_billing_manifest=BillingManifest(
        line_items=[
            BillingManifestItem(
                transaction_type=LineItemTransactionType.CREDIT,
                kind=BillingManifestLineItemKind.COMPONENT,
                amount_in_cents=24,
                memo='memo2',
                discount_amount_in_cents=172
            )
        ],
        total_in_cents=38,
        total_discount_in_cents=24,
        total_tax_in_cents=18,
        subtotal_in_cents=150
    ),
    next_billing_manifest=BillingManifest(
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
        total_in_cents=62,
        total_discount_in_cents=208,
        total_tax_in_cents=42,
        subtotal_in_cents=174
    )
)
```

