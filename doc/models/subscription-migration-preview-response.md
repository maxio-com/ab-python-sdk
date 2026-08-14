
# Subscription Migration Preview Response

## Structure

`SubscriptionMigrationPreviewResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `migration` | [`SubscriptionMigrationPreview`](../../doc/models/subscription-migration-preview.md) | Required | - |

## Example

```python
from advancedbilling.models.subscription_migration_preview import SubscriptionMigrationPreview
from advancedbilling.models.subscription_migration_preview_response import SubscriptionMigrationPreviewResponse

subscription_migration_preview_response = SubscriptionMigrationPreviewResponse(
    migration=SubscriptionMigrationPreview(
        prorated_adjustment_in_cents=196,
        charge_in_cents=78,
        payment_due_in_cents=250,
        credit_applied_in_cents=210
    )
)
```

