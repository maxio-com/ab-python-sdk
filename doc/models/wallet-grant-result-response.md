
# Wallet Grant Result Response

Returned by an adjustment: the ledger row written, plus the wallet's new balance.

## Structure

`WalletGrantResultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet_transactions` | [`List[WalletTransaction]`](../../doc/models/wallet-transaction.md) | Required | - |
| `balance` | `str` | Required | The wallet's new balance, as a decimal string. |

## Example

```python
from advancedbilling.models.wallet_grant_result_response import WalletGrantResultResponse
from advancedbilling.models.wallet_transaction import WalletTransaction

wallet_grant_result_response = WalletGrantResultResponse(
    wallet_transactions=[
        WalletTransaction(
            id=140,
            wallet_id=244,
            kind='grant',
            amount='-30.0',
            grant_id=160
        )
    ],
    balance='balance8'
)
```

