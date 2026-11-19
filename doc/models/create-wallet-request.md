
# Create Wallet Request

## Structure

`CreateWalletRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet` | [`Wallet1`](../../doc/models/wallet-1.md) | Required | - |

## Example

```python
from advancedbilling.models.create_wallet_request import CreateWalletRequest
from advancedbilling.models.wallet_1 import Wallet1
from advancedbilling.models.wallet_hard_stop_overflow import WalletHardStopOverflow

create_wallet_request = CreateWalletRequest(
    wallet=Wallet1(
        subscription_id=94,
        wallet_product_id=154,
        name='name6',
        depletion_policy='depletion_policy4',
        hard_stop_overflow=WalletHardStopOverflow.DISCARD,
        meter_id=146,
        conversion_rate='String9',
        initial_balance='String1'
    )
)
```

