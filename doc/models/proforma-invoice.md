
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
| `status` | `str` | Optional | - |
| `collection_method` | `str` | Optional | - |
| `payment_instructions` | `str` | Optional | - |
| `currency` | `str` | Optional | - |
| `consolidation_level` | `str` | Optional | - |
| `product_name` | `str` | Optional | - |
| `product_family_name` | `str` | Optional | - |
| `role` | `str` | Optional | - |
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

