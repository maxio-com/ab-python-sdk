"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class Feature3(object):
    """Implementation of the 'Feature3' model.

    Attributes:
        value (str): The model property of type str.
        periodicity_interval (int): The model property of type int.
        periodicity_unit (EntitlementPeriodicityUnit): The model property of type
            EntitlementPeriodicityUnit.
        propagate_to_subscriptions (bool): When `true`, existing subscriptions on the
            item's price point are updated with the new `value`/periodicity by a
            background job shortly after. Has no effect on a product/component-level
            item. When `false` (default) and the item's price point already has
            subscribers, the update is made on a clone of the price point instead,
            and existing subscribers are unaffected.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "value": "value",
        "periodicity_interval": "periodicity_interval",
        "periodicity_unit": "periodicity_unit",
        "propagate_to_subscriptions": "propagate_to_subscriptions",
    }

    _optionals = [
        "value",
        "periodicity_interval",
        "periodicity_unit",
        "propagate_to_subscriptions",
    ]

    _nullables = [
        "periodicity_interval",
        "periodicity_unit",
    ]

    def __init__(
        self,
        value=APIHelper.SKIP,
        periodicity_interval=APIHelper.SKIP,
        periodicity_unit=APIHelper.SKIP,
        propagate_to_subscriptions=False,
        additional_properties=None):
        """Initialize a Feature3 instance."""
        # Initialize members of the class
        if value is not APIHelper.SKIP:
            self.value = value
        if periodicity_interval is not APIHelper.SKIP:
            self.periodicity_interval = periodicity_interval
        if periodicity_unit is not APIHelper.SKIP:
            self.periodicity_unit = periodicity_unit
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
        propagate_to_subscriptions =\
            dictionary.get("propagate_to_subscriptions")\
            if dictionary.get("propagate_to_subscriptions")\
                else False

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(value,
                   periodicity_interval,
                   periodicity_unit,
                   propagate_to_subscriptions,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
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
        _propagate_to_subscriptions=(
            self.propagate_to_subscriptions
            if hasattr(self, "propagate_to_subscriptions")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"value={_value!r}, "
            f"periodicity_interval={_periodicity_interval!r}, "
            f"periodicity_unit={_periodicity_unit!r}, "
            f"propagate_to_subscriptions={_propagate_to_subscriptions!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
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
        _propagate_to_subscriptions=(
            self.propagate_to_subscriptions
            if hasattr(self, "propagate_to_subscriptions")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"value={_value!s}, "
            f"periodicity_interval={_periodicity_interval!s}, "
            f"periodicity_unit={_periodicity_unit!s}, "
            f"propagate_to_subscriptions={_propagate_to_subscriptions!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
