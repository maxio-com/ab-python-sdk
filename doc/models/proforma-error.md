
# Proforma Error

## Structure

`ProformaError`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription` | [`BaseStringError`](../../doc/models/base-string-error.md) | Optional | The error is base if it is not directly associated with a single attribute. |

## Example

```python
from advancedbilling.models.base_string_error import BaseStringError
from advancedbilling.models.proforma_error import ProformaError

proforma_error = ProformaError(
    subscription=BaseStringError(
        base=[
            'base3',
            'base4'
        ]
    )
)
```

