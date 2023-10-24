# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from advancedbilling.api_helper import APIHelper
from advancedbilling.configuration import Server
from advancedbilling.controllers.base_controller import BaseController
from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from advancedbilling.http.http_method_enum import HttpMethodEnum
from apimatic_core.types.array_serialization_format import SerializationFormats
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from advancedbilling.models.customer_response import CustomerResponse
from advancedbilling.models.subscription_response import SubscriptionResponse
from advancedbilling.exceptions.customers_json_422_error_exception import CustomersJson422ErrorException
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException


class CustomersController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(CustomersController, self).__init__(config)

    def create_customer(self,
                        body=None):
        """Does a POST request to /customers.json.

        You may create a new Customer at any time, or you may create a
        Customer at the same time you create a Subscription. The only
        validation restriction is that you may only create one customer for a
        given reference value.
        If provided, the `reference` value must be unique. It represents a
        unique identifier for the customer from your own app, i.e. the
        customer’s ID. This allows you to retrieve a given customer via a
        piece of shared information. Alternatively, you may choose to leave
        `reference` blank, and store Chargify’s unique ID for the customer,
        which is in the `id` attribute.
        Full documentation on how to locate, create and edit Customers in the
        Chargify UI can be located
        [here](https://chargify.zendesk.com/hc/en-us/articles/4407659914267).
        ## Required Country Format
        Chargify requires that you use the ISO Standard Country codes when
        formatting country attribute of the customer.
        Countries should be formatted as 2 characters. For more information,
        please see the following wikipedia article on
        [ISO_3166-1.](http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes)
        ## Required State Format
        Chargify requires that you use the ISO Standard State codes when
        formatting state attribute of the customer.
        + US States (2 characters):
        [ISO_3166-2](https://en.wikipedia.org/wiki/ISO_3166-2:US)
        + States Outside the US (2-3 characters): To find the correct state
        codes outside of the US, please go to
        [ISO_3166-1](http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes)
        and click on the link in the “ISO 3166-2 codes” column next to country
        you wish to populate.
        ## Locale
        Chargify allows you to attribute a language/region to your customer to
        deliver invoices in any required language.
        For more: [Customer
        Locale](https://chargify.zendesk.com/hc/en-us/articles/4407870384283#cu
        stomer-locale)

        Args:
            body (CreateCustomerRequest, optional): TODO: type description
                here.

        Returns:
            CustomerResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/customers.json')
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
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CustomerResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', CustomersJson422ErrorException)
        ).execute()

    def list_customers(self,
                       direction=None,
                       page=1,
                       per_page=50,
                       date_field=None,
                       start_date=None,
                       end_date=None,
                       start_datetime=None,
                       end_datetime=None,
                       q=None):
        """Does a GET request to /customers.json.

        This request will by default list all customers associated with your
        Site.
        ## Find Customer
        Use the search feature with the `q` query parameter to retrieve an
        array of customers that matches the search query.
        Common use cases are:
        + Search by an email
        + Search by a Chargify ID
        + Search by an organization
        + Search by a reference value from your application
        + Search by a first or last name
        To retrieve a single, exact match by reference, please use the [lookup
        endpoint](https://developers.chargify.com/docs/api-docs/b710d8fbef104-r
        ead-customer-by-reference).

        Args:
            direction (SortingDirection | None, optional): Direction to sort
                customers by time of creation
            page (int, optional): Result records are organized in pages. By
                default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can
                start navigating through the pages to consume the results. You
                do this by passing in a page parameter. Retrieve the next page
                by adding ?page=2 to the query string. If there are no results
                to return, then an empty result set will be returned. Use in
                query `page=1`.
            per_page (int, optional): This parameter indicates how many
                records to fetch in each request. Default value is 50. The
                maximum allowed values is 200; any per_page value over 200
                will be changed to 200. Use in query `per_page=200`.
            date_field (BasicDateField, optional): The type of filter you
                would like to apply to your search. Use in query:
                `date_field=created_at`.
            start_date (str, optional): The start date (format YYYY-MM-DD)
                with which to filter the date_field. Returns subscriptions
                with a timestamp at or after midnight (12:00:00 AM) in your
                site’s time zone on the date specified.
            end_date (str, optional): The end date (format YYYY-MM-DD) with
                which to filter the date_field. Returns subscriptions with a
                timestamp up to and including 11:59:59PM in your site’s time
                zone on the date specified.
            start_datetime (str, optional): The start date and time (format
                YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or after exact time
                provided in query. You can specify timezone in query -
                otherwise your site's time zone will be used. If provided,
                this parameter will be used instead of start_date.
            end_datetime (str, optional): The end date and time (format
                YYYY-MM-DD HH:MM:SS) with which to filter the date_field.
                Returns subscriptions with a timestamp at or before exact time
                provided in query. You can specify timezone in query -
                otherwise your site's time zone will be used. If provided,
                this parameter will be used instead of end_date.
            q (str, optional): A search query by which to filter customers
                (can be an email, an ID, a reference, organization)

        Returns:
            List[CustomerResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/customers.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('direction')
                         .value(direction)
                         .validator(lambda value: UnionTypeLookUp.get('ListCustomersDirection').validate(value)))
            .query_param(Parameter()
                         .key('page')
                         .value(page))
            .query_param(Parameter()
                         .key('per_page')
                         .value(per_page))
            .query_param(Parameter()
                         .key('date_field')
                         .value(date_field))
            .query_param(Parameter()
                         .key('start_date')
                         .value(start_date))
            .query_param(Parameter()
                         .key('end_date')
                         .value(end_date))
            .query_param(Parameter()
                         .key('start_datetime')
                         .value(start_datetime))
            .query_param(Parameter()
                         .key('end_datetime')
                         .value(end_datetime))
            .query_param(Parameter()
                         .key('q')
                         .value(q))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CustomerResponse.from_dictionary)
        ).execute()

    def read_customer(self,
                      id):
        """Does a GET request to /customers/{id}.json.

        This method allows to retrieve the Customer properties by
        Chargify-generated Customer ID.

        Args:
            id (int): The Chargify id of the customer

        Returns:
            CustomerResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/customers/{id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CustomerResponse.from_dictionary)
        ).execute()

    def update_customer(self,
                        id,
                        body=None):
        """Does a PUT request to /customers/{id}.json.

        This method allows to update the Customer.

        Args:
            id (int): The Chargify id of the customer
            body (UpdateCustomerRequest, optional): TODO: type description
                here.

        Returns:
            CustomerResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/customers/{id}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
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
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CustomerResponse.from_dictionary)
            .local_error('404', 'Not Found', APIException)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()

    def delete_customer(self,
                        id):
        """Does a DELETE request to /customers/{id}.json.

        This method allows you to delete the Customer.

        Args:
            id (int): The Chargify id of the customer

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
            .path('/customers/{id}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .is_required(True)
                            .should_encode(True))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
        ).execute()

    def read_customer_by_reference(self,
                                   reference):
        """Does a GET request to /customers/lookup.json.

        Use this method to return the customer object if you have the unique
        **Reference ID (Your App)** value handy. It will return a single
        match.

        Args:
            reference (str): Customer reference

        Returns:
            CustomerResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/customers/lookup.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('reference')
                         .value(reference)
                         .is_required(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CustomerResponse.from_dictionary)
        ).execute()

    def list_customer_subscriptions(self,
                                    customer_id):
        """Does a GET request to /customers/{customer_id}/subscriptions.json.

        This method lists all subscriptions that belong to a customer.

        Args:
            customer_id (int): The Chargify id of the customer

        Returns:
            List[SubscriptionResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/customers/{customer_id}/subscriptions.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('customer_id')
                            .value(customer_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .is_nullify404(True)
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
        ).execute()
