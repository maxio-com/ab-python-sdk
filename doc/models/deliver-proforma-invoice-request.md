
# Deliver Proforma Invoice Request

## Structure

`DeliverProformaInvoiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_emails` | `List[str]` | Optional | - |
| `cc_recipient_emails` | `List[str]` | Optional | - |
| `bcc_recipient_emails` | `List[str]` | Optional | - |

## Example

```python
from advancedbilling.models.deliver_proforma_invoice_request import DeliverProformaInvoiceRequest

deliver_proforma_invoice_request = DeliverProformaInvoiceRequest(
    recipient_emails=[
        'recipient_emails9',
        'recipient_emails0'
    ],
    cc_recipient_emails=[
        'cc_recipient_emails2',
        'cc_recipient_emails3',
        'cc_recipient_emails4'
    ],
    bcc_recipient_emails=[
        'bcc_recipient_emails8'
    ]
)
```

