
# Update Metafields Request

## Structure

`UpdateMetafieldsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metafields` | [Update Metafield](../../doc/models/update-metafield.md) \| List[[Update Metafield](../../doc/models/update-metafield.md)] \| None | Optional | This is a container for any-of cases. |

## Example (as JSON)

```json
{
  "metafields": {
    "current_name": "current_name0",
    "name": "name6",
    "scope": {
      "csv": "0",
      "invoices": "0",
      "statements": "0",
      "portal": "0",
      "public_show": "0"
    },
    "input_type": "balance_tracker",
    "enum": [
      "enum2"
    ]
  }
}
```

