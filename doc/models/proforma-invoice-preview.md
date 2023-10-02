
# Proforma Invoice Preview

## Structure

`ProformaInvoicePreview`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `site_id` | `float` | Optional | - |
| `customer_id` | `float` | Optional | - |
| `subscription_id` | `float` | Optional | - |
| `number` | `str` | Optional | - |
| `sequence_number` | `int` | Optional | - |
| `created_at` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `delivery_date` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `status` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `collection_method` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `payment_instructions` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `currency` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `consolidation_level` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `product_name` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `product_family_name` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `role` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `seller` | [`InvoiceSeller`](../../doc/models/invoice-seller.md) | Optional | Information about the seller (merchant) listed on the masthead of the invoice. |
| `customer` | [`ProformaCustomer`](../../doc/models/proforma-customer.md) | Optional | - |
| `memo` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `billing_address` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Optional | - |
| `shipping_address` | [`InvoiceAddress`](../../doc/models/invoice-address.md) | Optional | - |
| `subtotal_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `discount_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `tax_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `total_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `credit_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `paid_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `refund_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `due_amount` | `str` | Optional | **Constraints**: *Minimum Length*: `1` |
| `line_items` | [`List[ProformaInvoiceLineItem]`](../../doc/models/proforma-invoice-line-item.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `discounts` | [`List[ProformaInvoiceDiscount]`](../../doc/models/proforma-invoice-discount.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `taxes` | [`List[ProformaInvoiceTax]`](../../doc/models/proforma-invoice-tax.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `credits` | [`List[ProformaInvoiceCredit]`](../../doc/models/proforma-invoice-credit.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `payments` | [`List[ProformaInvoicePayment]`](../../doc/models/proforma-invoice-payment.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `custom_fields` | [`List[ProformaCustomField]`](../../doc/models/proforma-custom-field.md) | Optional | **Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `public_url` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "uid": "uid2",
  "site_id": 127.58,
  "customer_id": 51.9,
  "subscription_id": 206.22,
  "number": "number0"
}
```

