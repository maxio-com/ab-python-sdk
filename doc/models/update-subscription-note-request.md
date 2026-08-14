
# Update Subscription Note Request

Updatable fields for Subscription Note

## Structure

`UpdateSubscriptionNoteRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `note` | [`UpdateSubscriptionNote`](../../doc/models/update-subscription-note.md) | Required | Updatable fields for Subscription Note |

## Example

```python
from advancedbilling.models.update_subscription_note import UpdateSubscriptionNote
from advancedbilling.models.update_subscription_note_request import UpdateSubscriptionNoteRequest

update_subscription_note_request = UpdateSubscriptionNoteRequest(
    note=UpdateSubscriptionNote(
        body='body0',
        sticky=False
    )
)
```

