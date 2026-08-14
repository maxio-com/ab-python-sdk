
# Scheduled Renewal Configurations Response

## Structure

`ScheduledRenewalConfigurationsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `scheduled_renewal_configurations` | [`List[ScheduledRenewalConfiguration]`](../../doc/models/scheduled-renewal-configuration.md) | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.scheduled_renewal_configuration import ScheduledRenewalConfiguration
from advancedbilling.models.scheduled_renewal_configurations_response import ScheduledRenewalConfigurationsResponse

scheduled_renewal_configurations_response = ScheduledRenewalConfigurationsResponse(
    scheduled_renewal_configurations=[
        ScheduledRenewalConfiguration(
            id=122,
            site_id=48,
            subscription_id=232,
            starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            ends_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        ScheduledRenewalConfiguration(
            id=122,
            site_id=48,
            subscription_id=232,
            starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            ends_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ]
)
```

