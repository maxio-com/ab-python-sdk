
# Batch Job Response

## Structure

`BatchJobResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batchjob` | [`BatchJob`](../../doc/models/batch-job.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.batch_job import BatchJob
from advancedbilling.models.batch_job_response import BatchJobResponse

batch_job_response = BatchJobResponse(
    batchjob=BatchJob(
        id=54,
        finished_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        row_count=62,
        created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        completed='completed4'
    )
)
```

