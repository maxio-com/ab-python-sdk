
# Feature Templates List Response

## Structure

`FeatureTemplatesListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `items` | [`List[FeatureTemplate]`](../../doc/models/feature-template.md) | Required | - |
| `total_count` | `int` | Required | Total number of feature templates matching the filters, across all pages. |
| `archived_count` | `int` | Required | Number of archived feature templates matching the filters. Returned as `0` unless the active result set is empty or `status=archived` was requested. |

## Example

```python
from advancedbilling.models.feature_kind import FeatureKind
from advancedbilling.models.feature_template import FeatureTemplate
from advancedbilling.models.feature_templates_list_response import FeatureTemplatesListResponse

feature_templates_list_response = FeatureTemplatesListResponse(
    items=[
        FeatureTemplate(
            id=66,
            key='sso',
            name='Single Sign-On',
            description='description2',
            kind=FeatureKind.ACCESS_RIGHT
        )
    ],
    total_count=236,
    archived_count=4
)
```

