
# Wallet Product 1

## Structure

`WalletProduct1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `taxable` | `bool` | Optional | - |
| `tax_code` | `str` | Optional | - |
| `accounting_code` | `str` | Optional | - |
| `item_category` | [`ItemCategory`](../../doc/models/item-category.md) | Optional | One of the following: Business Software, Consumer Software, Digital Services, Physical Goods, Other |

## Example

```python
from advancedbilling.models.item_category import ItemCategory
from advancedbilling.models.wallet_product_1 import WalletProduct1

wallet_product_1 = WalletProduct1(
    name='name8',
    description='description8',
    taxable=False,
    tax_code='tax_code6',
    accounting_code='accounting_code4',
    item_category=ItemCategory.ENUM_BUSINESS_SOFTWARE
)
```

