
# Component

## Structure

`Component`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The unique ID assigned to the component by Chargify. This ID can be used to fetch the component from the API. |
| `name` | `str` | Optional | The name of the Component, suitable for display on statements. i.e. Text Messages. |
| `handle` | `str` | Optional | The component API handle |
| `pricing_scheme` | `str` | Optional | The handle for the pricing scheme. Available options: per_unit, volume, tiered, stairstep. See [Price Bracket Rules](https://chargify.zendesk.com/hc/en-us/articles/4407755865883#price-bracket-rules) for an overview of pricing schemes. |
| `unit_name` | `str` | Optional | The name of the unit that the component’s usage is measured in. i.e. message |
| `unit_price` | `str` | Optional | The amount the customer will be charged per unit. This field is only populated for ‘per_unit’ pricing schemes, otherwise it may be null. |
| `product_family_id` | `int` | Optional | The id of the Product Family to which the Component belongs |
| `product_family_name` | `str` | Optional | The name of the Product Family to which the Component belongs |
| `price_per_unit_in_cents` | `int` | Optional | deprecated - use unit_price instead |
| `kind` | [`ComponentKind`](../../doc/models/component-kind.md) | Optional | A handle for the component type |
| `archived` | `bool` | Optional | Boolean flag describing whether a component is archived or not. |
| `taxable` | `bool` | Optional | Boolean flag describing whether a component is taxable or not. |
| `description` | `str` | Optional | The description of the component. |
| `default_price_point_id` | `int` | Optional | - |
| `prices` | [`List[ComponentPrice]`](../../doc/models/component-price.md) | Optional | An array of price brackets. If the component uses the ‘per_unit’ pricing scheme, this array will be empty. |
| `price_point_count` | `int` | Optional | Count for the number of price points associated with the component |
| `price_points_url` | `str` | Optional | URL that points to the location to read the existing price points via GET request |
| `default_price_point_name` | `str` | Optional | - |
| `tax_code` | `str` | Optional | A string representing the tax code related to the component type. This is especially important when using the Avalara service to tax based on locale. This attribute has a max length of 10 characters. |
| `recurring` | `bool` | Optional | - |
| `upgrade_charge` | `str` | Optional | - |
| `downgrade_credit` | `str` | Optional | - |
| `created_at` | `str` | Optional | Timestamp indicating when this component was created |
| `updated_at` | `str` | Optional | Timestamp indicating when this component was updated |
| `archived_at` | `str` | Optional | Timestamp indicating when this component was archived |
| `hide_date_range_on_invoice` | `bool` | Optional | (Only available on Relationship Invoicing sites) Boolean flag describing if the service date range should show for the component on generated invoices. |
| `allow_fractional_quantities` | `bool` | Optional | - |
| `item_category` | [`ItemCategory`](../../doc/models/item-category.md) | Optional | One of the following: Business Software, Consumer Software, Digital Services, Physical Goods, Other |
| `use_site_exchange_rate` | `bool` | Optional | - |
| `accounting_code` | `str` | Optional | E.g. Internal ID or SKU Number |
| `event_based_billing_metric_id` | `int` | Optional | (Only for Event Based Components) This is an ID of a metric attached to the component. This metric is used to bill upon collected events. |

## Example (as JSON)

```json
{
  "item_category": "Business Software",
  "id": 24,
  "name": "name2",
  "handle": "handle8",
  "pricing_scheme": "pricing_scheme6",
  "unit_name": "unit_name4"
}
```

