
# Refund Consolidated Invoice

Refund consolidated invoice.

## Structure

`RefundConsolidatedInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `memo` | `str` | Required | A description for the refund |
| `payment_id` | `int` | Required | The ID of the payment to be refunded |
| `segment_uids` | List[str] \| str | Required | This is a container for one-of cases. |
| `external` | `bool` | Optional | Flag that marks refund as external (no money is returned to the customer). Defaults to `false`. |
| `apply_credit` | `bool` | Optional | If set to true, creates credit and applies it to an invoice. Defaults to `false`. |
| `amount` | `str` | Optional | The amount of payment to be refunded in decimal format. Example: "10.50". This will default to the full amount of the payment if not provided. |

## Example

```python
from advancedbilling.models.refund_consolidated_invoice import RefundConsolidatedInvoice

refund_consolidated_invoice = RefundConsolidatedInvoice(
    memo='memo2',
    payment_id=66,
    segment_uids=[
        'String2',
        'String3',
        'String4'
    ],
    external=False,
    apply_credit=False,
    amount='amount0'
)
```

