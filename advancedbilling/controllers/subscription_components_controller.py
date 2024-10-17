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
from advancedbilling.models.subscription_component_response import SubscriptionComponentResponse
from advancedbilling.models.bulk_components_price_point_assignment import BulkComponentsPricePointAssignment
from advancedbilling.models.subscription_response import SubscriptionResponse
from advancedbilling.models.allocation_response import AllocationResponse
from advancedbilling.models.allocation_preview_response import AllocationPreviewResponse
from advancedbilling.models.usage_response import UsageResponse
from advancedbilling.models.list_subscription_components_response import ListSubscriptionComponentsResponse
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.component_price_point_error_exception import ComponentPricePointErrorException
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.exceptions.component_allocation_error_exception import ComponentAllocationErrorException
from advancedbilling.exceptions.subscription_component_allocation_error_exception import SubscriptionComponentAllocationErrorException


class SubscriptionComponentsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(SubscriptionComponentsController, self).__init__(config)

    def read_subscription_component(self,
                                    subscription_id,
                                    component_id):
        """Does a GET request to /subscriptions/{subscription_id}/components/{component_id}.json.

        This request will list information regarding a specific component
        owned by a subscription.

        Args:
            subscription_id (int): The Chargify id of the subscription
            component_id (int): The Advanced Billing id of the component.
                Alternatively, the component's handle prefixed by `handle:`

        Returns:
            SubscriptionComponentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/components/{component_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionComponentResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
        ).execute()

    def list_subscription_components(self,
                                     options=dict()):
        """Does a GET request to /subscriptions/{subscription_id}/components.json.

        This request will list a subscription's applied components.
        ## Archived Components
        When requesting to list components for a given subscription, if the
        subscription contains **archived** components they will be listed in
        the server response.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    subscription_id -- int -- The Chargify id of the
                        subscription
                    date_field -- SubscriptionListDateField -- The type of
                        filter you'd like to apply to your search. Use in
                        query `date_field=updated_at`.
                    direction -- SortingDirection -- Controls the order in
                        which results are returned. Use in query
                        `direction=asc`.
                    filter -- ListSubscriptionComponentsFilter -- Filter to
                        use for List Subscription Components operation
                    end_date -- str -- The end date (format YYYY-MM-DD) with
                        which to filter the date_field. Returns components
                        with a timestamp up to and including 11:59:59PM in
                        your site’s time zone on the date specified.
                    end_datetime -- str -- The end date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns components with a timestamp at or
                        before exact time provided in query. You can specify
                        timezone in query - otherwise your site''s time zone
                        will be used. If provided, this parameter will be used
                        instead of end_date.
                    price_point_ids -- IncludeNotNull -- Allows fetching
                        components allocation only if price point id is
                        present. Use in query `price_point_ids=not_null`.
                    product_family_ids -- List[int] -- Allows fetching
                        components allocation with matching product family id
                        based on provided ids. Use in query
                        `product_family_ids=1,2,3`.
                    sort -- ListSubscriptionComponentsSort -- The attribute by
                        which to sort. Use in query `sort=updated_at`.
                    start_date -- str -- The start date (format YYYY-MM-DD)
                        with which to filter the date_field. Returns
                        components with a timestamp at or after midnight
                        (12:00:00 AM) in your site’s time zone on the date
                        specified.
                    start_datetime -- str -- The start date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns components with a timestamp at or
                        after exact time provided in query. You can specify
                        timezone in query - otherwise your site''s time zone
                        will be used. If provided, this parameter will be used
                        instead of start_date.
                    include -- List[ListSubscriptionComponentsInclude] --
                        Allows including additional data in the response. Use
                        in query `include=subscription,historic_usages`.
                    in_use -- bool -- If in_use is set to true, it returns
                        only components that are currently in use. However, if
                        it's set to false or not provided, it returns all
                        components connected with the subscription.

        Returns:
            List[SubscriptionComponentResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/components.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(options.get('subscription_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('date_field')
                         .value(options.get('date_field', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .query_param(Parameter()
                         .key('filter')
                         .value(options.get('filter', None)))
            .query_param(Parameter()
                         .key('end_date')
                         .value(options.get('end_date', None)))
            .query_param(Parameter()
                         .key('end_datetime')
                         .value(options.get('end_datetime', None)))
            .query_param(Parameter()
                         .key('price_point_ids')
                         .value(options.get('price_point_ids', None)))
            .query_param(Parameter()
                         .key('product_family_ids')
                         .value(options.get('product_family_ids', None)))
            .query_param(Parameter()
                         .key('sort')
                         .value(options.get('sort', None)))
            .query_param(Parameter()
                         .key('start_date')
                         .value(options.get('start_date', None)))
            .query_param(Parameter()
                         .key('start_datetime')
                         .value(options.get('start_datetime', None)))
            .query_param(Parameter()
                         .key('include')
                         .value(options.get('include', None)))
            .query_param(Parameter()
                         .key('in_use')
                         .value(options.get('in_use', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionComponentResponse.from_dictionary)
        ).execute()

    def bulk_update_subscription_components_price_points(self,
                                                         subscription_id,
                                                         body=None):
        """Does a POST request to /subscriptions/{subscription_id}/price_points.json.

        Updates the price points on one or more of a subscription's components.
        The `price_point` key can take either a:
        1. Price point id (integer)
        2. Price point handle (string)
        3. `"_default"` string, which will reset the price point to the
        component's current default price point.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (BulkComponentsPricePointAssignment, optional): TODO: type
                description here.

        Returns:
            BulkComponentsPricePointAssignment: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/price_points.json')
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
            .deserialize_into(BulkComponentsPricePointAssignment.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ComponentPricePointErrorException)
        ).execute()

    def bulk_reset_subscription_components_price_points(self,
                                                        subscription_id):
        """Does a POST request to /subscriptions/{subscription_id}/price_points/reset.json.

        Resets all of a subscription's components to use the current default.
        **Note**: this will update the price point for all of the
        subscription's components, even ones that have not been allocated yet.

        Args:
            subscription_id (int): The Chargify id of the subscription

        Returns:
            SubscriptionResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/price_points/reset.json')
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
            .deserialize_into(SubscriptionResponse.from_dictionary)
        ).execute()

    def allocate_component(self,
                           subscription_id,
                           component_id,
                           body=None):
        """Does a POST request to /subscriptions/{subscription_id}/components/{component_id}/allocations.json.

        This endpoint creates a new allocation, setting the current allocated
        quantity for the Component and recording a memo.
        **Notice**: Allocations can only be updated for Quantity, On/Off, and
        Prepaid Components.
        ## Allocations Documentation
        Full documentation on how to record Allocations in the Advanced
        Billing UI can be located
        [here](https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Compo
        nent-Allocations-Overview). It is focused on how allocations operate
        within the Advanced Billing UI.It goes into greater detail on how the
        user interface will react when recording allocations.
        This documentation also goes into greater detail on how proration is
        taken into consideration when applying component allocations.
        ## Proration Schemes
        Changing the allocated quantity of a component mid-period can result
        in either a Charge or Credit being applied to the subscription. When
        creating an allocation via the API, you can pass the `upgrade_charge`,
        `downgrade_credit`, and `accrue_charge` to be applied.
        **Notice:** These proration and accural fields will be ignored for
        Prepaid Components since this component type always generate charges
        immediately without proration.
        For background information on prorated components and
        upgrade/downgrade schemes, see [Setting Component
        Allocations.](https://maxio.zendesk.com/hc/en-us/articles/2425190616513
        3-Component-Allocations-Proration).
        See the tables below for valid values.
        | upgrade_charge | Definition                                        
        |
        |----------------|-----------------------------------------------------
        --------------|
        | `full`         | A charge is added for the full price of the
        component.            |
        | `prorated`     | A charge is added for the prorated price of the
        component change. |
        | `none`         | No charge is added.                                
        |
        | downgrade_credit | Definition                                      
        |
        |------------------|---------------------------------------------------
        |
        | `full`           | A full price credit is added for the amount owed.
        |
        | `prorated`       | A prorated credit is added for the amount owed.  
        |
        | `none`           | No charge is added.                              
        |
        | accrue_charge | Definition                                          
        |
        |---------------|------------------------------------------------------
        ------------------------------------------------------|
        | `true`        | Attempt to charge the customer at next renewal.     
        |
        | `false`       | Attempt to charge the customer right away. If it
        fails, the charge will be accrued until the next renewal. |
        ### Order of Resolution for upgrade_charge and downgrade_credit
        1. Per allocation in API call (within a single allocation of the
        `allocations` array)
        2. [Component-level default
        value](https://maxio.zendesk.com/hc/en-us/articles/24251883961485-Compo
        nent-Allocations-Overview)
        3. Allocation API call top level (outside of the `allocations` array)
        4. [Site-level default
        value](https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Compo
        nent-Allocations-Proration#proration-schemes)
        ### Order of Resolution for accrue charge
        1. Allocation API call top level (outside of the `allocations` array)
        2. [Site-level default
        value](https://maxio.zendesk.com/hc/en-us/articles/24251906165133-Compo
        nent-Allocations-Proration#proration-schemes)
        **NOTE: Proration uses the current price of the component as well as
        the current tax rates. Changes to either may cause the prorated
        charge/credit to be wrong.**

        Args:
            subscription_id (int): The Chargify id of the subscription
            component_id (int): The Advanced Billing id of the component
            body (CreateAllocationRequest, optional): TODO: type description
                here.

        Returns:
            AllocationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/components/{component_id}/allocations.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
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
            .deserialize_into(AllocationResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def list_allocations(self,
                         subscription_id,
                         component_id,
                         page=1):
        """Does a GET request to /subscriptions/{subscription_id}/components/{component_id}/allocations.json.

        This endpoint returns the 50 most recent Allocations, ordered by most
        recent first.
        ## On/Off Components
        When a subscription's on/off component has been toggled to on (`1`) or
        off (`0`), usage will be logged in this response.
        ## Querying data via Advanced Billing gem
        You can also query the current quantity via the [official Advanced
        Billing Gem.](http://github.com/chargify/chargify_api_ares)
        ```# First way
        component = Chargify::Subscription::Component.find(1, :params =>
        {:subscription_id => 7})
        puts component.allocated_quantity
        # => 23
        # Second way
        component = Chargify::Subscription.find(7).component(1)
        puts component.allocated_quantity
        # => 23
        ```

        Args:
            subscription_id (int): The Chargify id of the subscription
            component_id (int): The Advanced Billing id of the component
            page (int, optional): Result records are organized in pages. By
                default, the first page of results is displayed. The page
                parameter specifies a page number of results to fetch. You can
                start navigating through the pages to consume the results. You
                do this by passing in a page parameter. Retrieve the next page
                by adding ?page=2 to the query string. If there are no results
                to return, then an empty result set will be returned. Use in
                query `page=1`.

        Returns:
            List[AllocationResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/components/{component_id}/allocations.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(page))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AllocationResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def allocate_components(self,
                            subscription_id,
                            body=None):
        """Does a POST request to /subscriptions/{subscription_id}/allocations.json.

        Creates multiple allocations, setting the current allocated quantity
        for each of the components and recording a memo. The charges and/or
        credits that are created will be rolled up into a single total which
        is used to determine whether this is an upgrade or a downgrade. Be
        aware of the Order of Resolutions explained below in determining the
        proration scheme.
        A `component_id` is required for each allocation.
        This endpoint only responds to JSON. It is not available for XML.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (AllocateComponents, optional): TODO: type description here.

        Returns:
            List[AllocationResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/allocations.json')
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
            .deserialize_into(AllocationResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def preview_allocations(self,
                            subscription_id,
                            body=None):
        """Does a POST request to /subscriptions/{subscription_id}/allocations/preview.json.

        Advanced Billing offers the ability to preview a potential
        subscription's **quantity-based** or **on/off** component allocation
        in the middle of the current billing period.  This is useful if you
        want users to be able to see the effect of a component operation
        before actually doing it.
        ## Fine-grained Component Control: Use with multiple `upgrade_charge`s
        or `downgrade_credits`
        When the allocation uses multiple different types of `upgrade_charge`s
        or `downgrade_credit`s, the Allocation is viewed as an Allocation
        which uses "Fine-Grained Component Control". As a result, the response
        will not include `direction` and `proration` within the
        `allocation_preview`, but at the `line_items` and `allocations` level
        respectfully.
        See example below for Fine-Grained Component Control response.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (PreviewAllocationsRequest, optional): TODO: type description
                here.

        Returns:
            AllocationPreviewResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/allocations/preview.json')
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
            .deserialize_into(AllocationPreviewResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ComponentAllocationErrorException)
        ).execute()

    def update_prepaid_usage_allocation_expiration_date(self,
                                                        subscription_id,
                                                        component_id,
                                                        allocation_id,
                                                        body=None):
        """Does a PUT request to /subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json.

        When the expiration interval options are selected on a prepaid usage
        component price point, all allocations will be created with an
        expiration date. This expiration date can be changed after the fact to
        allow for extending or shortening the allocation's active window.
        In order to change a prepaid usage allocation's expiration date, a PUT
        call must be made to the allocation's endpoint with a new expiration
        date.
        ## Limitations
        A few limitations exist when changing an allocation's expiration date:
        - An expiration date can only be changed for an allocation that
        belongs to a price point with expiration interval options explicitly
        set.
        - An expiration date can be changed towards the future with no
        limitations.
        - An expiration date can be changed towards the past (essentially
        expiring it) up to the subscription's current period beginning date.

        Args:
            subscription_id (int): The Chargify id of the subscription
            component_id (int): The Advanced Billing id of the component
            allocation_id (int): The Advanced Billing id of the allocation
            body (UpdateAllocationExpirationDate, optional): TODO: type
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
            .path('/subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('allocation_id')
                            .value(allocation_id)
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

    def delete_prepaid_usage_allocation(self,
                                        subscription_id,
                                        component_id,
                                        allocation_id,
                                        body=None):
        """Does a DELETE request to /subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json.

        Prepaid Usage components are unique in that their allocations are
        always additive. In order to reduce a subscription's allocated
        quantity for a prepaid usage component each allocation must be
        destroyed individually via this endpoint.
        ## Credit Scheme
        By default, destroying an allocation will generate a service credit on
        the subscription. This behavior can be modified with the optional
        `credit_scheme` parameter on this endpoint. The accepted values are:
        1. `none`: The allocation will be destroyed and the balances will be
        updated but no service credit or refund will be created.
        2. `credit`: The allocation will be destroyed and the balances will be
        updated and a service credit will be generated. This is also the
        default behavior if the `credit_scheme` param is not passed.
        3. `refund`: The allocation will be destroyed and the balances will be
        updated and a refund will be issued along with a Credit Note.

        Args:
            subscription_id (int): The Chargify id of the subscription
            component_id (int): The Advanced Billing id of the component
            allocation_id (int): The Advanced Billing id of the allocation
            body (CreditSchemeRequest, optional): TODO: type description here.

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
            .path('/subscriptions/{subscription_id}/components/{component_id}/allocations/{allocation_id}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('allocation_id')
                            .value(allocation_id)
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

    def create_usage(self,
                     subscription_id,
                     component_id,
                     body=None):
        """Does a POST request to /subscriptions/{subscription_id}/components/{component_id}/usages.json.

        ## Documentation
        Full documentation on how to create Components in the Advanced Billing
        UI can be located
        [here](https://maxio.zendesk.com/hc/en-us/articles/24261149711501-Creat
        e-Edit-and-Archive-Components). Additionally, for information on how
        to record component usage against a subscription, please see the
        following resources:
        + [Recording Metered Component
        Usage](https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Repor
        ting-Component-Allocations#reporting-metered-component-usage)
        + [Reporting Prepaid Component
        Status](https://maxio.zendesk.com/hc/en-us/articles/24251890500109-Repo
        rting-Component-Allocations#reporting-prepaid-component-status)
        You may choose to report metered or prepaid usage to Advanced Billing
        as often as you wish. You may report usage as it happens. You may also
        report usage periodically, such as each night or once per billing
        period. If usage events occur in your system very frequently (on the
        order of thousands of times an hour), it is best to accumulate usage
        into batches on your side, and then report those batches less
        frequently, such as daily. This will ensure you remain below any API
        throttling limits. If your use case requires higher rates of usage
        reporting, we recommend utilizing Events Based Components.
        ## Create Usage for Subscription
        This endpoint allows you to record an instance of metered or prepaid
        usage for a subscription. The `quantity` from usage for each component
        is accumulated to the `unit_balance` on the [Component Line
        Item](./b3A6MTQxMDgzNzQ-read-subscription-component) for the
        subscription.
        ## Price Point ID usage
        If you are using price points, for metered and prepaid usage
        components, Advanced Billing gives you the option to specify a price
        point in your request.
        You do not need to specify a price point ID. If a price point is not
        included, the default price point for the component will be used when
        the usage is recorded.
        If an invalid `price_point_id` is submitted, the endpoint will return
        an error.
        ## Deducting Usage
        In the event that you need to reverse a previous usage report or
        otherwise deduct from the current usage balance, you may provide a
        negative quantity.
        Example:
        Previously recorded:
        ```json
        {
          "usage": {
            "quantity": 5000,
            "memo": "Recording 5000 units"
          }
        }
        ```
        At this point, `unit_balance` would be `5000`. To reduce the balance
        to `0`, POST the following payload:
        ```json
        {
          "usage": {
            "quantity": -5000,
            "memo": "Deducting 5000 units"
          }
        }
        ```
        The `unit_balance` has a floor of `0`; negative unit balances are
        never allowed. For example, if the usage balance is 100 and you deduct
        200 units, the unit balance would then be `0`, not `-100`.
        ## FAQ
        Q. Is it possible to record metered usage for more than one component
        at a time?
        A. No. Usage should be reported as one API call per component on a
        single subscription. For example, to record that a subscriber has sent
        both an SMS Message and an Email, send an API call for each.

        Args:
            subscription_id (int): The Chargify id of the subscription
            component_id (int | str): Either the Advanced Billing id for the
                component or the component's handle prefixed by `handle:`
            body (CreateUsageRequest, optional): TODO: type description here.

        Returns:
            UsageResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/components/{component_id}/usages.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('CreateUsageComponentId').validate(value)))
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
            .deserialize_into(UsageResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def list_usages(self,
                    options=dict()):
        """Does a GET request to /subscriptions/{subscription_id}/components/{component_id}/usages.json.

        This request will return a list of the usages associated with a
        subscription for a particular metered component. This will display the
        previously recorded components for a subscription.
        This endpoint is not compatible with quantity-based components.
        ## Since Date and Until Date Usage
        Note: The `since_date` and `until_date` attributes each default to
        midnight on the date specified. For example, in order to list usages
        for January 20th, you would need to append the following to the URL.
        ```
        ?since_date=2016-01-20&until_date=2016-01-21
        ```
        ## Read Usage by Handle
        Use this endpoint to read the previously recorded components for a
        subscription.  You can now specify either the component id (integer)
        or the component handle prefixed by "handle:" to specify the unique
        identifier for the component you are working with.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    subscription_id -- int -- The Chargify id of the
                        subscription
                    component_id -- int | str -- Either the Advanced Billing
                        id for the component or the component's handle
                        prefixed by `handle:`
                    since_id -- long|int -- Returns usages with an id greater
                        than or equal to the one specified
                    max_id -- long|int -- Returns usages with an id less than
                        or equal to the one specified
                    since_date -- date -- Returns usages with a created_at
                        date greater than or equal to midnight (12:00 AM) on
                        the date specified.
                    until_date -- date -- Returns usages with a created_at
                        date less than or equal to midnight (12:00 AM) on the
                        date specified.
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
            List[UsageResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/components/{component_id}/usages.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(options.get('subscription_id', None))
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_id')
                            .value(options.get('component_id', None))
                            .is_required(True)
                            .should_encode(True)
                            .validator(lambda value: UnionTypeLookUp.get('ListUsagesInputComponentId').validate(value)))
            .query_param(Parameter()
                         .key('since_id')
                         .value(options.get('since_id', None)))
            .query_param(Parameter()
                         .key('max_id')
                         .value(options.get('max_id', None)))
            .query_param(Parameter()
                         .key('since_date')
                         .value(options.get('since_date', None)))
            .query_param(Parameter()
                         .key('until_date')
                         .value(options.get('until_date', None)))
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
            .deserialize_into(UsageResponse.from_dictionary)
        ).execute()

    def activate_event_based_component(self,
                                       subscription_id,
                                       component_id,
                                       body=None):
        """Does a POST request to /event_based_billing/subscriptions/{subscription_id}/components/{component_id}/activate.json.

        In order to bill your subscribers on your Events data under the
        Events-Based Billing feature, the components must be activated for the
        subscriber.
        Learn more about the role of activation in the [Events-Based Billing
        docs](https://maxio.zendesk.com/hc/en-us/articles/24260323329805-Events
        -Based-Billing-Overview).
        Use this endpoint to activate an event-based component for a single
        subscription. Activating an event-based component causes Advanced
        Billing to bill for events when the subscription is renewed.
        *Note: it is possible to stream events for a subscription at any time,
        regardless of component activation status. The activation status only
        determines if the subscription should be billed for event-based
        component usage at renewal.*

        Args:
            subscription_id (int): The Advanced Billing id of the subscription
            component_id (int): The Advanced Billing id of the component
            body (ActivateEventBasedComponent, optional): TODO: type
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
            .path('/event_based_billing/subscriptions/{subscription_id}/components/{component_id}/activate.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
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

    def deactivate_event_based_component(self,
                                         subscription_id,
                                         component_id):
        """Does a POST request to /event_based_billing/subscriptions/{subscription_id}/components/{component_id}/deactivate.json.

        Use this endpoint to deactivate an event-based component for a single
        subscription. Deactivating the event-based component causes Advanced
        Billing to ignore related events at subscription renewal.

        Args:
            subscription_id (int): The Advanced Billing id of the subscription
            component_id (int): The Advanced Billing id of the component

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
            .path('/event_based_billing/subscriptions/{subscription_id}/components/{component_id}/deactivate.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .auth(Single('BasicAuth'))
        ).execute()

    def record_event(self,
                     subdomain,
                     api_handle,
                     store_uid=None,
                     body=None):
        """Does a POST request to /{subdomain}/events/{api_handle}.json.

        ## Documentation
        Events-Based Billing is an evolved form of metered billing that is
        based on data-rich events streamed in real-time from your system to
        Advanced Billing.
        These events can then be transformed, enriched, or analyzed to form
        the computed totals of usage charges billed to your customers.
        This API allows you to stream events into the Advanced Billing data
        ingestion engine.
        Learn more about the feature in general in the [Events-Based Billing
        help
        docs](https://maxio.zendesk.com/hc/en-us/articles/24260323329805-Events
        -Based-Billing-Overview).
        ## Record Event
        Use this endpoint to record a single event.
        *Note: this endpoint differs from the standard Chargify API endpoints
        in that the URL subdomain will be `events` and your site subdomain
        will be included in the URL path. For example:*
        ```
        https://events.chargify.com/my-site-subdomain/events/my-stream-api-hand
        le
        ```

        Args:
            subdomain (str): Your site's subdomain
            api_handle (str): Identifies the Stream for which the event should
                be published.
            store_uid (str, optional): If you've attached your own Keen
                project as an Advanced Billing event data-store, use this
                parameter to indicate the data-store.
            body (EBBEvent, optional): TODO: type description here.

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
            .path('/{subdomain}/events/{api_handle}.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subdomain')
                            .value(subdomain)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('api_handle')
                            .value(api_handle)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .query_param(Parameter()
                         .key('store_uid')
                         .value(store_uid))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).execute()

    def bulk_record_events(self,
                           subdomain,
                           api_handle,
                           store_uid=None,
                           body=None):
        """Does a POST request to /{subdomain}/events/{api_handle}/bulk.json.

        Use this endpoint to record a collection of events.
        *Note: this endpoint differs from the standard Chargify API endpoints
        in that the subdomain will be `events` and your site subdomain will be
        included in the URL path.*
        A maximum of 1000 events can be published in a single request. A 422
        will be returned if this limit is exceeded.

        Args:
            subdomain (str): Your site's subdomain
            api_handle (str): Identifies the Stream for which the events
                should be published.
            store_uid (str, optional): If you've attached your own Keen
                project as an Advanced Billing event data-store, use this
                parameter to indicate the data-store.
            body (List[EBBEvent], optional): TODO: type description here.

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
            .path('/{subdomain}/events/{api_handle}/bulk.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subdomain')
                            .value(subdomain)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('api_handle')
                            .value(api_handle)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .query_param(Parameter()
                         .key('store_uid')
                         .value(store_uid))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).execute()

    def list_subscription_components_for_site(self,
                                              options=dict()):
        """Does a GET request to /subscriptions_components.json.

        This request will list components applied to each subscription.

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
                    sort -- ListSubscriptionComponentsSort -- The attribute by
                        which to sort. Use in query: `sort=updated_at`.
                    direction -- SortingDirection -- Controls the order in
                        which results are returned. Use in query
                        `direction=asc`.
                    filter -- ListSubscriptionComponentsForSiteFilter --
                        Filter to use for List Subscription Components For
                        Site operation
                    date_field -- SubscriptionListDateField -- The type of
                        filter you'd like to apply to your search. Use in
                        query: `date_field=updated_at`.
                    start_date -- str -- The start date (format YYYY-MM-DD)
                        with which to filter the date_field. Returns
                        components with a timestamp at or after midnight
                        (12:00:00 AM) in your site’s time zone on the date
                        specified. Use in query `start_date=2011-12-15`.
                    start_datetime -- str -- The start date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns components with a timestamp at or
                        after exact time provided in query. You can specify
                        timezone in query - otherwise your site''s time zone
                        will be used. If provided, this parameter will be used
                        instead of start_date. Use in query
                        `start_datetime=2022-07-01 09:00:05`.
                    end_date -- str -- The end date (format YYYY-MM-DD) with
                        which to filter the date_field. Returns components
                        with a timestamp up to and including 11:59:59PM in
                        your site’s time zone on the date specified. Use in
                        query `end_date=2011-12-16`.
                    end_datetime -- str -- The end date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns components with a timestamp at or
                        before exact time provided in query. You can specify
                        timezone in query - otherwise your site''s time zone
                        will be used. If provided, this parameter will be used
                        instead of end_date. Use in query
                        `end_datetime=2022-07-01 09:00:05`.
                    subscription_ids -- List[int] -- Allows fetching
                        components allocation with matching subscription id
                        based on provided ids. Use in query
                        `subscription_ids=1,2,3`.
                    price_point_ids -- IncludeNotNull -- Allows fetching
                        components allocation only if price point id is
                        present. Use in query `price_point_ids=not_null`.
                    product_family_ids -- List[int] -- Allows fetching
                        components allocation with matching product family id
                        based on provided ids. Use in query
                        `product_family_ids=1,2,3`.
                    include -- ListSubscriptionComponentsInclude -- Allows
                        including additional data in the response. Use in
                        query `include=subscription,historic_usages`.

        Returns:
            ListSubscriptionComponentsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions_components.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('sort')
                         .value(options.get('sort', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .query_param(Parameter()
                         .key('filter')
                         .value(options.get('filter', None)))
            .query_param(Parameter()
                         .key('date_field')
                         .value(options.get('date_field', None)))
            .query_param(Parameter()
                         .key('start_date')
                         .value(options.get('start_date', None)))
            .query_param(Parameter()
                         .key('start_datetime')
                         .value(options.get('start_datetime', None)))
            .query_param(Parameter()
                         .key('end_date')
                         .value(options.get('end_date', None)))
            .query_param(Parameter()
                         .key('end_datetime')
                         .value(options.get('end_datetime', None)))
            .query_param(Parameter()
                         .key('subscription_ids')
                         .value(options.get('subscription_ids', None)))
            .query_param(Parameter()
                         .key('price_point_ids')
                         .value(options.get('price_point_ids', None)))
            .query_param(Parameter()
                         .key('product_family_ids')
                         .value(options.get('product_family_ids', None)))
            .query_param(Parameter()
                         .key('include')
                         .value(options.get('include', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListSubscriptionComponentsResponse.from_dictionary)
        ).execute()
