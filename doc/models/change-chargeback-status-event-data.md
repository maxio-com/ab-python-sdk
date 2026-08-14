
# Change Chargeback Status Event Data

Example schema for an `change_chargeback_status` event

## Structure

`ChangeChargebackStatusEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chargeback_status` | [`ChargebackStatus`](../../doc/models/chargeback-status.md) | Required | - |

## Example

```python
from advancedbilling.models.change_chargeback_status_event_data import ChangeChargebackStatusEventData
from advancedbilling.models.chargeback_status import ChargebackStatus

change_chargeback_status_event_data = ChangeChargebackStatusEventData(
    chargeback_status=ChargebackStatus.OPEN
)
```

