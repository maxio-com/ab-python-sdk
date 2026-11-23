
# Feature 2

## Structure

`Feature2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `feature_template_id` | `int` | Required | The id of the feature template to attach. |
| `value` | `str` | Optional | The value granted. Defaults to the feature template's `default_value`; required when the template has none. |
| `periodicity_interval` | `int` | Optional | Required for `usage_limit` features, unless the feature template has a default periodicity, which is used when omitted. Must be omitted for other kinds. |
| `periodicity_unit` | [`EntitlementPeriodicityUnit`](../../doc/models/entitlement-periodicity-unit.md) | Optional | Required for `usage_limit` features, unless the feature template has a default periodicity, which is used when omitted. Must be omitted for other kinds. |
| `price_point_type` | [`FeatureOwnerPricePointType`](../../doc/models/feature-owner-price-point-type.md) | Optional | Set together with `price_point_id` to scope the feature catalog item to a single price point. Omit both to create a product/component-level item, which is a template: it is copied onto price points created afterwards (except bulk-created ones; Clone Component Price Point applies only the items sent with it), but not added to price points that already exist or to their subscribers. |
| `price_point_id` | `int` | Optional | - |
| `propagate_to_subscriptions` | `bool` | Optional | Applies to price-point-scoped items only. When `true`, existing subscriptions on that price point are granted an entitlement for this feature by a background job shortly after, instead of at their next subscription change. When `false` (default) and the price point already has subscribers, the feature is created on a clone of the price point instead, and existing subscribers are unaffected. On a product/component-level item it has no effect, except when the call restores that item's archived price-point copies (creating an item again for a feature template whose item was archived): then `true` grants the feature to those price points' subscribers, and without it the call returns `422` if any of them lack the feature.<br><br>**Default**: `False` |

## Example

```python
from advancedbilling.models.entitlement_periodicity_unit import EntitlementPeriodicityUnit
from advancedbilling.models.feature_2 import Feature2
from advancedbilling.models.feature_owner_price_point_type import FeatureOwnerPricePointType

feature_2 = Feature2(
    feature_template_id=246,
    value='value4',
    periodicity_interval=118,
    periodicity_unit=EntitlementPeriodicityUnit.HOUR,
    price_point_type=FeatureOwnerPricePointType.PRODUCTPRICEPOINT,
    price_point_id=122,
    propagate_to_subscriptions=False
)
```

