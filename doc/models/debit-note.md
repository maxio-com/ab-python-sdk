
# Debit Note

## Structure

`DebitNote`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | Unique identifier for the debit note. It is generated automatically by Chargify and has the prefix "db_" followed by alphanumeric characters. |
| `site_id` | `int` | Optional | ID of the site to which the debit note belongs. |
| `customer_id` | `int` | Optional | ID of the customer to which the debit note belongs. |
| `subscription_id` | `int` | Optional | ID of the subscription that generated the debit note. |
| `number` | `int` | Optional | A unique, identifier that appears on the debit note and in places it is referenced. |
| `sequence_number` | `int` | Optional | A monotonically increasing number assigned to debit notes as they are created. |
| `origin_credit_note_uid` | `str` | Optional | Unique identifier for the connected credit note. It is generated automatically by Chargify and has the prefix "cn_" followed by alphanumeric characters.<br><br>While the UID is long and not appropriate to show to customers, the number is usually shorter and consumable by the customer and the merchant alike. |
| `origin_credit_note_number` | `str` | Optional | A unique, identifying string of the connected credit note. |
| `issue_date` | `date` | Optional | Date the document was issued to the customer. This is the date that the document was made available for payment.<br><br>The format is "YYYY-MM-DD". |
| `applied_date` | `date` | Optional | Debit notes are applied to invoices to offset invoiced amounts - they adjust the amount due. This field is the date the debit note document became fully applied to the invoice.<br><br>The format is "YYYY-MM-DD". |
| `due_date` | `date` | Optional | Date the document is due for payment. The format is "YYYY-MM-DD". |
| `status` | [`DebitNoteStatus`](../../doc/models/debit-note-status.md) | Optional | Current status of the debit note. |
| `memo` | `str` | Optional | The memo printed on debit note, which is a description of the reason for the debit. |
| `role` | [`DebitNoteRole`](../../doc/models/debit-note-role.md) | Optional | The role of the debit note. |
| `currency` | `str` | Optional | The ISO 4217 currency code (3 character string) representing the currency of the credit note amount fields. |
| `seller` | [`InvoiceSeller`](../../doc/models/invoice-seller.md) | Optional | Information about the seller (merchant) listed on the masthead of the debit note. |
| `customer` | [`InvoiceCustomer`](../../doc/models/invoice-customer.md) | Optional | Information about the customer who is owner or recipient the debited subscription. |
| `billing_address` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Optional | The billing address of the debited subscription. |
| `shipping_address` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Optional | The shipping address of the debited subscription. |
| `line_items` | [`List[CreditNoteLineItem]`](../../doc/models/credit-note-line-item.md) | Optional | Line items on the debit note. |
| `discounts` | [`List[InvoiceDiscount]`](../../doc/models/invoice-discount.md) | Optional | - |
| `taxes` | [`List[InvoiceTax]`](../../doc/models/invoice-tax.md) | Optional | - |
| `refunds` | [`List[InvoiceRefund]`](../../doc/models/invoice-refund.md) | Optional | - |

## Example (as JSON)

```json
{
  "uid": "uid2",
  "site_id": 112,
  "customer_id": 224,
  "subscription_id": 40,
  "number": 172
}
```

