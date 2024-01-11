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
from advancedbilling.models.account_balances import AccountBalances
from advancedbilling.models.create_prepayment_response import CreatePrepaymentResponse
from advancedbilling.models.prepayments_response import PrepaymentsResponse
from advancedbilling.models.service_credit import ServiceCredit
from advancedbilling.models.prepayment_response import PrepaymentResponse
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.exceptions.refund_prepayment_base_errors_response_exception import RefundPrepaymentBaseErrorsResponseException
from advancedbilling.exceptions.refund_prepayment_aggregated_errors_response_exception import RefundPrepaymentAggregatedErrorsResponseException


class SubscriptionInvoiceAccountController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(SubscriptionInvoiceAccountController, self).__init__(config)

    def read_account_balances(self,
                              subscription_id):
        """Does a GET request to /subscriptions/{subscription_id}/account_balances.json.

        Returns the `balance_in_cents` of the Subscription's Pending Discount,
        Service Credit, and Prepayment accounts, as well as the sum of the
        Subscription's open, payable invoices.

        Args:
            subscription_id (int): The Chargify id of the subscription

        Returns:
            AccountBalances: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/account_balances.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AccountBalances.from_dictionary)
        ).execute()

    def create_prepayment(self,
                          subscription_id,
                          body=None):
        """Does a POST request to /subscriptions/{subscription_id}/prepayments.json.

        ## Create Prepayment
        In order to specify a prepayment made against a subscription, specify
        the `amount, memo, details, method`.
        When the `method` specified is `"credit_card_on_file"`, the prepayment
        amount will be collected using the default credit card payment profile
        and applied to the prepayment account balance.  This is especially
        useful for manual replenishment of prepaid subscriptions.
        Please note that you **can't** pass `amount_in_cents`.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (CreatePrepaymentRequest, optional): TODO: type description
                here.

        Returns:
            CreatePrepaymentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/prepayments.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
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
            .deserialize_into(CreatePrepaymentResponse.from_dictionary)
        ).execute()

    def list_prepayments(self,
                         options=dict()):
        """Does a GET request to /subscriptions/{subscription_id}/prepayments.json.

        This request will list a subscription's prepayments.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    subscription_id -- int -- The Chargify id of the
                        subscription
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
                    filter_date_field -- BasicDateField -- The type of filter
                        you would like to apply to your search. created_at -
                        Time when prepayment was created. application_at -
                        Time when prepayment was applied to invoice. Use in
                        query `filter[date_field]=created_at`.
                    filter_start_date -- date -- The start date (format
                        YYYY-MM-DD) with which to filter the date_field.
                        Returns prepayments with a timestamp at or after
                        midnight (12:00:00 AM) in your site’s time zone on the
                        date specified. Use in query
                        `filter[start_date]=2011-12-15`.
                    filter_end_date -- date -- The end date (format
                        YYYY-MM-DD) with which to filter the date_field.
                        Returns prepayments with a timestamp up to and
                        including 11:59:59PM in your site’s time zone on the
                        date specified. Use in query
                        `filter[end_date]=2011-12-15`.

        Returns:
            PrepaymentsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/prepayments.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(options.get('subscription_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('filter[date_field]')
                         .value(options.get('filter_date_field', None)))
            .query_param(Parameter()
                         .key('filter[start_date]')
                         .value(options.get('filter_start_date', None)))
            .query_param(Parameter()
                         .key('filter[end_date]')
                         .value(options.get('filter_end_date', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PrepaymentsResponse.from_dictionary)
            .local_error('401', 'Unauthorized', APIException)
            .local_error('403', 'Forbidden', APIException)
            .local_error('404', 'Not Found', APIException)
        ).execute()

    def issue_service_credit(self,
                             subscription_id,
                             body=None):
        """Does a POST request to /subscriptions/{subscription_id}/service_credits.json.

        Credit will be added to the subscription in the amount specified in
        the request body. The credit is subsequently applied to the next
        generated invoice.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (IssueServiceCreditRequest, optional): TODO: type description
                here.

        Returns:
            ServiceCredit: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/service_credits.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
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
        ).execute()

    def deduct_service_credit(self,
                              subscription_id,
                              body=None):
        """Does a POST request to /subscriptions/{subscription_id}/service_credit_deductions.json.

        Credit will be removed from the subscription in the amount specified
        in the request body. The credit amount being deducted must be equal to
        or less than the current credit balance.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (DeductServiceCreditRequest, optional): TODO: type
                description here.

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/service_credit_deductions.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).execute()

    def refund_prepayment(self,
                          subscription_id,
                          prepayment_id,
                          body=None):
        """Does a POST request to /subscriptions/{subscription_id}/prepayments/{prepayment_id}/refunds.json.

        This endpoint will refund, completely or partially, a particular
        prepayment applied to a subscription. The `prepayment_id` will be the
        account transaction ID of the original payment. The prepayment must
        have some amount remaining in order to be refunded.
        The amount may be passed either as a decimal, with `amount`, or an
        integer in cents, with `amount_in_cents`.

        Args:
            subscription_id (int): The Chargify id of the subscription
            prepayment_id (str): id of prepayment
            body (RefundPrepaymentRequest, optional): TODO: type description
                here.

        Returns:
            PrepaymentResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/prepayments/{prepayment_id}/refunds.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('prepayment_id')
                            .value(prepayment_id)
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
            .deserialize_into(PrepaymentResponse.from_dictionary)
            .local_error('400', 'Bad Request', RefundPrepaymentBaseErrorsResponseException)
            .local_error('404', 'Not Found', APIException)
            .local_error('422', 'Unprocessable Entity', RefundPrepaymentAggregatedErrorsResponseException)
        ).execute()
