
# Update Component

## Structure

`UpdateComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `handle` | `str` | Optional | - |
| `name` | `str` | Optional | The name of the Component, suitable for display on statements. e.g., Text Messages. |
| `description` | `str` | Optional | The description of the component. |
| `accounting_code` | `str` | Optional | - |
| `taxable` | `bool` | Optional | Boolean flag describing whether a component is taxable or not. |
| `tax_code` | `str` | Optional | A string representing the tax code related to the component type. This is especially important when using AvaTax to tax based on locale. This attribute has a max length of 25 characters. |
| `item_category` | [`ItemCategory`](../../doc/models/item-category.md) | Optional | One of the following: Business Software, Consumer Software, Digital Services, Physical Goods, Other |
| `display_on_hosted_page` | `bool` | Optional | - |
| `upgrade_charge` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided. |
| `unspsc_code` | `str` | Optional | (Optional) Custom UNSPSC commodity code for Level 3/CEDP payment data. When set, this value is sent as the commodity code on invoice line items for this component instead of the default derived from item_category. |

## Example

```python
from advancedbilling.models.item_category import ItemCategory
from advancedbilling.models.update_component import UpdateComponent

update_component = UpdateComponent(
    handle='handle2',
    name='name6',
    description='description4',
    accounting_code='accounting_code2',
    taxable=False,
    item_category=ItemCategory.ENUM_BUSINESS_SOFTWARE
)
```

