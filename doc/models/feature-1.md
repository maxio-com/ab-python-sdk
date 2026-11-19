
# Feature 1

`key` cannot be changed once set. `kind` cannot be changed once any feature catalog item has been created from this template.

## Structure

`Feature1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `unit` | `str` | Optional | - |
| `value_type` | [`FeatureValueType`](../../doc/models/feature-value-type.md) | Optional | The data type of a feature's value. For `access_right` features this is always `boolean`, and for `usage_limit` features this is always `numeric`. For `service_right` features, you choose the value type explicitly. |
| `default_value` | `str` | Optional | - |
| `default_periodicity_interval` | `int` | Optional | - |
| `default_periodicity_unit` | [`EntitlementPeriodicityUnit`](../../doc/models/entitlement-periodicity-unit.md) | Optional | - |

## Example

```python
from advancedbilling.models.feature_1 import Feature1
from advancedbilling.models.feature_value_type import FeatureValueType

feature_1 = Feature1(
    name='name2',
    description='description2',
    unit='unit0',
    value_type=FeatureValueType.TEXT,
    default_value='default_value2'
)
```

