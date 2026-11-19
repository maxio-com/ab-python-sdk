
# Feature Template Response

## Structure

`FeatureTemplateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `feature` | [`FeatureTemplate`](../../doc/models/feature-template.md) | Required | A feature that can be granted to subscribers, defined once at the site level and then attached to products or components. |

## Example

```python
from advancedbilling.models.feature_kind import FeatureKind
from advancedbilling.models.feature_template import FeatureTemplate
from advancedbilling.models.feature_template_response import FeatureTemplateResponse

feature_template_response = FeatureTemplateResponse(
    feature=FeatureTemplate(
        id=206,
        key='sso',
        name='Single Sign-On',
        description='description4',
        kind=FeatureKind.USAGE_LIMIT
    )
)
```

