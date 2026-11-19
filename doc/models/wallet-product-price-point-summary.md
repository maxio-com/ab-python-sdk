
# Wallet Product Price Point Summary

A summary of the Wallet Product's default price point, for rendering a catalog listing without a separate price points call.

## Structure

`WalletProductPricePointSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `archived_count` | `int` | Optional | Number of archived price points on this Wallet Product. |
| `pricing_scheme` | `str` | Optional | The default price point's pricing scheme. `null` if the Wallet Product has no default price point. |
| `tier_count` | `int` | Optional | Number of price brackets on the default price point. A `per_unit` scheme always stores exactly one synthesized bracket, so this is `1` for `per_unit`, not `0`. |
| `entry_price` | `str` | Optional | The unit price of the default price point's first bracket, as a decimal string. `null` if there are no brackets. |
| `final_price` | `str` | Optional | The unit price of the default price point's last bracket, as a decimal string. `null` if there are no brackets. |

## Example

```python
from advancedbilling.models.wallet_product_price_point_summary import WalletProductPricePointSummary

wallet_product_price_point_summary = WalletProductPricePointSummary(
    archived_count=2,
    pricing_scheme='pricing_scheme2',
    tier_count=44,
    entry_price='entry_price4',
    final_price='final_price0'
)
```

