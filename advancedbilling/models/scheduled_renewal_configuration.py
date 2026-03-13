"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.contract import (
    Contract,
)
from advancedbilling.models.scheduled_renewal_configuration_item import (
    ScheduledRenewalConfigurationItem,
)


class ScheduledRenewalConfiguration(object):
    """Implementation of the 'Scheduled Renewal Configuration' model.

    Attributes:
        id (int): ID of the renewal.
        site_id (int): ID of the site to which the renewal belongs.
        subscription_id (int): The id of the subscription.
        starts_at (datetime): The model property of type datetime.
        ends_at (datetime): The model property of type datetime.
        lock_in_at (datetime): The model property of type datetime.
        created_at (datetime): The model property of type datetime.
        status (str): The model property of type str.
        scheduled_renewal_configuration_items
            (List[ScheduledRenewalConfigurationItem]): The model property of type
            List[ScheduledRenewalConfigurationItem].
        contract (Contract): Contract linked to the scheduled renewal configuration.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": "id",
        "site_id": "site_id",
        "subscription_id": "subscription_id",
        "starts_at": "starts_at",
        "ends_at": "ends_at",
        "lock_in_at": "lock_in_at",
        "created_at": "created_at",
        "status": "status",
        "scheduled_renewal_configuration_items":
            "scheduled_renewal_configuration_items",
        "contract": "contract",
    }

    _optionals = [
        "id",
        "site_id",
        "subscription_id",
        "starts_at",
        "ends_at",
        "lock_in_at",
        "created_at",
        "status",
        "scheduled_renewal_configuration_items",
        "contract",
    ]

    def __init__(
        self,
        id=APIHelper.SKIP,
        site_id=APIHelper.SKIP,
        subscription_id=APIHelper.SKIP,
        starts_at=APIHelper.SKIP,
        ends_at=APIHelper.SKIP,
        lock_in_at=APIHelper.SKIP,
        created_at=APIHelper.SKIP,
        status=APIHelper.SKIP,
        scheduled_renewal_configuration_items=APIHelper.SKIP,
        contract=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a ScheduledRenewalConfiguration instance."""
        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id
        if subscription_id is not APIHelper.SKIP:
            self.subscription_id = subscription_id
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
        if created_at is not APIHelper.SKIP:
            self.created_at =\
                 APIHelper.apply_datetime_converter(
                created_at, APIHelper.RFC3339DateTime)\
                 if created_at else None
        if status is not APIHelper.SKIP:
            self.status = status
        if scheduled_renewal_configuration_items is not APIHelper.SKIP:
            self.scheduled_renewal_configuration_items =\
                 scheduled_renewal_configuration_items
        if contract is not APIHelper.SKIP:
            self.contract = contract

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
        id =\
            dictionary.get("id")\
            if dictionary.get("id")\
                else APIHelper.SKIP
        site_id =\
            dictionary.get("site_id")\
            if dictionary.get("site_id")\
                else APIHelper.SKIP
        subscription_id =\
            dictionary.get("subscription_id")\
            if dictionary.get("subscription_id")\
                else APIHelper.SKIP
        starts_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("starts_at")).datetime\
            if dictionary.get("starts_at") else APIHelper.SKIP
        ends_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("ends_at")).datetime\
            if dictionary.get("ends_at") else APIHelper.SKIP
        lock_in_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("lock_in_at")).datetime\
            if dictionary.get("lock_in_at") else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_at")).datetime\
            if dictionary.get("created_at") else APIHelper.SKIP
        status =\
            dictionary.get("status")\
            if dictionary.get("status")\
                else APIHelper.SKIP
        scheduled_renewal_configuration_items = None
        if dictionary.get("scheduled_renewal_configuration_items") is not None:
            scheduled_renewal_configuration_items = [
                ScheduledRenewalConfigurationItem.from_dictionary(x)
                    for x in dictionary.get("scheduled_renewal_configuration_items")
            ]
        else:
            scheduled_renewal_configuration_items = APIHelper.SKIP
        contract =\
            Contract.from_dictionary(
                dictionary.get("contract"))\
                if "contract" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(id,
                   site_id,
                   subscription_id,
                   starts_at,
                   ends_at,
                   lock_in_at,
                   created_at,
                   status,
                   scheduled_renewal_configuration_items,
                   contract,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _site_id=(
            self.site_id
            if hasattr(self, "site_id")
            else None
        )
        _subscription_id=(
            self.subscription_id
            if hasattr(self, "subscription_id")
            else None
        )
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
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _scheduled_renewal_configuration_items=(
            self.scheduled_renewal_configuration_items
            if hasattr(self, "scheduled_renewal_configuration_items")
            else None
        )
        _contract=(
            self.contract
            if hasattr(self, "contract")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!r}, "
            f"site_id={_site_id!r}, "
            f"subscription_id={_subscription_id!r}, "
            f"starts_at={_starts_at!r}, "
            f"ends_at={_ends_at!r}, "
            f"lock_in_at={_lock_in_at!r}, "
            f"created_at={_created_at!r}, "
            f"status={_status!r}, "
            f"scheduled_renewal_configuration_items={_scheduled_renewal_configuration_items!r}, "
            f"contract={_contract!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _id=(
            self.id
            if hasattr(self, "id")
            else None
        )
        _site_id=(
            self.site_id
            if hasattr(self, "site_id")
            else None
        )
        _subscription_id=(
            self.subscription_id
            if hasattr(self, "subscription_id")
            else None
        )
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
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _scheduled_renewal_configuration_items=(
            self.scheduled_renewal_configuration_items
            if hasattr(self, "scheduled_renewal_configuration_items")
            else None
        )
        _contract=(
            self.contract
            if hasattr(self, "contract")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"id={_id!s}, "
            f"site_id={_site_id!s}, "
            f"subscription_id={_subscription_id!s}, "
            f"starts_at={_starts_at!s}, "
            f"ends_at={_ends_at!s}, "
            f"lock_in_at={_lock_in_at!s}, "
            f"created_at={_created_at!s}, "
            f"status={_status!s}, "
            f"scheduled_renewal_configuration_items={_scheduled_renewal_configuration_items!s}, "
            f"contract={_contract!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
