
# Proforma Custom Field

## Structure

`ProformaCustomField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `owner_id` | `int` | Optional | - |
| `owner_type` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `name` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `value` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `metadatum_id` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "owner_id": 224,
  "owner_type": "owner_type0",
  "name": "name8",
  "value": "value0",
  "metadatum_id": 224
}
```

