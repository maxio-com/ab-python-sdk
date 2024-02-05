
# Invoice Custom Field

## Structure

`InvoiceCustomField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `owner_id` | `int` | Optional | - |
| `owner_type` | [`CustomFieldOwner`](../../doc/models/custom-field-owner.md) | Optional | - |
| `name` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `value` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `metadatum_id` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "owner_id": 142,
  "owner_type": "Customer",
  "name": "name0",
  "value": "value2",
  "metadatum_id": 142
}
```

