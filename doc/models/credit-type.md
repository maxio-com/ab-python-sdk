
# Credit Type

The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.

## Enumeration

`CreditType`

## Fields

| Name |
|  --- |
| `FULL` |
| `PRORATED` |
| `NONE` |

## Example

```python
from advancedbilling.models.credit_type import CreditType

credit_type = CreditType.NONE
```

