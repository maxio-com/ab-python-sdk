"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.aggregated_entitlement_periodicity import (
    AggregatedEntitlementPeriodicity,
)


class AggregatedEntitlement(object):
    """Implementation of the 'Aggregated Entitlement' model.

    One entitlement in a subscriber's aggregated entitlements list. Entries are
    aggregated per feature key and periodicity window, not per feature key alone. A
    `usage_limit` feature granted with two different periodicities yields two entries
    sharing one `feature_key`. Use `periodicity_key` to identify an entry uniquely.

    Attributes:
        feature_key (str): The feature's key, prefixed by kind: `feature.*` for
            `access_right`, `usage.*` for `usage_limit`, `service.*` for
            `service_right`.
        periodicity_key (str): Uniquely identifies this aggregated entry: the
            prefixed feature key, suffixed with `:{interval}:{unit}` when the
            entitlement has a periodicity window. Equal to `feature_key` when
            `periodicity` is `null`.
        name (str): The model property of type str.
        mtype (FeatureKind): The behavior of a feature: - `access_right`: a boolean
            entitlement. A subscriber either has access or does not. - `usage_limit`:
            a quantified allowance measured over a recurring period (for example,
            "10,000 API calls per month"). - `service_right`: a free-form value
            (text, boolean, or number) that isn't a simple access flag or a metered
            limit.
        value (bool | float | str | None): The aggregated value, coerced according to
            `type`: a boolean for `access_right` (and boolean `service_right`), a
            number for `usage_limit` (and numeric `service_right`), or a string for
            text `service_right`.
        enabled (bool): `true` only when the aggregated value is truthy for this
            feature's kind, and the subscription is in a live state (`active`,
            `trialing`, `assessing`, `past_due`, or `soft_failure`). `false`
            otherwise, including for `awaiting_signup`, canceled, expired, and
            on-hold subscriptions. Entitlements deliberately stay enabled through
            dunning.
        periodicity (AggregatedEntitlementPeriodicity): The model property of type
            AggregatedEntitlementPeriodicity.
        source_products (List[str]): The names of the products/components
            contributing to this entitlement. For `access_right` features, only
            contributors that granted `true` are listed.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "feature_key": "feature_key",
        "periodicity_key": "periodicity_key",
        "name": "name",
        "mtype": "type",
        "value": "value",
        "enabled": "enabled",
        "periodicity": "periodicity",
        "source_products": "source_products",
    }

    _optionals = [
        "feature_key",
        "periodicity_key",
        "name",
        "mtype",
        "value",
        "enabled",
        "periodicity",
        "source_products",
    ]

    _nullables = [
        "periodicity",
    ]

    def __init__(
        self,
        feature_key=APIHelper.SKIP,
        periodicity_key=APIHelper.SKIP,
        name=APIHelper.SKIP,
        mtype=APIHelper.SKIP,
        value=APIHelper.SKIP,
        enabled=APIHelper.SKIP,
        periodicity=APIHelper.SKIP,
        source_products=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a AggregatedEntitlement instance."""
        # Initialize members of the class
        if feature_key is not APIHelper.SKIP:
            self.feature_key = feature_key
        if periodicity_key is not APIHelper.SKIP:
            self.periodicity_key = periodicity_key
        if name is not APIHelper.SKIP:
            self.name = name
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if value is not APIHelper.SKIP:
            self.value = value
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if periodicity is not APIHelper.SKIP:
            self.periodicity = periodicity
        if source_products is not APIHelper.SKIP:
            self.source_products = source_products

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
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        feature_key =\
            dictionary.get("feature_key")\
            if dictionary.get("feature_key")\
                else APIHelper.SKIP
        periodicity_key =\
            dictionary.get("periodicity_key")\
            if dictionary.get("periodicity_key")\
                else APIHelper.SKIP
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
        mtype =\
            dictionary.get("type")\
            if dictionary.get("type")\
                else APIHelper.SKIP
        value = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("AggregatedEntitlementValue"),
            dictionary.get("value"),
            False)\
            if dictionary.get("value") is not None\
            else APIHelper.SKIP
        enabled =\
            dictionary.get("enabled")\
            if "enabled" in dictionary.keys()\
                else APIHelper.SKIP
        if "periodicity" in dictionary.keys():
            periodicity =\
                AggregatedEntitlementPeriodicity.from_dictionary(
                dictionary.get("periodicity"))\
                if dictionary.get("periodicity") else None
        else:
            periodicity = APIHelper.SKIP
        source_products =\
            dictionary.get("source_products")\
            if dictionary.get("source_products")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(feature_key,
                   periodicity_key,
                   name,
                   mtype,
                   value,
                   enabled,
                   periodicity,
                   source_products,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _feature_key=(
            self.feature_key
            if hasattr(self, "feature_key")
            else None
        )
        _periodicity_key=(
            self.periodicity_key
            if hasattr(self, "periodicity_key")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _mtype=(
            self.mtype
            if hasattr(self, "mtype")
            else None
        )
        _value=(
            self.value
            if hasattr(self, "value")
            else None
        )
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _periodicity=(
            self.periodicity
            if hasattr(self, "periodicity")
            else None
        )
        _source_products=(
            self.source_products
            if hasattr(self, "source_products")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"feature_key={_feature_key!r}, "
            f"periodicity_key={_periodicity_key!r}, "
            f"name={_name!r}, "
            f"mtype={_mtype!r}, "
            f"value={_value!r}, "
            f"enabled={_enabled!r}, "
            f"periodicity={_periodicity!r}, "
            f"source_products={_source_products!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _feature_key=(
            self.feature_key
            if hasattr(self, "feature_key")
            else None
        )
        _periodicity_key=(
            self.periodicity_key
            if hasattr(self, "periodicity_key")
            else None
        )
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _mtype=(
            self.mtype
            if hasattr(self, "mtype")
            else None
        )
        _value=(
            self.value
            if hasattr(self, "value")
            else None
        )
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _periodicity=(
            self.periodicity
            if hasattr(self, "periodicity")
            else None
        )
        _source_products=(
            self.source_products
            if hasattr(self, "source_products")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"feature_key={_feature_key!s}, "
            f"periodicity_key={_periodicity_key!s}, "
            f"name={_name!s}, "
            f"mtype={_mtype!s}, "
            f"value={_value!s}, "
            f"enabled={_enabled!s}, "
            f"periodicity={_periodicity!s}, "
            f"source_products={_source_products!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
