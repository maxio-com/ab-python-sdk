
# Proforma Invoice Payment

## Structure

`ProformaInvoicePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `memo` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `original_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `applied_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `prepayment` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "memo": "memo4",
  "original_amount": "original_amount4",
  "applied_amount": "applied_amount8",
  "prepayment": false
}
```

