
# Wallet Transactions List Response

## Structure

`WalletTransactionsListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `wallet_transactions` | [`List[WalletTransaction]`](../../doc/models/wallet-transaction.md) | Required | - |
| `meta` | [`ListPublicKeysMeta`](../../doc/models/list-public-keys-meta.md) | Required | - |

## Example

```python
from advancedbilling.models.list_public_keys_meta import ListPublicKeysMeta
from advancedbilling.models.wallet_transaction import WalletTransaction
from advancedbilling.models.wallet_transactions_list_response import WalletTransactionsListResponse

wallet_transactions_list_response = WalletTransactionsListResponse(
    wallet_transactions=[
        WalletTransaction(
            id=140,
            wallet_id=244,
            kind='grant',
            amount='-30.0',
            grant_id=160
        )
    ],
    meta=ListPublicKeysMeta(
        total_count=150,
        current_page=126,
        total_pages=138,
        per_page=152
    )
)
```

