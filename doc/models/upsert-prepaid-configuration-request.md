
# Upsert Prepaid Configuration Request

## Structure

`UpsertPrepaidConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `prepaid_configuration` | [`UpsertPrepaidConfiguration`](../../doc/models/upsert-prepaid-configuration.md) | Required | - |

## Example

```python
from advancedbilling.models.upsert_prepaid_configuration import UpsertPrepaidConfiguration
from advancedbilling.models.upsert_prepaid_configuration_request import UpsertPrepaidConfigurationRequest

upsert_prepaid_configuration_request = UpsertPrepaidConfigurationRequest(
    prepaid_configuration=UpsertPrepaidConfiguration(
        initial_funding_amount_in_cents=74,
        replenish_to_amount_in_cents=76,
        auto_replenish=False,
        replenish_threshold_amount_in_cents=20
    )
)
```

