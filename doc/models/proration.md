
# Proration

## Structure

`Proration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `preserve_period` | `bool` | Optional | The alternative to sending preserve_period as a direct attribute to migration |

## Example

```python
from advancedbilling.models.proration import Proration

proration = Proration(
    preserve_period=False
)
```

