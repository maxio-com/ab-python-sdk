
# Too Many Management Link Requests

## Structure

`TooManyManagementLinkRequests`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `str` | Required | - |
| `new_link_available_at` | `datetime` | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.too_many_management_link_requests import TooManyManagementLinkRequests

too_many_management_link_requests = TooManyManagementLinkRequests(
    error='error4',
    new_link_available_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

