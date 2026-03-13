"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
class SubscriptionMRRBreakout(object):
    """Implementation of the 'Subscription MRR Breakout' model.

    Attributes:
        plan_amount_in_cents (int): The model property of type int.
        usage_amount_in_cents (int): The model property of type int.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "plan_amount_in_cents": "plan_amount_in_cents",
        "usage_amount_in_cents": "usage_amount_in_cents",
    }

    def __init__(
        self,
        plan_amount_in_cents=None,
        usage_amount_in_cents=None,
        additional_properties=None):
        """Initialize a SubscriptionMRRBreakout instance."""
        # Initialize members of the class
        self.plan_amount_in_cents = plan_amount_in_cents
        self.usage_amount_in_cents = usage_amount_in_cents

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
        plan_amount_in_cents =\
            dictionary.get("plan_amount_in_cents")\
            if dictionary.get("plan_amount_in_cents")\
                else None
        usage_amount_in_cents =\
            dictionary.get("usage_amount_in_cents")\
            if dictionary.get("usage_amount_in_cents")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(plan_amount_in_cents,
                   usage_amount_in_cents,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _plan_amount_in_cents=self.plan_amount_in_cents
        _usage_amount_in_cents=self.usage_amount_in_cents
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"plan_amount_in_cents={_plan_amount_in_cents!r}, "
            f"usage_amount_in_cents={_usage_amount_in_cents!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _plan_amount_in_cents=self.plan_amount_in_cents
        _usage_amount_in_cents=self.usage_amount_in_cents
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"plan_amount_in_cents={_plan_amount_in_cents!s}, "
            f"usage_amount_in_cents={_usage_amount_in_cents!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
