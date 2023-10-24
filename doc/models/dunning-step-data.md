
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

## Example (as JSON)

```json
{
  "day_threshold": 88,
  "action": "action4",
  "email_body": "email_body4",
  "email_subject": "email_subject4",
  "send_email": false,
  "send_bcc_email": false,
  "send_sms": false,
  "sms_body": "sms_body0"
}
```

