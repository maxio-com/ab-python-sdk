
# Invoice Line Item 1

## Structure

`InvoiceLineItem1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | Unique identifier for the line item.  Useful when cross-referencing the line against individual discounts in the `discounts` or `taxes` lists. |
| `title` | `str` | Optional | A short descriptor for the charge or item represented by this line. |
| `description` | `str` | Optional | Detailed description for the charge or item represented by this line.  May include proration details in plain text.<br><br>Note: this string may contain line breaks that are hints for the best display format on the invoice. |
| `quantity` | `str` | Optional | The quantity or count of units billed by the line item.<br><br>This is a decimal number represented as a string. (See "About Decimal Numbers".) |
| `unit_price` | `str` | Optional | The price per unit for the line item.<br><br>When tiered pricing was used (i.e. not every unit was actually priced at the same price) this will be the blended average cost per unit and the `tiered_unit_price` field will be set to `true`. |
| `subtotal_amount` | `str` | Optional | The line subtotal, generally calculated as `quantity * unit_price`. This is the canonical amount of record for the line - when rounding differences are in play, `subtotal_amount` takes precedence over the value derived from `quantity * unit_price` (which may not have the proper precision to exactly equal this amount). |
| `discount_amount` | `str` | Optional | The approximate discount applied to just this line.<br><br>The value is approximated in cases where rounding errors make it difficult to apportion exactly a total discount among many lines. Several lines may have been summed prior to applying the discount to arrive at `discount_amount` for the invoice - backing that out to the discount on a single line may introduce rounding or precision errors. |
| `tax_amount` | `str` | Optional | The approximate tax applied to just this line.<br><br>The value is approximated in cases where rounding errors make it difficult to apportion exactly a total tax among many lines. Several lines may have been summed prior to applying the tax rate to arrive at `tax_amount` for the invoice - backing that out to the tax on a single line may introduce rounding or precision errors. |
| `total_amount` | `str` | Optional | The non-canonical total amount for the line.<br><br>`subtotal_amount` is the canonical amount for a line. The invoice `total_amount` is derived from the sum of the line `subtotal_amount`s and discounts or taxes applied thereafter.  Therefore, due to rounding or precision errors, the sum of line `total_amount`s may not equal the invoice `total_amount`. |
| `tiered_unit_price` | `bool` | Optional | When `true`, indicates that the actual pricing scheme for the line was tiered, so the `unit_price` shown is the blended average for all units. |
| `period_range_start` | `date` | Optional | Start date for the period covered by this line. The format is `"YYYY-MM-DD"`.<br><br>* For periodic charges paid in advance, this date will match the billing date, and the end date will be in the future.<br>* For periodic charges paid in arrears (e.g. metered charges), this date will be the date of the previous billing, and the end date will be the current billing date.<br>* For non-periodic charges, this date and the end date will match. |
| `period_range_end` | `date` | Optional | End date for the period covered by this line. The format is `"YYYY-MM-DD"`.<br><br>* For periodic charges paid in advance, this date will match the next (future) billing date.<br>* For periodic charges paid in arrears (e.g. metered charges), this date will be the date of the current billing date.<br>* For non-periodic charges, this date and the start date will match. |
| `transaction_id` | `int` | Optional | - |
| `product_id` | `int` | Optional | The ID of the product subscribed when the charge was made.<br><br>This may be set even for component charges, so true product-only (non-component) charges will also have a nil `component_id`. |
| `product_version` | `int` | Optional | The version of the product subscribed when the charge was made. |
| `component_id` | `int` | Optional | The ID of the component being billed. Will be `nil` for non-component charges. |
| `price_point_id` | `int` | Optional | The price point ID of the component being billed. Will be `nil` for non-component charges. |
| `hide` | `bool` | Optional | - |
| `component_cost_data` | [`ComponentCostData1`](../../doc/models/component-cost-data-1.md) | Optional | - |
| `product_price_point_id` | `int` | Optional | The price point ID of the line item's product |
| `custom_item` | `bool` | Optional | - |
| `kind` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "uid": "uid8",
  "title": "title4",
  "description": "description8",
  "quantity": "quantity4",
  "unit_price": "unit_price6"
}
```

