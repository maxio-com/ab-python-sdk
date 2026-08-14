
# Usage Response

## Structure

`UsageResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `usage` | [`Usage`](../../doc/models/usage.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.usage import Usage
from advancedbilling.models.usage_response import UsageResponse

usage_response = UsageResponse(
    usage=Usage(
        id=150,
        memo='memo2',
        created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        price_point_id=28,
        quantity=28
    )
)
```

