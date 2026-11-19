
# Wallet Purchase Preview

A price quote for a purchase, without charging anything.

## Structure

`WalletPurchasePreview`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point_id` | `int` | Required | - |
| `currency` | `str` | Required | The three-letter currency code the `amount` is denominated in, matching the subscription's currency. |
| `quantity` | `str` | Required | The number of units the quote is for, as a decimal string. |
| `amount` | `str` | Required | The price for `quantity` units at this price point, as a decimal string. |

## Example

```python
from advancedbilling.models.wallet_purchase_preview import WalletPurchasePreview

wallet_purchase_preview = WalletPurchasePreview(
    price_point_id=230,
    currency='USD',
    quantity='quantity6',
    amount='amount2'
)
```

