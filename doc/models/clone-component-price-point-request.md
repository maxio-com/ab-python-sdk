
# Clone Component Price Point Request

## Structure

`CloneComponentPricePointRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | [`CloneComponentPricePoint`](../../doc/models/clone-component-price-point.md) | Required | - |

## Example

```python
from advancedbilling.models.clone_component_price_point import CloneComponentPricePoint
from advancedbilling.models.clone_component_price_point_request import CloneComponentPricePointRequest
from advancedbilling.models.clone_feature_catalog_item import CloneFeatureCatalogItem
from advancedbilling.models.entitlement_periodicity_unit import EntitlementPeriodicityUnit
from advancedbilling.models.grant_expiration_unit import GrantExpirationUnit

clone_component_price_point_request = CloneComponentPricePointRequest(
    price_point=CloneComponentPricePoint(
        name='name0',
        handle='handle6',
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
)
```

