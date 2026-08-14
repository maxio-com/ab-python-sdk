
# Renewal Preview Response

## Structure

`RenewalPreviewResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `renewal_preview` | [`RenewalPreview`](../../doc/models/renewal-preview.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.renewal_preview import RenewalPreview
from advancedbilling.models.renewal_preview_response import RenewalPreviewResponse

renewal_preview_response = RenewalPreviewResponse(
    renewal_preview=RenewalPreview(
        next_assessment_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        subtotal_in_cents=132,
        total_tax_in_cents=0,
        total_discount_in_cents=250,
        total_in_cents=20
    )
)
```

