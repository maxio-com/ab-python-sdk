
# Prepaid Usage Component

## Structure

`PrepaidUsageComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | A name for this component that is suitable for showing customers and displaying on billing statements, ie. "Minutes". |
| `unit_name` | `str` | Required | The name of the unit of measurement for the component. It should be singular since it will be automatically pluralized when necessary. i.e. “message”, which may then be shown as “5 messages” on a subscription’s component line-item |
| `description` | `str` | Optional | A description for the component that will be displayed to the user on the hosted signup page. |
| `handle` | `str` | Optional | A unique identifier for your use that can be used to retrieve this component is subsequent requests.  Must start with a letter or number and may only contain lowercase letters, numbers, or the characters '.', ':', '-', or '_'.<br><br>**Constraints**: *Pattern*: `^[a-z0-9][a-z0-9\-_:.]*$` |
| `taxable` | `bool` | Optional | Boolean flag describing whether a component is taxable or not. |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Required | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `prices` | [`List[Price]`](../../doc/models/price.md) | Optional | (Not required for ‘per_unit’ pricing schemes) One or more price brackets. See [Price Bracket Rules](https://maxio.zendesk.com/hc/en-us/articles/24261149166733-Component-Pricing-Schemes#price-bracket-rules) for an overview of how price brackets work for different pricing schemes. |
| `upgrade_charge` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.<br>Available values: `full`, `prorated`, `none`. |
| `downgrade_credit` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.<br>Available values: `full`, `prorated`, `none`. |
| `price_points` | [`List[CreatePrepaidUsageComponentPricePoint]`](../../doc/models/create-prepaid-usage-component-price-point.md) | Optional | - |
| `unit_price` | str \| float \| None | Optional | This is a container for one-of cases. |
| `tax_code` | `str` | Optional | A string representing the tax code related to the component type. This is especially important when using the Avalara service to tax based on locale. This attribute has a max length of 10 characters. |
| `hide_date_range_on_invoice` | `bool` | Optional | (Only available on Relationship Invoicing sites) Boolean flag describing if the service date range should show for the component on generated invoices. |
| `overage_pricing` | [`OveragePricing`](../../doc/models/overage-pricing.md) | Required | - |
| `rollover_prepaid_remainder` | `bool` | Optional | Boolean which controls whether or not remaining units should be rolled over to the next period |
| `renew_prepaid_allocation` | `bool` | Optional | Boolean which controls whether or not the allocated quantity should be renewed at the beginning of each period |
| `expiration_interval` | `float` | Optional | (only for prepaid usage components where rollover_prepaid_remainder is true) The number of `expiration_interval_unit`s after which rollover amounts should expire |
| `expiration_interval_unit` | [`ExpirationIntervalUnit`](../../doc/models/expiration-interval-unit.md) | Optional | - |
| `display_on_hosted_page` | `bool` | Optional | - |
| `allow_fractional_quantities` | `bool` | Optional | - |
| `public_signup_page_ids` | `List[int]` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name2",
  "unit_name": "unit_name4",
  "description": "description8",
  "handle": "handle8",
  "taxable": false,
  "pricing_scheme": "stairstep",
  "prices": [
    {
      "starting_quantity": 242,
      "ending_quantity": 40,
      "unit_price": 23.26
    },
    {
      "starting_quantity": 242,
      "ending_quantity": 40,
      "unit_price": 23.26
    }
  ],
  "upgrade_charge": "prorated",
  "overage_pricing": {
    "pricing_scheme": "stairstep",
    "prices": [
      {
        "starting_quantity": 242,
        "ending_quantity": 40,
        "unit_price": 23.26
      }
    ]
  }
}
```

