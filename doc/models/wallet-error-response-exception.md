
# Wallet Error Response Exception

The JSON error body returned by every wallet, transaction, adjustment, purchase, and Wallet Product endpoint for `400`, `404`, `409`, `422`, `500`, and `503` responses. A `403` is not JSON; it is the plain text `403 Forbidden`.

## Structure

`WalletErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | `List[str]` | Required | Human-readable messages. These may be reworded, so match on `code` instead. |
| `code` | `str` | Required | A stable, machine-readable reason, for example `wallet_depleted`, `wallet_not_found`, `wallet_product_not_found`, `price_point_archived`, `kind_invalid`, or `parameter_missing`. Failures that come from record validation, such as a field that fails a model rule, report `validation_failed`. |
| `invoice_uid` | `str` | Optional | Returned only by Create Wallet Purchase with `purchase_paid_but_uncredited`, `purchase_declined_invoice_open`, `purchase_invoice_left_open` and `purchase_payment_outcome_unknown`: the uid of the invoice the purchase created. Check it before buying again. |
| `invoice_number` | `str` | Optional | Returned alongside `invoice_uid`: the number of the invoice the purchase created. |

## Example

```python
try:
    # make the API call
except WalletErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

