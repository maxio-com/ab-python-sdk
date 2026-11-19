
# Wallet Purchase Preview Response

## Structure

`WalletPurchasePreviewResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet_purchase_previews` | [`List[WalletPurchasePreview]`](../../doc/models/wallet-purchase-preview.md) | Required | - |

## Example

```python
from advancedbilling.models.wallet_purchase_preview import WalletPurchasePreview
from advancedbilling.models.wallet_purchase_preview_response import WalletPurchasePreviewResponse

wallet_purchase_preview_response = WalletPurchasePreviewResponse(
    wallet_purchase_previews=[
        WalletPurchasePreview(
            price_point_id=126,
            currency='USD',
            quantity='quantity6',
            amount='amount2'
        )
    ]
)
```

