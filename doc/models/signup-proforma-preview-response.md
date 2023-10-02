
# Signup Proforma Preview Response

## Structure

`SignupProformaPreviewResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `proforma_invoice_preview` | [`SignupProformaPreview`](../../doc/models/signup-proforma-preview.md) | Required | - |

## Example (as JSON)

```json
{
  "proforma_invoice_preview": {
    "current_proforma_invoice": {
      "key1": "val1",
      "key2": "val2"
    },
    "next_proforma_invoice": {
      "key1": "val1",
      "key2": "val2"
    }
  }
}
```

