
# Public Key

## Structure

`PublicKey`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `public_key` | `str` | Optional | - |
| `requires_security_token` | `bool` | Optional | - |
| `created_at` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.public_key import PublicKey

public_key = PublicKey(
    public_key='public_key0',
    requires_security_token=False,
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

