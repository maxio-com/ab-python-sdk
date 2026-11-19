
# Wallet Purchase Result Response

## Structure

`WalletPurchaseResultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet_purchases` | [`List[WalletPurchase]`](../../doc/models/wallet-purchase.md) | Required | - |
| `balance` | `str` | Required | The wallet's new balance, as a decimal string. |

## Example

```python
import dateutil.parser

from advancedbilling.models.wallet_purchase import WalletPurchase
from advancedbilling.models.wallet_purchase_result_response import WalletPurchaseResultResponse

wallet_purchase_result_response = WalletPurchaseResultResponse(
    wallet_purchases=[
        WalletPurchase(
            id=244,
            price_point_id=134,
            invoice_uid='invoice_uid0',
            quantity='quantity6',
            expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ],
    balance='balance6'
)
```

