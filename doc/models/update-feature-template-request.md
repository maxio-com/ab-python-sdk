
# Update Feature Template Request

## Structure

`UpdateFeatureTemplateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `feature` | [`Feature1`](../../doc/models/feature-1.md) | Required | `key` cannot be changed once set. `kind` cannot be changed once any feature catalog item has been created from this template. |

## Example

```python
from advancedbilling.models.feature_1 import Feature1
from advancedbilling.models.feature_value_type import FeatureValueType
from advancedbilling.models.update_feature_template_request import UpdateFeatureTemplateRequest

update_feature_template_request = UpdateFeatureTemplateRequest(
    feature=Feature1(
        name='name4',
        description='description4',
        unit='unit2',
        value_type=FeatureValueType.BOOLEAN,
        default_value='default_value4'
    )
)
```

