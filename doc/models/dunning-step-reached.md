
# Dunning Step Reached

## Structure

`DunningStepReached`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dunner` | [`DunnerData`](../../doc/models/dunner-data.md) | Required | - |
| `current_step` | [`DunningStepData`](../../doc/models/dunning-step-data.md) | Required | - |
| `next_step` | [`DunningStepData`](../../doc/models/dunning-step-data.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.dunner_data import DunnerData
from advancedbilling.models.dunning_step_data import DunningStepData
from advancedbilling.models.dunning_step_reached import DunningStepReached

dunning_step_reached = DunningStepReached(
    dunner=DunnerData(
        state='state8',
        subscription_id=194,
        revenue_at_risk_in_cents=98,
        created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        attempts=42,
        last_attempted_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    ),
    current_step=DunningStepData(
        day_threshold=198,
        action='action4',
        send_email=False,
        send_bcc_email=False,
        send_sms=False,
        email_body='email_body4',
        email_subject='email_subject6',
        sms_body='sms_body0'
    ),
    next_step=DunningStepData(
        day_threshold=30,
        action='action4',
        send_email=False,
        send_bcc_email=False,
        send_sms=False,
        email_body='email_body4',
        email_subject='email_subject4',
        sms_body='sms_body0'
    )
)
```

