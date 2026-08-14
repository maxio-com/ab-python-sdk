
# Errors

## Structure

`Errors`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `per_page` | `List[str]` | Optional | - |
| `price_point` | `List[str]` | Optional | - |

## Example

```python
from advancedbilling.models.errors import Errors

errors = Errors(
    per_page=[
        'per_page1',
        'per_page2',
        'per_page3'
    ],
    price_point=[
        'price_point0',
        'price_point9',
        'price_point8'
    ]
)
```

