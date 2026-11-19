
# Feature Value Type

The data type of a feature's value. For `access_right` features this is always `boolean`, and for `usage_limit` features this is always `numeric`. For `service_right` features, you choose the value type explicitly.

## Enumeration

`FeatureValueType`

## Fields

| Name |
|  --- |
| `TEXT` |
| `BOOLEAN` |
| `NUMERIC` |

## Example

```python
from advancedbilling.models.feature_value_type import FeatureValueType

feature_value_type = FeatureValueType.BOOLEAN
```

