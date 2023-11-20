
# Send Invoice Request

## Structure

`SendInvoiceRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `recipient_emails` | `List[str]` | Optional | **Constraints**: *Maximum Items*: `5` |
| `cc_recipient_emails` | `List[str]` | Optional | **Constraints**: *Maximum Items*: `5` |
| `bcc_recipient_emails` | `List[str]` | Optional | **Constraints**: *Maximum Items*: `5` |

## Example (as JSON)

```json
{
  "recipient_emails": [
    "recipient_emails3",
    "recipient_emails4"
  ],
  "cc_recipient_emails": [
    "cc_recipient_emails6",
    "cc_recipient_emails5"
  ],
  "bcc_recipient_emails": [
    "bcc_recipient_emails6"
  ]
}
```

