
# Create Wallet Purchase Request

Purchases prepaid units for the wallet at a price point, charging the subscription's payment method.

## Structure

`CreateWalletPurchaseRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `purchase` | [`Purchase`](../../doc/models/purchase.md) | Required | - |

## Example

```python
from advancedbilling.models.create_wallet_purchase_request import CreateWalletPurchaseRequest
from advancedbilling.models.purchase import Purchase

create_wallet_purchase_request = CreateWalletPurchaseRequest(
    purchase=Purchase(
        quantity='String5',
        price_point_id=20,
        memo='memo2'
    )
)
```

