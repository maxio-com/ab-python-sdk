
# Feature Catalog Item

A feature template attached to a specific product or component (or one of their price points), with a concrete value. When a subscriber signs up for or is assigned this product/component, the feature catalog item is provisioned as an entitlement on their subscription.

## Structure

`FeatureCatalogItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `feature_template_id` | `int` | Optional | The id of the feature template this item was created from. |
| `feature_key` | `str` | Optional | The `key` of the parent feature template. |
| `feature_name` | `str` | Optional | The `name` of the parent feature template. |
| `feature_kind` | [`FeatureKind`](../../doc/models/feature-kind.md) | Optional | The behavior of a feature:<br><br>- `access_right`: a boolean entitlement. A subscriber either has access or does not.<br>- `usage_limit`: a quantified allowance measured over a recurring period (for example, "10,000 API calls per month").<br>- `service_right`: a free-form value (text, boolean, or number) that isn't a simple access flag or a metered limit. |
| `value` | `str` | Optional | The value granted by this feature catalog item. Interpreted according to `feature_kind`: `"true"`/`"false"` for `access_right`, a numeric string for `usage_limit`, or any string for `service_right` (shaped by the feature template's `value_type`). |
| `periodicity_interval` | `int` | Optional | Set when `feature_kind` is `usage_limit`; `null` otherwise. |
| `periodicity_unit` | [`EntitlementPeriodicityUnit`](../../doc/models/entitlement-periodicity-unit.md) | Optional | Set when `feature_kind` is `usage_limit`; `null` otherwise. |
| `price_point_type` | [`FeatureOwnerPricePointType`](../../doc/models/feature-owner-price-point-type.md) | Optional | `null` when this feature catalog item applies to every price point of its owning product/component. Set when the feature catalog item is an override for one specific price point. |
| `price_point_id` | `int` | Optional | Set together with `price_point_type` for price-point-specific overrides. |
| `archived_at` | `datetime` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |

## Example

```python
from advancedbilling.models.feature_catalog_item import FeatureCatalogItem
from advancedbilling.models.feature_kind import FeatureKind

feature_catalog_item = FeatureCatalogItem(
    id=230,
    feature_template_id=220,
    feature_key='feature_key0',
    feature_name='feature_name4',
    feature_kind=FeatureKind.SERVICE_RIGHT
)
```

