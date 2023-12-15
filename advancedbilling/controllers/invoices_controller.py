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
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.list_invoices_response import ListInvoicesResponse
from advancedbilling.models.list_invoice_events_response import ListInvoiceEventsResponse
from advancedbilling.models.multi_invoice_payment_response import MultiInvoicePaymentResponse
from advancedbilling.models.list_credit_notes_response import ListCreditNotesResponse
from advancedbilling.models.credit_note import CreditNote
from advancedbilling.models.payment_response import PaymentResponse
from advancedbilling.models.consolidated_invoice import ConsolidatedInvoice
from advancedbilling.models.invoice_response import InvoiceResponse
from advancedbilling.models.customer_changes_preview_response import CustomerChangesPreviewResponse
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.nested_error_response_exception import NestedErrorResponseException


class InvoicesController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(InvoicesController, self).__init__(config)

    def refund_invoice(self,
                       uid,
                       body=None):
        """Does a POST request to /invoices/{uid}/refunds.json.

        Refund an invoice, segment, or consolidated invoice.
        ## Partial Refund for Consolidated Invoice
        A refund less than the total of a consolidated invoice will be split
        across its segments.
        A $50.00 refund on a $100.00 consolidated invoice with one $60.00 and
        one $40.00 segment, the refunded amount will be applied as 50% of each
        ($30.00 and $20.00 respectively).

        Args:
            uid (str): The unique identifier for the invoice, this does not
                refer to the public facing invoice number.
            body (RefundInvoiceRequest, optional): TODO: type description
                here.

        Returns:
            Invoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{uid}/refunds.json')
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Invoice.from_dictionary)
        ).execute()

    def list_invoices(self,
                      options=dict()):
        """Does a GET request to /invoices.json.

        By default, invoices returned on the index will only include totals,
        not detailed breakdowns for `line_items`, `discounts`, `taxes`,
        `credits`, `payments`, `custom_fields`, or `refunds`. To include
        breakdowns, pass the specific field as a key in the query with a value
        set to `true`.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    start_date -- str -- The start date (format YYYY-MM-DD)
                        with which to filter the date_field. Returns invoices
                        with a timestamp at or after midnight (12:00:00 AM) in
                        your site’s time zone on the date specified.
                    end_date -- str -- The end date (format YYYY-MM-DD) with
                        which to filter the date_field. Returns invoices with
                        a timestamp up to and including 11:59:59PM in your
                        site’s time zone on the date specified.
                    status -- InvoiceStatus -- The current status of the
                        invoice.  Allowed Values: draft, open, paid, pending,
                        voided
                    subscription_id -- int -- The subscription's ID.
                    subscription_group_uid -- str -- The UID of the
                        subscription group you want to fetch consolidated
                        invoices for. This will return a paginated list of
                        consolidated invoices for the specified group.
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
                    refunds -- bool -- Include refunds data
                    date_field -- InvoiceDateField -- The type of filter you
                        would like to apply to your search. Use in query
                        `date_field=issue_date`.
                    start_datetime -- str -- The start date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns invoices with a timestamp at or
                        after exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of start_date. Allowed to be used only along
                        with date_field set to created_at or updated_at.
                    end_datetime -- str -- The end date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns invoices with a timestamp at or
                        before exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of end_date. Allowed to be used only along
                        with date_field set to created_at or updated_at.
                    customer_ids -- List[int] -- Allows fetching invoices with
                        matching customer id based on provided values. Use in
                        query `customer_ids=1,2,3`.
                    number -- List[str] -- Allows fetching invoices with
                        matching invoice number based on provided values. Use
                        in query `number=1234,1235`.
                    product_ids -- List[int] -- Allows fetching invoices with
                        matching line items product ids based on provided
                        values. Use in query `product_ids=23,34`.
                    sort -- InvoiceSortField -- Allows specification of the
                        order of the returned list. Use in query
                        `sort=total_amount`.

        Returns:
            ListInvoicesResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices.json')
            .http_method(HttpMethodEnum.GET)
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
                         .key('subscription_id')
                         .value(options.get('subscription_id', None)))
            .query_param(Parameter()
                         .key('subscription_group_uid')
                         .value(options.get('subscription_group_uid', None)))
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
            .query_param(Parameter()
                         .key('refunds')
                         .value(options.get('refunds', None)))
            .query_param(Parameter()
                         .key('date_field')
                         .value(options.get('date_field', None)))
            .query_param(Parameter()
                         .key('start_datetime')
                         .value(options.get('start_datetime', None)))
            .query_param(Parameter()
                         .key('end_datetime')
                         .value(options.get('end_datetime', None)))
            .query_param(Parameter()
                         .key('customer_ids')
                         .value(options.get('customer_ids', None)))
            .query_param(Parameter()
                         .key('number')
                         .value(options.get('number', None)))
            .query_param(Parameter()
                         .key('product_ids')
                         .value(options.get('product_ids', None)))
            .query_param(Parameter()
                         .key('sort')
                         .value(options.get('sort', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListInvoicesResponse.from_dictionary)
        ).execute()

    def read_invoice(self,
                     uid):
        """Does a GET request to /invoices/{uid}.json.

        Use this endpoint to retrieve the details for an invoice.

        Args:
            uid (str): The unique identifier for the invoice, this does not
                refer to the public facing invoice number.

        Returns:
            Invoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{uid}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Invoice.from_dictionary)
        ).execute()

    def list_invoice_events(self,
                            options=dict()):
        """Does a GET request to /invoices/events.json.

        This endpoint returns a list of invoice events. Each event contains
        event "data" (such as an applied payment) as well as a snapshot of the
        `invoice` at the time of event completion.
        Exposed event types are:
        + issue_invoice
        + apply_credit_note
        + apply_payment
        + refund_invoice
        + void_invoice
        + void_remainder
        + backport_invoice
        + change_invoice_status
        + change_invoice_collection_method
        + remove_payment
        + failed_payment
        + apply_debit_note
        + create_debit_note
        + change_chargeback_status
        Invoice events are returned in ascending order.
        If both a `since_date` and `since_id` are provided in request
        parameters, the `since_date` will be used.
        Note - invoice events that occurred prior to 09/05/2018 __will not__
        contain an `invoice` snapshot.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    since_date -- str -- The timestamp in a format `YYYY-MM-DD
                        T HH:MM:SS Z`, or `YYYY-MM-DD`(in this case, it
                        returns data from the beginning of the day). of the
                        event from which you want to start the search. All the
                        events before the `since_date` timestamp are not
                        returned in the response.
                    since_id -- int -- The ID of the event from which you want
                        to start the search(ID is not included. e.g. if ID is
                        set to 2, then all events with ID 3 and more will be
                        shown) This parameter is not used if since_date is
                        defined.
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
                        records to fetch in each request. Default value is
                        100. The maximum allowed values is 200; any per_page
                        value over 200 will be changed to 200.
                    invoice_uid -- str -- Providing an invoice_uid allows for
                        scoping of the invoice events to a single invoice or
                        credit note.
                    with_change_invoice_status -- str -- Use this parameter if
                        you want to fetch also invoice events with
                        change_invoice_status type.
                    event_types -- List[InvoiceEventType] -- Filter results by
                        event_type. Supply a comma separated list of event
                        types (listed above). Use in query:
                        `event_types=void_invoice,void_remainder`.

        Returns:
            ListInvoiceEventsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/events.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('since_date')
                         .value(options.get('since_date', None)))
            .query_param(Parameter()
                         .key('since_id')
                         .value(options.get('since_id', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('invoice_uid')
                         .value(options.get('invoice_uid', None)))
            .query_param(Parameter()
                         .key('with_change_invoice_status')
                         .value(options.get('with_change_invoice_status', None)))
            .query_param(Parameter()
                         .key('event_types')
                         .value(options.get('event_types', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListInvoiceEventsResponse.from_dictionary)
        ).execute()

    def record_payment_for_invoice(self,
                                   uid,
                                   body=None):
        """Does a POST request to /invoices/{uid}/payments.json.

        This API call should be used when you want to record a payment of a
        given type against a specific invoice. If you would like to apply a
        payment across multiple invoices, you can use the Bulk Payment
        endpoint.
        ## Create a Payment from the existing payment profile
        In order to apply a payment to an invoice using an existing payment
        profile, specify `type` as `payment`, the amount less than the invoice
        total, and the customer's `payment_profile_id`. The ID of a payment
        profile might be retrieved via the Payment Profiles API endpoint.
        ```
        {
          "type": "payment",
          "payment": {
            "amount": 10.00,
            "payment_profile_id": 123
          }
        }
        ```
        ## Create a Payment from the Subscription's Prepayment Account
        In order apply a prepayment to an invoice, specify the `type` as
        `prepayment`, and also the `amount`.
        ```
        {
          "type": "prepayment",
          "payment": {
            "amount": 10.00
          }
        }
        ```
        Note that the `amount` must be less than or equal to the
        Subscription's Prepayment account balance.
        ## Create a Payment from the Subscription's Service Credit Account
        In order to apply a service credit to an invoice, specify the `type`
        as `service_credit`, and also the `amount`:
        ```
        {
          "type": "service_credit",
          "payment": {
            "amount": 10.00
          }
        }
        ```
        Note that Chargify will attempt to fully pay the invoice's
        `due_amount` from the Subscription's Service Credit account. At this
        time, partial payments from a Service Credit Account are only allowed
        for consolidated invoices (subscription groups). Therefore, for normal
        invoices the Service Credit account balance must be greater than or
        equal to the invoice's `due_amount`.

        Args:
            uid (str): The unique identifier for the invoice, this does not
                refer to the public facing invoice number.
            body (CreateInvoicePaymentRequest, optional): TODO: type
                description here.

        Returns:
            Invoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{uid}/payments.json')
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Invoice.from_dictionary)
        ).execute()

    def record_external_payment_for_invoices(self,
                                             body=None):
        """Does a POST request to /invoices/payments.json.

        This API call should be used when you want to record an external
        payment against multiple invoices.
         In order apply a payment to multiple invoices, at minimum, specify
         the `amount` and `applications` (i.e., `invoice_uid` and `amount`)
         details.
        ```
        {
          "payment": {
            "memo": "to pay the bills",
            "details": "check number 8675309",
            "method": "check",
            "amount": "250.00",
            "applications": [
              {
                "invoice_uid": "inv_8gk5bwkct3gqt",
                "amount": "100.00"
              },
              {
                "invoice_uid": "inv_7bc6bwkct3lyt",
                "amount": "150.00"
              }
            ]
          }
        }
        ```
        Note that the invoice payment amounts must be greater than 0. Total
        amount must be greater or equal to invoices payment amount sum.

        Args:
            body (CreateMultiInvoicePaymentRequest, optional): TODO: type
                description here.

        Returns:
            MultiInvoicePaymentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/payments.json')
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
            .deserialize_into(MultiInvoicePaymentResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity', ErrorListResponseException)
        ).execute()

    def list_credit_notes(self,
                          options=dict()):
        """Does a GET request to /credit_notes.json.

        Credit Notes are like inverse invoices. They reduce the amount a
        customer owes.
        By default, the credit notes returned by this endpoint will exclude
        the arrays of `line_items`, `discounts`, `taxes`, `applications`, or
        `refunds`. To include these arrays, pass the specific field as a key
        in the query with a value set to `true`.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    subscription_id -- int -- The subscription's Chargify id
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
                    line_items -- bool -- Include line items data
                    discounts -- bool -- Include discounts data
                    taxes -- bool -- Include taxes data
                    refunds -- bool -- Include refunds data
                    applications -- bool -- Include applications data

        Returns:
            ListCreditNotesResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/credit_notes.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('subscription_id')
                         .value(options.get('subscription_id', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
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
                         .key('refunds')
                         .value(options.get('refunds', None)))
            .query_param(Parameter()
                         .key('applications')
                         .value(options.get('applications', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListCreditNotesResponse.from_dictionary)
        ).execute()

    def read_credit_note(self,
                         uid):
        """Does a GET request to /credit_notes/{uid}.json.

        Use this endpoint to retrieve the details for a credit note.

        Args:
            uid (str): The unique identifier of the credit note

        Returns:
            CreditNote: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/credit_notes/{uid}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CreditNote.from_dictionary)
        ).execute()

    def record_payment_for_subscription(self,
                                        subscription_id,
                                        body=None):
        """Does a POST request to /subscriptions/{subscription_id}/payments.json.

        Record an external payment made against a subscription that will pay
        partially or in full one or more invoices.
        Payment will be applied starting with the oldest open invoice and then
        next oldest, and so on until the amount of the payment is fully
        consumed.
        Excess payment will result in the creation of a prepayment on the
        Invoice Account.
        Only ungrouped or primary subscriptions may be paid using the "bulk"
        payment request.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (RecordPaymentRequest, optional): TODO: type description
                here.

        Returns:
            PaymentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/payments.json')
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaymentResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()

    def reopen_invoice(self,
                       uid):
        """Does a POST request to /invoices/{uid}/reopen.json.

        This endpoint allows you to reopen any invoice with the "canceled"
        status. Invoices enter "canceled" status if they were open at the time
        the subscription was canceled (whether through dunning or an
        intentional cancellation).
        Invoices with "canceled" status are no longer considered to be due.
        Once reopened, they are considered due for payment. Payment may then
        be captured in one of the following ways:
        - Reactivating the subscription, which will capture all open invoices
        (See note below about automatic reopening of invoices.)
        - Recording a payment directly against the invoice
        A note about reactivations: any canceled invoices from the most recent
        active period are automatically opened as a part of the reactivation
        process. Reactivating via this endpoint prior to reactivation is only
        necessary when you wish to capture older invoices from previous
        periods during the reactivation.
        ### Reopening Consolidated Invoices
        When reopening a consolidated invoice, all of its canceled segments
        will also be reopened.

        Args:
            uid (str): The unique identifier for the invoice, this does not
                refer to the public facing invoice number.

        Returns:
            Invoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{uid}/reopen.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Invoice.from_dictionary)
            .local_error('404', 'Not Found', APIException)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()

    def void_invoice(self,
                     uid,
                     body=None):
        """Does a POST request to /invoices/{uid}/void.json.

        This endpoint allows you to void any invoice with the "open" or
        "canceled" status.  It will also allow voiding of an invoice with the
        "pending" status if it is not a consolidated invoice.

        Args:
            uid (str): The unique identifier for the invoice, this does not
                refer to the public facing invoice number.
            body (VoidInvoiceRequest, optional): TODO: type description here.

        Returns:
            Invoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{uid}/void.json')
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Invoice.from_dictionary)
            .local_error('404', 'Not Found', APIException)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()

    def list_invoice_segments(self,
                              options=dict()):
        """Does a GET request to /invoices/{invoice_uid}/segments.json.

        Invoice segments returned on the index will only include totals, not
        detailed breakdowns for `line_items`, `discounts`, `taxes`, `credits`,
        `payments`, or `custom_fields`.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    invoice_uid -- str -- The unique identifier of the
                        consolidated invoice
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
                    direction -- Direction -- Sort direction of the returned
                        segments.

        Returns:
            ConsolidatedInvoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{invoice_uid}/segments.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('invoice_uid')
                            .value(options.get('invoice_uid', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ConsolidatedInvoice.from_dictionary)
        ).execute()

    def create_invoice(self,
                       subscription_id,
                       body=None):
        """Does a POST request to /subscriptions/{subscription_id}/invoices.json.

        This endpoint will allow you to create an ad hoc invoice.
        ### Basic Behavior
        You can create a basic invoice by sending an array of line items to
        this endpoint. Each line item, at a minimum, must include a title, a
        quantity and a unit price. Example:
        ```json
        {
          "invoice": {
            "line_items": [
              {
                "title": "A Product",
                "quantity": 12,
                "unit_price": "150.00"
              }
            ]
          }
        }
        ```
        ### Catalog items
        Instead of creating custom products like in above example, You can
        pass existing items like products, components.
        ```json
        {
          "invoice": {
            "line_items": [
              {
                "product_id": "handle:gold-product",
                "quantity": 2,
              }
            ]
          }
        }
        ```
        The price for each line item will be calculated as well as a total due
        amount for the invoice. Multiple line items can be sent.
        ### Line items types
        When defining line item, You can choose one of 3 types for one line
        item:
        #### Custom item
        Like in basic behavior example above, You can pass `title` and
        `unit_price` for custom item.
        #### Product id
        Product handle (with handle: prefix) or id from the scope of current
        subscription's site can be provided with `product_id`. By default
        `unit_price` is taken from product's default price point, but can be
        overwritten by passing `unit_price` or `product_price_point_id`. If
        `product_id` is used, following fields cannot be used: `title`,
        `component_id`.
        #### Component id
        Component handle (with handle: prefix) or id from the scope of current
        subscription's site can be provided with `component_id`. If
        `component_id` is used, following fields cannot be used: `title`,
        `product_id`. By default `unit_price` is taken from product's default
        price point, but can be overwritten by passing `unit_price` or
        `price_point_id`. At this moment price points are supportted only for
        quantity based, on/off and metered components. For prepaid and event
        based billing components `unit_price` is required.
        ### Coupons
        When creating ad hoc invoice, new discounts can be applied in
        following way:
        ```json
        {
          "invoice": {
            "line_items": [
              {
                "product_id": "handle:gold-product",
                "quantity": 1
              }
            ],
            "coupons": [
              {
                "code": "COUPONCODE",
                "percentage": 50.0
              }
            ]
          }
        }
        ```
        If You want to use existing coupon for discount creation, only `code`
        and optional `product_family_id` is needed
        ```json
        ...
         "coupons": [
              {
                "code": "FREESETUP",
                "product_family_id": 1
              }
          ]
        ...
        ```
        ### Coupon options
        #### Code
        Coupon `code` will be displayed on invoice discount section.
        Coupon code can only contain uppercase letters, numbers, and allowed
        special characters.
        Lowercase letters will be converted to uppercase. It can be used to
        select an existing coupon from the catalog, or as an ad hoc coupon
        when passed with `percentage` or `amount`.
        #### Percentage
        Coupon `percentage` can take values from 0 to 100 and up to 4 decimal
        places. It cannot be used with `amount`. Only for ad hoc coupons, will
        be ignored if `code` is used to select an existing coupon from the
        catalog.
        #### Amount
        Coupon `amount` takes number value. It cannot be used with
        `percentage`. Used only when not matching existing coupon by `code`.
        #### Description
        Optional `description` will be displayed with coupon `code`. Used only
        when not matching existing coupon by `code`.
        #### Product Family id
        Optional `product_family_id` handle (with handle: prefix) or id is
        used to match existing coupon within site, when codes are not unique.
        #### Compounding Strategy
        Optional `compounding_strategy` for percentage coupons, can take
        values `compound` or `full-price`.
        For amount coupons, discounts will be always calculated against the
        original item price, before other discounts are applied.
        `compound` strategy:
        Percentage-based discounts will be calculated against the remaining
        price, after prior discounts have been calculated. It is set by
        default.
        `full-price` strategy:
        Percentage-based discounts will always be calculated against the
        original item price, before other discounts are applied.
        ### Line Item Options
        #### Period Date Range
        A custom period date range can be defined for each line item with the
        `period_range_start` and `period_range_end` parameters. Dates must be
        sent in the `YYYY-MM-DD` format.
        `period_range_end` must be greater or equal `period_range_start`.
        #### Taxes
        The `taxable` parameter can be sent as `true` if taxes should be
        calculated for a specific line item. For this to work, the site should
        be configured to use and calculate taxes. Further, if the site uses
        Avalara for tax calculations, a `tax_code` parameter should also be
        sent. For existing catalog items: products/components taxes cannot be
        overwritten.
        #### Price Point
        Price point handle (with handle: prefix) or id from the scope of
        current subscription's site can be provided with `price_point_id` for
        components with `component_id` or `product_price_point_id` for
        products with `product_id` parameter. If price point is passed
        `unit_price` cannot be used. It can be used only with catalog items
        products and components.
        #### Description
        Optional `description` parameter, it will overwrite default generated
        description for line item.
        ### Invoice Options
        #### Issue Date
        By default, invoices will be created with a issue date set to today.
        `issue_date` parameter can be send to alter that. Only dates in the
        past can be send. `issue_date` should be send in `YYYY-MM-DD` format.
        #### Net Terms
        By default, invoices will be created with a due date matching the date
        of invoice creation. If a different due date is desired, the
        `net_terms` parameter can be sent indicating the number of days in
        advance the due date should be.
        #### Addresses
        The seller, shipping and billing addresses can be sent to override the
        site's defaults. Each address requires to send a `first_name` at a
        minimum in order to work. Please see below for the details on which
        parameters can be sent for each address object.
        #### Memo and Payment Instructions
        A custom memo can be sent with the `memo` parameter to override the
        site's default. Likewise, custom payment instructions can be sent with
        the `payment_instrucions` parameter.
        #### Status
        By default, invoices will be created with open status. Possible
        alternative is `draft`.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (CreateInvoiceRequest, optional): TODO: type description
                here.

        Returns:
            InvoiceResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/invoices.json')
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(InvoiceResponse.from_dictionary)
            .local_error('401', 'Unauthorized', APIException)
            .local_error('422', 'Unprocessable Entity (WebDAV)', NestedErrorResponseException)
        ).execute()

    def send_invoice(self,
                     uid,
                     body=None):
        """Does a POST request to /invoices/{uid}/deliveries.json.

        This endpoint allows for invoices to be programmatically delivered via
        email. This endpoint supports the delivery of both ad-hoc and
        automatically generated invoices. Additionally, this endpoint supports
        email delivery to direct recipients, carbon-copy (cc) recipients, and
        blind carbon-copy (bcc) recipients.
        Please note that if no recipient email addresses are specified in the
        request, then the subscription's default email configuration will be
        used. For example, if `recipient_emails` is left blank, then the
        invoice will be delivered to the subscription's customer email
        address.
        On success, a 204 no-content response will be returned. Please note
        that this does not indicate that email(s) have been delivered, but
        instead indicates that emails have been successfully queued for
        delivery. If _any_ invalid or malformed email address is found in the
        request body, the entire request will be rejected and a 422 response
        will be returned.

        Args:
            uid (str): The unique identifier for the invoice, this does not
                refer to the public facing invoice number.
            body (SendInvoiceRequest, optional): TODO: type description here.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{uid}/deliveries.json')
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
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).execute()

    def preview_customer_information_changes(self,
                                             uid):
        """Does a POST request to /invoices/{uid}/customer_information/preview.json.

        Customer information may change after an invoice is issued which may
        lead to a mismatch between customer information that are present on an
        open invoice and actual customer information. This endpoint allows to
        preview these differences, if any.
        The endpoint doesn't accept a request body. Customer information
        differences are calculated on the application side.

        Args:
            uid (str): The unique identifier for the invoice, this does not
                refer to the public facing invoice number.

        Returns:
            CustomerChangesPreviewResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{uid}/customer_information/preview.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CustomerChangesPreviewResponse.from_dictionary)
            .local_error('404', 'Not Found', ErrorListResponseException)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()

    def update_customer_information(self,
                                    uid):
        """Does a PUT request to /invoices/{uid}/customer_information.json.

        This endpoint updates customer information on an open invoice and
        returns the updated invoice. If you would like to preview changes that
        will be applied, use the
        `/invoices/{uid}/customer_information/preview.json` endpoint before.
        The endpoint doesn't accept a request body. Customer information
        differences are calculated on the application side.

        Args:
            uid (str): The unique identifier for the invoice, this does not
                refer to the public facing invoice number.

        Returns:
            Invoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{uid}/customer_information.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('uid')
                            .value(uid)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Invoice.from_dictionary)
            .local_error('404', 'Not Found', ErrorListResponseException)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()

    def issue_invoice(self,
                      uid,
                      body=None):
        """Does a POST request to /invoices/{uid}/issue.json.

        This endpoint allows you to issue an invoice that is in "pending"
        status. For example, you can issue an invoice that was created when
        allocating new quantity on a component and using "accrue charges"
        option.
        You cannot issue a pending child invoice that was created for a member
        subscription in a group.
        For Remittance subscriptions, the invoice will go into "open" status
        and payment won't be attempted. The value for `on_failed_payment`
        would be rejected if sent. Any prepayments or service credits that
        exist on subscription will be automatically applied. Additionally, if
        setting is on, an email will be sent for issued invoice.
        For Automatic subscriptions, prepayments and service credits will
        apply to the invoice and before payment is attempted. On successful
        payment, the invoice will go into "paid" status and email will be sent
        to the customer (if setting applies). When payment fails, the next
        event depends on the `on_failed_payment` value:
        - `leave_open_invoice` - prepayments and credits applied to invoice;
        invoice status set to "open"; email sent to the customer for the
        issued invoice (if setting applies); payment failure recorded in the
        invoice history. This is the default option.
        - `rollback_to_pending` - prepayments and credits not applied; invoice
        remains in "pending" status; no email sent to the customer; payment
        failure recorded in the invoice history.
        - `initiate_dunning` - prepayments and credits applied to the invoice;
        invoice status set to "open"; email sent to the customer for the
        issued invoice (if setting applies); payment failure recorded in the
        invoice history; subscription will  most likely go into "past_due" or
        "canceled" state (depending upon net terms and dunning settings).

        Args:
            uid (str): The unique identifier for the invoice, this does not
                refer to the public facing invoice number.
            body (IssueInvoiceRequest, optional): TODO: type description
                here.

        Returns:
            Invoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/invoices/{uid}/issue.json')
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Invoice.from_dictionary)
            .local_error('401', 'Unauthorized', APIException)
            .local_error('404', 'Not Found', APIException)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()
