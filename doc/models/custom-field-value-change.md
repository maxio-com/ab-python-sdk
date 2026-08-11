
# Custom Field Value Change

## Structure

`CustomFieldValueChange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | `str` | Required | - |
| `metafield_name` | `str` | Required | - |
| `metafield_id` | `int` | Required | - |
| `old_value` | `str` | Required | - |
| `new_value` | `str` | Required | - |
| `resource_type` | `str` | Required | - |
| `resource_id` | `int` | Required | - |

## Example

```python
from advancedbilling.models.custom_field_value_change import CustomFieldValueChange

custom_field_value_change = CustomFieldValueChange(
    event_type='event_type0',
    metafield_name='metafield_name4',
    metafield_id=176,
    old_value='old_value4',
    new_value='new_value0',
    resource_type='resource_type4',
    resource_id=232
)
```

