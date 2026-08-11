
# List Public Keys Meta

## Structure

`ListPublicKeysMeta`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_count` | `int` | Optional | - |
| `current_page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `per_page` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.list_public_keys_meta import ListPublicKeysMeta

list_public_keys_meta = ListPublicKeysMeta(
    total_count=240,
    current_page=216,
    total_pages=228,
    per_page=62
)
```

