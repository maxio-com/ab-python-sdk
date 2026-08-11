
# Subscription Migration Preview Request

## Structure

`SubscriptionMigrationPreviewRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `migration` | [`SubscriptionMigrationPreviewOptions`](../../doc/models/subscription-migration-preview-options.md) | Required | - |

## Example

```python
from advancedbilling.models.subscription_migration_preview_options import SubscriptionMigrationPreviewOptions
from advancedbilling.models.subscription_migration_preview_request import SubscriptionMigrationPreviewRequest

subscription_migration_preview_request = SubscriptionMigrationPreviewRequest(
    migration=SubscriptionMigrationPreviewOptions(
        product_id=158,
        product_price_point_id=82,
        include_trial=False,
        include_initial_charge=False,
        include_coupons=True,
        preserve_period=False
    )
)
```

