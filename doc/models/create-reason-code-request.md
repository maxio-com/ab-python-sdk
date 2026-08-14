
# Create Reason Code Request

## Structure

`CreateReasonCodeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason_code` | [`CreateReasonCode`](../../doc/models/create-reason-code.md) | Required | - |

## Example

```python
from advancedbilling.models.create_reason_code import CreateReasonCode
from advancedbilling.models.create_reason_code_request import CreateReasonCodeRequest

create_reason_code_request = CreateReasonCodeRequest(
    reason_code=CreateReasonCode(
        code='code4',
        description='description6',
        position=14
    )
)
```

