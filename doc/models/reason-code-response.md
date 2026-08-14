
# Reason Code Response

## Structure

`ReasonCodeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason_code` | [`ReasonCode`](../../doc/models/reason-code.md) | Required | - |

## Example

```python
from advancedbilling.models.reason_code import ReasonCode
from advancedbilling.models.reason_code_response import ReasonCodeResponse

reason_code_response = ReasonCodeResponse(
    reason_code=ReasonCode(
        id=240,
        site_id=166,
        code='code4',
        description='description6',
        position=14
    )
)
```

