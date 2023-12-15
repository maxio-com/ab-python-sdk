# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_allocation_request import CreateAllocationRequest


class AllocateComponents(object):

    """Implementation of the 'Allocate Components' model.

    TODO: type model description here.

    Attributes:
        proration_upgrade_scheme (str): TODO: type description here.
        proration_downgrade_scheme (str): TODO: type description here.
        allocations (List[CreateAllocationRequest]): TODO: type description
            here.
        accrue_charge (bool): TODO: type description here.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        payment_collection_method (PaymentCollectionMethod1): (Optional) If
            not passed, the allocation(s) will use the payment collection
            method on the subscription

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "proration_upgrade_scheme": 'proration_upgrade_scheme',
        "proration_downgrade_scheme": 'proration_downgrade_scheme',
        "allocations": 'allocations',
        "accrue_charge": 'accrue_charge',
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "payment_collection_method": 'payment_collection_method'
    }

    _optionals = [
        'proration_upgrade_scheme',
        'proration_downgrade_scheme',
        'allocations',
        'accrue_charge',
        'upgrade_charge',
        'downgrade_credit',
        'payment_collection_method',
    ]

    _nullables = [
        'upgrade_charge',
        'downgrade_credit',
    ]

    def __init__(self,
                 proration_upgrade_scheme='no-prorate',
                 proration_downgrade_scheme='no-prorate',
                 allocations=APIHelper.SKIP,
                 accrue_charge=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 payment_collection_method='automatic'):
        """Constructor for the AllocateComponents class"""

        # Initialize members of the class
        self.proration_upgrade_scheme = proration_upgrade_scheme 
        self.proration_downgrade_scheme = proration_downgrade_scheme 
        if allocations is not APIHelper.SKIP:
            self.allocations = allocations 
        if accrue_charge is not APIHelper.SKIP:
            self.accrue_charge = accrue_charge 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        self.payment_collection_method = payment_collection_method 

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
        proration_upgrade_scheme = dictionary.get("proration_upgrade_scheme") if dictionary.get("proration_upgrade_scheme") else 'no-prorate'
        proration_downgrade_scheme = dictionary.get("proration_downgrade_scheme") if dictionary.get("proration_downgrade_scheme") else 'no-prorate'
        allocations = None
        if dictionary.get('allocations') is not None:
            allocations = [CreateAllocationRequest.from_dictionary(x) for x in dictionary.get('allocations')]
        else:
            allocations = APIHelper.SKIP
        accrue_charge = dictionary.get("accrue_charge") if "accrue_charge" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        payment_collection_method = dictionary.get("payment_collection_method") if dictionary.get("payment_collection_method") else 'automatic'
        # Return an object of this model
        return cls(proration_upgrade_scheme,
                   proration_downgrade_scheme,
                   allocations,
                   accrue_charge,
                   upgrade_charge,
                   downgrade_credit,
                   payment_collection_method)
