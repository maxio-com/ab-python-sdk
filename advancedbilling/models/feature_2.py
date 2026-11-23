"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Feature2(object):
    """Implementation of the 'Feature2' model.

    Attributes:
        feature_template_id (int): The id of the feature template to attach.
        value (str): The value granted. Defaults to the feature template's
            `default_value`; required when the template has none.
        periodicity_interval (int): Required for `usage_limit` features, unless the
            feature template has a default periodicity, which is used when omitted.
            Must be omitted for other kinds.
        periodicity_unit (EntitlementPeriodicityUnit): Required for `usage_limit`
            features, unless the feature template has a default periodicity, which is
            used when omitted. Must be omitted for other kinds.
        price_point_type (FeatureOwnerPricePointType): Set together with
            `price_point_id` to scope the feature catalog item to a single price
            point. Omit both to create a product/component-level item, which is a
            template: it is copied onto price points created afterwards (except
            bulk-created ones; Clone Component Price Point applies only the items
            sent with it), but not added to price points that already exist or to
            their subscribers.
        price_point_id (int): The model property of type int.
        propagate_to_subscriptions (bool): Applies to price-point-scoped items only.
            When `true`, existing subscriptions on that price point are granted an
            entitlement for this feature by a background job shortly after, instead
            of at their next subscription change. When `false` (default) and the
            price point already has subscribers, the feature is created on a clone of
            the price point instead, and existing subscribers are unaffected. On a
            product/component-level item it has no effect, except when the call
            restores that item's archived price-point copies (creating an item again
            for a feature template whose item was archived): then `true` grants the
            feature to those price points' subscribers, and without it the call
            returns `422` if any of them lack the feature.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "feature_template_id": "feature_template_id",
        "value": "value",
        "periodicity_interval": "periodicity_interval",
        "periodicity_unit": "periodicity_unit",
        "price_point_type": "price_point_type",
        "price_point_id": "price_point_id",
        "propagate_to_subscriptions": "propagate_to_subscriptions",
    }

    _optionals = [
        "value",
        "periodicity_interval",
        "periodicity_unit",
        "price_point_type",
        "price_point_id",
        "propagate_to_subscriptions",
    ]

    _nullables = [
        "periodicity_interval",
        "periodicity_unit",
        "price_point_type",
        "price_point_id",
    ]

    def __init__(
        self,
        feature_template_id=None,
        value=APIHelper.SKIP,
        periodicity_interval=APIHelper.SKIP,
        periodicity_unit=APIHelper.SKIP,
        price_point_type=APIHelper.SKIP,
        price_point_id=APIHelper.SKIP,
        propagate_to_subscriptions=False,
        additional_properties=None):
        """Initialize a Feature2 instance."""
        # Initialize members of the class
        self.feature_template_id = feature_template_id
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
        self.propagate_to_subscriptions = propagate_to_subscriptions

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
        feature_template_id =\
            dictionary.get("feature_template_id")\
            if dictionary.get("feature_template_id")\
                else None
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
        propagate_to_subscriptions =\
            dictionary.get("propagate_to_subscriptions")\
            if dictionary.get("propagate_to_subscriptions")\
                else False

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(feature_template_id,
                   value,
                   periodicity_interval,
                   periodicity_unit,
                   price_point_type,
                   price_point_id,
                   propagate_to_subscriptions,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _feature_template_id=self.feature_template_id
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
        _propagate_to_subscriptions=(
            self.propagate_to_subscriptions
            if hasattr(self, "propagate_to_subscriptions")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"feature_template_id={_feature_template_id!r}, "
            f"value={_value!r}, "
            f"periodicity_interval={_periodicity_interval!r}, "
            f"periodicity_unit={_periodicity_unit!r}, "
            f"price_point_type={_price_point_type!r}, "
            f"price_point_id={_price_point_id!r}, "
            f"propagate_to_subscriptions={_propagate_to_subscriptions!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _feature_template_id=self.feature_template_id
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
        _propagate_to_subscriptions=(
            self.propagate_to_subscriptions
            if hasattr(self, "propagate_to_subscriptions")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"feature_template_id={_feature_template_id!s}, "
            f"value={_value!s}, "
            f"periodicity_interval={_periodicity_interval!s}, "
            f"periodicity_unit={_periodicity_unit!s}, "
            f"price_point_type={_price_point_type!s}, "
            f"price_point_id={_price_point_id!s}, "
            f"propagate_to_subscriptions={_propagate_to_subscriptions!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
