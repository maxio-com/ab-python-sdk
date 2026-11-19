
# Update Feature Catalog Item Request

## Structure

`UpdateFeatureCatalogItemRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `feature` | [`Feature3`](../../doc/models/feature-3.md) | Required | - |

## Example

```python
from advancedbilling.models.entitlement_periodicity_unit import EntitlementPeriodicityUnit
from advancedbilling.models.feature_3 import Feature3
from advancedbilling.models.update_feature_catalog_item_request import UpdateFeatureCatalogItemRequest

update_feature_catalog_item_request = UpdateFeatureCatalogItemRequest(
    feature=Feature3(
        value='value6',
        periodicity_interval=68,
        periodicity_unit=EntitlementPeriodicityUnit.WEEK,
        propagate_to_subscriptions=False
    )
)
```

