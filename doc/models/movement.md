
# Movement

## Structure

`Movement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp` | `datetime` | Optional | - |
| `amount_in_cents` | `int` | Optional | - |
| `amount_formatted` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `category` | `str` | Optional | - |
| `breakouts` | [`Breakouts`](../../doc/models/breakouts.md) | Optional | - |
| `line_items` | [`List[MovementLineItem]`](../../doc/models/movement-line-item.md) | Optional | - |
| `subscription_id` | `int` | Optional | - |
| `subscriber_name` | `str` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.movement import Movement

movement = Movement(
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    amount_in_cents=34,
    amount_formatted='amount_formatted6',
    description='description4',
    category='category2'
)
```

