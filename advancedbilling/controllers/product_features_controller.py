"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: D410, E501, E101, D206
from apimatic_core.authentication.multiple.single_auth import (
    Single,
)
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter

from advancedbilling.api_helper import APIHelper
from advancedbilling.configuration import Server
from advancedbilling.controllers.base_controller import (
    BaseController,
)
from advancedbilling.exceptions.api_exception import (
    APIException,
)
from advancedbilling.exceptions.error_list_response_exception import (
    ErrorListResponseException,
)
from advancedbilling.http.http_method_enum import (
    HttpMethodEnum,
)
from advancedbilling.models.feature_catalog_item_response import (
    FeatureCatalogItemResponse,
)
from advancedbilling.models.feature_catalog_items_list_response import (
    FeatureCatalogItemsListResponse,
)


class ProductFeaturesController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize ProductFeaturesController object."""
        super(ProductFeaturesController, self).__init__(config)

    def list_product_features(self,
                              product_id):
        """Perform a GET request to /products/{product_id}/features.json.

        Lists the feature catalog items attached to this product, including
        price-point-specific overrides.

        Args:
            product_id (int): The Advanced Billing id of the product.

        Returns:
            FeatureCatalogItemsListResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/products/{product_id}/features.json")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("product_id")
                .value(product_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(FeatureCatalogItemsListResponse.from_dictionary)
            .local_error("403", "Forbidden", ErrorListResponseException)
            .local_error("404", "Not Found", APIException),
        ).execute()

    def create_product_feature(self,
                               product_id,
                               body=None):
        """Perform a POST request to /products/{product_id}/features.json.

        Attaches a feature template to this product. Pass `price_point_type:
        "ProductPricePoint"` and `price_point_id` to scope the feature catalog item
        to a single product price point instead of the whole product. `value`, the
        periodicity and the grant expiration fall back to the feature template's
        defaults when omitted.
        **Product- or component-level items are a template.** A feature catalog item
        without `price_point_id` is copied onto price points created after it (except
        bulk-created price points; [Clone Component Price
        Point]($e/Component%3A%20Price%20Points/cloneComponentPricePoint) applies
        only the `feature_catalog_items` you send with it, and the automatic clone
        described below copies the source's features), but it is not added to price
        points that already exist, so their subscribers get nothing from it, even
        with `propagate_to_subscriptions: true`. To grant a feature to existing
        subscribers, create the item on each existing price point.
        **Restoring a template item.** Restoring an archived product- or
        component-level item, or creating one again for the same feature template,
        also restores the price-point copies that were archived together with it (for
        example, when the feature template was archived). If one of those price
        points has subscribers without the feature, the call returns `422` naming
        that price point, unless you send `propagate_to_subscriptions: true`, which
        restores the copies and grants the feature to those subscribers.
        **Price points with subscribers.** When the feature catalog item is scoped to
        a price point that already has subscribers and you don't send
        `propagate_to_subscriptions: true`, the new feature applies to new
        subscriptions only. The price point is cloned with its current features, the
        new feature is applied to the clone, and the response carries the clone's
        `price_point_id`. The feature catalog item in the response is also a
        different record, with a new `id`: later calls for the clone must use that
        `id`, not the original one. Existing subscribers stay on the original price
        point, unchanged; sign new subscriptions up on the clone to give them the
        change. A product price point has subscribers when any live subscription
        (including one in `awaiting_signup`) is on it. Price points that can't be
        cloned (archived or custom ones, or a component price point with an interval
        on a site without multi-frequency) make the request return `422`, with a
        message naming `propagate_to_subscriptions: true` as the way to apply the
        change to existing subscribers instead.

        Args:
            product_id (int): The Advanced Billing id of the product.
            body (CreateFeatureCatalogItemRequest, optional): The request body
                parameter.

        Returns:
            FeatureCatalogItemResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/products/{product_id}/features.json")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("product_id")
                .value(product_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(FeatureCatalogItemResponse.from_dictionary)
            .local_error("403", "Forbidden", ErrorListResponseException)
            .local_error("404", "Not Found", APIException)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()

    def read_product_feature(self,
                             product_id,
                             id):
        """Perform a GET request to /products/{product_id}/features/{id}.json.

        Returns a single feature catalog item attached to this product.

        Args:
            product_id (int): The Advanced Billing id of the product.
            id (int): The Advanced Billing id of the feature catalog item.

        Returns:
            FeatureCatalogItemResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/products/{product_id}/features/{id}.json")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("product_id")
                .value(product_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(FeatureCatalogItemResponse.from_dictionary)
            .local_error("403", "Forbidden", ErrorListResponseException)
            .local_error("404", "Not Found", APIException),
        ).execute()

    def update_product_feature(self,
                               product_id,
                               id,
                               body=None):
        """Perform a PUT request to /products/{product_id}/features/{id}.json.

        Updates the value or periodicity of a feature catalog item attached to this
        product. A request that changes nothing returns the item as it is.
        **Price points with subscribers.** When the feature catalog item is scoped to
        a price point that already has subscribers and you don't send
        `propagate_to_subscriptions: true`, the update applies to new subscriptions
        only. The price point is cloned with its current features, the update is
        applied to the clone, and the response carries the clone's `price_point_id`.
        The feature catalog item in the response is also a different record, with a
        new `id`: later calls for the clone must use that `id`, not the original one.
        Existing subscribers stay on the original price point, unchanged; sign new
        subscriptions up on the clone to give them the change. A product price point
        has subscribers when any live subscription (including one in
        `awaiting_signup`) is on it. Price points that can't be cloned (archived or
        custom ones, or a component price point with an interval on a site without
        multi-frequency) make the request return `422`, with a message naming
        `propagate_to_subscriptions: true` as the way to apply the change to existing
        subscribers instead.

        Args:
            product_id (int): The Advanced Billing id of the product.
            id (int): The Advanced Billing id of the feature catalog item.
            body (UpdateFeatureCatalogItemRequest, optional): The request body
                parameter.

        Returns:
            FeatureCatalogItemResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/products/{product_id}/features/{id}.json")
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                .key("product_id")
                .value(product_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(FeatureCatalogItemResponse.from_dictionary)
            .local_error("403", "Forbidden", ErrorListResponseException)
            .local_error("404", "Not Found", APIException)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()

    def remove_product_feature(self,
                               product_id,
                               id,
                               destroy_entitlements=False):
        """Perform a DELETE request to
        /products/{product_id}/features/{id}.json.

        Removes a feature catalog item from this product. Returns `204` when the item
        is removed in place.
        **Price points with subscribers.** When the feature catalog item is scoped to
        a price point that already has subscribers and you don't send
        `destroy_entitlements=true`, the removal applies to new subscriptions only.
        The price point is cloned with its current features, the removal is applied
        to the clone, and the call returns `200` with the archived feature catalog
        item on the clone (carrying the clone's `price_point_id` and a new `id`)
        instead of `204`. Existing subscribers stay on the original price point,
        unchanged; sign new subscriptions up on the clone to give them the change. A
        product price point has subscribers when any live subscription (including one
        in `awaiting_signup`) is on it. Price points that can't be cloned (archived
        or custom ones, or a component price point with an interval on a site without
        multi-frequency) make the request return `422`, with a message naming
        `destroy_entitlements=true` as the way to apply the change to existing
        subscribers instead.

        Args:
            product_id (int): The Advanced Billing id of the product.
            id (int): The Advanced Billing id of the feature catalog item.
            destroy_entitlements (bool, optional): When `true`, permanently deletes
                this feature catalog item and every entitlement it created, revoking
                subscriber access immediately. When `false` (default), the feature
                catalog item is archived and existing entitlements are preserved.

        Returns:
            FeatureCatalogItemResponse: Response from the API. The price point had
                subscribers, so the removal was made on a clone of it. Returns the
                archived feature catalog item on the clone.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/products/{product_id}/features/{id}.json")
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                .key("product_id")
                .value(product_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .query_param(Parameter()
                .key("destroy_entitlements")
                .value(destroy_entitlements))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(FeatureCatalogItemResponse.from_dictionary)
            .local_error("403", "Forbidden", ErrorListResponseException)
            .local_error("404", "Not Found", APIException)
            .local_error("422",
                "The price point has subscribers but can't be cloned (it is archived "
                "or custom, or it is a component price point with an interval on a si"
                "te without multi-frequency). Send `destroy_entitlements=true` to rem"
                "ove the feature from its existing subscribers instead.",
                ErrorListResponseException),
        ).execute()

    def restore_product_feature(self,
                                product_id,
                                id,
                                propagate_to_subscriptions=False):
        """Perform a POST request to
        /products/{product_id}/features/{id}/restore.json.

        Clears the archived state of a feature catalog item attached to this product.
        Returns `422` if the parent feature template is still archived. Restore the
        feature template first. Otherwise, restoring an item that isn't archived
        returns it unchanged.
        **Price points with subscribers.** When the feature catalog item is scoped to
        a price point that already has subscribers and you don't send
        `propagate_to_subscriptions=true`, the restore applies to new subscriptions
        only. The price point is cloned with its current features, the restore is
        applied to the clone, and the response carries the clone's `price_point_id`.
        The feature catalog item in the response is also a different record, with a
        new `id`: later calls for the clone must use that `id`, not the original one.
        Existing subscribers stay on the original price point, unchanged; sign new
        subscriptions up on the clone to give them the change. A product price point
        has subscribers when any live subscription (including one in
        `awaiting_signup`) is on it. Price points that can't be cloned (archived or
        custom ones, or a component price point with an interval on a site without
        multi-frequency) make the request return `422`, with a message naming
        `propagate_to_subscriptions: true` as the way to apply the change to existing
        subscribers instead.

        Args:
            product_id (int): The Advanced Billing id of the product.
            id (int): The Advanced Billing id of the feature catalog item.
            propagate_to_subscriptions (bool, optional): When `true`, the restored
                feature is applied to the existing subscriptions on its price point.
                When `false` (default), an item scoped to a price point with
                subscribers is restored on a clone of that price point instead; a
                product- or component-level item is never cloned, and returns `422`
                if a price-point copy it restores has subscribers without the
                feature. See the description.

        Returns:
            FeatureCatalogItemResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/products/{product_id}/features/{id}/restore.json")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("product_id")
                .value(product_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .query_param(Parameter()
                .key("propagate_to_subscriptions")
                .value(propagate_to_subscriptions))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(FeatureCatalogItemResponse.from_dictionary)
            .local_error("403", "Forbidden", ErrorListResponseException)
            .local_error("404", "Not Found", APIException)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()
