
# Site Response

## Structure

`SiteResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site` | [`Site`](../../doc/models/site.md) | Required | - |

## Example

```python
from advancedbilling.models.site import Site
from advancedbilling.models.site_response import SiteResponse

site_response = SiteResponse(
    site=Site(
        id=64,
        name='name4',
        subdomain='subdomain0',
        currency='currency4',
        seller_id=228
    )
)
```

