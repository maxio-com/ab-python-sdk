
# List Metafields Response

## Structure

`ListMetafieldsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_count` | `int` | Optional | - |
| `current_page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `per_page` | `int` | Optional | - |
| `metafields` | [`List[Metafield]`](../../doc/models/metafield.md) | Optional | - |

## Example

```python
from advancedbilling.models.include_option import IncludeOption
from advancedbilling.models.list_metafields_response import ListMetafieldsResponse
from advancedbilling.models.metafield import Metafield
from advancedbilling.models.metafield_input import MetafieldInput
from advancedbilling.models.metafield_scope import MetafieldScope

list_metafields_response = ListMetafieldsResponse(
    total_count=70,
    current_page=46,
    total_pages=58,
    per_page=232,
    metafields=[
        Metafield(
            id=22,
            name='name2',
            scope=MetafieldScope(
                csv=IncludeOption.EXCLUDE,
                invoices=IncludeOption.EXCLUDE,
                statements=IncludeOption.EXCLUDE,
                portal=IncludeOption.EXCLUDE,
                public_show=IncludeOption.EXCLUDE
            ),
            data_count=10,
            input_type=MetafieldInput.BALANCE_TRACKER
        ),
        Metafield(
            id=22,
            name='name2',
            scope=MetafieldScope(
                csv=IncludeOption.EXCLUDE,
                invoices=IncludeOption.EXCLUDE,
                statements=IncludeOption.EXCLUDE,
                portal=IncludeOption.EXCLUDE,
                public_show=IncludeOption.EXCLUDE
            ),
            data_count=10,
            input_type=MetafieldInput.BALANCE_TRACKER
        ),
        Metafield(
            id=22,
            name='name2',
            scope=MetafieldScope(
                csv=IncludeOption.EXCLUDE,
                invoices=IncludeOption.EXCLUDE,
                statements=IncludeOption.EXCLUDE,
                portal=IncludeOption.EXCLUDE,
                public_show=IncludeOption.EXCLUDE
            ),
            data_count=10,
            input_type=MetafieldInput.BALANCE_TRACKER
        )
    ]
)
```

