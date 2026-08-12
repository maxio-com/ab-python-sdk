"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: D410, E501, E101, D206
from apimatic_core.authentication.multiple.single_auth import (
    Single,
)
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter

from advancedbilling.api_helper import APIHelper
from advancedbilling.configuration import Server
from advancedbilling.controllers.base_controller import (
    BaseController,
)
from advancedbilling.exceptions.single_string_error_response_exception import (
    SingleStringErrorResponseException,
)
from advancedbilling.http.http_method_enum import (
    HttpMethodEnum,
)
from advancedbilling.models.referral_validation_response import (
    ReferralValidationResponse,
)


class ReferralCodesController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize ReferralCodesController object."""
        super(ReferralCodesController, self).__init__(config)

    def validate_referral_code(self,
                               code):
        """Perform a GET request to /referral_codes/validate.json.

        Validates whether a referral code is valid and applicable within your site.
        This method is useful for validating referral codes that are entered by a
        customer.
        For more information, see [Understanding
        Referrals](https://docs.maxio.com/hc/en-us/articles/24286981223693-Understandi
        ng-Referrals) in the product documentation.

        Args:
            code (str): The referral code you are trying to validate

        Returns:
            ReferralValidationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/referral_codes/validate.json")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("code")
                .value(code)
                .is_required(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ReferralValidationResponse.from_dictionary)
            .local_error_template("404",
                "Invalid referral code.",
                SingleStringErrorResponseException),
        ).execute()
