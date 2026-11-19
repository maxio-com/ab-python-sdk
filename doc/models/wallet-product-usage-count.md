
# Wallet Product Usage Count

A rollup of what's using this Wallet Product, for the catalog listing.

## Structure

`WalletProductUsageCount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet_configurations` | `int` | Required | Number of wallet templates billing through this product, whether or not any wallet has been created from them yet. |
| `active_wallets` | `int` | Required | Number of active (non-archived) wallets currently denominated by this product. |

## Example

```python
from advancedbilling.models.wallet_product_usage_count import WalletProductUsageCount

wallet_product_usage_count = WalletProductUsageCount(
    wallet_configurations=218,
    active_wallets=8
)
```

