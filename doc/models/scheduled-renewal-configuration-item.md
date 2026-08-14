
# Scheduled Renewal Configuration Item

## Structure

`ScheduledRenewalConfigurationItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `subscription_id` | `int` | Optional | - |
| `subscription_renewal_configuration_id` | `int` | Optional | - |
| `item_id` | `int` | Optional | - |
| `item_type` | `str` | Optional | - |
| `item_subclass` | `str` | Optional | - |
| `price_point_id` | `int` | Optional | - |
| `price_point_type` | `str` | Optional | - |
| `quantity` | `int` | Optional | - |
| `decimal_quantity` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |

## Example

```python
from advancedbilling.models.scheduled_renewal_configuration_item import ScheduledRenewalConfigurationItem

scheduled_renewal_configuration_item = ScheduledRenewalConfigurationItem(
    id=98,
    subscription_id=208,
    subscription_renewal_configuration_id=108,
    item_id=246,
    item_type='item_type2'
)
```

