
# Wallet Product Usage Response

## Structure

`WalletProductUsageResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet_templates` | [`List[WalletProductUsageTemplate]`](../../doc/models/wallet-product-usage-template.md) | Required | Wallet templates billing through this product at its default price point. |
| `price_point_overrides` | [`List[WalletProductUsageTemplate]`](../../doc/models/wallet-product-usage-template.md) | Required | Wallet templates billing through this product at a price point other than the default. |
| `active_wallets` | [`ActiveWallets`](../../doc/models/active-wallets.md) | Required | - |

## Example

```python
from advancedbilling.models.active_wallets import ActiveWallets
from advancedbilling.models.wallet_product_active_wallet import WalletProductActiveWallet
from advancedbilling.models.wallet_product_usage_response import WalletProductUsageResponse
from advancedbilling.models.wallet_product_usage_template import WalletProductUsageTemplate

wallet_product_usage_response = WalletProductUsageResponse(
    wallet_templates=[
        WalletProductUsageTemplate(
            plan_name='plan_name4',
            wallet_template_name='wallet_template_name2',
            unit_name='unit_name4',
            purchase_mechanism='purchase_mechanism2',
            price_point_name='price_point_name4'
        )
    ],
    price_point_overrides=[
        WalletProductUsageTemplate(
            plan_name='plan_name0',
            wallet_template_name='wallet_template_name2',
            unit_name='unit_name0',
            purchase_mechanism='purchase_mechanism8',
            price_point_name='price_point_name8'
        )
    ],
    active_wallets=ActiveWallets(
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
)
```

