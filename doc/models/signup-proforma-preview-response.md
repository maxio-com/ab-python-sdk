
# Signup Proforma Preview Response

## Structure

`SignupProformaPreviewResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `proforma_invoice_preview` | [`SignupProformaPreview`](../../doc/models/signup-proforma-preview.md) | Required | - |

## Example

```python
from advancedbilling.models.proforma_invoice import ProformaInvoice
from advancedbilling.models.signup_proforma_preview import SignupProformaPreview
from advancedbilling.models.signup_proforma_preview_response import SignupProformaPreviewResponse

signup_proforma_preview_response = SignupProformaPreviewResponse(
    proforma_invoice_preview=SignupProformaPreview(
        current_proforma_invoice=ProformaInvoice(
            uid='uid6',
            site_id=72,
            customer_id=184,
            subscription_id=0,
            number=132
        ),
        next_proforma_invoice=ProformaInvoice(
            uid='uid8',
            site_id=212,
            customer_id=68,
            subscription_id=140,
            number=16
        )
    )
)
```

