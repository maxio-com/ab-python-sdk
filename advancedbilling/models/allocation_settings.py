# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class AllocationSettings(object):

    """Implementation of the 'Allocation Settings' model.

    TODO: type model description here.

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
                 additional_properties={}):
        """Constructor for the AllocationSettings class"""

        # Initialize members of the class
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        if accrue_charge is not APIHelper.SKIP:
            self.accrue_charge = accrue_charge 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        accrue_charge = dictionary.get("accrue_charge") if dictionary.get("accrue_charge") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(upgrade_charge,
                   downgrade_credit,
                   accrue_charge,
                   dictionary)
