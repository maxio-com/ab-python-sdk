
# Send Invoice Request

## Structure

`SendInvoiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_emails` | `List[str]` | Optional | **Constraints**: *Maximum Items*: `5` |
| `cc_recipient_emails` | `List[str]` | Optional | **Constraints**: *Maximum Items*: `5` |
| `bcc_recipient_emails` | `List[str]` | Optional | **Constraints**: *Maximum Items*: `5` |
| `attachment_urls` | `List[str]` | Optional | Array of URLs to files to attach to the invoice email. Max 10 files, 10MB each.<br><br>**Constraints**: *Maximum Items*: `10` |

## Example

```python
from advancedbilling.models.send_invoice_request import SendInvoiceRequest

send_invoice_request = SendInvoiceRequest(
    recipient_emails=[
        'recipient_emails9',
        'recipient_emails0',
        'recipient_emails1'
    ],
    cc_recipient_emails=[
        'cc_recipient_emails2',
        'cc_recipient_emails3'
    ],
    bcc_recipient_emails=[
        'bcc_recipient_emails2',
        'bcc_recipient_emails1',
        'bcc_recipient_emails0'
    ],
    attachment_urls=[
        'attachment_urls6',
        'attachment_urls7',
        'attachment_urls8'
    ]
)
```

