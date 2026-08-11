
# Portal Management Link

## Structure

`PortalManagementLink`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | - |
| `fetch_count` | `int` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `new_link_available_at` | `datetime` | Optional | - |
| `expires_at` | `datetime` | Optional | - |
| `last_invite_sent_at` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.portal_management_link import PortalManagementLink

portal_management_link = PortalManagementLink(
    url='url0',
    fetch_count=46,
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    new_link_available_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

