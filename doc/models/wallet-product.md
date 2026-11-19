
# Wallet Product

## Structure

`WalletProduct`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `unit_name` | `str` | Required | The name of the unit the Wallet Product's usage is measured in, for example `tokens`. |
| `handle` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `taxable` | `bool` | Optional | - |
| `tax_code` | `str` | Optional | - |
| `accounting_code` | `str` | Optional | - |
| `item_category` | [`ItemCategory`](../../doc/models/item-category.md) | Optional | One of the following: Business Software, Consumer Software, Digital Services, Physical Goods, Other |
| `price_point` | [`WalletProductPricePointAttributes`](../../doc/models/wallet-product-price-point-attributes.md) | Optional | Creates one price point for the Wallet Product in the same call. Ignored if `price_points` is also sent. |
| `price_points` | [`List[WalletProductPricePointAttributes]`](../../doc/models/wallet-product-price-point-attributes.md) | Optional | Creates several price points for the Wallet Product in the same call, winning over `price_point` if both are sent. The first price point created becomes the Wallet Product's default. The whole call is one transaction: if any price point in the array fails validation, nothing is created, including the Wallet Product itself. |

## Example

```python
from advancedbilling.models.item_category import ItemCategory
from advancedbilling.models.wallet_product import WalletProduct

wallet_product = WalletProduct(
    name='name0',
    unit_name='unit_name2',
    handle='handle6',
    description='description0',
    taxable=False,
    tax_code='tax_code8',
    accounting_code='accounting_code6',
    item_category=ItemCategory.ENUM_BUSINESS_SOFTWARE
)
```

