
# Product

## Structure

`Product`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | The product name |
| `handle` | `str` | Optional | The product API handle |
| `description` | `str` | Optional | The product description |
| `accounting_code` | `str` | Optional | E.g. Internal ID or SKU Number |
| `request_credit_card` | `bool` | Optional | Deprecated value that can be ignored unless you have legacy hosted pages. For Public Signup Page users, please read this attribute from under the signup page. |
| `expiration_interval` | `int` | Optional | A numerical interval for the length a subscription to this product will run before it expires. See the description of interval for a description of how this value is coupled with an interval unit to calculate the full interval |
| `expiration_interval_unit` | [Extended Interval Unit](../../doc/models/extended-interval-unit.md) \| None | Optional | This is a container for one-of cases. |
| `created_at` | `datetime` | Optional | Timestamp indicating when this product was created |
| `updated_at` | `datetime` | Optional | Timestamp indicating when this product was last updated |
| `price_in_cents` | `long\|int` | Optional | The product price, in integer cents |
| `interval` | `int` | Optional | The numerical interval. i.e. an interval of ‘30’ coupled with an interval_unit of day would mean this product would renew every 30 days |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the interval unit for this product, either month or day |
| `initial_charge_in_cents` | `long\|int` | Optional | The up front charge you have specified. |
| `trial_price_in_cents` | `long\|int` | Optional | The price of the trial period for a subscription to this product, in integer cents. |
| `trial_interval` | `int` | Optional | A numerical interval for the length of the trial period of a subscription to this product. See the description of interval for a description of how this value is coupled with an interval unit to calculate the full interval |
| `trial_interval_unit` | [Interval Unit](../../doc/models/interval-unit.md) \| None | Optional | This is a container for one-of cases. |
| `archived_at` | `datetime` | Optional | Timestamp indicating when this product was archived |
| `require_credit_card` | `bool` | Optional | Boolean that controls whether a payment profile is required to be entered for customers wishing to sign up on this product. |
| `return_params` | `str` | Optional | - |
| `taxable` | `bool` | Optional | - |
| `update_return_url` | `str` | Optional | The url to which a customer will be returned after a successful account update |
| `initial_charge_after_trial` | `bool` | Optional | - |
| `version_number` | `int` | Optional | The version of the product |
| `update_return_params` | `str` | Optional | The parameters will append to the url after a successful account update. See [help documentation](https://help.chargify.com/products/product-editing.html#return-parameters-after-account-update) |
| `product_family` | [`ProductFamily`](../../doc/models/product-family.md) | Optional | - |
| `public_signup_pages` | [`List[PublicSignupPage]`](../../doc/models/public-signup-page.md) | Optional | - |
| `product_price_point_name` | `str` | Optional | - |
| `request_billing_address` | `bool` | Optional | A boolean indicating whether to request a billing address on any Self-Service Pages that are used by subscribers of this product. |
| `require_billing_address` | `bool` | Optional | A boolean indicating whether a billing address is required to add a payment profile, especially at signup. |
| `require_shipping_address` | `bool` | Optional | A boolean indicating whether a shipping address is required for the customer, especially at signup. |
| `tax_code` | `str` | Optional | A string representing the tax code related to the product type. This is especially important when using the Avalara service to tax based on locale. This attribute has a max length of 10 characters. |
| `default_product_price_point_id` | `int` | Optional | - |
| `use_site_exchange_rate` | `bool` | Optional | - |
| `item_category` | `str` | Optional | One of the following: Business Software, Consumer Software, Digital Services, Physical Goods, Other |
| `product_price_point_id` | `int` | Optional | - |
| `product_price_point_handle` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "id": 180,
  "name": "name4",
  "handle": "handle0",
  "description": "description4",
  "accounting_code": "accounting_code0"
}
```

