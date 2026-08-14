
# Metadata

## Structure

`Metadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `value` | `str` | Optional | - |
| `resource_id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `deleted_at` | `datetime` | Optional | - |
| `metafield_id` | `int` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.metadata import Metadata

metadata = Metadata(
    id=50,
    value='value8',
    resource_id=134,
    name='name6',
    deleted_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

