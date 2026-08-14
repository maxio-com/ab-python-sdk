
# Update Metafields Request

## Structure

`UpdateMetafieldsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metafields` | [Update Metafield](../../doc/models/update-metafield.md) \| List[[Update Metafield](../../doc/models/update-metafield.md)] \| None | Optional | This is a container for one-of cases. |

## Example

```python
from advancedbilling.models.include_option import IncludeOption
from advancedbilling.models.metafield_input import MetafieldInput
from advancedbilling.models.metafield_scope import MetafieldScope
from advancedbilling.models.update_metafield import UpdateMetafield
from advancedbilling.models.update_metafields_request import UpdateMetafieldsRequest

update_metafields_request = UpdateMetafieldsRequest(
    metafields=UpdateMetafield(
        current_name='current_name0',
        name='name6',
        scope=MetafieldScope(
            csv=IncludeOption.EXCLUDE,
            invoices=IncludeOption.EXCLUDE,
            statements=IncludeOption.EXCLUDE,
            portal=IncludeOption.EXCLUDE,
            public_show=IncludeOption.EXCLUDE
        ),
        input_type=MetafieldInput.BALANCE_TRACKER,
        enum=[
            'enum2'
        ]
    )
)
```

