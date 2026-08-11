
# Resent Invitation

## Structure

`ResentInvitation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `last_sent_at` | `str` | Optional | - |
| `last_accepted_at` | `str` | Optional | - |
| `send_invite_link_text` | `str` | Optional | - |
| `uninvited_count` | `int` | Optional | - |
| `last_invite_sent_at` | `datetime` | Optional | - |
| `last_invite_accepted_at` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.resent_invitation import ResentInvitation

resent_invitation = ResentInvitation(
    last_sent_at='last_sent_at6',
    last_accepted_at='last_accepted_at6',
    send_invite_link_text='send_invite_link_text4',
    uninvited_count=78,
    last_invite_sent_at=dateutil.parser.parse('2024-01-01T04:30:00+00:00'),
    last_invite_accepted_at=dateutil.parser.parse('2024-01-01T04:35:00+00:00')
)
```

