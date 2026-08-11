
# Update Component Request

## Structure

`UpdateComponentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component` | [`UpdateComponent`](../../doc/models/update-component.md) | Required | - |

## Example

```python
from advancedbilling.models.item_category import ItemCategory
from advancedbilling.models.update_component import UpdateComponent
from advancedbilling.models.update_component_request import UpdateComponentRequest

update_component_request = UpdateComponentRequest(
    component=UpdateComponent(
        handle='handle4',
        name='name8',
        description='description2',
        accounting_code='accounting_code4',
        taxable=False,
        item_category=ItemCategory.ENUM_BUSINESS_SOFTWARE
    )
)
```

