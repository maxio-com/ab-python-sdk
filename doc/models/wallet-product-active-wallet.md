
# Wallet Product Active Wallet

One active wallet drawing on this Wallet Product.

## Structure

`WalletProductActiveWallet`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The Advanced Billing id of the wallet. |
| `subscription_id` | `int` | Optional | - |
| `company_name` | `str` | Optional | The owning customer's organization name, falling back to their full name, then to `"Customer #<id>"`. `"Customer"` (with no id) when the wallet's subscription has no customer at all. |
| `purchase_mechanism` | `str` | Optional | See the same field on [Wallet Product Usage Template](../../doc/models/wallet-product-usage-template.md). The same caveats apply. |
| `price_point_name` | `str` | Optional | - |
| `currency` | `str` | Optional | - |
| `active` | `bool` | Optional | `false` when the wallet's Feature is archived. |

## Example

```python
from advancedbilling.models.wallet_product_active_wallet import WalletProductActiveWallet

wallet_product_active_wallet = WalletProductActiveWallet(
    id=204,
    subscription_id=58,
    company_name='company_name4',
    purchase_mechanism='purchase_mechanism8',
    price_point_name='price_point_name8'
)
```

