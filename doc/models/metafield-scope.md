
# Metafield Scope

Warning: When updating a metafield's scope attribute, all scope attributes must be passed. Partially complete scope attributes will override the existing settings.

## Structure

`MetafieldScope`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `csv` | [`IncludeOption`](../../doc/models/include-option.md) | Optional | Include (1) or exclude (0) metafields from the csv export. |
| `invoices` | [`IncludeOption`](../../doc/models/include-option.md) | Optional | Include (1) or exclude (0) metafields from invoices. |
| `statements` | [`IncludeOption`](../../doc/models/include-option.md) | Optional | Include (1) or exclude (0) metafields from statements. |
| `portal` | [`IncludeOption`](../../doc/models/include-option.md) | Optional | Include (1) or exclude (0) metafields from the portal. |
| `public_show` | [`IncludeOption`](../../doc/models/include-option.md) | Optional | Include (1) or exclude (0) metafields used in [Embeddable Components](page:development-tools/embeddable-components/overview) from being viewable by your ecosystem. |
| `public_edit` | [`IncludeOption`](../../doc/models/include-option.md) | Optional | Include (1) or exclude (0) metafields used in [Embeddable Components](page:development-tools/embeddable-components/overview) from being editable by your ecosystem. |
| `hosted` | `List[str]` | Optional | - |

## Example

```python
from advancedbilling.models.include_option import IncludeOption
from advancedbilling.models.metafield_scope import MetafieldScope

metafield_scope = MetafieldScope(
    csv=IncludeOption.EXCLUDE,
    invoices=IncludeOption.EXCLUDE,
    statements=IncludeOption.EXCLUDE,
    portal=IncludeOption.EXCLUDE,
    public_show=IncludeOption.EXCLUDE
)
```

