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
from advancedbilling.models.proforma_invoice import ProformaInvoice
from advancedbilling.models.list_proforma_invoices_response import ListProformaInvoicesResponse
from advancedbilling.models.signup_proforma_preview_response import SignupProformaPreviewResponse
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.proforma_bad_request_error_response_exception import ProformaBadRequestErrorResponseException
from advancedbilling.exceptions.error_array_map_response_exception import ErrorArrayMapResponseException


class ProformaInvoicesController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(ProformaInvoicesController, self).__init__(config)

    def create_consolidated_proforma_invoice(self,
                                             uid):
        """Does a POST request to /subscription_groups/{uid}/proforma_invoices.json.

        This endpoint will trigger the creation of a consolidated proforma
        invoice asynchronously. It will return a 201 with no message, or a 422
        with any errors. To find and view the new consolidated proforma
        invoice, you may poll the subscription group listing for proforma
        invoices; only one consolidated proforma invoice may be created per
        group at a time.
        If the information becomes outdated, simply void the old consolidated
        proforma invoice and generate a new one.
        ## Restrictions
        Proforma invoices are only available on Relationship Invoicing sites.
        To create a proforma invoice, the subscription must not be prepaid,
        and must be in a live state.

        Args:
            uid (str): The uid of the subscription group

        Returns:
            void: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscription_groups/{uid}/proforma_invoices.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
                            .is_required(True)
                            .should_encode(True))
            .auth(Single('BasicAuth'))
        ).execute()

    def create_proforma_invoice(self,
                                subscription_id):
        """Does a POST request to /subscriptions/{subscription_id}/proforma_invoices.json.

        This endpoint will create a proforma invoice and return it as a
        response. If the information becomes outdated, simply void the old
        proforma invoice and generate a new one.
        If you would like to preview the next billing amounts without
        generating a full proforma invoice, please use the renewal preview
        endpoint.
        ## Restrictions
        Proforma invoices are only available on Relationship Invoicing sites.
        To create a proforma invoice, the subscription must not be in a group,
        must not be prepaid, and must be in a live state.

        Args:
            subscription_id (int): The Chargify id of the subscription

        Returns:
            ProformaInvoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/proforma_invoices.json')
            .http_method(HttpMethodEnum.POST)
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
            .deserialize_into(ProformaInvoice.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def preview_proforma_invoice(self,
                                 subscription_id):
        """Does a POST request to /subscriptions/{subscription_id}/proforma_invoices/preview.json.

        Return a preview of the data that will be included on a given
        subscription's proforma invoice if one were to be generated. It will
        have similar line items and totals as a renewal preview, but the
        response will be presented in the format of a proforma invoice.
        Consequently it will include additional information such as the name
        and addresses that will appear on the proforma invoice.
        The preview endpoint is subject to all the same conditions as the
        proforma invoice endpoint. For example, previews are only available on
        the Relationship Invoicing architecture, and previews cannot be made
        for end-of-life subscriptions.
        If all the data returned in the preview is as expected, you may then
        create a static proforma invoice and send it to your customer. The
        data within a preview will not be saved and will not be accessible
        after the call is made.
        Alternatively, if you have some proforma invoices already, you may
        make a preview call to determine whether any billing information for
        the subscription's upcoming renewal has changed.

        Args:
            subscription_id (int): The Chargify id of the subscription

        Returns:
            ProformaInvoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/proforma_invoices/preview.json')
            .http_method(HttpMethodEnum.POST)
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
            .deserialize_into(ProformaInvoice.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def read_proforma_invoice(self,
                              proforma_invoice_uid):
        """Does a GET request to /proforma_invoices/{proforma_invoice_uid}.json.

        Use this endpoint to read the details of an existing proforma
        invoice.
        ## Restrictions
        Proforma invoices are only available on Relationship Invoicing sites.

        Args:
            proforma_invoice_uid (str): The uid of the proforma invoice

        Returns:
            ProformaInvoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/proforma_invoices/{proforma_invoice_uid}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('proforma_invoice_uid')
                            .value(proforma_invoice_uid)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ProformaInvoice.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
        ).execute()

    def list_proforma_invoices(self,
                               options=dict()):
        """Does a GET request to /subscriptions/{subscription_id}/proforma_invoices.json.

        By default, proforma invoices returned on the index will only include
        totals, not detailed breakdowns for `line_items`, `discounts`,
        `taxes`, `credits`, `payments`, or `custom_fields`. To include
        breakdowns, pass the specific field as a key in the query with a value
        set to `true`.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    subscription_id -- int -- The Chargify id of the
                        subscription
                    start_date -- str -- The beginning date range for the
                        invoice's Due Date, in the YYYY-MM-DD format.
                    end_date -- str -- The ending date range for the invoice's
                        Due Date, in the YYYY-MM-DD format.
                    status -- ProformaInvoiceStatus -- The current status of
                        the invoice.  Allowed Values: draft, open, paid,
                        pending, voided
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
                    direction -- Direction -- The sort direction of the
                        returned invoices.
                    line_items -- bool -- Include line items data
                    discounts -- bool -- Include discounts data
                    taxes -- bool -- Include taxes data
                    credits -- bool -- Include credits data
                    payments -- bool -- Include payments data
                    custom_fields -- bool -- Include custom fields data

        Returns:
            ListProformaInvoicesResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/proforma_invoices.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(options.get('subscription_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('start_date')
                         .value(options.get('start_date', None)))
            .query_param(Parameter()
                         .key('end_date')
                         .value(options.get('end_date', None)))
            .query_param(Parameter()
                         .key('status')
                         .value(options.get('status', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .query_param(Parameter()
                         .key('line_items')
                         .value(options.get('line_items', None)))
            .query_param(Parameter()
                         .key('discounts')
                         .value(options.get('discounts', None)))
            .query_param(Parameter()
                         .key('taxes')
                         .value(options.get('taxes', None)))
            .query_param(Parameter()
                         .key('credits')
                         .value(options.get('credits', None)))
            .query_param(Parameter()
                         .key('payments')
                         .value(options.get('payments', None)))
            .query_param(Parameter()
                         .key('custom_fields')
                         .value(options.get('custom_fields', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListProformaInvoicesResponse.from_dictionary)
        ).execute()

    def preview_signup_proforma_invoice(self,
                                        include=None,
                                        body=None):
        """Does a POST request to /subscriptions/proforma_invoices/preview.json.

        This endpoint is only available for Relationship Invoicing sites. It
        cannot be used to create consolidated proforma invoice previews or
        preview prepaid subscriptions.
        Create a signup preview in the format of a proforma invoice to preview
        costs before a subscription's signup. You have the option of
        optionally previewing the first renewal's costs as well. The proforma
        invoice preview will not be persisted.
        Pass a payload that resembles a subscription create or signup preview
        request. For example, you can specify components, coupons/a referral,
        offers, custom pricing, and an existing customer or payment profile to
        populate a shipping or billing address.
        A product and customer first name, last name, and email are the
        minimum requirements.

        Args:
            include (CreateSignupProformaPreviewInclude, optional): Choose to
                include a proforma invoice preview for the first renewal. Use
                in query `include=next_proforma_invoice`.
            body (CreateSubscriptionRequest, optional): TODO: type description
                here.

        Returns:
            SignupProformaPreviewResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/proforma_invoices/preview.json')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .query_param(Parameter()
                         .key('include')
                         .value(include))
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
            .deserialize_into(SignupProformaPreviewResponse.from_dictionary)
            .local_error_template('400', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ProformaBadRequestErrorResponseException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorArrayMapResponseException)
        ).execute()

    def list_subscription_group_proforma_invoices(self,
                                                  options=dict()):
        """Does a GET request to /subscription_groups/{uid}/proforma_invoices.json.

        Only proforma invoices with a `consolidation_level` of parent are
        returned.
        By default, proforma invoices returned on the index will only include
        totals, not detailed breakdowns for `line_items`, `discounts`,
        `taxes`, `credits`, `payments`, `custom_fields`. To include
        breakdowns, pass the specific field as a key in the query with a value
        set to true.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    uid -- str -- The uid of the subscription group
                    line_items -- bool -- Include line items data
                    discounts -- bool -- Include discounts data
                    taxes -- bool -- Include taxes data
                    credits -- bool -- Include credits data
                    payments -- bool -- Include payments data
                    custom_fields -- bool -- Include custom fields data

        Returns:
            ListProformaInvoicesResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscription_groups/{uid}/proforma_invoices.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('uid')
                            .value(options.get('uid', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('line_items')
                         .value(options.get('line_items', None)))
            .query_param(Parameter()
                         .key('discounts')
                         .value(options.get('discounts', None)))
            .query_param(Parameter()
                         .key('taxes')
                         .value(options.get('taxes', None)))
            .query_param(Parameter()
                         .key('credits')
                         .value(options.get('credits', None)))
            .query_param(Parameter()
                         .key('payments')
                         .value(options.get('payments', None)))
            .query_param(Parameter()
                         .key('custom_fields')
                         .value(options.get('custom_fields', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListProformaInvoicesResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
        ).execute()

    def void_proforma_invoice(self,
                              proforma_invoice_uid,
                              body=None):
        """Does a POST request to /proforma_invoices/{proforma_invoice_uid}/void.json.

        This endpoint will void a proforma invoice that has the status
        "draft".
        ## Restrictions
        Proforma invoices are only available on Relationship Invoicing sites.
        Only proforma invoices that have the appropriate status may be
        reopened. If the invoice identified by {uid} does not have the
        appropriate status, the response will have HTTP status code 422 and an
        error message.
        A reason for the void operation is required to be included in the
        request body. If one is not provided, the response will have HTTP
        status code 422 and an error message.

        Args:
            proforma_invoice_uid (str): The uid of the proforma invoice
            body (VoidInvoiceRequest, optional): TODO: type description here.

        Returns:
            ProformaInvoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/proforma_invoices/{proforma_invoice_uid}/void.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('proforma_invoice_uid')
                            .value(proforma_invoice_uid)
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
            .deserialize_into(ProformaInvoice.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def create_signup_proforma_invoice(self,
                                       body=None):
        """Does a POST request to /subscriptions/proforma_invoices.json.

        This endpoint is only available for Relationship Invoicing sites. It
        cannot be used to create consolidated proforma invoices or preview
        prepaid subscriptions.
        Create a proforma invoice to preview costs before a subscription's
        signup. Like other proforma invoices, it can be emailed to the
        customer, voided, and publicly viewed on the chargifypay domain.
        Pass a payload that resembles a subscription create or signup preview
        request. For example, you can specify components, coupons/a referral,
        offers, custom pricing, and an existing customer or payment profile to
        populate a shipping or billing address.
        A product and customer first name, last name, and email are the
        minimum requirements. We recommend associating the proforma invoice
        with a customer_id to easily find their proforma invoices, since the
        subscription_id will always be blank.

        Args:
            body (CreateSubscriptionRequest, optional): TODO: type description
                here.

        Returns:
            ProformaInvoice: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/proforma_invoices.json')
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ProformaInvoice.from_dictionary)
            .local_error_template('400', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ProformaBadRequestErrorResponseException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorArrayMapResponseException)
        ).execute()
