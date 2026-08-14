
# Renewal Preview Request

## Structure

`RenewalPreviewRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `components` | [`List[RenewalPreviewComponent]`](../../doc/models/renewal-preview-component.md) | Optional | (Optional) Array of component definitions to preview. Providing any component definitions here will override the actual components on the subscription (and their quantities), and the billing preview will contain only these components (in addition to any product base fees). |

## Example

```python
from advancedbilling.models.renewal_preview_component import RenewalPreviewComponent
from advancedbilling.models.renewal_preview_request import RenewalPreviewRequest

renewal_preview_request = RenewalPreviewRequest(
    components=[
        RenewalPreviewComponent(
            component_id='String5',
            quantity=210,
            price_point_id='String3'
        ),
        RenewalPreviewComponent(
            component_id='String5',
            quantity=210,
            price_point_id='String3'
        )
    ]
)
```

