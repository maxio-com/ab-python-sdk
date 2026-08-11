
# Register

## Structure

`Register`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `maxio_id` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `currency_code` | `str` | Optional | The ISO 4217 currency code (3 character string) representing the currency of an invoice transaction. |

## Example

```python
from advancedbilling.models.register import Register

register = Register(
    id=54,
    maxio_id='maxio_id4',
    name='name2',
    currency_code='currency_code2'
)
```

