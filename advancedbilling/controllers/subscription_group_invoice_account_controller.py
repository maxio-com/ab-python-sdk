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
from apimatic_core.types.array_serialization_format import SerializationFormats
from apimatic_core.authentication.multiple.single_auth import Single
from advancedbilling.models.subscription_group_prepayment_response import SubscriptionGroupPrepaymentResponse
from advancedbilling.models.list_subscription_group_prepayment_response import ListSubscriptionGroupPrepaymentResponse
from advancedbilling.models.service_credit_response import ServiceCreditResponse
from advancedbilling.models.service_credit import ServiceCredit
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.exceptions.api_exception import APIException


class SubscriptionGroupInvoiceAccountController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(SubscriptionGroupInvoiceAccountController, self).__init__(config)

    def create_subscription_group_prepayment(self,
                                             uid,
                                             body=None):
        """Does a POST request to /subscription_groups/{uid}/prepayments.json.

        A prepayment can be added for a subscription group identified by the
        group's `uid`. This endpoint requires a `amount`, `details`, `method`,
        and `memo`. On success, the prepayment will be added to the group's
        prepayment balance.

        Args:
            uid (str): The uid of the subscription group
            body (SubscriptionGroupPrepaymentRequest, optional): The request
                body parameter.

        Returns:
            SubscriptionGroupPrepaymentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscription_groups/{uid}/prepayments.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionGroupPrepaymentResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def list_prepayments_for_subscription_group(self,
                                                options=dict()):
        """Does a GET request to /subscription_groups/{uid}/prepayments.json.

        This request will list a subscription group's prepayments.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    uid -- str -- The uid of the subscription group
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
                    filter -- ListPrepaymentsFilter -- Filter to use for List
                        Prepayments operations

        Returns:
            ListSubscriptionGroupPrepaymentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscription_groups/{uid}/prepayments.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('uid')
                            .value(options.get('uid', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('filter')
                         .value(options.get('filter', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListSubscriptionGroupPrepaymentResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
        ).execute()

    def issue_subscription_group_service_credit(self,
                                                uid,
                                                body=None):
        """Does a POST request to /subscription_groups/{uid}/service_credits.json.

        Credit can be issued for a subscription group identified by the
        group's `uid`. Credit will be added to the group in the amount
        specified in the request body. The credit will be applied to group
        member invoices as they are generated.

        Args:
            uid (str): The uid of the subscription group
            body (IssueServiceCreditRequest, optional): The request body
                parameter.

        Returns:
            ServiceCreditResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscription_groups/{uid}/service_credits.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServiceCreditResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def deduct_subscription_group_service_credit(self,
                                                 uid,
                                                 body=None):
        """Does a POST request to /subscription_groups/{uid}/service_credit_deductions.json.

        Credit can be deducted for a subscription group identified by the
        group's `uid`. Credit will be deducted from the group in the amount
        specified in the request body.

        Args:
            uid (str): The uid of the subscription group
            body (DeductServiceCreditRequest, optional): The request body
                parameter.

        Returns:
            ServiceCredit: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscription_groups/{uid}/service_credit_deductions.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServiceCredit.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()
