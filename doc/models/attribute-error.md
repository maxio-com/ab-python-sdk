
# Attribute Error

## Structure

`AttributeError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attribute` | `List[str]` | Required | - |

## Example

```python
from advancedbilling.models.attribute_error import AttributeError

attribute_error = AttributeError(
    attribute=[
        'attribute6',
        'attribute5',
        'attribute4'
    ]
)
```

