
# Send Email

## Structure

`SendEmail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `can_execute` | `bool` | Required | - |
| `url` | `str` | Required | - |

## Example

```python
from advancedbilling.models.send_email import SendEmail

send_email = SendEmail(
    can_execute=False,
    url='url0'
)
```

