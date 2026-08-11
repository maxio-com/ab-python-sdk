
# Scheduled Renewal Configuration Request

## Structure

`ScheduledRenewalConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `renewal_configuration` | [`ScheduledRenewalConfigurationRequestBody`](../../doc/models/scheduled-renewal-configuration-request-body.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.scheduled_renewal_configuration_request import ScheduledRenewalConfigurationRequest
from advancedbilling.models.scheduled_renewal_configuration_request_body import ScheduledRenewalConfigurationRequestBody

scheduled_renewal_configuration_request = ScheduledRenewalConfigurationRequest(
    renewal_configuration=ScheduledRenewalConfigurationRequestBody(
        starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        ends_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        lock_in_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        contract_id=244,
        create_new_contract=False
    )
)
```

