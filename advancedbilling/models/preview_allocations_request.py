# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_allocation import CreateAllocation


class PreviewAllocationsRequest(object):

    """Implementation of the 'Preview Allocations Request' model.

    TODO: type model description here.

    Attributes:
        allocations (List[CreateAllocation]): TODO: type description here.
        effective_proration_date (date): To calculate proration amounts for a
            future time. Only within a current subscription period. Only
            ISO8601 format is supported.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allocations": 'allocations',
        "effective_proration_date": 'effective_proration_date',
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit'
    }

    _optionals = [
        'effective_proration_date',
        'upgrade_charge',
        'downgrade_credit',
    ]

    _nullables = [
        'upgrade_charge',
        'downgrade_credit',
    ]

    def __init__(self,
                 allocations=None,
                 effective_proration_date=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP):
        """Constructor for the PreviewAllocationsRequest class"""

        # Initialize members of the class
        self.allocations = allocations 
        if effective_proration_date is not APIHelper.SKIP:
            self.effective_proration_date = effective_proration_date 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 

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
        allocations = None
        if dictionary.get('allocations') is not None:
            allocations = [CreateAllocation.from_dictionary(x) for x in dictionary.get('allocations')]
        effective_proration_date = dateutil.parser.parse(dictionary.get('effective_proration_date')).date() if dictionary.get('effective_proration_date') else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(allocations,
                   effective_proration_date,
                   upgrade_charge,
                   downgrade_credit)
