
# Subscription Note

## Structure

`SubscriptionNote`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `body` | `str` | Optional | - |
| `subscription_id` | `int` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `sticky` | `bool` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.subscription_note import SubscriptionNote

subscription_note = SubscriptionNote(
    id=114,
    body='body0',
    subscription_id=224,
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    updated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

