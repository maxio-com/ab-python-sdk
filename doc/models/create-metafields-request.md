
# Create Metafields Request

## Structure

`CreateMetafieldsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metafields` | [Create Metafield](../../doc/models/create-metafield.md) \| List[[Create Metafield](../../doc/models/create-metafield.md)] | Required | This is a container for one-of cases. |

## Example

```python
from advancedbilling.models.create_metafield import CreateMetafield
from advancedbilling.models.create_metafields_request import CreateMetafieldsRequest
from advancedbilling.models.include_option import IncludeOption
from advancedbilling.models.metafield_input import MetafieldInput
from advancedbilling.models.metafield_scope import MetafieldScope

create_metafields_request = CreateMetafieldsRequest(
    metafields=CreateMetafield(
        name='my_field',
        scope=MetafieldScope(
            csv=IncludeOption.EXCLUDE,
            invoices=IncludeOption.EXCLUDE,
            statements=IncludeOption.EXCLUDE,
            portal=IncludeOption.EXCLUDE,
            public_show=IncludeOption.EXCLUDE,
            public_edit=IncludeOption.EXCLUDE
        ),
        input_type=MetafieldInput.TEXT,
        enum=[
            'string'
        ]
    )
)
```

