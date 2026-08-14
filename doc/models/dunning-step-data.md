
# Dunning Step Data

## Structure

`DunningStepData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `day_threshold` | `int` | Required | - |
| `action` | `str` | Required | - |
| `email_body` | `str` | Optional | - |
| `email_subject` | `str` | Optional | - |
| `send_email` | `bool` | Required | - |
| `send_bcc_email` | `bool` | Required | - |
| `send_sms` | `bool` | Required | - |
| `sms_body` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.dunning_step_data import DunningStepData

dunning_step_data = DunningStepData(
    day_threshold=90,
    action='action0',
    send_email=False,
    send_bcc_email=False,
    send_sms=False,
    email_body='email_body0',
    email_subject='email_subject0',
    sms_body='sms_body4'
)
```

