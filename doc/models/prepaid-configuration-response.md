
# Prepaid Configuration Response

## Structure

`PrepaidConfigurationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `prepaid_configuration` | [`PrepaidConfiguration`](../../doc/models/prepaid-configuration.md) | Required | - |

## Example

```python
from advancedbilling.models.prepaid_configuration import PrepaidConfiguration
from advancedbilling.models.prepaid_configuration_response import PrepaidConfigurationResponse

prepaid_configuration_response = PrepaidConfigurationResponse(
    prepaid_configuration=PrepaidConfiguration(
        id=142,
        initial_funding_amount_in_cents=74,
        replenish_to_amount_in_cents=76,
        auto_replenish=False,
        replenish_threshold_amount_in_cents=20
    )
)
```

