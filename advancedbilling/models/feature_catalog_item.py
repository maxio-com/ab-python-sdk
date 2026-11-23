"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class FeatureCatalogItem(object):
    """Implementation of the 'Feature Catalog Item' model.

    A feature template attached to a specific product or component (or one of their
    price points), with a concrete value. When a subscriber signs up for or is
    assigned this product/component, the feature catalog item is provisioned as an
    entitlement on their subscription.

    Attributes:
        id (int): The model property of type int.
        feature_template_id (int): The id of the feature template this item was
            created from.
        feature_key (str): The `key` of the parent feature template.
        feature_name (str): The `name` of the parent feature template.
        feature_kind (FeatureKind): The behavior of a feature: - `access_right`: a
            boolean entitlement. A subscriber either has access or does not. -
            `usage_limit`: a quantified allowance measured over a recurring period
            (for example, "10,000 API calls per month"). - `service_right`: a
            free-form value (text, boolean, or number) that isn't a simple access
            flag or a metered limit.
        value (str): The value granted by this feature catalog item. Interpreted
            according to `feature_kind`: `"true"`/`"false"` for `access_right`, a
            numeric string for `usage_limit`, or any string for `service_right`
            (shaped by the feature template's `value_type`).
        periodicity_interval (int): Set when `feature_kind` is `usage_limit`; `null`
            otherwise.
        periodicity_unit (EntitlementPeriodicityUnit): Set when `feature_kind` is
            `usage_limit`; `null` otherwise.
        price_point_type (FeatureOwnerPricePointType): `null` when this feature
            catalog item applies to every price point of its owning
            product/component. Set when the feature catalog item is an override for
            one specific price point.
        price_point_id (int): Set together with `price_point_type` for
            price-point-specific overrides.
        archived_at (datetime): The model property of type datetime.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "feature_template_id": "feature_template_id",
        "feature_key": "feature_key",
        "feature_name": "feature_name",
        "feature_kind": "feature_kind",
        "value": "value",
        "periodicity_interval": "periodicity_interval",
        "periodicity_unit": "periodicity_unit",
        "price_point_type": "price_point_type",
        "price_point_id": "price_point_id",
        "archived_at": "archived_at",
        "created_at": "created_at",
        "updated_at": "updated_at",
    }

    _optionals = [
        "id",
        "feature_template_id",
        "feature_key",
        "feature_name",
        "feature_kind",
        "value",
        "periodicity_interval",
        "periodicity_unit",
        "price_point_type",
        "price_point_id",
        "archived_at",
        "created_at",
        "updated_at",
    ]

    _nullables = [
        "periodicity_interval",
        "periodicity_unit",
        "price_point_type",
        "price_point_id",
        "archived_at",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        feature_template_id=APIHelper.SKIP,
        feature_key=APIHelper.SKIP,
        feature_name=APIHelper.SKIP,
        feature_kind=APIHelper.SKIP,
        value=APIHelper.SKIP,
        periodicity_interval=APIHelper.SKIP,
        periodicity_unit=APIHelper.SKIP,
        price_point_type=APIHelper.SKIP,
        price_point_id=APIHelper.SKIP,
        archived_at=APIHelper.SKIP,
        created_at=APIHelper.SKIP,
        updated_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a FeatureCatalogItem instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if feature_template_id is not APIHelper.SKIP:
            self.feature_template_id = feature_template_id
        if feature_key is not APIHelper.SKIP:
            self.feature_key = feature_key
        if feature_name is not APIHelper.SKIP:
            self.feature_name = feature_name
        if feature_kind is not APIHelper.SKIP:
            self.feature_kind = feature_kind
        if value is not APIHelper.SKIP:
            self.value = value
        if periodicity_interval is not APIHelper.SKIP:
            self.periodicity_interval = periodicity_interval
        if periodicity_unit is not APIHelper.SKIP:
            self.periodicity_unit = periodicity_unit
        if price_point_type is not APIHelper.SKIP:
            self.price_point_type = price_point_type
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id
        if archived_at is not APIHelper.SKIP:
            self.archived_at =\
                 APIHelper.apply_datetime_converter(
                archived_at, APIHelper.RFC3339DateTime)\
                 if archived_at else None
        if created_at is not APIHelper.SKIP:
            self.created_at =\
                 APIHelper.apply_datetime_converter(
                created_at, APIHelper.RFC3339DateTime)\
                 if created_at else None
        if updated_at is not APIHelper.SKIP:
            self.updated_at =\
                 APIHelper.apply_datetime_converter(
                updated_at, APIHelper.RFC3339DateTime)\
                 if updated_at else None

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        feature_template_id =\
            dictionary.get("feature_template_id")\
            if dictionary.get("feature_template_id")\
                else APIHelper.SKIP
        feature_key =\
            dictionary.get("feature_key")\
            if dictionary.get("feature_key")\
                else APIHelper.SKIP
        feature_name =\
            dictionary.get("feature_name")\
            if dictionary.get("feature_name")\
                else APIHelper.SKIP
        feature_kind =\
            dictionary.get("feature_kind")\
            if dictionary.get("feature_kind")\
                else APIHelper.SKIP
        value =\
            dictionary.get("value")\
            if dictionary.get("value")\
                else APIHelper.SKIP
        periodicity_interval =\
            dictionary.get("periodicity_interval")\
            if "periodicity_interval" in dictionary.keys()\
                else APIHelper.SKIP
        periodicity_unit =\
            dictionary.get("periodicity_unit")\
            if "periodicity_unit" in dictionary.keys()\
                else APIHelper.SKIP
        price_point_type =\
            dictionary.get("price_point_type")\
            if "price_point_type" in dictionary.keys()\
                else APIHelper.SKIP
        price_point_id =\
            dictionary.get("price_point_id")\
            if "price_point_id" in dictionary.keys()\
                else APIHelper.SKIP
        if "archived_at" in dictionary.keys():
            archived_at = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("archived_at")).datetime\
                if dictionary.get("archived_at") else None

        else:
            archived_at = APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_at")).datetime\
            if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("updated_at")).datetime\
            if dictionary.get("updated_at") else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   feature_template_id,
                   feature_key,
                   feature_name,
                   feature_kind,
                   value,
                   periodicity_interval,
                   periodicity_unit,
                   price_point_type,
                   price_point_id,
                   archived_at,
                   created_at,
                   updated_at,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _feature_template_id=(
            self.feature_template_id
            if hasattr(self, "feature_template_id")
            else None
        )
        _feature_key=(
            self.feature_key
            if hasattr(self, "feature_key")
            else None
        )
        _feature_name=(
            self.feature_name
            if hasattr(self, "feature_name")
            else None
        )
        _feature_kind=(
            self.feature_kind
            if hasattr(self, "feature_kind")
            else None
        )
        _value=(
            self.value
            if hasattr(self, "value")
            else None
        )
        _periodicity_interval=(
            self.periodicity_interval
            if hasattr(self, "periodicity_interval")
            else None
        )
        _periodicity_unit=(
            self.periodicity_unit
            if hasattr(self, "periodicity_unit")
            else None
        )
        _price_point_type=(
            self.price_point_type
            if hasattr(self, "price_point_type")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _archived_at=(
            self.archived_at
            if hasattr(self, "archived_at")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _updated_at=(
            self.updated_at
            if hasattr(self, "updated_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"feature_template_id={_feature_template_id!r}, "
            f"feature_key={_feature_key!r}, "
            f"feature_name={_feature_name!r}, "
            f"feature_kind={_feature_kind!r}, "
            f"value={_value!r}, "
            f"periodicity_interval={_periodicity_interval!r}, "
            f"periodicity_unit={_periodicity_unit!r}, "
            f"price_point_type={_price_point_type!r}, "
            f"price_point_id={_price_point_id!r}, "
            f"archived_at={_archived_at!r}, "
            f"created_at={_created_at!r}, "
            f"updated_at={_updated_at!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _feature_template_id=(
            self.feature_template_id
            if hasattr(self, "feature_template_id")
            else None
        )
        _feature_key=(
            self.feature_key
            if hasattr(self, "feature_key")
            else None
        )
        _feature_name=(
            self.feature_name
            if hasattr(self, "feature_name")
            else None
        )
        _feature_kind=(
            self.feature_kind
            if hasattr(self, "feature_kind")
            else None
        )
        _value=(
            self.value
            if hasattr(self, "value")
            else None
        )
        _periodicity_interval=(
            self.periodicity_interval
            if hasattr(self, "periodicity_interval")
            else None
        )
        _periodicity_unit=(
            self.periodicity_unit
            if hasattr(self, "periodicity_unit")
            else None
        )
        _price_point_type=(
            self.price_point_type
            if hasattr(self, "price_point_type")
            else None
        )
        _price_point_id=(
            self.price_point_id
            if hasattr(self, "price_point_id")
            else None
        )
        _archived_at=(
            self.archived_at
            if hasattr(self, "archived_at")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _updated_at=(
            self.updated_at
            if hasattr(self, "updated_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"feature_template_id={_feature_template_id!s}, "
            f"feature_key={_feature_key!s}, "
            f"feature_name={_feature_name!s}, "
            f"feature_kind={_feature_kind!s}, "
            f"value={_value!s}, "
            f"periodicity_interval={_periodicity_interval!s}, "
            f"periodicity_unit={_periodicity_unit!s}, "
            f"price_point_type={_price_point_type!s}, "
            f"price_point_id={_price_point_id!s}, "
            f"archived_at={_archived_at!s}, "
            f"created_at={_created_at!s}, "
            f"updated_at={_updated_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
