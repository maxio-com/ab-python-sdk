
# Metafield

## Structure

`Metafield`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `scope` | [`MetafieldScope`](../../doc/models/metafield-scope.md) | Optional | Warning: When updating a metafield's scope attribute, all scope attributes must be passed. Partially complete scope attributes will override the existing settings. |
| `data_count` | `int` | Optional | The amount of subscriptions this metafield has been applied to in Advanced Billing. |
| `input_type` | [`MetafieldInput`](../../doc/models/metafield-input.md) | Optional | Indicates the type of metafield. A text metafield allows any string value. Dropdown and radio metafields have a set of values that can be selected. Defaults to 'text'. |
| `enum` | str \| List[str] \| None | Optional | This is a container for one-of cases. |

## Example

```python
from advancedbilling.models.include_option import IncludeOption
from advancedbilling.models.metafield import Metafield
from advancedbilling.models.metafield_input import MetafieldInput
from advancedbilling.models.metafield_scope import MetafieldScope

metafield = Metafield(
    id=242,
    name='name4',
    scope=MetafieldScope(
        csv=IncludeOption.EXCLUDE,
        invoices=IncludeOption.EXCLUDE,
        statements=IncludeOption.EXCLUDE,
        portal=IncludeOption.EXCLUDE,
        public_show=IncludeOption.EXCLUDE
    ),
    data_count=26,
    input_type=MetafieldInput.BALANCE_TRACKER
)
```

