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
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.subscription import Subscription
from advancedbilling.models.batch_job_response import BatchJobResponse
from advancedbilling.models.proforma_invoice import ProformaInvoice
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.single_error_response_exception import SingleErrorResponseException


class APIExportsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(APIExportsController, self).__init__(config)

    def list_exported_invoices(self,
                               options=dict()):
        """Does a GET request to /api_exports/invoices/{batch_id}/rows.json.

        This API returns an array of exported invoices for a provided
        `batch_id`. Pay close attention to pagination in order to control
        responses from the server.
        Example: `GET
        https://{subdomain}.chargify.com/api_exports/invoices/123/rows?per_page
        =10000&page=1`.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    batch_id -- str -- Id of a Batch Job.
                    per_page -- int -- This parameter indicates how many
                        records to fetch in each request.  Default value is
                        100.  The maximum allowed values is 10000; any
                        per_page value over 10000 will be changed to 10000.
                    page -- int -- Result records are organized in pages. By
                        default, the first page of results is displayed. The
                        page parameter specifies a page number of results to
                        fetch. You can start navigating through the pages to
                        consume the results. You do this by passing in a page
                        parameter. Retrieve the next page by adding ?page=2 to
                        the query string. If there are no results to return,
                        then an empty result set will be returned. Use in
                        query `page=1`.

        Returns:
            List[Invoice]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api_exports/invoices/{batch_id}/rows.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('batch_id')
                            .value(options.get('batch_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Invoice.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
        ).execute()

    def list_exported_subscriptions(self,
                                    options=dict()):
        """Does a GET request to /api_exports/subscriptions/{batch_id}/rows.json.

        This API returns an array of exported subscriptions for a provided
        `batch_id`. Pay close attention to pagination in order to control
        responses from the server.
        Example: `GET
        https://{subdomain}.chargify.com/api_exports/subscriptions/123/rows?per
        _page=200&page=1`.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    batch_id -- str -- Id of a Batch Job.
                    per_page -- int -- This parameter indicates how many
                        records to fetch in each request.  Default value is
                        100.  The maximum allowed values is 10000; any
                        per_page value over 10000 will be changed to 10000.
                    page -- int -- Result records are organized in pages. By
                        default, the first page of results is displayed. The
                        page parameter specifies a page number of results to
                        fetch. You can start navigating through the pages to
                        consume the results. You do this by passing in a page
                        parameter. Retrieve the next page by adding ?page=2 to
                        the query string. If there are no results to return,
                        then an empty result set will be returned. Use in
                        query `page=1`.

        Returns:
            List[Subscription]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api_exports/subscriptions/{batch_id}/rows.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('batch_id')
                            .value(options.get('batch_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Subscription.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
        ).execute()

    def export_proforma_invoices(self):
        """Does a POST request to /api_exports/proforma_invoices.json.

        This API creates a proforma invoices export and returns a batchjob
        object.
        It is only available for Relationship Invoicing architecture.

        Returns:
            BatchJobResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api_exports/proforma_invoices.json')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BatchJobResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('409', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SingleErrorResponseException)
        ).execute()

    def read_proforma_invoices_export(self,
                                      batch_id):
        """Does a GET request to /api_exports/proforma_invoices/{batch_id}.json.

        This API returns a batchjob object for proforma invoices export.

        Args:
            batch_id (str): Id of a Batch Job.

        Returns:
            BatchJobResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api_exports/proforma_invoices/{batch_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('batch_id')
                            .value(batch_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BatchJobResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
        ).execute()

    def list_exported_proforma_invoices(self,
                                        options=dict()):
        """Does a GET request to /api_exports/proforma_invoices/{batch_id}/rows.json.

        This API returns an array of exported proforma invoices for a provided
        `batch_id`. Pay close attention to pagination in order to control
        responses from the server.
        Example: `GET
        https://{subdomain}.chargify.com/api_exports/proforma_invoices/123/rows
        ?per_page=10000&page=1`.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    batch_id -- str -- Id of a Batch Job.
                    per_page -- int -- This parameter indicates how many
                        records to fetch in each request.  Default value is
                        100.  The maximum allowed values is 10000; any
                        per_page value over 10000 will be changed to 10000.
                    page -- int -- Result records are organized in pages. By
                        default, the first page of results is displayed. The
                        page parameter specifies a page number of results to
                        fetch. You can start navigating through the pages to
                        consume the results. You do this by passing in a page
                        parameter. Retrieve the next page by adding ?page=2 to
                        the query string. If there are no results to return,
                        then an empty result set will be returned. Use in
                        query `page=1`.

        Returns:
            List[ProformaInvoice]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api_exports/proforma_invoices/{batch_id}/rows.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('batch_id')
                            .value(options.get('batch_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
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

    def export_subscriptions(self):
        """Does a POST request to /api_exports/subscriptions.json.

        This API creates a subscriptions export and returns a batchjob
        object.

        Returns:
            BatchJobResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api_exports/subscriptions.json')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BatchJobResponse.from_dictionary)
            .local_error_template('409', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SingleErrorResponseException)
        ).execute()

    def read_invoices_export(self,
                             batch_id):
        """Does a GET request to /api_exports/invoices/{batch_id}.json.

        This API returns a batchjob object for invoices export.

        Args:
            batch_id (str): Id of a Batch Job.

        Returns:
            BatchJobResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api_exports/invoices/{batch_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('batch_id')
                            .value(batch_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BatchJobResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
        ).execute()

    def read_subscriptions_export(self,
                                  batch_id):
        """Does a GET request to /api_exports/subscriptions/{batch_id}.json.

        This API returns a batchjob object for subscriptions export.

        Args:
            batch_id (str): Id of a Batch Job.

        Returns:
            BatchJobResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api_exports/subscriptions/{batch_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('batch_id')
                            .value(batch_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BatchJobResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
        ).execute()

    def export_invoices(self):
        """Does a POST request to /api_exports/invoices.json.

        This API creates an invoices export and returns a batchjob object.

        Returns:
            BatchJobResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/api_exports/invoices.json')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BatchJobResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('409', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SingleErrorResponseException)
        ).execute()
