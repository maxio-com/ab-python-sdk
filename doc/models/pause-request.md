
# Pause Request

Allows you to pause a Subscription.

## Structure

`PauseRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hold` | [`AutoResume`](../../doc/models/auto-resume.md) | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.auto_resume import AutoResume
from advancedbilling.models.pause_request import PauseRequest

pause_request = PauseRequest(
    hold=AutoResume(
        automatically_resume_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

