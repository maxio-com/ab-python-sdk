
# Update Reason Code

## Structure

`UpdateReasonCode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The unique identifier for the ReasonCode |
| `description` | `str` | Optional | The friendly summary of what the code signifies |
| `position` | `int` | Optional | The order that code appears in lists |

## Example

```python
from advancedbilling.models.update_reason_code import UpdateReasonCode

update_reason_code = UpdateReasonCode(
    code='code2',
    description='description4',
    position=12
)
```

