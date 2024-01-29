
# Invoice

## Structure

`Invoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `long\|int` | Optional | - |
| `uid` | `str` | Optional | Unique identifier for the invoice. It is generated automatically by Chargify and has the prefix "inv_" followed by alphanumeric characters. |
| `site_id` | `int` | Optional | ID of the site to which the invoice belongs. |
| `customer_id` | `int` | Optional | ID of the customer to which the invoice belongs. |
| `subscription_id` | `int` | Optional | ID of the subscription that generated the invoice. |
| `number` | `str` | Optional | A unique, identifying string that appears on the invoice and in places the invoice is referenced.<br><br>While the UID is long and not appropriate to show to customers, the number is usually shorter and consumable by the customer and the merchant alike. |
| `sequence_number` | `int` | Optional | A monotonically increasing number assigned to invoices as they are created.  This number is unique within a site and can be used to sort and order invoices. |
| `transaction_time` | `datetime` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `issue_date` | `date` | Optional | Date the invoice was issued to the customer.  This is the date that the invoice was made available for payment.<br><br>The format is `"YYYY-MM-DD"`. |
| `due_date` | `date` | Optional | Date the invoice is due.<br><br>The format is `"YYYY-MM-DD"`. |
| `paid_date` | `date` | Optional | Date the invoice became fully paid.<br><br>If partial payments are applied to the invoice, this date will not be present until payment has been made in full.<br><br>The format is `"YYYY-MM-DD"`. |
| `status` | [`InvoiceStatus`](../../doc/models/invoice-status.md) | Optional | The current status of the invoice. See [Invoice Statuses](https://chargify.zendesk.com/hc/en-us/articles/4407737494171#line-item-breakdowns) for more. |
| `role` | [`InvoiceRole`](../../doc/models/invoice-role.md) | Optional | - |
| `parent_invoice_id` | `int` | Optional | - |
| `collection_method` | [`CollectionMethod`](../../doc/models/collection-method.md) | Optional | The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options are - `invoice`, `automatic`. For current Relationship Invoicing Architecture valid options are - `remittance`, `automatic`, `prepaid`.<br>**Default**: `'automatic'` |
| `payment_instructions` | `str` | Optional | A message that is printed on the invoice when it is marked for remittance collection. It is intended to describe to the customer how they may make payment, and is configured by the merchant. |
| `currency` | `str` | Optional | The ISO 4217 currency code (3 character string) representing the currency of invoice transaction. |
| `consolidation_level` | [`InvoiceConsolidationLevel`](../../doc/models/invoice-consolidation-level.md) | Optional | Consolidation level of the invoice, which is applicable to invoice consolidation.  It will hold one of the following values:<br><br>* "none": A normal invoice with no consolidation.<br>* "child": An invoice segment which has been combined into a consolidated invoice.<br>* "parent": A consolidated invoice, whose contents are composed of invoice segments.<br><br>"Parent" invoices do not have lines of their own, but they have subtotals and totals which aggregate the member invoice segments.<br><br>See also the [invoice consolidation documentation](https://chargify.zendesk.com/hc/en-us/articles/4407746391835). |
| `parent_invoice_uid` | `str` | Optional | For invoices with `consolidation_level` of `child`, this specifies the UID of the parent (consolidated) invoice. |
| `subscription_group_id` | `int` | Optional | - |
| `parent_invoice_number` | `int` | Optional | For invoices with `consolidation_level` of `child`, this specifies the number of the parent (consolidated) invoice. |
| `group_primary_subscription_id` | `int` | Optional | For invoices with `consolidation_level` of `parent`, this specifies the ID of the subscription which was the primary subscription of the subscription group that generated the invoice. |
| `product_name` | `str` | Optional | The name of the product subscribed when the invoice was generated. |
| `product_family_name` | `str` | Optional | The name of the product family subscribed when the invoice was generated. |
| `seller` | [`InvoiceSeller`](../../doc/models/invoice-seller.md) | Optional | Information about the seller (merchant) listed on the masthead of the invoice. |
| `customer` | [`InvoiceCustomer`](../../doc/models/invoice-customer.md) | Optional | Information about the customer who is owner or recipient the invoiced subscription. |
| `payer` | [`InvoicePayer`](../../doc/models/invoice-payer.md) | Optional | - |
| `recipient_emails` | `List[str]` | Optional | **Constraints**: *Maximum Items*: `5` |
| `net_terms` | `int` | Optional | - |
| `memo` | `str` | Optional | The memo printed on invoices of any collection type.  This message is in control of the merchant. |
| `billing_address` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Optional | The invoice billing address. |
| `shipping_address` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Optional | The invoice shipping address. |
| `subtotal_amount` | `str` | Optional | Subtotal of the invoice, which is the sum of all line items before discounts or taxes. |
| `discount_amount` | `str` | Optional | Total discount applied to the invoice. |
| `tax_amount` | `str` | Optional | Total tax on the invoice. |
| `total_amount` | `str` | Optional | The invoice total, which is `subtotal_amount - discount_amount + tax_amount`.' |
| `credit_amount` | `str` | Optional | The amount of credit (from credit notes) applied to this invoice.<br><br>Credits offset the amount due from the customer. |
| `refund_amount` | `str` | Optional | - |
| `paid_amount` | `str` | Optional | The amount paid on the invoice by the customer. |
| `due_amount` | `str` | Optional | Amount due on the invoice, which is `total_amount - credit_amount - paid_amount`. |
| `line_items` | [`List[InvoiceLineItem]`](../../doc/models/invoice-line-item.md) | Optional | Line items on the invoice. |
| `discounts` | [`List[InvoiceDiscount]`](../../doc/models/invoice-discount.md) | Optional | - |
| `taxes` | [`List[InvoiceTax]`](../../doc/models/invoice-tax.md) | Optional | - |
| `credits` | [`List[InvoiceCredit]`](../../doc/models/invoice-credit.md) | Optional | - |
| `refunds` | [`List[InvoiceRefund]`](../../doc/models/invoice-refund.md) | Optional | - |
| `payments` | [`List[InvoicePayment]`](../../doc/models/invoice-payment.md) | Optional | - |
| `custom_fields` | [`List[InvoiceCustomField]`](../../doc/models/invoice-custom-field.md) | Optional | - |
| `display_settings` | [`InvoiceDisplaySettings`](../../doc/models/invoice-display-settings.md) | Optional | - |
| `public_url` | `str` | Optional | The public URL of the invoice |
| `previous_balance_data` | [`InvoicePreviousBalance`](../../doc/models/invoice-previous-balance.md) | Optional | - |

## Example (as JSON)

```json
{
  "issue_date": "2024-01-01",
  "due_date": "2024-01-01",
  "paid_date": "2024-01-01",
  "collection_method": "automatic",
  "id": 252,
  "uid": "uid0",
  "site_id": 178,
  "customer_id": 34,
  "subscription_id": 106
}
```

