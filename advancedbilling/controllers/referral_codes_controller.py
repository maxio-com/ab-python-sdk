# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from advancedbilling.api_helper import APIHelper
from advancedbilling.configuration import Server
from advancedbilling.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from advancedbilling.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from advancedbilling.models.referral_validation_response import ReferralValidationResponse
from advancedbilling.exceptions.single_string_error_response_exception import SingleStringErrorResponseException


class ReferralCodesController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(ReferralCodesController, self).__init__(config)

    def validate_referral_code(self,
                               code):
        """Does a GET request to /referral_codes/validate.json.

        Use this method to determine if the referral code is valid and
        applicable within your Site. This method is useful for validating
        referral codes that are entered by a customer.
        ## Referrals Documentation
        Full documentation on how to use the referrals feature in the Chargify
        UI can be located
        [here](https://chargify.zendesk.com/hc/en-us/articles/4407802831643).
        ## Server Response
        If the referral code is valid the status code will be `200` and the
        referral code will be returned. If the referral code is invalid, a
        `404` response will be returned.

        Args:
            code (str): The referral code you are trying to validate

        Returns:
            ReferralValidationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/referral_codes/validate.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('code')
                         .value(code)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ReferralValidationResponse.from_dictionary)
            .local_error_template('404', 'Invalid referral code.', SingleStringErrorResponseException)
        ).execute()
