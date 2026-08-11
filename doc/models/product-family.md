
# Product Family

## Structure

`ProductFamily`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `handle` | `str` | Optional | - |
| `accounting_code` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `surcharging` | `bool` | Optional | Whether surcharging applies to this product family. Only included on sites where surcharging is enabled. |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `archived_at` | `datetime` | Optional | Timestamp indicating when this product family was archived. `null` if the product family is not archived. |

## Example

```python
from advancedbilling.models.product_family import ProductFamily

product_family = ProductFamily(
    id=14,
    name='name0',
    handle='handle6',
    accounting_code='accounting_code6',
    description='description0'
)
```

