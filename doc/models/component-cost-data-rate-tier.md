
# Component Cost Data Rate Tier

## Structure

`ComponentCostDataRateTier`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `starting_quantity` | `int` | Optional | - |
| `ending_quantity` | `int` | Optional | - |
| `quantity` | `str` | Optional | - |
| `unit_price` | `str` | Optional | - |
| `amount` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.component_cost_data_rate_tier import ComponentCostDataRateTier

component_cost_data_rate_tier = ComponentCostDataRateTier(
    starting_quantity=216,
    ending_quantity=190,
    quantity='quantity0',
    unit_price='unit_price2',
    amount='amount6'
)
```

