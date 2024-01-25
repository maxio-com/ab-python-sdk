
# Component

## Structure

`Component`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The unique ID assigned to the component by Chargify. This ID can be used to fetch the component from the API. |
| `name` | `str` | Optional | The name of the Component, suitable for display on statements. i.e. Text Messages. |
| `handle` | `str` | Optional | The component API handle |
| `pricing_scheme` | [Pricing Scheme](../../doc/models/pricing-scheme.md) \| None | Optional | This is a container for one-of cases. |
| `unit_name` | `str` | Optional | The name of the unit that the component’s usage is measured in. i.e. message |
| `unit_price` | `str` | Optional | The amount the customer will be charged per unit. This field is only populated for ‘per_unit’ pricing schemes, otherwise it may be null. |
| `product_family_id` | `int` | Optional | The id of the Product Family to which the Component belongs |
| `product_family_name` | `str` | Optional | The name of the Product Family to which the Component belongs |
| `price_per_unit_in_cents` | `long\|int` | Optional | deprecated - use unit_price instead |
| `kind` | [`ComponentKind`](../../doc/models/component-kind.md) | Optional | A handle for the component type |
| `archived` | `bool` | Optional | Boolean flag describing whether a component is archived or not. |
| `taxable` | `bool` | Optional | Boolean flag describing whether a component is taxable or not. |
| `description` | `str` | Optional | The description of the component. |
| `default_price_point_id` | `int` | Optional | - |
| `overage_prices` | [`List[ComponentPrice]`](../../doc/models/component-price.md) | Optional | An array of price brackets. If the component uses the ‘per_unit’ pricing scheme, this array will be empty. |
| `prices` | [`List[ComponentPrice]`](../../doc/models/component-price.md) | Optional | An array of price brackets. If the component uses the ‘per_unit’ pricing scheme, this array will be empty. |
| `price_point_count` | `int` | Optional | Count for the number of price points associated with the component |
| `price_points_url` | `str` | Optional | URL that points to the location to read the existing price points via GET request |
| `default_price_point_name` | `str` | Optional | - |
| `tax_code` | `str` | Optional | A string representing the tax code related to the component type. This is especially important when using the Avalara service to tax based on locale. This attribute has a max length of 10 characters. |
| `recurring` | `bool` | Optional | - |
| `upgrade_charge` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.<br>Available values: `full`, `prorated`, `none`. |
| `downgrade_credit` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.<br>Available values: `full`, `prorated`, `none`. |
| `created_at` | `datetime` | Optional | Timestamp indicating when this component was created |
| `updated_at` | `datetime` | Optional | Timestamp indicating when this component was updated |
| `archived_at` | `str` | Optional | Timestamp indicating when this component was archived |
| `hide_date_range_on_invoice` | `bool` | Optional | (Only available on Relationship Invoicing sites) Boolean flag describing if the service date range should show for the component on generated invoices. |
| `allow_fractional_quantities` | `bool` | Optional | - |
| `item_category` | [`ItemCategory`](../../doc/models/item-category.md) | Optional | One of the following: Business Software, Consumer Software, Digital Services, Physical Goods, Other |
| `use_site_exchange_rate` | `bool` | Optional | - |
| `accounting_code` | `str` | Optional | E.g. Internal ID or SKU Number |
| `event_based_billing_metric_id` | `int` | Optional | (Only for Event Based Components) This is an ID of a metric attached to the component. This metric is used to bill upon collected events. |
| `interval` | `int` | Optional | The numerical interval. i.e. an interval of ‘30’ coupled with an interval_unit of day would mean this component's default price point would renew every 30 days. This property is only available for sites with Multifrequency enabled. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the interval unit for this component's default price point, either month or day. This property is only available for sites with Multifrequency enabled. |

## Example (as JSON)

```json
{
  "item_category": "Business Software",
  "id": 24,
  "name": "name2",
  "handle": "handle8",
  "pricing_scheme": "tiered",
  "unit_name": "unit_name4"
}
```

