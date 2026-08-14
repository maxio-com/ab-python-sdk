
# Reason Code

## Structure

`ReasonCode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `site_id` | `int` | Optional | - |
| `code` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `position` | `int` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |

## Example

```python
from advancedbilling.models.reason_code import ReasonCode

reason_code = ReasonCode(
    id=240,
    site_id=166,
    code='code4',
    description='description6',
    position=14
)
```

