# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class AllocationSettings(object):

    """Implementation of the 'Allocation Settings' model.

    Attributes:
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        accrue_charge (str): Either "true" or "false".
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "accrue_charge": 'accrue_charge'
    }

    _optionals = [
        'upgrade_charge',
        'downgrade_credit',
        'accrue_charge',
    ]

    _nullables = [
        'upgrade_charge',
        'downgrade_credit',
    ]

    def __init__(self,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 accrue_charge=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the AllocationSettings class"""

        # Initialize members of the class
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        if accrue_charge is not APIHelper.SKIP:
            self.accrue_charge = accrue_charge 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

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
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        accrue_charge = dictionary.get("accrue_charge") if dictionary.get("accrue_charge") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(upgrade_charge,
                   downgrade_credit,
                   accrue_charge,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'upgrade_charge={(self.upgrade_charge if hasattr(self, "upgrade_charge") else None)!r}, '
                f'downgrade_credit={(self.downgrade_credit if hasattr(self, "downgrade_credit") else None)!r}, '
                f'accrue_charge={(self.accrue_charge if hasattr(self, "accrue_charge") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'upgrade_charge={(self.upgrade_charge if hasattr(self, "upgrade_charge") else None)!s}, '
                f'downgrade_credit={(self.downgrade_credit if hasattr(self, "downgrade_credit") else None)!s}, '
                f'accrue_charge={(self.accrue_charge if hasattr(self, "accrue_charge") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
