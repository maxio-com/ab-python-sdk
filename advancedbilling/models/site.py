# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.allocation_settings import AllocationSettings
from advancedbilling.models.net_terms import NetTerms
from advancedbilling.models.organization_address import OrganizationAddress
from advancedbilling.models.tax_configuration import TaxConfiguration


class Site(object):

    """Implementation of the 'Site' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        name (str): TODO: type description here.
        subdomain (str): TODO: type description here.
        currency (str): TODO: type description here.
        seller_id (int): TODO: type description here.
        non_primary_currencies (List[str]): TODO: type description here.
        relationship_invoicing_enabled (bool): TODO: type description here.
        customer_hierarchy_enabled (bool): TODO: type description here.
        whopays_enabled (bool): TODO: type description here.
        whopays_default_payer (str): TODO: type description here.
        allocation_settings (AllocationSettings): TODO: type description
            here.
        default_payment_collection_method (str): TODO: type description here.
        organization_address (OrganizationAddress): TODO: type description
            here.
        tax_configuration (TaxConfiguration): TODO: type description here.
        net_terms (NetTerms): TODO: type description here.
        test (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "subdomain": 'subdomain',
        "currency": 'currency',
        "seller_id": 'seller_id',
        "non_primary_currencies": 'non_primary_currencies',
        "relationship_invoicing_enabled": 'relationship_invoicing_enabled',
        "customer_hierarchy_enabled": 'customer_hierarchy_enabled',
        "whopays_enabled": 'whopays_enabled',
        "whopays_default_payer": 'whopays_default_payer',
        "allocation_settings": 'allocation_settings',
        "default_payment_collection_method": 'default_payment_collection_method',
        "organization_address": 'organization_address',
        "tax_configuration": 'tax_configuration',
        "net_terms": 'net_terms',
        "test": 'test'
    }

    _optionals = [
        'id',
        'name',
        'subdomain',
        'currency',
        'seller_id',
        'non_primary_currencies',
        'relationship_invoicing_enabled',
        'customer_hierarchy_enabled',
        'whopays_enabled',
        'whopays_default_payer',
        'allocation_settings',
        'default_payment_collection_method',
        'organization_address',
        'tax_configuration',
        'net_terms',
        'test',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 subdomain=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 seller_id=APIHelper.SKIP,
                 non_primary_currencies=APIHelper.SKIP,
                 relationship_invoicing_enabled=APIHelper.SKIP,
                 customer_hierarchy_enabled=APIHelper.SKIP,
                 whopays_enabled=APIHelper.SKIP,
                 whopays_default_payer=APIHelper.SKIP,
                 allocation_settings=APIHelper.SKIP,
                 default_payment_collection_method=APIHelper.SKIP,
                 organization_address=APIHelper.SKIP,
                 tax_configuration=APIHelper.SKIP,
                 net_terms=APIHelper.SKIP,
                 test=APIHelper.SKIP):
        """Constructor for the Site class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if subdomain is not APIHelper.SKIP:
            self.subdomain = subdomain 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if seller_id is not APIHelper.SKIP:
            self.seller_id = seller_id 
        if non_primary_currencies is not APIHelper.SKIP:
            self.non_primary_currencies = non_primary_currencies 
        if relationship_invoicing_enabled is not APIHelper.SKIP:
            self.relationship_invoicing_enabled = relationship_invoicing_enabled 
        if customer_hierarchy_enabled is not APIHelper.SKIP:
            self.customer_hierarchy_enabled = customer_hierarchy_enabled 
        if whopays_enabled is not APIHelper.SKIP:
            self.whopays_enabled = whopays_enabled 
        if whopays_default_payer is not APIHelper.SKIP:
            self.whopays_default_payer = whopays_default_payer 
        if allocation_settings is not APIHelper.SKIP:
            self.allocation_settings = allocation_settings 
        if default_payment_collection_method is not APIHelper.SKIP:
            self.default_payment_collection_method = default_payment_collection_method 
        if organization_address is not APIHelper.SKIP:
            self.organization_address = organization_address 
        if tax_configuration is not APIHelper.SKIP:
            self.tax_configuration = tax_configuration 
        if net_terms is not APIHelper.SKIP:
            self.net_terms = net_terms 
        if test is not APIHelper.SKIP:
            self.test = test 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        subdomain = dictionary.get("subdomain") if dictionary.get("subdomain") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        seller_id = dictionary.get("seller_id") if dictionary.get("seller_id") else APIHelper.SKIP
        non_primary_currencies = dictionary.get("non_primary_currencies") if dictionary.get("non_primary_currencies") else APIHelper.SKIP
        relationship_invoicing_enabled = dictionary.get("relationship_invoicing_enabled") if "relationship_invoicing_enabled" in dictionary.keys() else APIHelper.SKIP
        customer_hierarchy_enabled = dictionary.get("customer_hierarchy_enabled") if "customer_hierarchy_enabled" in dictionary.keys() else APIHelper.SKIP
        whopays_enabled = dictionary.get("whopays_enabled") if "whopays_enabled" in dictionary.keys() else APIHelper.SKIP
        whopays_default_payer = dictionary.get("whopays_default_payer") if dictionary.get("whopays_default_payer") else APIHelper.SKIP
        allocation_settings = AllocationSettings.from_dictionary(dictionary.get('allocation_settings')) if 'allocation_settings' in dictionary.keys() else APIHelper.SKIP
        default_payment_collection_method = dictionary.get("default_payment_collection_method") if dictionary.get("default_payment_collection_method") else APIHelper.SKIP
        organization_address = OrganizationAddress.from_dictionary(dictionary.get('organization_address')) if 'organization_address' in dictionary.keys() else APIHelper.SKIP
        tax_configuration = TaxConfiguration.from_dictionary(dictionary.get('tax_configuration')) if 'tax_configuration' in dictionary.keys() else APIHelper.SKIP
        net_terms = NetTerms.from_dictionary(dictionary.get('net_terms')) if 'net_terms' in dictionary.keys() else APIHelper.SKIP
        test = dictionary.get("test") if "test" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   name,
                   subdomain,
                   currency,
                   seller_id,
                   non_primary_currencies,
                   relationship_invoicing_enabled,
                   customer_hierarchy_enabled,
                   whopays_enabled,
                   whopays_default_payer,
                   allocation_settings,
                   default_payment_collection_method,
                   organization_address,
                   tax_configuration,
                   net_terms,
                   test)
