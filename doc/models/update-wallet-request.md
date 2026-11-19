
# Update Wallet Request

## Structure

`UpdateWalletRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet` | [`Wallet2`](../../doc/models/wallet-2.md) | Required | - |

## Example

```python
from advancedbilling.models.update_wallet_request import UpdateWalletRequest
from advancedbilling.models.wallet_2 import Wallet2

update_wallet_request = UpdateWalletRequest(
    wallet=Wallet2(
        name='name6'
    )
)
```

