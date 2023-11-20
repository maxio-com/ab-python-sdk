
# Renewal Preview

## Structure

`RenewalPreview`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `next_assessment_at` | `str` | Optional | The timestamp for the subscription’s next renewal |
| `subtotal_in_cents` | `long\|int` | Optional | An integer representing the amount of the total pre-tax, pre-discount charges that will be assessed at the next renewal |
| `total_tax_in_cents` | `long\|int` | Optional | An integer representing the total tax charges that will be assessed at the next renewal |
| `total_discount_in_cents` | `long\|int` | Optional | An integer representing the amount of the coupon discounts that will be applied to the next renewal |
| `total_in_cents` | `long\|int` | Optional | An integer representing the total amount owed, less any discounts, that will be assessed at the next renewal |
| `existing_balance_in_cents` | `long\|int` | Optional | An integer representing the amount of the subscription’s current balance |
| `total_amount_due_in_cents` | `long\|int` | Optional | An integer representing the existing_balance_in_cents plus the total_in_cents |
| `uncalculated_taxes` | `bool` | Optional | A boolean indicating whether or not additional taxes will be calculated at the time of renewal. This will be true if you are using Avalara and the address of the subscription is in one of your defined taxable regions. |
| `line_items` | [`List[RenewalPreviewLineItem]`](../../doc/models/renewal-preview-line-item.md) | Optional | An array of objects representing the individual transactions that will be created at the next renewal |

## Example (as JSON)

```json
{
  "next_assessment_at": "next_assessment_at0",
  "subtotal_in_cents": 160,
  "total_tax_in_cents": 28,
  "total_discount_in_cents": 34,
  "total_in_cents": 48
}
```

