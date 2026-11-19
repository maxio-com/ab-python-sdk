
# Feature Catalog Items List Response

## Structure

`FeatureCatalogItemsListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `features` | [`List[FeatureCatalogItem]`](../../doc/models/feature-catalog-item.md) | Required | - |
| `subscriptions_count` | `int` | Required | The number of subscriptions on this product/component that would be affected if a feature catalog item change were propagated with `propagate_to_subscriptions=true`. |

## Example

```python
from advancedbilling.models.feature_catalog_item import FeatureCatalogItem
from advancedbilling.models.feature_catalog_items_list_response import FeatureCatalogItemsListResponse
from advancedbilling.models.feature_kind import FeatureKind

feature_catalog_items_list_response = FeatureCatalogItemsListResponse(
    features=[
        FeatureCatalogItem(
            id=174,
            feature_template_id=164,
            feature_key='feature_key2',
            feature_name='feature_name6',
            feature_kind=FeatureKind.ACCESS_RIGHT
        )
    ],
    subscriptions_count=214
)
```

