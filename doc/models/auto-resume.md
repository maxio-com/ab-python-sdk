
# Auto Resume

## Structure

`AutoResume`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `automatically_resume_at` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.auto_resume import AutoResume

auto_resume = AutoResume(
    automatically_resume_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

