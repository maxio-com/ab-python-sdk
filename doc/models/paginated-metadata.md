
# Paginated Metadata

## Structure

`PaginatedMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_count` | `int` | Optional | - |
| `current_page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `per_page` | `int` | Optional | - |
| `metadata` | [`List[Metadata]`](../../doc/models/metadata.md) | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.metadata import Metadata
from advancedbilling.models.paginated_metadata import PaginatedMetadata

paginated_metadata = PaginatedMetadata(
    total_count=144,
    current_page=120,
    total_pages=132,
    per_page=158,
    metadata=[
        Metadata(
            id=50,
            value='value8',
            resource_id=134,
            name='name6',
            deleted_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        Metadata(
            id=50,
            value='value8',
            resource_id=134,
            name='name6',
            deleted_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        Metadata(
            id=50,
            value='value8',
            resource_id=134,
            name='name6',
            deleted_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ]
)
```

