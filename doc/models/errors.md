
# Errors

## Structure

`Errors`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | `List[str]` | Required | - |

## Example

```python
from advancedbilling.models.errors import Errors

errors = Errors(
    price_point=[
        'price_point0',
        'price_point9',
        'price_point8'
    ]
)
```

