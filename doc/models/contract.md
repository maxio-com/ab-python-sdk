
# Contract

Contract linked to the scheduled renewal configuration.

## Structure

`Contract`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `maxio_id` | `str` | Optional | - |
| `number` | `str` | Optional | - |
| `register` | [`Register`](../../doc/models/register.md) | Optional | - |

## Example

```python
from advancedbilling.models.contract import Contract
from advancedbilling.models.register import Register

contract = Contract(
    id=112,
    maxio_id='maxio_id6',
    number='number2',
    register=Register(
        id=54,
        maxio_id='maxio_id4',
        name='name2',
        currency_code='currency_code2'
    )
)
```

