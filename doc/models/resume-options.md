
# Resume Options

## Structure

`ResumeOptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `require_resume` | `bool` | Optional | Chargify will only attempt to resume the subscription's billing period. If not resumable, the subscription will be left in its current state. |
| `forgive_balance` | `bool` | Optional | Indicates whether or not Chargify should clear the subscription's existing balance before attempting to resume the subscription. If subscription cannot be resumed, the balance will remain as it was before the attempt to resume was made. |

## Example

```python
from advancedbilling.models.resume_options import ResumeOptions

resume_options = ResumeOptions(
    require_resume=False,
    forgive_balance=False
)
```

