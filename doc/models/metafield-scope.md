
# Metafield Scope

Warning: When updating a metafield's scope attribute, all scope attributes must be passed. Partially complete scope attributes will override the existing settings.

## Structure

`MetafieldScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `csv` | [`IncludeOptionEnum`](../../doc/models/include-option-enum.md) | Optional | Include (1) or exclude (0) metafields from the csv export. |
| `invoices` | [`IncludeOptionEnum`](../../doc/models/include-option-enum.md) | Optional | Include (1) or exclude (0) metafields from invoices. |
| `statements` | [`IncludeOptionEnum`](../../doc/models/include-option-enum.md) | Optional | Include (1) or exclude (0) metafields from statements. |
| `portal` | [`IncludeOptionEnum`](../../doc/models/include-option-enum.md) | Optional | Include (1) or exclude (0) metafields from the portal. |
| `public_show` | [`IncludeOptionEnum`](../../doc/models/include-option-enum.md) | Optional | Include (1) or exclude (0) metafields from being viewable by your ecosystem. |
| `public_edit` | [`IncludeOptionEnum`](../../doc/models/include-option-enum.md) | Optional | Include (1) or exclude (0) metafields from being edited by your ecosystem. |

## Example (as JSON)

```json
{
  "csv": "0",
  "invoices": "0",
  "statements": "0",
  "portal": "0",
  "public_show": "0"
}
```

