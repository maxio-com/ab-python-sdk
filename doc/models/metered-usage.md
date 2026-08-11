
# Metered Usage

## Structure

`MeteredUsage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `previous_unit_balance` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `new_unit_balance` | int \| str | Required | This is a container for one-of cases. |
| `usage_quantity` | `int` | Required | - |
| `component_id` | `int` | Required | - |
| `component_handle` | `str` | Required | - |
| `memo` | `str` | Required | - |

## Example

```python
from advancedbilling.models.metered_usage import MeteredUsage

metered_usage = MeteredUsage(
    previous_unit_balance='previous_unit_balance2',
    new_unit_balance=244,
    usage_quantity=28,
    component_id=246,
    component_handle='component_handle2',
    memo='memo6'
)
```

