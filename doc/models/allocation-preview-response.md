
# Allocation Preview Response

## Structure

`AllocationPreviewResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allocation_preview` | [`AllocationPreview`](../../doc/models/allocation-preview.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.allocation_preview import AllocationPreview
from advancedbilling.models.allocation_preview_response import AllocationPreviewResponse

allocation_preview_response = AllocationPreviewResponse(
    allocation_preview=AllocationPreview(
        start_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        end_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        subtotal_in_cents=240,
        total_tax_in_cents=108,
        total_discount_in_cents=142
    )
)
```

