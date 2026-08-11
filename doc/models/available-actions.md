
# Available Actions

## Structure

`AvailableActions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `send_email` | [`SendEmail`](../../doc/models/send-email.md) | Optional | - |

## Example

```python
from advancedbilling.models.available_actions import AvailableActions
from advancedbilling.models.send_email import SendEmail

available_actions = AvailableActions(
    send_email=SendEmail(
        can_execute=False,
        url='url0'
    )
)
```

