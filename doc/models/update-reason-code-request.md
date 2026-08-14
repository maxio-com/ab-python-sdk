
# Update Reason Code Request

## Structure

`UpdateReasonCodeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason_code` | [`UpdateReasonCode`](../../doc/models/update-reason-code.md) | Required | - |

## Example

```python
from advancedbilling.models.update_reason_code import UpdateReasonCode
from advancedbilling.models.update_reason_code_request import UpdateReasonCodeRequest

update_reason_code_request = UpdateReasonCodeRequest(
    reason_code=UpdateReasonCode(
        code='code4',
        description='description6',
        position=14
    )
)
```

