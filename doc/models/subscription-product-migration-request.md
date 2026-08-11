
# Subscription Product Migration Request

## Structure

`SubscriptionProductMigrationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `migration` | [`SubscriptionProductMigration`](../../doc/models/subscription-product-migration.md) | Required | - |

## Example

```python
from advancedbilling.models.subscription_product_migration import SubscriptionProductMigration
from advancedbilling.models.subscription_product_migration_request import SubscriptionProductMigrationRequest

subscription_product_migration_request = SubscriptionProductMigrationRequest(
    migration=SubscriptionProductMigration(
        product_id=158,
        product_price_point_id=82,
        include_trial=False,
        include_initial_charge=False,
        include_coupons=True,
        preserve_period=False
    )
)
```

