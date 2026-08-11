
# Update Metafield

## Structure

`UpdateMetafield`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `current_name` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `scope` | [`MetafieldScope`](../../doc/models/metafield-scope.md) | Optional | Warning: When updating a metafield's scope attribute, all scope attributes must be passed. Partially complete scope attributes will override the existing settings. |
| `input_type` | [`MetafieldInput`](../../doc/models/metafield-input.md) | Optional | Indicates the type of metafield. A text metafield allows any string value. Dropdown and radio metafields have a set of values that can be selected. Defaults to 'text'. |
| `enum` | `List[str]` | Optional | Only applicable when input_type is radio or dropdown. |

## Example

```python
from advancedbilling.models.include_option import IncludeOption
from advancedbilling.models.metafield_input import MetafieldInput
from advancedbilling.models.metafield_scope import MetafieldScope
from advancedbilling.models.update_metafield import UpdateMetafield

update_metafield = UpdateMetafield(
    current_name='current_name0',
    name='name6',
    scope=MetafieldScope(
        csv=IncludeOption.EXCLUDE,
        invoices=IncludeOption.EXCLUDE,
        statements=IncludeOption.EXCLUDE,
        portal=IncludeOption.EXCLUDE,
        public_show=IncludeOption.EXCLUDE
    ),
    input_type=MetafieldInput.RADIO,
    enum=[
        'enum2',
        'enum3'
    ]
)
```

