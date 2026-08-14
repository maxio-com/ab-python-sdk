
# Update Subscription Note

Updatable fields for Subscription Note

## Structure

`UpdateSubscriptionNote`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `str` | Required | - |
| `sticky` | `bool` | Required | - |

## Example

```python
from advancedbilling.models.update_subscription_note import UpdateSubscriptionNote

update_subscription_note = UpdateSubscriptionNote(
    body='body8',
    sticky=False
)
```

