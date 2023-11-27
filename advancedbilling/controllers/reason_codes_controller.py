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
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from advancedbilling.models.reason_code_response import ReasonCodeResponse
from advancedbilling.models.reason_codes_json_response import ReasonCodesJsonResponse
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.exceptions.api_exception import APIException


class ReasonCodesController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(ReasonCodesController, self).__init__(config)

    def create_reason_code(self,
                           body=None):
        """Does a POST request to /reason_codes.json.

        # Reason Codes Intro
        ReasonCodes are a way to gain a high level view of why your customers
        are cancelling the subcription to your product or service.
        Add a set of churn reason codes to be displayed in-app and/or the
        Chargify Billing Portal. As your subscribers decide to cancel their
        subscription, learn why they decided to cancel.
        ## Reason Code Documentation
        Full documentation on how Reason Codes operate within Chargify can be
        located under the following links.
        [Churn Reason
        Codes](https://chargify.zendesk.com/hc/en-us/articles/4407896775579#chu
        rn-reason-codes)
        ## Create Reason Code
        This method gives a merchant the option to create a reason codes for a
        given Site.

        Args:
            body (CreateReasonCodeRequest, optional): TODO: type description
                here.

        Returns:
            ReasonCodeResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/reason_codes.json')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ReasonCodeResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()

    def list_reason_codes(self,
                          options=dict()):
        """Does a GET request to /reason_codes.json.

        This method gives a merchant the option to retrieve a list of all of
        the current churn codes for a given site.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    page -- int -- Result records are organized in pages. By
                        default, the first page of results is displayed. The
                        page parameter specifies a page number of results to
                        fetch. You can start navigating through the pages to
                        consume the results. You do this by passing in a page
                        parameter. Retrieve the next page by adding ?page=2 to
                        the query string. If there are no results to return,
                        then an empty result set will be returned. Use in
                        query `page=1`.
                    per_page -- int -- This parameter indicates how many
                        records to fetch in each request. Default value is 20.
                        The maximum allowed values is 200; any per_page value
                        over 200 will be changed to 200. Use in query
                        `per_page=200`.

        Returns:
            List[ReasonCodeResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/reason_codes.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ReasonCodeResponse.from_dictionary)
        ).execute()

    def read_reason_code(self,
                         reason_code_id):
        """Does a GET request to /reason_codes/{reason_code_id}.json.

        This method gives a merchant the option to retrieve a list of a
        particular code for a given Site by providing the unique numerical ID
        of the code.

        Args:
            reason_code_id (int): The Chargify id of the reason code

        Returns:
            ReasonCodeResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/reason_codes/{reason_code_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('reason_code_id')
                            .value(reason_code_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ReasonCodeResponse.from_dictionary)
            .local_error('404', 'Not Found', APIException)
        ).execute()

    def update_reason_code(self,
                           reason_code_id,
                           body=None):
        """Does a PUT request to /reason_codes/{reason_code_id}.json.

        This method gives a merchant the option to update an existing reason
        code for a given site.

        Args:
            reason_code_id (int): The Chargify id of the reason code
            body (UpdateReasonCodeRequest, optional): TODO: type description
                here.

        Returns:
            ReasonCodeResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/reason_codes/{reason_code_id}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('reason_code_id')
                            .value(reason_code_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ReasonCodeResponse.from_dictionary)
            .local_error('404', 'Not Found', APIException)
        ).execute()

    def delete_reason_code(self,
                           reason_code_id):
        """Does a DELETE request to /reason_codes/{reason_code_id}.json.

        This method gives a merchant the option to delete one reason code from
        the Churn Reason Codes. This code will be immediately removed. This
        action is not reversable.

        Args:
            reason_code_id (int): The Chargify id of the reason code

        Returns:
            ReasonCodesJsonResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/reason_codes/{reason_code_id}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('reason_code_id')
                            .value(reason_code_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ReasonCodesJsonResponse.from_dictionary)
            .local_error('404', 'Not Found', APIException)
        ).execute()
