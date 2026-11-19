
# Errors 1

## Structure

`Errors1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `per_page` | `List[str]` | Optional | - |
| `price_point` | `List[str]` | Optional | - |

## Example

```python
from advancedbilling.models.errors_1 import Errors1

errors_1 = Errors1(
    per_page=[
        'per_page1',
        'per_page2',
        'per_page3'
    ],
    price_point=[
        'price_point0',
        'price_point9'
    ]
)
```

