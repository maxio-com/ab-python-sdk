
# Invoice Event Data

The event data is the data that, when combined with the command, results in the output invoice found in the invoice field.

## Structure

`InvoiceEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | Unique identifier for the credit note application. It is generated automatically by Chargify and has the prefix "cdt_" followed by alphanumeric characters. |
| `credit_note_number` | `str` | Optional | A unique, identifying string that appears on the credit note and in places it is referenced. |
| `credit_note_uid` | `str` | Optional | Unique identifier for the credit note. It is generated automatically by Chargify and has the prefix "cn_" followed by alphanumeric characters. |
| `original_amount` | `str` | Optional | The full, original amount of the credit note. |
| `applied_amount` | `str` | Optional | The amount of the credit note applied to invoice. |
| `transaction_time` | `datetime` | Optional | The time the credit note was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" |
| `memo` | `str` | Optional | The credit note memo. |
| `role` | `str` | Optional | The role of the credit note (e.g. 'general') |
| `consolidated_invoice` | `bool` | Optional | Shows whether it was applied to consolidated invoice or not |
| `applied_credit_notes` | [`List[AppliedCreditNoteData]`](../../doc/models/applied-credit-note-data.md) | Optional | List of credit notes applied to children invoices (if consolidated invoice) |
| `debit_note_number` | `str` | Optional | A unique, identifying string that appears on the debit note and in places it is referenced. |
| `debit_note_uid` | `str` | Optional | Unique identifier for the debit note. It is generated automatically by Chargify and has the prefix "db_" followed by alphanumeric characters. |
| `payment_method` | [Payment Method Apple Pay](../../doc/models/payment-method-apple-pay.md) \| [Payment Method Bank Account](../../doc/models/payment-method-bank-account.md) \| [Payment Method Credit Card](../../doc/models/payment-method-credit-card.md) \| [Payment Method External](../../doc/models/payment-method-external.md) \| [Payment Method Paypal](../../doc/models/payment-method-paypal.md) \| None | Optional | This is a container for any-of cases. |
| `transaction_id` | `int` | Optional | The Chargify id of the original payment |
| `parent_invoice_number` | `int` | Optional | - |
| `remaining_prepayment_amount` | `str` | Optional | - |
| `prepayment` | `bool` | Optional | The flag that shows whether the original payment was a prepayment or not |
| `external` | `bool` | Optional | - |
| `from_collection_method` | `str` | Optional | The previous collection method of the invoice. |
| `to_collection_method` | `str` | Optional | The new collection method of the invoice. |
| `consolidation_level` | [`InvoiceConsolidationLevel`](../../doc/models/invoice-consolidation-level.md) | Optional | Consolidation level of the invoice, which is applicable to invoice consolidation.  It will hold one of the following values:<br><br>* "none": A normal invoice with no consolidation.<br>* "child": An invoice segment which has been combined into a consolidated invoice.<br>* "parent": A consolidated invoice, whose contents are composed of invoice segments.<br><br>"Parent" invoices do not have lines of their own, but they have subtotals and totals which aggregate the member invoice segments.<br><br>See also the [invoice consolidation documentation](https://chargify.zendesk.com/hc/en-us/articles/4407746391835). |
| `from_status` | [`InvoiceStatus`](../../doc/models/invoice-status.md) | Optional | The status of the invoice before event occurence. See [Invoice Statuses](https://chargify.zendesk.com/hc/en-us/articles/4407737494171#line-item-breakdowns) for more. |
| `to_status` | [`InvoiceStatus`](../../doc/models/invoice-status.md) | Optional | The status of the invoice after event occurence. See [Invoice Statuses](https://chargify.zendesk.com/hc/en-us/articles/4407737494171#line-item-breakdowns) for more. |
| `due_amount` | `str` | Optional | Amount due on the invoice, which is `total_amount - credit_amount - paid_amount`. |
| `total_amount` | `str` | Optional | The invoice total, which is `subtotal_amount - discount_amount + tax_amount`.' |
| `apply_credit` | `bool` | Optional | If true, credit was created and applied it to the invoice. |
| `credit_note_attributes` | [`CreditNote1`](../../doc/models/credit-note-1.md) | Optional | - |
| `payment_id` | `int` | Optional | The ID of the payment transaction to be refunded. |
| `refund_amount` | `str` | Optional | The amount of the refund. |
| `refund_id` | `int` | Optional | The ID of the refund transaction. |
| `is_advance_invoice` | `bool` | Optional | If true, the invoice is an advance invoice. |
| `reason` | `str` | Optional | The reason for the void. |

## Example (as JSON)

```json
{
  "uid": "uid0",
  "credit_note_number": "credit_note_number6",
  "credit_note_uid": "credit_note_uid6",
  "original_amount": "original_amount4",
  "applied_amount": "applied_amount8"
}
```

