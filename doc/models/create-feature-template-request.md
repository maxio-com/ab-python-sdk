
# Create Feature Template Request

## Structure

`CreateFeatureTemplateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `feature` | [`Feature`](../../doc/models/feature.md) | Required | - |

## Example

```python
from advancedbilling.models.create_feature_template_request import CreateFeatureTemplateRequest
from advancedbilling.models.feature import Feature
from advancedbilling.models.feature_kind import FeatureKind
from advancedbilling.models.feature_value_type import FeatureValueType

create_feature_template_request = CreateFeatureTemplateRequest(
    feature=Feature(
        key='sso',
        name='name4',
        kind=FeatureKind.USAGE_LIMIT,
        description='description4',
        unit='unit2',
        value_type=FeatureValueType.BOOLEAN,
        default_value='default_value4',
        default_periodicity_interval=150
    )
)
```

