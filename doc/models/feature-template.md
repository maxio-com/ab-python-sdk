
# Feature Template

A feature that can be granted to subscribers, defined once at the site level and then attached to products or components.

## Structure

`FeatureTemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The Advanced Billing id of the feature template. |
| `key` | `str` | Optional | A unique, lowercase, underscore-separated identifier for the feature. Immutable once set. |
| `name` | `str` | Optional | The display name of the feature. |
| `description` | `str` | Optional | - |
| `kind` | [`FeatureKind`](../../doc/models/feature-kind.md) | Optional | The behavior of a feature:<br><br>- `access_right`: a boolean entitlement. A subscriber either has access or does not.<br>- `usage_limit`: a quantified allowance measured over a recurring period (for example, "10,000 API calls per month").<br>- `service_right`: a free-form value (text, boolean, or number) that isn't a simple access flag or a metered limit. |
| `unit` | `str` | Optional | The unit the feature is measured in (for example, `requests` or `GB`). Required when `kind` is `usage_limit`. |
| `value_type` | [`FeatureValueType`](../../doc/models/feature-value-type.md) | Optional | The data type of a feature's value. For `access_right` features this is always `boolean`, and for `usage_limit` features this is always `numeric`. For `service_right` features, you choose the value type explicitly. |
| `default_value` | `str` | Optional | A default value used to pre-populate new feature catalog items created from this template. |
| `default_periodicity_interval` | `int` | Optional | For `usage_limit` features, the default periodicity interval used to pre-populate new feature catalog items. Always `null` for other kinds. |
| `default_periodicity_unit` | [`EntitlementPeriodicityUnit`](../../doc/models/entitlement-periodicity-unit.md) | Optional | For `usage_limit` features, the default periodicity unit used to pre-populate new feature catalog items. Always `null` for other kinds. |
| `archived_at` | `datetime` | Optional | The date and time the feature template was archived, or `null` if it is active. |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `products_count` | `int` | Optional | The number of **components** this feature template is currently attached to via an active feature catalog item. Despite the name, this counts components, not products. In the Advanced Billing UI, components are labeled "Products." |
| `plans_count` | `int` | Optional | The number of **products** this feature template is currently attached to via an active feature catalog item. Despite the name, this counts products, not plans. In the Advanced Billing UI, products are labeled "Plans." |

## Example

```python
from advancedbilling.models.feature_kind import FeatureKind
from advancedbilling.models.feature_template import FeatureTemplate

feature_template = FeatureTemplate(
    id=12,
    key='sso',
    name='Single Sign-On',
    description='description2',
    kind=FeatureKind.SERVICE_RIGHT
)
```

