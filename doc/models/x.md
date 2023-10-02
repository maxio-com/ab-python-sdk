
# X

An attribute 'x' would be changed for a number (an index in request array) where the error occured.

In this object, the key represents the field and the value is an array with error messages. In most cases this object would contain just one key.

## Structure

`X`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `base` | `List[str]` | Optional | - |
| `pricing_scheme` | `List[str]` | Optional | - |
| `prices` | `List[str]` | Optional | - |
| `property_values_fingerprint` | `List[str]` | Optional | - |

## Example (as JSON)

```json
{
  "base": [
    "base9",
    "base0",
    "base1"
  ],
  "pricing_scheme": [
    "pricing_scheme9",
    "pricing_scheme0",
    "pricing_scheme1"
  ],
  "prices": [
    "prices7",
    "prices8",
    "prices9"
  ],
  "property_values_fingerprint": [
    "property_values_fingerprint5",
    "property_values_fingerprint6"
  ]
}
```
