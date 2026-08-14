
# Subscription Note Response

## Structure

`SubscriptionNoteResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `note` | [`SubscriptionNote`](../../doc/models/subscription-note.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.subscription_note import SubscriptionNote
from advancedbilling.models.subscription_note_response import SubscriptionNoteResponse

subscription_note_response = SubscriptionNoteResponse(
    note=SubscriptionNote(
        id=28,
        body='body0',
        subscription_id=138,
        created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

