"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.models.aggregated_entitlement import (
    AggregatedEntitlement,
)


class AggregatedEntitlementsResponse(object):
    """Implementation of the 'Aggregated Entitlements Response' model.

    Attributes:
        subscription_id (int): The model property of type int.
        customer_id (int): The model property of type int.
        status (str): The subscription's current state, e.g. `active`, `trialing`,
            `canceled`.
        entitlements (List[AggregatedEntitlement]): The model property of type
            List[AggregatedEntitlement].
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subscription_id": "subscription_id",
        "customer_id": "customer_id",
        "status": "status",
        "entitlements": "entitlements",
    }

    def __init__(
        self,
        subscription_id=None,
        customer_id=None,
        status=None,
        entitlements=None,
        additional_properties=None):
        """Initialize a AggregatedEntitlementsResponse instance."""
        # Initialize members of the class
        self.subscription_id = subscription_id
        self.customer_id = customer_id
        self.status = status
        self.entitlements = entitlements

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
        subscription_id =\
            dictionary.get("subscription_id")\
            if dictionary.get("subscription_id")\
                else None
        customer_id =\
            dictionary.get("customer_id")\
            if dictionary.get("customer_id")\
                else None
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else None
        entitlements = None
        if dictionary.get("entitlements") is not None:
            entitlements = [
                AggregatedEntitlement.from_dictionary(x)
                    for x in dictionary.get("entitlements")
            ]

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(subscription_id,
                   customer_id,
                   status,
                   entitlements,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _subscription_id=self.subscription_id
        _customer_id=self.customer_id
        _status=self.status
        _entitlements=self.entitlements
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"subscription_id={_subscription_id!r}, "
            f"customer_id={_customer_id!r}, "
            f"status={_status!r}, "
            f"entitlements={_entitlements!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _subscription_id=self.subscription_id
        _customer_id=self.customer_id
        _status=self.status
        _entitlements=self.entitlements
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"subscription_id={_subscription_id!s}, "
            f"customer_id={_customer_id!s}, "
            f"status={_status!s}, "
            f"entitlements={_entitlements!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
