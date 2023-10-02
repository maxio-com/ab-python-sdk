
# Refund

## Structure

`Refund`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `str` | Optional | The amount to be refunded in decimal format as a string. Example: "10.50". Must not exceed the remaining refundable balance of the payment. |
| `memo` | `str` | Optional | A description that will be attached to the refund |
| `payment_id` | `int` | Optional | The ID of the payment to be refunded |
| `external` | `bool` | Optional | Flag that marks refund as external (no money is returned to the customer). Defaults to `false`. |
| `apply_credit` | `bool` | Optional | If set to true, creates credit and applies it to an invoice. Defaults to `false`. |
| `void_invoice` | `bool` | Optional | If `apply_credit` set to false and refunding full amount, if `void_invoice` set to true, invoice will be voided after refund. Defaults to `false`. |
| `segment_uids` | List[str] \| str \| None | Optional | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "amount": "amount8",
  "memo": "memo0",
  "payment_id": 130,
  "external": false,
  "apply_credit": false
}
```

