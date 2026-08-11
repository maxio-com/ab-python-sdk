
# Create Reason Code

## Structure

`CreateReasonCode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Required | The unique identifier for the ReasonCode |
| `description` | `str` | Required | The friendly summary of what the code signifies |
| `position` | `int` | Optional | The order that code appears in lists |

## Example

```python
from advancedbilling.models.create_reason_code import CreateReasonCode

create_reason_code = CreateReasonCode(
    code='code6',
    description='description8',
    position=252
)
```

