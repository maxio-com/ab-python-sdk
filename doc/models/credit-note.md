
# Credit Note

## Structure

`CreditNote`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | Unique identifier for the credit note. It is generated automatically by Chargify and has the prefix "cn_" followed by alphanumeric characters. |
| `site_id` | `int` | Optional | ID of the site to which the credit note belongs. |
| `customer_id` | `int` | Optional | ID of the customer to which the credit note belongs. |
| `subscription_id` | `int` | Optional | ID of the subscription that generated the credit note. |
| `number` | `str` | Optional | A unique, identifying string that appears on the credit note and in places it is referenced.<br><br>While the UID is long and not appropriate to show to customers, the number is usually shorter and consumable by the customer and the merchant alike. |
| `sequence_number` | `int` | Optional | A monotonically increasing number assigned to credit notes as they are created.  This number is unique within a site and can be used to sort and order credit notes. |
| `issue_date` | `date` | Optional | Date the credit note was issued to the customer.  This is the date that the credit was made available for application, and may come before it is fully applied.<br><br>The format is `"YYYY-MM-DD"`. |
| `applied_date` | `date` | Optional | Credit notes are applied to invoices to offset invoiced amounts - they reduce the amount due. This field is the date the credit note became fully applied to invoices.<br><br>If the credit note has been partially applied, this field will not have a value until it has been fully applied.<br><br>The format is `"YYYY-MM-DD"`. |
| `status` | [`CreditNoteStatus`](../../doc/models/credit-note-status.md) | Optional | Current status of the credit note. |
| `currency` | `str` | Optional | The ISO 4217 currency code (3 character string) representing the currency of the credit note amount fields. |
| `memo` | `str` | Optional | The memo printed on credit note, which is a description of the reason for the credit. |
| `seller` | [`InvoiceSeller`](../../doc/models/invoice-seller.md) | Optional | Information about the seller (merchant) listed on the masthead of the credit note. |
| `customer` | [`InvoiceCustomer`](../../doc/models/invoice-customer.md) | Optional | Information about the customer who is owner or recipient the credited subscription. |
| `billing_address` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Optional | The billing address of the credit subscription. |
| `shipping_address` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Optional | The shipping address of the credited subscription. |
| `subtotal_amount` | `str` | Optional | Subtotal of the credit note, which is the sum of all line items before discounts or taxes. Note that this is a positive amount representing the credit back to the customer. |
| `discount_amount` | `str` | Optional | Total discount applied to the credit note. Note that this is a positive amount representing the discount amount being credited back to the customer (i.e. a credit on an earlier discount). For example, if the original purchase was $1.00 and the original discount was $0.10, a credit of $0.50 of the original purchase (half) would have a discount credit of $0.05 (also half). |
| `tax_amount` | `str` | Optional | Total tax of the credit note. Note that this is a positive amount representing a previously taxex amount being credited back to the customer (i.e. a credit of an earlier tax). For example, if the original purchase was $1.00 and the original tax was $0.10, a credit of $0.50 of the original purchase (half) would also have a tax credit of $0.05 (also half). |
| `total_amount` | `str` | Optional | The credit note total, which is `subtotal_amount - discount_amount + tax_amount`.' |
| `applied_amount` | `str` | Optional | The amount of the credit note that has already been applied to invoices. |
| `remaining_amount` | `str` | Optional | The amount of the credit note remaining to be applied to invoices, which is `total_amount - applied_amount`. |
| `line_items` | [`List[CreditNoteLineItem]`](../../doc/models/credit-note-line-item.md) | Optional | Line items on the credit note. |
| `discounts` | [`List[InvoiceDiscount]`](../../doc/models/invoice-discount.md) | Optional | - |
| `taxes` | [`List[InvoiceTax]`](../../doc/models/invoice-tax.md) | Optional | - |
| `applications` | [`List[CreditNoteApplication]`](../../doc/models/credit-note-application.md) | Optional | - |
| `refunds` | [`List[InvoiceRefund]`](../../doc/models/invoice-refund.md) | Optional | - |
| `origin_invoices` | [`List[OriginInvoice]`](../../doc/models/origin-invoice.md) | Optional | An array of origin invoices for the credit note. Learn more about [Origin Invoice from our docs](https://maxio.zendesk.com/hc/en-us/articles/24252261284749-Credit-Notes-Proration#origin-invoices) |

## Example (as JSON)

```json
{
  "uid": "uid2",
  "site_id": 218,
  "customer_id": 74,
  "subscription_id": 146,
  "number": "number0"
}
```

