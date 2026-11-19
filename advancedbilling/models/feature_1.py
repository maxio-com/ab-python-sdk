"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Feature1(object):
    """Implementation of the 'Feature1' model.

    `key` cannot be changed once set. `kind` cannot be changed once any feature
    catalog item has been created from this template.

    Attributes:
        name (str): The model property of type str.
        description (str): The model property of type str.
        unit (str): The model property of type str.
        value_type (FeatureValueType): The data type of a feature's value. For
            `access_right` features this is always `boolean`, and for `usage_limit`
            features this is always `numeric`. For `service_right` features, you
            choose the value type explicitly.
        default_value (str): The model property of type str.
        default_periodicity_interval (int): The model property of type int.
        default_periodicity_unit (EntitlementPeriodicityUnit): The model property of
            type EntitlementPeriodicityUnit.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": "name",
        "description": "description",
        "unit": "unit",
        "value_type": "value_type",
        "default_value": "default_value",
        "default_periodicity_interval": "default_periodicity_interval",
        "default_periodicity_unit": "default_periodicity_unit",
    }

    _optionals = [
        "name",
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
        name=APIHelper.SKIP,
        description=APIHelper.SKIP,
        unit=APIHelper.SKIP,
        value_type=APIHelper.SKIP,
        default_value=APIHelper.SKIP,
        default_periodicity_interval=APIHelper.SKIP,
        default_periodicity_unit=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a Feature1 instance."""
        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name
        if description is not APIHelper.SKIP:
            self.description = description
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
        name =\
            dictionary.get("name")\
            if dictionary.get("name")\
                else APIHelper.SKIP
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
        return cls(name,
                   description,
                   unit,
                   value_type,
                   default_value,
                   default_periodicity_interval,
                   default_periodicity_unit,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _description=(
            self.description
            if hasattr(self, "description")
            else None
        )
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
            f"name={_name!r}, "
            f"description={_description!r}, "
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
        _name=(
            self.name
            if hasattr(self, "name")
            else None
        )
        _description=(
            self.description
            if hasattr(self, "description")
            else None
        )
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
            f"name={_name!s}, "
            f"description={_description!s}, "
            f"unit={_unit!s}, "
            f"value_type={_value_type!s}, "
            f"default_value={_default_value!s}, "
            f"default_periodicity_interval={_default_periodicity_interval!s}, "
            f"default_periodicity_unit={_default_periodicity_unit!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
