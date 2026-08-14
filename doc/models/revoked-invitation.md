
# Revoked Invitation

## Structure

`RevokedInvitation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `last_sent_at` | `str` | Optional | - |
| `last_accepted_at` | `str` | Optional | - |
| `uninvited_count` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.revoked_invitation import RevokedInvitation

revoked_invitation = RevokedInvitation(
    last_sent_at='last_sent_at4',
    last_accepted_at='last_accepted_at4',
    uninvited_count=58
)
```

