
# Scheduled Renewal Configuration Request Body

## Structure

`ScheduledRenewalConfigurationRequestBody`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `starts_at` | `datetime` | Optional | (Optional) Start of the renewal term. |
| `ends_at` | `datetime` | Optional | (Optional) End of the renewal term. |
| `lock_in_at` | `datetime` | Optional | (Optional) Lock-in date for the renewal. |
| `contract_id` | `int` | Optional | (Optional) Existing contract to associate with the scheduled renewal. Contracts must be enabled for your site. |
| `create_new_contract` | `bool` | Optional | (Optional) Set to true to create a new contract when contracts are enabled. Contracts must be enabled for your site. |

## Example

```python
import dateutil.parser

from advancedbilling.models.scheduled_renewal_configuration_request_body import ScheduledRenewalConfigurationRequestBody

scheduled_renewal_configuration_request_body = ScheduledRenewalConfigurationRequestBody(
    starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    ends_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    lock_in_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    contract_id=88,
    create_new_contract=False
)
```

