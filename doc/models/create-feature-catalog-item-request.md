
# Create Feature Catalog Item Request

The owning product or component is taken from the URL and must not be included in the request body.

## Structure

`CreateFeatureCatalogItemRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `feature` | [`Feature2`](../../doc/models/feature-2.md) | Required | - |

## Example

```python
from advancedbilling.models.create_feature_catalog_item_request import CreateFeatureCatalogItemRequest
from advancedbilling.models.entitlement_periodicity_unit import EntitlementPeriodicityUnit
from advancedbilling.models.feature_2 import Feature2
from advancedbilling.models.feature_owner_price_point_type import FeatureOwnerPricePointType

create_feature_catalog_item_request = CreateFeatureCatalogItemRequest(
    feature=Feature2(
        feature_template_id=196,
        value='value6',
        periodicity_interval=68,
        periodicity_unit=EntitlementPeriodicityUnit.WEEK,
        price_point_type=FeatureOwnerPricePointType.PRODUCTPRICEPOINT,
        price_point_id=84,
        propagate_to_subscriptions=False
    )
)
```

