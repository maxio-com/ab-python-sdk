
# Invoice Payment Application

## Structure

`InvoicePaymentApplication`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_uid` | `str` | Optional | Unique identifier for the paid invoice. It has the prefix "inv_" followed by alphanumeric characters. |
| `application_uid` | `str` | Optional | Unique identifier for the payment. It has the prefix "pmt_" followed by alphanumeric characters. |
| `applied_amount` | `str` | Optional | Dollar amount of the paid invoice. |

## Example (as JSON)

```json
{
  "invoice_uid": "invoice_uid2",
  "application_uid": "application_uid4",
  "applied_amount": "applied_amount6"
}
```

