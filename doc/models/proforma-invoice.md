
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
| `created_at` | `str` | Optional | - |
| `delivery_date` | `str` | Optional | - |
| `status` | `str` | Optional | - |
| `collection_method` | `str` | Optional | - |
| `payment_instructions` | `str` | Optional | - |
| `currency` | `str` | Optional | - |
| `consolidation_level` | `str` | Optional | - |
| `product_name` | `str` | Optional | - |
| `product_family_name` | `str` | Optional | - |
| `role` | `str` | Optional | - |
| `seller` | [`InvoiceSeller`](../../doc/models/invoice-seller.md) | Optional | Information about the seller (merchant) listed on the masthead of the invoice. |
| `customer` | [`ProformaCustomer`](../../doc/models/proforma-customer.md) | Optional | - |
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
| `line_items` | [`List[ProformaInvoiceLineItem]`](../../doc/models/proforma-invoice-line-item.md) | Optional | - |
| `discounts` | `List[object]` | Optional | - |
| `taxes` | `List[object]` | Optional | - |
| `credits` | `List[object]` | Optional | - |
| `payments` | `List[object]` | Optional | - |
| `custom_fields` | `List[object]` | Optional | - |
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

