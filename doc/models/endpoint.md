
# Endpoint

## Structure

`Endpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `url` | `str` | Optional | - |
| `site_id` | `int` | Optional | - |
| `status` | `str` | Optional | - |
| `webhook_subscriptions` | `List[str]` | Optional | - |

## Example

```python
from advancedbilling.models.endpoint import Endpoint

endpoint = Endpoint(
    id=202,
    url='url2',
    site_id=128,
    status='status0',
    webhook_subscriptions=[
        'webhook_subscriptions4'
    ]
)
```

