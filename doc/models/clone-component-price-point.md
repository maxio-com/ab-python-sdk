
# Clone Component Price Point

## Structure

`CloneComponentPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `handle` | `str` | Optional | - |
| `feature_catalog_items` | [`List[CloneFeatureCatalogItem]`](../../doc/models/clone-feature-catalog-item.md) | Optional | The features the clone gets. The clone does not copy the source price point's features, so send every feature it should have. |

## Example

```python
from advancedbilling.models.clone_component_price_point import CloneComponentPricePoint
from advancedbilling.models.clone_feature_catalog_item import CloneFeatureCatalogItem
from advancedbilling.models.entitlement_periodicity_unit import EntitlementPeriodicityUnit
from advancedbilling.models.grant_expiration_unit import GrantExpirationUnit

clone_component_price_point = CloneComponentPricePoint(
    name='name2',
    handle='handle8',
    feature_catalog_items=[
        CloneFeatureCatalogItem(
            feature_template_id=8,
            value='value4',
            periodicity_interval=136,
            periodicity_unit=EntitlementPeriodicityUnit.HOUR,
            grant_expiration_interval=60,
            grant_expiration_unit=GrantExpirationUnit.MONTH
        ),
        CloneFeatureCatalogItem(
            feature_template_id=8,
            value='value4',
            periodicity_interval=136,
            periodicity_unit=EntitlementPeriodicityUnit.HOUR,
            grant_expiration_interval=60,
            grant_expiration_unit=GrantExpirationUnit.MONTH
        ),
        CloneFeatureCatalogItem(
            feature_template_id=8,
            value='value4',
            periodicity_interval=136,
            periodicity_unit=EntitlementPeriodicityUnit.HOUR,
            grant_expiration_interval=60,
            grant_expiration_unit=GrantExpirationUnit.MONTH
        )
    ]
)
```

