
# Create Product Family

## Structure

`CreateProductFamily`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `handle` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `surcharging` | `bool` | Optional | Whether surcharging applies to this product family. Defaults to `true` when omitted. Only applied on sites where surcharging is enabled. |

## Example

```python
from advancedbilling.models.create_product_family import CreateProductFamily

create_product_family = CreateProductFamily(
    name='name6',
    handle='handle2',
    description='description4',
    surcharging=False
)
```

