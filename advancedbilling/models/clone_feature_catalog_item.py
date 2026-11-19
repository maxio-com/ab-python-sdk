"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class CloneFeatureCatalogItem(object):
    """Implementation of the 'Clone Feature Catalog Item' model.

    A feature to put on the cloned price point. Requires Entitlements to be enabled
    for the site; ignored otherwise.
    Unlike Create Feature Catalog Item, nothing falls back to the feature template's
    defaults: send `value`, and for a `usage_limit` feature its periodicity (and any
    grant expiration) explicitly. If any item can't be applied, for example a missing
    `value`, a `usage_limit` item without periodicity, or an archived or unknown
    feature template, the whole clone fails with `422` and nothing is created.

    Attributes:
        feature_template_id (int): The model property of type int.
        value (str): The model property of type str.
        periodicity_interval (int): Required for `usage_limit` features; must be
            omitted for other kinds.
        periodicity_unit (EntitlementPeriodicityUnit): Required for `usage_limit`
            features; must be omitted for other kinds.
        grant_expiration_interval (int): `usage_limit` features only. A positive
            number of `grant_expiration_unit`s; required with `day` or `month`, and
            must be omitted with `until_next_refill`.
        grant_expiration_unit (GrantExpirationUnit): `usage_limit` features only.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "feature_template_id": "feature_template_id",
        "value": "value",
        "periodicity_interval": "periodicity_interval",
        "periodicity_unit": "periodicity_unit",
        "grant_expiration_interval": "grant_expiration_interval",
        "grant_expiration_unit": "grant_expiration_unit",
    }

    _optionals = [
        "periodicity_interval",
        "periodicity_unit",
        "grant_expiration_interval",
        "grant_expiration_unit",
    ]

    _nullables = [
        "periodicity_interval",
        "periodicity_unit",
        "grant_expiration_interval",
        "grant_expiration_unit",
    ]

    def __init__(
        self,
        feature_template_id=None,
        value=None,
        periodicity_interval=APIHelper.SKIP,
        periodicity_unit=APIHelper.SKIP,
        grant_expiration_interval=APIHelper.SKIP,
        grant_expiration_unit=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CloneFeatureCatalogItem instance."""
        # Initialize members of the class
        self.feature_template_id = feature_template_id
        self.value = value
        if periodicity_interval is not APIHelper.SKIP:
            self.periodicity_interval = periodicity_interval
        if periodicity_unit is not APIHelper.SKIP:
            self.periodicity_unit = periodicity_unit
        if grant_expiration_interval is not APIHelper.SKIP:
            self.grant_expiration_interval = grant_expiration_interval
        if grant_expiration_unit is not APIHelper.SKIP:
            self.grant_expiration_unit = grant_expiration_unit

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
                else None
        periodicity_interval =\
            dictionary.get("periodicity_interval")\
            if "periodicity_interval" in dictionary.keys()\
                else APIHelper.SKIP
        periodicity_unit =\
            dictionary.get("periodicity_unit")\
            if "periodicity_unit" in dictionary.keys()\
                else APIHelper.SKIP
        grant_expiration_interval =\
            dictionary.get("grant_expiration_interval")\
            if "grant_expiration_interval" in dictionary.keys()\
                else APIHelper.SKIP
        grant_expiration_unit =\
            dictionary.get("grant_expiration_unit")\
            if "grant_expiration_unit" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(feature_template_id,
                   value,
                   periodicity_interval,
                   periodicity_unit,
                   grant_expiration_interval,
                   grant_expiration_unit,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _feature_template_id=self.feature_template_id
        _value=self.value
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
        _grant_expiration_interval=(
            self.grant_expiration_interval
            if hasattr(self, "grant_expiration_interval")
            else None
        )
        _grant_expiration_unit=(
            self.grant_expiration_unit
            if hasattr(self, "grant_expiration_unit")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"feature_template_id={_feature_template_id!r}, "
            f"value={_value!r}, "
            f"periodicity_interval={_periodicity_interval!r}, "
            f"periodicity_unit={_periodicity_unit!r}, "
            f"grant_expiration_interval={_grant_expiration_interval!r}, "
            f"grant_expiration_unit={_grant_expiration_unit!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _feature_template_id=self.feature_template_id
        _value=self.value
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
        _grant_expiration_interval=(
            self.grant_expiration_interval
            if hasattr(self, "grant_expiration_interval")
            else None
        )
        _grant_expiration_unit=(
            self.grant_expiration_unit
            if hasattr(self, "grant_expiration_unit")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"feature_template_id={_feature_template_id!s}, "
            f"value={_value!s}, "
            f"periodicity_interval={_periodicity_interval!s}, "
            f"periodicity_unit={_periodicity_unit!s}, "
            f"grant_expiration_interval={_grant_expiration_interval!s}, "
            f"grant_expiration_unit={_grant_expiration_unit!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
