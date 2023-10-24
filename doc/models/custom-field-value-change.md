
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

## Example (as JSON)

```json
{
  "event_type": "event_type2",
  "metafield_name": "metafield_name6",
  "metafield_id": 78,
  "old_value": "old_value2",
  "new_value": "new_value8",
  "resource_type": "resource_type2",
  "resource_id": 74
}
```

