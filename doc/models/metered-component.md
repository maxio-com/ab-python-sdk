
# Metered Component

## Structure

`MeteredComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | A name for this component that is suitable for showing customers and displaying on billing statements, ie. "Minutes". |
| `unit_name` | `str` | Required | The name of the unit of measurement for the component. It should be singular since it will be automatically pluralized when necessary. i.e. “message”, which may then be shown as “5 messages” on a subscription’s component line-item |
| `description` | `str` | Optional | A description for the component that will be displayed to the user on the hosted signup page. |
| `handle` | `str` | Optional | A unique identifier for your use that can be used to retrieve this component is subsequent requests.  Must start with a letter or number and may only contain lowercase letters, numbers, or the characters '.', ':', '-', or '_'.<br>**Constraints**: *Pattern*: `^[a-z0-9][a-z0-9\-_:.]*$` |
| `taxable` | `bool` | Optional | Boolean flag describing whether a component is taxable or not. |
| `pricing_scheme` | [Pricing Scheme](../../doc/models/pricing-scheme-enum.md) | Required | This is a container for one-of cases. |
| `prices` | [`List[CreateComponentPrice]`](../../doc/models/create-component-price.md) | Optional | (Not required for ‘per_unit’ pricing schemes) One or more price brackets. See [Price Bracket Rules](https://maxio-chargify.zendesk.com/hc/en-us/articles/5405020625677#price-bracket-rules) for an overview of how price brackets work for different pricing schemes. |
| `upgrade_charge` | `str` | Optional | - |
| `downgrade_credit` | `str` | Optional | - |
| `price_points` | [`List[ComponentPricePointItem]`](../../doc/models/component-price-point-item.md) | Optional | - |
| `unit_price` | str \| float \| None | Optional | This is a container for one-of cases. |
| `tax_code` | `str` | Optional | A string representing the tax code related to the component type. This is especially important when using the Avalara service to tax based on locale. This attribute has a max length of 10 characters. |
| `hide_date_range_on_invoice` | `bool` | Optional | (Only available on Relationship Invoicing sites) Boolean flag describing if the service date range should show for the component on generated invoices. |
| `price_in_cents` | `str` | Optional | deprecated May 2011 - use unit_price instead |

## Example (as JSON)

```json
{
  "name": "name4",
  "unit_name": "unit_name6",
  "description": "description6",
  "handle": "handle0",
  "taxable": false,
  "pricing_scheme": "volume",
  "prices": [
    {
      "starting_quantity": 64,
      "unit_price": "String3"
    }
  ],
  "upgrade_charge": "upgrade_charge4"
}
```

