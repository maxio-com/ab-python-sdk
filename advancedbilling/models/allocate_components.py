"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_allocation import (
    CreateAllocation,
)


class AllocateComponents(object):
    """Implementation of the 'Allocate Components' model.

    Attributes:
        proration_upgrade_scheme (str): The model property of type str.
        proration_downgrade_scheme (str): The model property of type str.
        allocations (List[CreateAllocation]): The model property of type
            List[CreateAllocation].
        accrue_charge (bool): The model property of type bool.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site setting if
            one is not provided.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site setting if
            one is not provided.
        payment_collection_method (CollectionMethod): (Optional) If not passed, the
            allocation(s) will use the payment collection method on the subscription
        initiate_dunning (bool): If true, if the immediate component payment fails,
            initiate dunning for the subscription.  Otherwise, leave the charges on
            the subscription to pay for at renewal.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "proration_upgrade_scheme": "proration_upgrade_scheme",
        "proration_downgrade_scheme": "proration_downgrade_scheme",
        "allocations": "allocations",
        "accrue_charge": "accrue_charge",
        "upgrade_charge": "upgrade_charge",
        "downgrade_credit": "downgrade_credit",
        "payment_collection_method": "payment_collection_method",
        "initiate_dunning": "initiate_dunning",
    }

    _optionals = [
        "proration_upgrade_scheme",
        "proration_downgrade_scheme",
        "allocations",
        "accrue_charge",
        "upgrade_charge",
        "downgrade_credit",
        "payment_collection_method",
        "initiate_dunning",
    ]

    _nullables = [
        "upgrade_charge",
        "downgrade_credit",
    ]

    def __init__(
        self,
        proration_upgrade_scheme=APIHelper.SKIP,
        proration_downgrade_scheme=APIHelper.SKIP,
        allocations=APIHelper.SKIP,
        accrue_charge=APIHelper.SKIP,
        upgrade_charge=APIHelper.SKIP,
        downgrade_credit=APIHelper.SKIP,
        payment_collection_method=APIHelper.SKIP,
        initiate_dunning=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a AllocateComponents instance."""
        # Initialize members of the class
        if proration_upgrade_scheme is not APIHelper.SKIP:
            self.proration_upgrade_scheme = proration_upgrade_scheme
        if proration_downgrade_scheme is not APIHelper.SKIP:
            self.proration_downgrade_scheme = proration_downgrade_scheme
        if allocations is not APIHelper.SKIP:
            self.allocations = allocations
        if accrue_charge is not APIHelper.SKIP:
            self.accrue_charge = accrue_charge
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit
        if payment_collection_method is not APIHelper.SKIP:
            self.payment_collection_method = payment_collection_method
        if initiate_dunning is not APIHelper.SKIP:
            self.initiate_dunning = initiate_dunning

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
        proration_upgrade_scheme =\
            dictionary.get("proration_upgrade_scheme")\
            if dictionary.get("proration_upgrade_scheme")\
                else APIHelper.SKIP
        proration_downgrade_scheme =\
            dictionary.get("proration_downgrade_scheme")\
            if dictionary.get("proration_downgrade_scheme")\
                else APIHelper.SKIP
        allocations = None
        if dictionary.get("allocations") is not None:
            allocations = [
                CreateAllocation.from_dictionary(x)
                    for x in dictionary.get("allocations")
            ]
        else:
            allocations = APIHelper.SKIP
        accrue_charge =\
            dictionary.get("accrue_charge")\
            if "accrue_charge" in dictionary.keys()\
                else APIHelper.SKIP
        upgrade_charge =\
            dictionary.get("upgrade_charge")\
            if "upgrade_charge" in dictionary.keys()\
                else APIHelper.SKIP
        downgrade_credit =\
            dictionary.get("downgrade_credit")\
            if "downgrade_credit" in dictionary.keys()\
                else APIHelper.SKIP
        payment_collection_method =\
            dictionary.get("payment_collection_method")\
            if dictionary.get("payment_collection_method")\
                else APIHelper.SKIP
        initiate_dunning =\
            dictionary.get("initiate_dunning")\
            if "initiate_dunning" in dictionary.keys()\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(proration_upgrade_scheme,
                   proration_downgrade_scheme,
                   allocations,
                   accrue_charge,
                   upgrade_charge,
                   downgrade_credit,
                   payment_collection_method,
                   initiate_dunning,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _proration_upgrade_scheme=(
            self.proration_upgrade_scheme
            if hasattr(self, "proration_upgrade_scheme")
            else None
        )
        _proration_downgrade_scheme=(
            self.proration_downgrade_scheme
            if hasattr(self, "proration_downgrade_scheme")
            else None
        )
        _allocations=(
            self.allocations
            if hasattr(self, "allocations")
            else None
        )
        _accrue_charge=(
            self.accrue_charge
            if hasattr(self, "accrue_charge")
            else None
        )
        _upgrade_charge=(
            self.upgrade_charge
            if hasattr(self, "upgrade_charge")
            else None
        )
        _downgrade_credit=(
            self.downgrade_credit
            if hasattr(self, "downgrade_credit")
            else None
        )
        _payment_collection_method=(
            self.payment_collection_method
            if hasattr(self, "payment_collection_method")
            else None
        )
        _initiate_dunning=(
            self.initiate_dunning
            if hasattr(self, "initiate_dunning")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"proration_upgrade_scheme={_proration_upgrade_scheme!r}, "
            f"proration_downgrade_scheme={_proration_downgrade_scheme!r}, "
            f"allocations={_allocations!r}, "
            f"accrue_charge={_accrue_charge!r}, "
            f"upgrade_charge={_upgrade_charge!r}, "
            f"downgrade_credit={_downgrade_credit!r}, "
            f"payment_collection_method={_payment_collection_method!r}, "
            f"initiate_dunning={_initiate_dunning!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _proration_upgrade_scheme=(
            self.proration_upgrade_scheme
            if hasattr(self, "proration_upgrade_scheme")
            else None
        )
        _proration_downgrade_scheme=(
            self.proration_downgrade_scheme
            if hasattr(self, "proration_downgrade_scheme")
            else None
        )
        _allocations=(
            self.allocations
            if hasattr(self, "allocations")
            else None
        )
        _accrue_charge=(
            self.accrue_charge
            if hasattr(self, "accrue_charge")
            else None
        )
        _upgrade_charge=(
            self.upgrade_charge
            if hasattr(self, "upgrade_charge")
            else None
        )
        _downgrade_credit=(
            self.downgrade_credit
            if hasattr(self, "downgrade_credit")
            else None
        )
        _payment_collection_method=(
            self.payment_collection_method
            if hasattr(self, "payment_collection_method")
            else None
        )
        _initiate_dunning=(
            self.initiate_dunning
            if hasattr(self, "initiate_dunning")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"proration_upgrade_scheme={_proration_upgrade_scheme!s}, "
            f"proration_downgrade_scheme={_proration_downgrade_scheme!s}, "
            f"allocations={_allocations!s}, "
            f"accrue_charge={_accrue_charge!s}, "
            f"upgrade_charge={_upgrade_charge!s}, "
            f"downgrade_credit={_downgrade_credit!s}, "
            f"payment_collection_method={_payment_collection_method!s}, "
            f"initiate_dunning={_initiate_dunning!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
