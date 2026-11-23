
# Create Wallet Transaction Request

## Structure

`CreateWalletTransactionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet_transaction` | [`WalletTransaction1`](../../doc/models/wallet-transaction-1.md) | Required | - |

## Example

```python
from advancedbilling.models.create_wallet_transaction_request import CreateWalletTransactionRequest
from advancedbilling.models.kind_1 import Kind1
from advancedbilling.models.wallet_transaction_1 import WalletTransaction1

create_wallet_transaction_request = CreateWalletTransactionRequest(
    wallet_transaction=WalletTransaction1(
        kind=Kind1.GRANT,
        amount='String5',
        memo='memo6',
        expires_at='expires_at6'
    )
)
```

