
# Feature Catalog Item Response

## Structure

`FeatureCatalogItemResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `feature` | [`FeatureCatalogItem`](../../doc/models/feature-catalog-item.md) | Required | A feature template attached to a specific product or component (or one of their price points), with a concrete value. When a subscriber signs up for or is assigned this product/component, the feature catalog item is provisioned as an entitlement on their subscription. |

## Example

```python
from advancedbilling.models.feature_catalog_item import FeatureCatalogItem
from advancedbilling.models.feature_catalog_item_response import FeatureCatalogItemResponse
from advancedbilling.models.feature_kind import FeatureKind

feature_catalog_item_response = FeatureCatalogItemResponse(
    feature=FeatureCatalogItem(
        id=206,
        feature_template_id=196,
        feature_key='feature_key2',
        feature_name='feature_name6',
        feature_kind=FeatureKind.SERVICE_RIGHT
    )
)
```

