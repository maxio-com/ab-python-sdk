
# Usage

## Structure

`Usage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | **Constraints**: `>= 0` |
| `memo` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `price_point_id` | `int` | Optional | - |
| `quantity` | int \| str \| None | Optional | This is a container for one-of cases. |
| `overage_quantity` | `int` | Optional | - |
| `component_id` | `int` | Optional | - |
| `component_handle` | `str` | Optional | - |
| `subscription_id` | `int` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.usage import Usage

usage = Usage(
    id=150,
    memo='memo2',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    price_point_id=28,
    quantity=28
)
```

