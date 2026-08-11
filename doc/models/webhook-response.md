
# Webhook Response

## Structure

`WebhookResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook` | [`Webhook`](../../doc/models/webhook.md) | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.webhook import Webhook
from advancedbilling.models.webhook_response import WebhookResponse

webhook_response = WebhookResponse(
    webhook=Webhook(
        event='event2',
        id=18,
        created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        last_error='last_error4',
        last_error_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

