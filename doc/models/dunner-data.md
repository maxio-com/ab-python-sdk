
# Dunner Data

## Structure

`DunnerData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state` | `str` | Required | - |
| `subscription_id` | `int` | Required | - |
| `revenue_at_risk_in_cents` | `int` | Required | - |
| `created_at` | `datetime` | Required | - |
| `attempts` | `int` | Required | - |
| `last_attempted_at` | `datetime` | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.dunner_data import DunnerData

dunner_data = DunnerData(
    state='state2',
    subscription_id=216,
    revenue_at_risk_in_cents=120,
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    attempts=20,
    last_attempted_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

