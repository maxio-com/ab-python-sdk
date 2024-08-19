
# Proforma Invoice

## Structure

`ProformaInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `site_id` | `int` | Optional | - |
| `customer_id` | `int` | Optional | - |
| `subscription_id` | `int` | Optional | - |
| `number` | `int` | Optional | - |
| `sequence_number` | `int` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `delivery_date` | `date` | Optional | - |
| `status` | [`ProformaInvoiceStatus`](../../doc/models/proforma-invoice-status.md) | Optional | - |
| `collection_method` | [`CollectionMethod`](../../doc/models/collection-method.md) | Optional | The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options are - `invoice`, `automatic`. For current Relationship Invoicing Architecture valid options are - `remittance`, `automatic`, `prepaid`. |
| `payment_instructions` | `str` | Optional | - |
| `currency` | `str` | Optional | - |
| `consolidation_level` | [`InvoiceConsolidationLevel`](../../doc/models/invoice-consolidation-level.md) | Optional | Consolidation level of the invoice, which is applicable to invoice consolidation.  It will hold one of the following values:<br><br>* "none": A normal invoice with no consolidation.<br>* "child": An invoice segment which has been combined into a consolidated invoice.<br>* "parent": A consolidated invoice, whose contents are composed of invoice segments.<br><br>"Parent" invoices do not have lines of their own, but they have subtotals and totals which aggregate the member invoice segments.<br><br>See also the [invoice consolidation documentation](https://maxio.zendesk.com/hc/en-us/articles/24252269909389-Invoice-Consolidation). |
| `product_name` | `str` | Optional | - |
| `product_family_name` | `str` | Optional | - |
| `role` | [`ProformaInvoiceRole`](../../doc/models/proforma-invoice-role.md) | Optional | 'proforma' value is deprecated in favor of proforma_adhoc and proforma_automatic |
| `seller` | [`InvoiceSeller`](../../doc/models/invoice-seller.md) | Optional | Information about the seller (merchant) listed on the masthead of the invoice. |
| `customer` | [`InvoiceCustomer`](../../doc/models/invoice-customer.md) | Optional | Information about the customer who is owner or recipient the invoiced subscription. |
| `memo` | `str` | Optional | - |
| `billing_address` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Optional | - |
| `shipping_address` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Optional | - |
| `subtotal_amount` | `str` | Optional | - |
| `discount_amount` | `str` | Optional | - |
| `tax_amount` | `str` | Optional | - |
| `total_amount` | `str` | Optional | - |
| `credit_amount` | `str` | Optional | - |
| `paid_amount` | `str` | Optional | - |
| `refund_amount` | `str` | Optional | - |
| `due_amount` | `str` | Optional | - |
| `line_items` | [`List[InvoiceLineItem]`](../../doc/models/invoice-line-item.md) | Optional | - |
| `discounts` | [`List[ProformaInvoiceDiscount]`](../../doc/models/proforma-invoice-discount.md) | Optional | - |
| `taxes` | [`List[ProformaInvoiceTax]`](../../doc/models/proforma-invoice-tax.md) | Optional | - |
| `credits` | [`List[ProformaInvoiceCredit]`](../../doc/models/proforma-invoice-credit.md) | Optional | - |
| `payments` | [`List[ProformaInvoicePayment]`](../../doc/models/proforma-invoice-payment.md) | Optional | - |
| `custom_fields` | [`List[InvoiceCustomField]`](../../doc/models/invoice-custom-field.md) | Optional | - |
| `public_url` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "uid": "uid6",
  "site_id": 196,
  "customer_id": 52,
  "subscription_id": 124,
  "number": 0
}
```

