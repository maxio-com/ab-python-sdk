
# Update Wallet Product Request

Only `name`, `description`, `taxable`, `tax_code`, `accounting_code`, and `item_category` are mutable. `unit_name`, `handle`, `price_point`, and `price_points` are not accepted here: the request still returns `200`, but those fields are silently ignored and nothing about them changes. `handle` stays fixed because it's the Wallet Product's only stable identifier on a surface with no product family in the path; `unit_name` stays fixed because a wallet's behavior snapshots it into the wallet's own `unit` field and never re-derives it.

## Structure

`UpdateWalletProductRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet_product` | [`WalletProduct1`](../../doc/models/wallet-product-1.md) | Required | - |

## Example

```python
from advancedbilling.models.item_category import ItemCategory
from advancedbilling.models.update_wallet_product_request import UpdateWalletProductRequest
from advancedbilling.models.wallet_product_1 import WalletProduct1

update_wallet_product_request = UpdateWalletProductRequest(
    wallet_product=WalletProduct1(
        name='name0',
        description='description0',
        taxable=False,
        tax_code='tax_code8',
        accounting_code='accounting_code6',
        item_category=ItemCategory.ENUM_BUSINESS_SOFTWARE
    )
)
```

