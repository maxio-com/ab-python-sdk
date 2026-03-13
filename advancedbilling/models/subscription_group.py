"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.subscription_group_payment_profile import (
    SubscriptionGroupPaymentProfile,
)


class SubscriptionGroup(object):
    """Implementation of the 'Subscription Group' model.

    Attributes:
        uid (str): The model property of type str.
        customer_id (int): The model property of type int.
        payment_profile (SubscriptionGroupPaymentProfile): The model property of type
            SubscriptionGroupPaymentProfile.
        payment_collection_method (CollectionMethod): The type of payment collection
            to be used in the subscription. For legacy Statements Architecture valid
            options are - `invoice`, `automatic`. For current Relationship Invoicing
            Architecture valid options are - `remittance`, `automatic`, `prepaid`.
        subscription_ids (List[int]): The model property of type List[int].
        created_at (datetime): The model property of type datetime.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": "uid",
        "customer_id": "customer_id",
        "payment_profile": "payment_profile",
        "payment_collection_method": "payment_collection_method",
        "subscription_ids": "subscription_ids",
        "created_at": "created_at",
    }

    _optionals = [
        "uid",
        "customer_id",
        "payment_profile",
        "payment_collection_method",
        "subscription_ids",
        "created_at",
    ]

    def __init__(
        self,
        uid=APIHelper.SKIP,
        customer_id=APIHelper.SKIP,
        payment_profile=APIHelper.SKIP,
        payment_collection_method=APIHelper.SKIP,
        subscription_ids=APIHelper.SKIP,
        created_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionGroup instance."""
        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id
        if payment_profile is not APIHelper.SKIP:
            self.payment_profile = payment_profile
        if payment_collection_method is not APIHelper.SKIP:
            self.payment_collection_method = payment_collection_method
        if subscription_ids is not APIHelper.SKIP:
            self.subscription_ids = subscription_ids
        if created_at is not APIHelper.SKIP:
            self.created_at =\
                 APIHelper.apply_datetime_converter(
                created_at, APIHelper.RFC3339DateTime)\
                 if created_at else None

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
        uid =\
            dictionary.get("uid")\
            if dictionary.get("uid")\
                else APIHelper.SKIP
        customer_id =\
            dictionary.get("customer_id")\
            if dictionary.get("customer_id")\
                else APIHelper.SKIP
        payment_profile =\
            SubscriptionGroupPaymentProfile.from_dictionary(
                dictionary.get("payment_profile"))\
                if "payment_profile" in dictionary.keys()\
                else APIHelper.SKIP
        payment_collection_method =\
            dictionary.get("payment_collection_method")\
            if dictionary.get("payment_collection_method")\
                else APIHelper.SKIP
        subscription_ids =\
            dictionary.get("subscription_ids")\
            if dictionary.get("subscription_ids")\
                else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(
            dictionary.get("created_at")).datetime\
            if dictionary.get("created_at") else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(uid,
                   customer_id,
                   payment_profile,
                   payment_collection_method,
                   subscription_ids,
                   created_at,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _uid=(
            self.uid
            if hasattr(self, "uid")
            else None
        )
        _customer_id=(
            self.customer_id
            if hasattr(self, "customer_id")
            else None
        )
        _payment_profile=(
            self.payment_profile
            if hasattr(self, "payment_profile")
            else None
        )
        _payment_collection_method=(
            self.payment_collection_method
            if hasattr(self, "payment_collection_method")
            else None
        )
        _subscription_ids=(
            self.subscription_ids
            if hasattr(self, "subscription_ids")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!r}, "
            f"customer_id={_customer_id!r}, "
            f"payment_profile={_payment_profile!r}, "
            f"payment_collection_method={_payment_collection_method!r}, "
            f"subscription_ids={_subscription_ids!r}, "
            f"created_at={_created_at!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _uid=(
            self.uid
            if hasattr(self, "uid")
            else None
        )
        _customer_id=(
            self.customer_id
            if hasattr(self, "customer_id")
            else None
        )
        _payment_profile=(
            self.payment_profile
            if hasattr(self, "payment_profile")
            else None
        )
        _payment_collection_method=(
            self.payment_collection_method
            if hasattr(self, "payment_collection_method")
            else None
        )
        _subscription_ids=(
            self.subscription_ids
            if hasattr(self, "subscription_ids")
            else None
        )
        _created_at=(
            self.created_at
            if hasattr(self, "created_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"uid={_uid!s}, "
            f"customer_id={_customer_id!s}, "
            f"payment_profile={_payment_profile!s}, "
            f"payment_collection_method={_payment_collection_method!s}, "
            f"subscription_ids={_subscription_ids!s}, "
            f"created_at={_created_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
