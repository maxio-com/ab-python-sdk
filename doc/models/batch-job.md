
# Batch Job

## Structure

`BatchJob`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `finished_at` | `datetime` | Optional | - |
| `row_count` | `int` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `completed` | `str` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.batch_job import BatchJob

batch_job = BatchJob(
    id=240,
    finished_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    row_count=248,
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    completed='completed2'
)
```

