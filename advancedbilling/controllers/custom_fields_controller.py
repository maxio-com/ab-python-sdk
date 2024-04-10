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
from advancedbilling.models.metafield import Metafield
from advancedbilling.models.list_metafields_response import ListMetafieldsResponse
from advancedbilling.models.metadata import Metadata
from advancedbilling.models.paginated_metadata import PaginatedMetadata
from advancedbilling.exceptions.single_error_response_exception import SingleErrorResponseException
from advancedbilling.exceptions.api_exception import APIException


class CustomFieldsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(CustomFieldsController, self).__init__(config)

    def create_metafields(self,
                          resource_type,
                          body=None):
        """Does a POST request to /{resource_type}/metafields.json.

        ## Custom Fields: Metafield Intro
        **Chargify refers to Custom Fields in the API documentation as
        metafields and metadata.** Within the Chargify UI, metadata and
        metafields are grouped together under the umbrella of "Custom Fields."
        All of our UI-based documentation that references custom fields will
        not cite the terminology metafields or metadata.
        + **Metafield is the custom field**
        + **Metadata is the data populating the custom field.**
        Chargify Metafields are used to add meaningful attributes to
        subscription and customer resources. Full documentation on how to
        create Custom Fields in the Chargify UI can be located
        [here](https://maxio-chargify.zendesk.com/hc/en-us/articles/54053325536
        13-Custom-Fields-Reference). For additional documentation on how to
        record data within custom fields, please see our subscription-based
        documentation
        [here.](https://maxio-chargify.zendesk.com/hc/en-us/articles/5404434903
        181-Subscription-Summary#custom-fields)
        Metafield are the place where you will set up your resource to accept
        additional data. It is scoped to the site instead of a specific
        customer or subscription. Think of it as the key, and Metadata as the
        value on every record.
        ## Create Metafields
        Use this endpoint to create metafields for your Site. Metafields can
        be populated with metadata after the fact.
        Each site is limited to 100 unique Metafields (i.e. keys, or names)
        per resource. This means you can have 100 Metafields for Subscription
        and another 100 for Customer.
        ### Metafields "On-the-Fly"
        It is possible to create Metafields “on the fly” when you create your
        Metadata – if a non-existant name is passed when creating Metadata, a
        Metafield for that key will be automatically created. The Metafield
        API, however, gives you more control over your “keys”.
        ### Metafield Scope Warning
        If configuring metafields in the Admin UI or via the API, be careful
        sending updates to metafields with the scope attribute – **if a
        partial update is sent it will overwrite the current configuration**.

        Args:
            resource_type (ResourceType): the resource type to which the
                metafields belong
            body (CreateMetafieldsRequest, optional): TODO: type description
                here.

        Returns:
            List[Metafield]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/{resource_type}/metafields.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(resource_type)
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
            .deserialize_into(Metafield.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SingleErrorResponseException)
        ).execute()

    def list_metafields(self,
                        options=dict()):
        """Does a GET request to /{resource_type}/metafields.json.

        This endpoint lists metafields associated with a site. The metafield
        description and usage is contained in the response.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    resource_type -- ResourceType -- the resource type to
                        which the metafields belong
                    name -- str -- filter by the name of the metafield
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
                    direction -- SortingDirection -- Controls the order in
                        which results are returned. Use in query
                        `direction=asc`.

        Returns:
            ListMetafieldsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/{resource_type}/metafields.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(options.get('resource_type', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('name')
                         .value(options.get('name', None)))
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
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListMetafieldsResponse.from_dictionary)
        ).execute()

    def update_metafield(self,
                         resource_type,
                         body=None):
        """Does a PUT request to /{resource_type}/metafields.json.

        Use the following method to update metafields for your Site.
        Metafields can be populated with metadata after the fact.

        Args:
            resource_type (ResourceType): the resource type to which the
                metafields belong
            body (UpdateMetafieldsRequest, optional): TODO: type description
                here.

        Returns:
            List[Metafield]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/{resource_type}/metafields.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(resource_type)
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
            .deserialize_into(Metafield.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SingleErrorResponseException)
        ).execute()

    def delete_metafield(self,
                         resource_type,
                         name=None):
        """Does a DELETE request to /{resource_type}/metafields.json.

        Use the following method to delete a metafield. This will remove the
        metafield from the Site.
        Additionally, this will remove the metafield and associated metadata
        with all Subscriptions on the Site.

        Args:
            resource_type (ResourceType): the resource type to which the
                metafields belong
            name (str, optional): The name of the metafield to be deleted

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
            .path('/{resource_type}/metafields.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(resource_type)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('name')
                         .value(name))
            .auth(Single('BasicAuth'))
        ).execute()

    def create_metadata(self,
                        resource_type,
                        resource_id,
                        body=None):
        """Does a POST request to /{resource_type}/{resource_id}/metadata.json.

        ## Custom Fields: Metadata Intro
        **Chargify refers to Custom Fields in the API documentation as
        metafields and metadata.** Within the Chargify UI, metadata and
        metafields are grouped together under the umbrella of "Custom Fields."
        All of our UI-based documentation that references custom fields will
        not cite the terminology metafields or metadata.
        + **Metafield is the custom field**
        + **Metadata is the data populating the custom field.**
        Chargify Metafields are used to add meaningful attributes to
        subscription and customer resources. Full documentation on how to
        create Custom Fields in the Chargify UI can be located
        [here](https://chargify.zendesk.com/hc/en-us/articles/4407659856411).
        For additional documentation on how to record data within custom
        fields, please see our subscription-based documentation
        [here.](https://chargify.zendesk.com/hc/en-us/articles/4407884887835#cu
        stom-fields)
        Metadata is associated to a customer or subscription, and corresponds
        to a Metafield. When creating a new metadata object for a given
        record, **if the metafield is not present it will be created**.
        ## Metadata limits
        Metadata values are limited to 2kB in size. Additonally, there are
        limits on the number of unique metafields available per resource.
        ## Create Metadata
        This method will create a metafield for the site on the fly if it does
        not already exist, and populate the metadata value.
        ### Subscription or Customer Resource
        Please pay special attention to the resource you use when creating
        metadata.

        Args:
            resource_type (ResourceType): the resource type to which the
                metafields belong
            resource_id (int): The Chargify id of the customer or the
                subscription for which the metadata applies
            body (CreateMetadataRequest, optional): TODO: type description
                here.

        Returns:
            List[Metadata]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/{resource_type}/{resource_id}/metadata.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(resource_type)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('resource_id')
                            .value(resource_id)
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
            .deserialize_into(Metadata.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SingleErrorResponseException)
        ).execute()

    def list_metadata(self,
                      options=dict()):
        """Does a GET request to /{resource_type}/{resource_id}/metadata.json.

        This request will list all of the metadata belonging to a particular
        resource (ie. subscription, customer) that is specified.
        ## Metadata Data
        This endpoint will also display the current stats of your metadata to
        use as a tool for pagination.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    resource_type -- ResourceType -- the resource type to
                        which the metafields belong
                    resource_id -- int -- The Chargify id of the customer or
                        the subscription for which the metadata applies
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
            PaginatedMetadata: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/{resource_type}/{resource_id}/metadata.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(options.get('resource_type', None))
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('resource_id')
                            .value(options.get('resource_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaginatedMetadata.from_dictionary)
        ).execute()

    def update_metadata(self,
                        resource_type,
                        resource_id,
                        body=None):
        """Does a PUT request to /{resource_type}/{resource_id}/metadata.json.

        This method allows you to update the existing metadata associated with
        a subscription or customer.

        Args:
            resource_type (ResourceType): the resource type to which the
                metafields belong
            resource_id (int): The Chargify id of the customer or the
                subscription for which the metadata applies
            body (UpdateMetadataRequest, optional): TODO: type description
                here.

        Returns:
            List[Metadata]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/{resource_type}/{resource_id}/metadata.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(resource_type)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('resource_id')
                            .value(resource_id)
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
            .deserialize_into(Metadata.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SingleErrorResponseException)
        ).execute()

    def delete_metadata(self,
                        resource_type,
                        resource_id,
                        name=None,
                        names=None):
        """Does a DELETE request to /{resource_type}/{resource_id}/metadata.json.

        This method removes the metadata from the subscriber/customer cited.
        ## Query String Usage
        For instance if you wanted to delete the metadata for customer 99
        named weight you would request:
        ```
        https://acme.chargify.com/customers/99/metadata.json?name=weight
        ```
        If you want to delete multiple metadata fields for a customer 99
        named: `weight` and `age` you wrould request:
        ```
        https://acme.chargify.com/customers/99/metadata.json?names[]=weight&nam
        es[]=age
        ```
        ## Successful Response
        For a success, there will be a code `200` and the plain text response
        `true`.
        ## Unsuccessful Response
        When a failed response is encountered, you will receive a `404`
        response and the plain text response of `true`.

        Args:
            resource_type (ResourceType): the resource type to which the
                metafields belong
            resource_id (int): The Chargify id of the customer or the
                subscription for which the metadata applies
            name (str, optional): Name of field to be removed.
            names (List[str], optional): Names of fields to be removed. Use in
                query:
                `names[]=field1&names[]=my-field&names[]=another-field`.

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
            .path('/{resource_type}/{resource_id}/metadata.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(resource_type)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('resource_id')
                            .value(resource_id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('name')
                         .value(name))
            .query_param(Parameter()
                         .key('names')
                         .value(names))
            .array_serialization_format(SerializationFormats.UN_INDEXED)
            .auth(Single('BasicAuth'))
        ).execute()

    def list_metadata_for_resource_type(self,
                                        options=dict()):
        """Does a GET request to /{resource_type}/metadata.json.

        This method will provide you information on usage of metadata across
        your selected resource (ie. subscriptions, customers)
        ## Metadata Data
        This endpoint will also display the current stats of your metadata to
        use as a tool for pagination.
        ### Metadata for multiple records
        `https://acme.chargify.com/subscriptions/metadata.json?resource_ids[]=1
        &resource_ids[]=2`
        ## Read Metadata for a Site
        This endpoint will list the number of pages of metadata information
        that are contained within a site.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    resource_type -- ResourceType -- the resource type to
                        which the metafields belong
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
                    date_field -- BasicDateField -- The type of filter you
                        would like to apply to your search.
                    start_date -- date -- The start date (format YYYY-MM-DD)
                        with which to filter the date_field. Returns metadata
                        with a timestamp at or after midnight (12:00:00 AM) in
                        your site’s time zone on the date specified.
                    end_date -- date -- The end date (format YYYY-MM-DD) with
                        which to filter the date_field. Returns metadata with
                        a timestamp up to and including 11:59:59PM in your
                        site’s time zone on the date specified.
                    start_datetime -- datetime -- The start date and time
                        (format YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns metadata with a timestamp at or
                        after exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of start_date.
                    end_datetime -- datetime -- The end date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns metadata with a timestamp at or
                        before exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of end_date.
                    with_deleted -- bool -- Allow to fetch deleted metadata.
                    resource_ids -- List[int] -- Allow to fetch metadata for
                        multiple records based on provided ids. Use in query:
                        `resource_ids[]=122&resource_ids[]=123&resource_ids[]=1
                        24`.
                    direction -- SortingDirection -- Controls the order in
                        which results are returned. Use in query
                        `direction=asc`.

        Returns:
            PaginatedMetadata: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/{resource_type}/metadata.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(options.get('resource_type', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('date_field')
                         .value(options.get('date_field', None)))
            .query_param(Parameter()
                         .key('start_date')
                         .value(options.get('start_date', None)))
            .query_param(Parameter()
                         .key('end_date')
                         .value(options.get('end_date', None)))
            .query_param(Parameter()
                         .key('start_datetime')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, options.get('start_datetime', None))))
            .query_param(Parameter()
                         .key('end_datetime')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, options.get('end_datetime', None))))
            .query_param(Parameter()
                         .key('with_deleted')
                         .value(options.get('with_deleted', None)))
            .query_param(Parameter()
                         .key('resource_ids')
                         .value(options.get('resource_ids', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.UN_INDEXED)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaginatedMetadata.from_dictionary)
        ).execute()
