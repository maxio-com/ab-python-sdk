# Referral Codes

```python
referral_codes_controller = client.referral_codes
```

## Class Name

`ReferralCodesController`


# Validate Referral Code

Use this method to determine if the referral code is valid and applicable within your Site. This method is useful for validating referral codes that are entered by a customer.

## Referrals Documentation

Full documentation on how to use the referrals feature in the Advanced Billing UI can be located [here](https://maxio.zendesk.com/hc/en-us/sections/24286965611405-Referrals).

## Server Response

If the referral code is valid the status code will be `200` and the referral code will be returned. If the referral code is invalid, a `404` response will be returned.

```python
def validate_referral_code(self,
                          code)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Query, Required | The referral code you are trying to validate |

## Response Type

[`ReferralValidationResponse`](../../doc/models/referral-validation-response.md)

## Example Usage

```python
code = 'code8'

result = referral_codes_controller.validate_referral_code(code)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "referral_code": {
    "id": 1032514,
    "site_id": 31615,
    "subscription_id": 16254270,
    "code": "9b6cdw"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | [`SingleStringErrorResponseException`](../../doc/models/single-string-error-response-exception.md) |

