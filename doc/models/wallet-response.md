
# Wallet Response

## Structure

`WalletResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet` | [`Wallet`](../../doc/models/wallet.md) | Required | A balance, denominated in the unit of a Wallet Product, owned by a subscription. Grants and recurring funding schedules are embedded so a single read shows the full balance breakdown. |

## Example

```python
from advancedbilling.models.owner_type import OwnerType
from advancedbilling.models.wallet import Wallet
from advancedbilling.models.wallet_response import WalletResponse

wallet_response = WalletResponse(
    wallet=Wallet(
        id=240,
        owner_type=OwnerType.SUBSCRIPTION,
        owner_id=60,
        name='name6',
        wallet_product_id=232,
        unit='tokens',
        balance='150.0',
        posted_balance='150.0',
        depletion_policy='hard_stop'
    )
)
```

