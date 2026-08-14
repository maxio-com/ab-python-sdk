
# Base String Error

The error is base if it is not directly associated with a single attribute.

## Structure

`BaseStringError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `base` | `List[str]` | Optional | - |

## Example

```python
from advancedbilling.models.base_string_error import BaseStringError

base_string_error = BaseStringError(
    base=[
        'base3',
        'base4'
    ]
)
```

