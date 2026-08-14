
# List Public Keys Response

## Structure

`ListPublicKeysResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chargify_js_keys` | [`List[PublicKey]`](../../doc/models/public-key.md) | Optional | - |
| `meta` | [`ListPublicKeysMeta`](../../doc/models/list-public-keys-meta.md) | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.list_public_keys_meta import ListPublicKeysMeta
from advancedbilling.models.list_public_keys_response import ListPublicKeysResponse
from advancedbilling.models.public_key import PublicKey

list_public_keys_response = ListPublicKeysResponse(
    chargify_js_keys=[
        PublicKey(
            public_key='public_key8',
            requires_security_token=False,
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        PublicKey(
            public_key='public_key8',
            requires_security_token=False,
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ],
    meta=ListPublicKeysMeta(
        total_count=150,
        current_page=126,
        total_pages=138,
        per_page=152
    )
)
```

