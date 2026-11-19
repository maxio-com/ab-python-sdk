"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Feature(object):
    """Implementation of the 'Feature' model.

    Attributes:
        key (str): A unique, lowercase, underscore-separated identifier for the
            feature. Immutable once set.
        name (str): The display name of the feature.
        description (str): The model property of type str.
        kind (FeatureKind): The behavior of a feature: - `access_right`: a boolean
            entitlement. A subscriber either has access or does not. - `usage_limit`:
            a quantified allowance measured over a recurring period (for example,
            "10,000 API calls per month"). - `service_right`: a free-form value
            (text, boolean, or number) that isn't a simple access flag or a metered
            limit.
        unit (str): Required when `kind` is `usage_limit`.
        value_type (FeatureValueType): Required when `kind` is `service_right`.
            Ignored for other kinds, where it is inferred automatically.
        default_value (str): The model property of type str.
        default_periodicity_interval (int): Only valid when `kind` is `usage_limit`.
        default_periodicity_unit (EntitlementPeriodicityUnit): Only valid when `kind`
            is `usage_limit`. Must be set together with
            `default_periodicity_interval`.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key": "key",
        "name": "name",
        "kind": "kind",
        "description": "description",
        "unit": "unit",
        "value_type": "value_type",
        "default_value": "default_value",
        "default_periodicity_interval": "default_periodicity_interval",
        "default_periodicity_unit": "default_periodicity_unit",
    }

    _optionals = [
        "description",
        "unit",
        "value_type",
        "default_value",
        "default_periodicity_interval",
        "default_periodicity_unit",
    ]

    _nullables = [
        "description",
        "unit",
        "default_value",
        "default_periodicity_interval",
        "default_periodicity_unit",
    ]

    def __init__(
        self,
        key=None,
        name=None,
        kind=None,
        description=APIHelper.SKIP,
        unit=APIHelper.SKIP,
        value_type=APIHelper.SKIP,
        default_value=APIHelper.SKIP,
        default_periodicity_interval=APIHelper.SKIP,
        default_periodicity_unit=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Feature instance."""
        # Initialize members of the class
        self.key = key
        self.name = name
        if description is not APIHelper.SKIP:
            self.description = description
        self.kind = kind
        if unit is not APIHelper.SKIP:
            self.unit = unit
        if value_type is not APIHelper.SKIP:
            self.value_type = value_type
        if default_value is not APIHelper.SKIP:
            self.default_value = default_value
        if default_periodicity_interval is not APIHelper.SKIP:
            self.default_periodicity_interval = default_periodicity_interval
        if default_periodicity_unit is not APIHelper.SKIP:
            self.default_periodicity_unit = default_periodicity_unit

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
        key =\
            dictionary.get("key")\
            if dictionary.get("key")\
                else None
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else None
        kind =\
            dictionary.get("kind")\
            if dictionary.get("kind")\
                else None
        description =\
            dictionary.get("description")\
            if "description" in dictionary.keys()\
                else APIHelper.SKIP
        unit =\
            dictionary.get("unit")\
            if "unit" in dictionary.keys()\
                else APIHelper.SKIP
        value_type =\
            dictionary.get("value_type")\
            if dictionary.get("value_type")\
                else APIHelper.SKIP
        default_value =\
            dictionary.get("default_value")\
            if "default_value" in dictionary.keys()\
                else APIHelper.SKIP
        default_periodicity_interval =\
            dictionary.get("default_periodicity_interval")\
            if "default_periodicity_interval" in dictionary.keys()\
                else APIHelper.SKIP
        default_periodicity_unit =\
            dictionary.get("default_periodicity_unit")\
            if "default_periodicity_unit" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(key,
                   name,
                   kind,
                   description,
                   unit,
                   value_type,
                   default_value,
                   default_periodicity_interval,
                   default_periodicity_unit,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _key=self.key
        _name=self.name
        _description=(
            self.description
            if hasattr(self, "description")
            else None
        )
        _kind=self.kind
        _unit=(
            self.unit
            if hasattr(self, "unit")
            else None
        )
        _value_type=(
            self.value_type
            if hasattr(self, "value_type")
            else None
        )
        _default_value=(
            self.default_value
            if hasattr(self, "default_value")
            else None
        )
        _default_periodicity_interval=(
            self.default_periodicity_interval
            if hasattr(self, "default_periodicity_interval")
            else None
        )
        _default_periodicity_unit=(
            self.default_periodicity_unit
            if hasattr(self, "default_periodicity_unit")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"key={_key!r}, "
            f"name={_name!r}, "
            f"description={_description!r}, "
            f"kind={_kind!r}, "
            f"unit={_unit!r}, "
            f"value_type={_value_type!r}, "
            f"default_value={_default_value!r}, "
            f"default_periodicity_interval={_default_periodicity_interval!r}, "
            f"default_periodicity_unit={_default_periodicity_unit!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _key=self.key
        _name=self.name
        _description=(
            self.description
            if hasattr(self, "description")
            else None
        )
        _kind=self.kind
        _unit=(
            self.unit
            if hasattr(self, "unit")
            else None
        )
        _value_type=(
            self.value_type
            if hasattr(self, "value_type")
            else None
        )
        _default_value=(
            self.default_value
            if hasattr(self, "default_value")
            else None
        )
        _default_periodicity_interval=(
            self.default_periodicity_interval
            if hasattr(self, "default_periodicity_interval")
            else None
        )
        _default_periodicity_unit=(
            self.default_periodicity_unit
            if hasattr(self, "default_periodicity_unit")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"key={_key!s}, "
            f"name={_name!s}, "
            f"description={_description!s}, "
            f"kind={_kind!s}, "
            f"unit={_unit!s}, "
            f"value_type={_value_type!s}, "
            f"default_value={_default_value!s}, "
            f"default_periodicity_interval={_default_periodicity_interval!s}, "
            f"default_periodicity_unit={_default_periodicity_unit!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
