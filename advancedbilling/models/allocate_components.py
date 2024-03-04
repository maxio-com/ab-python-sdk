# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_allocation import CreateAllocation


class AllocateComponents(object):

    """Implementation of the 'Allocate Components' model.

    TODO: type model description here.

    Attributes:
        proration_upgrade_scheme (str): TODO: type description here.
        proration_downgrade_scheme (str): TODO: type description here.
        allocations (List[CreateAllocation]): TODO: type description here.
        accrue_charge (bool): TODO: type description here.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        payment_collection_method (CollectionMethod): (Optional) If not
            passed, the allocation(s) will use the payment collection method
            on the subscription
        initiate_dunning (bool): If true, if the immediate component payment
            fails, initiate dunning for the subscription.  Otherwise, leave
            the charges on the subscription to pay for at renewal.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "proration_upgrade_scheme": 'proration_upgrade_scheme',
        "proration_downgrade_scheme": 'proration_downgrade_scheme',
        "allocations": 'allocations',
        "accrue_charge": 'accrue_charge',
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "payment_collection_method": 'payment_collection_method',
        "initiate_dunning": 'initiate_dunning'
    }

    _optionals = [
        'proration_upgrade_scheme',
        'proration_downgrade_scheme',
        'allocations',
        'accrue_charge',
        'upgrade_charge',
        'downgrade_credit',
        'payment_collection_method',
        'initiate_dunning',
    ]

    _nullables = [
        'upgrade_charge',
        'downgrade_credit',
    ]

    def __init__(self,
                 proration_upgrade_scheme=APIHelper.SKIP,
                 proration_downgrade_scheme=APIHelper.SKIP,
                 allocations=APIHelper.SKIP,
                 accrue_charge=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 payment_collection_method=APIHelper.SKIP,
                 initiate_dunning=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the AllocateComponents class"""

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
        proration_upgrade_scheme = dictionary.get("proration_upgrade_scheme") if dictionary.get("proration_upgrade_scheme") else APIHelper.SKIP
        proration_downgrade_scheme = dictionary.get("proration_downgrade_scheme") if dictionary.get("proration_downgrade_scheme") else APIHelper.SKIP
        allocations = None
        if dictionary.get('allocations') is not None:
            allocations = [CreateAllocation.from_dictionary(x) for x in dictionary.get('allocations')]
        else:
            allocations = APIHelper.SKIP
        accrue_charge = dictionary.get("accrue_charge") if "accrue_charge" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        payment_collection_method = dictionary.get("payment_collection_method") if dictionary.get("payment_collection_method") else APIHelper.SKIP
        initiate_dunning = dictionary.get("initiate_dunning") if "initiate_dunning" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(proration_upgrade_scheme,
                   proration_downgrade_scheme,
                   allocations,
                   accrue_charge,
                   upgrade_charge,
                   downgrade_credit,
                   payment_collection_method,
                   initiate_dunning,
                   dictionary)
