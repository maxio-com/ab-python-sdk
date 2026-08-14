
# Payer Error

## Structure

`PayerError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `last_name` | `List[str]` | Optional | - |
| `first_name` | `List[str]` | Optional | - |
| `email` | `List[str]` | Optional | - |

## Example

```python
from advancedbilling.models.payer_error import PayerError

payer_error = PayerError(
    last_name=[
        'last_name9'
    ],
    first_name=[
        'first_name2',
        'first_name3',
        'first_name4'
    ],
    email=[
        'email4',
        'email3',
        'email2'
    ]
)
```

