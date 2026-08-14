
# Scheduled Renewal Configuration Response

## Structure

`ScheduledRenewalConfigurationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scheduled_renewal_configuration` | [`ScheduledRenewalConfiguration`](../../doc/models/scheduled-renewal-configuration.md) | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.scheduled_renewal_configuration import ScheduledRenewalConfiguration
from advancedbilling.models.scheduled_renewal_configuration_response import ScheduledRenewalConfigurationResponse

scheduled_renewal_configuration_response = ScheduledRenewalConfigurationResponse(
    scheduled_renewal_configuration=ScheduledRenewalConfiguration(
        id=134,
        site_id=60,
        subscription_id=244,
        starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        ends_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

