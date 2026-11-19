
# Active Wallets

## Structure

`ActiveWallets`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total` | `int` | Required | Total count of active wallets drawing on this product. |
| `sample` | [`List[WalletProductActiveWallet]`](../../doc/models/wallet-product-active-wallet.md) | Required | Up to 50 of the most recently created active wallets, newest first. |

## Example

```python
from advancedbilling.models.active_wallets import ActiveWallets
from advancedbilling.models.wallet_product_active_wallet import WalletProductActiveWallet

active_wallets = ActiveWallets(
    total=164,
    sample=[
        WalletProductActiveWallet(
            id=180,
            subscription_id=34,
            company_name='company_name4',
            purchase_mechanism='purchase_mechanism8',
            price_point_name='price_point_name8'
        )
    ]
)
```

