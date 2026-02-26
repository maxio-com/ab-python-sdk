"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser


class ScheduledRenewalLockInRequest(object):
    """Implementation of the 'Scheduled Renewal Lock In Request' model.

    Attributes:
        lock_in_at (date): Date to lock in the renewal.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "lock_in_at": "lock_in_at",
    }

    def __init__(
        self,
        lock_in_at=None,
        additional_properties=None):
        """Initialize a ScheduledRenewalLockInRequest instance."""
        # Initialize members of the class
        self.lock_in_at = lock_in_at

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
        lock_in_at = dateutil.parser.parse(
            dictionary.get("lock_in_at")).date()\
            if dictionary.get("lock_in_at") else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(lock_in_at,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _lock_in_at=self.lock_in_at
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"lock_in_at={_lock_in_at!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _lock_in_at=self.lock_in_at
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"lock_in_at={_lock_in_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
