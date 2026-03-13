"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class ScheduledRenewalConfigurationRequestBody(object):
    """Implementation of the 'Scheduled Renewal Configuration Request Body' model.

    Attributes:
        starts_at (datetime): (Optional) Start of the renewal term.
        ends_at (datetime): (Optional) End of the renewal term.
        lock_in_at (datetime): (Optional) Lock-in date for the renewal.
        contract_id (int): (Optional) Existing contract to associate with the
            scheduled renewal. Contracts must be enabled for your site.
        create_new_contract (bool): (Optional) Set to true to create a new contract
            when contracts are enabled. Contracts must be enabled for your site.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "starts_at": "starts_at",
        "ends_at": "ends_at",
        "lock_in_at": "lock_in_at",
        "contract_id": "contract_id",
        "create_new_contract": "create_new_contract",
    }

    _optionals = [
        "starts_at",
        "ends_at",
        "lock_in_at",
        "contract_id",
        "create_new_contract",
    ]

    def __init__(
        self,
        starts_at=APIHelper.SKIP,
        ends_at=APIHelper.SKIP,
        lock_in_at=APIHelper.SKIP,
        contract_id=APIHelper.SKIP,
        create_new_contract=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ScheduledRenewalConfigurationRequestBody instance."""
        # Initialize members of the class
        if starts_at is not APIHelper.SKIP:
            self.starts_at =\
                 APIHelper.apply_datetime_converter(
                starts_at, APIHelper.RFC3339DateTime)\
                 if starts_at else None
        if ends_at is not APIHelper.SKIP:
            self.ends_at =\
                 APIHelper.apply_datetime_converter(
                ends_at, APIHelper.RFC3339DateTime)\
                 if ends_at else None
        if lock_in_at is not APIHelper.SKIP:
            self.lock_in_at =\
                 APIHelper.apply_datetime_converter(
                lock_in_at, APIHelper.RFC3339DateTime)\
                 if lock_in_at else None
        if contract_id is not APIHelper.SKIP:
            self.contract_id = contract_id
        if create_new_contract is not APIHelper.SKIP:
            self.create_new_contract = create_new_contract

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
        starts_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("starts_at")).datetime\
            if dictionary.get("starts_at") else APIHelper.SKIP
        ends_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("ends_at")).datetime\
            if dictionary.get("ends_at") else APIHelper.SKIP
        lock_in_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("lock_in_at")).datetime\
            if dictionary.get("lock_in_at") else APIHelper.SKIP
        contract_id =\
            dictionary.get("contract_id")\
            if dictionary.get("contract_id")\
                else APIHelper.SKIP
        create_new_contract =\
            dictionary.get("create_new_contract")\
            if "create_new_contract" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(starts_at,
                   ends_at,
                   lock_in_at,
                   contract_id,
                   create_new_contract,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _starts_at=(
            self.starts_at
            if hasattr(self, "starts_at")
            else None
        )
        _ends_at=(
            self.ends_at
            if hasattr(self, "ends_at")
            else None
        )
        _lock_in_at=(
            self.lock_in_at
            if hasattr(self, "lock_in_at")
            else None
        )
        _contract_id=(
            self.contract_id
            if hasattr(self, "contract_id")
            else None
        )
        _create_new_contract=(
            self.create_new_contract
            if hasattr(self, "create_new_contract")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"starts_at={_starts_at!r}, "
            f"ends_at={_ends_at!r}, "
            f"lock_in_at={_lock_in_at!r}, "
            f"contract_id={_contract_id!r}, "
            f"create_new_contract={_create_new_contract!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _starts_at=(
            self.starts_at
            if hasattr(self, "starts_at")
            else None
        )
        _ends_at=(
            self.ends_at
            if hasattr(self, "ends_at")
            else None
        )
        _lock_in_at=(
            self.lock_in_at
            if hasattr(self, "lock_in_at")
            else None
        )
        _contract_id=(
            self.contract_id
            if hasattr(self, "contract_id")
            else None
        )
        _create_new_contract=(
            self.create_new_contract
            if hasattr(self, "create_new_contract")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"starts_at={_starts_at!s}, "
            f"ends_at={_ends_at!s}, "
            f"lock_in_at={_lock_in_at!s}, "
            f"contract_id={_contract_id!s}, "
            f"create_new_contract={_create_new_contract!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
