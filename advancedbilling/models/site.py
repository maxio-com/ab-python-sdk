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

    Attributes:
        id (int): The model property of type int.
        name (str): The model property of type str.
        subdomain (str): The model property of type str.
        currency (str): The model property of type str.
        seller_id (int): The model property of type int.
        non_primary_currencies (List[str]): The model property of type
            List[str].
        relationship_invoicing_enabled (bool): The model property of type bool.
        schedule_subscription_cancellation_enabled (bool): The model property
            of type bool.
        customer_hierarchy_enabled (bool): The model property of type bool.
        whopays_enabled (bool): The model property of type bool.
        whopays_default_payer (str): The model property of type str.
        allocation_settings (AllocationSettings): The model property of type
            AllocationSettings.
        default_payment_collection_method (str): The model property of type
            str.
        organization_address (OrganizationAddress): The model property of type
            OrganizationAddress.
        tax_configuration (TaxConfiguration): The model property of type
            TaxConfiguration.
        net_terms (NetTerms): The model property of type NetTerms.
        test (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
        "schedule_subscription_cancellation_enabled": 'schedule_subscription_cancellation_enabled',
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
        'schedule_subscription_cancellation_enabled',
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
                 schedule_subscription_cancellation_enabled=APIHelper.SKIP,
                 customer_hierarchy_enabled=APIHelper.SKIP,
                 whopays_enabled=APIHelper.SKIP,
                 whopays_default_payer=APIHelper.SKIP,
                 allocation_settings=APIHelper.SKIP,
                 default_payment_collection_method=APIHelper.SKIP,
                 organization_address=APIHelper.SKIP,
                 tax_configuration=APIHelper.SKIP,
                 net_terms=APIHelper.SKIP,
                 test=APIHelper.SKIP,
                 additional_properties=None):
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
        if schedule_subscription_cancellation_enabled is not APIHelper.SKIP:
            self.schedule_subscription_cancellation_enabled = schedule_subscription_cancellation_enabled 
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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        subdomain = dictionary.get("subdomain") if dictionary.get("subdomain") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        seller_id = dictionary.get("seller_id") if dictionary.get("seller_id") else APIHelper.SKIP
        non_primary_currencies = dictionary.get("non_primary_currencies") if dictionary.get("non_primary_currencies") else APIHelper.SKIP
        relationship_invoicing_enabled = dictionary.get("relationship_invoicing_enabled") if "relationship_invoicing_enabled" in dictionary.keys() else APIHelper.SKIP
        schedule_subscription_cancellation_enabled = dictionary.get("schedule_subscription_cancellation_enabled") if "schedule_subscription_cancellation_enabled" in dictionary.keys() else APIHelper.SKIP
        customer_hierarchy_enabled = dictionary.get("customer_hierarchy_enabled") if "customer_hierarchy_enabled" in dictionary.keys() else APIHelper.SKIP
        whopays_enabled = dictionary.get("whopays_enabled") if "whopays_enabled" in dictionary.keys() else APIHelper.SKIP
        whopays_default_payer = dictionary.get("whopays_default_payer") if dictionary.get("whopays_default_payer") else APIHelper.SKIP
        allocation_settings = AllocationSettings.from_dictionary(dictionary.get('allocation_settings')) if 'allocation_settings' in dictionary.keys() else APIHelper.SKIP
        default_payment_collection_method = dictionary.get("default_payment_collection_method") if dictionary.get("default_payment_collection_method") else APIHelper.SKIP
        organization_address = OrganizationAddress.from_dictionary(dictionary.get('organization_address')) if 'organization_address' in dictionary.keys() else APIHelper.SKIP
        tax_configuration = TaxConfiguration.from_dictionary(dictionary.get('tax_configuration')) if 'tax_configuration' in dictionary.keys() else APIHelper.SKIP
        net_terms = NetTerms.from_dictionary(dictionary.get('net_terms')) if 'net_terms' in dictionary.keys() else APIHelper.SKIP
        test = dictionary.get("test") if "test" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   name,
                   subdomain,
                   currency,
                   seller_id,
                   non_primary_currencies,
                   relationship_invoicing_enabled,
                   schedule_subscription_cancellation_enabled,
                   customer_hierarchy_enabled,
                   whopays_enabled,
                   whopays_default_payer,
                   allocation_settings,
                   default_payment_collection_method,
                   organization_address,
                   tax_configuration,
                   net_terms,
                   test,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'subdomain={(self.subdomain if hasattr(self, "subdomain") else None)!r}, '
                f'currency={(self.currency if hasattr(self, "currency") else None)!r}, '
                f'seller_id={(self.seller_id if hasattr(self, "seller_id") else None)!r}, '
                f'non_primary_currencies={(self.non_primary_currencies if hasattr(self, "non_primary_currencies") else None)!r}, '
                f'relationship_invoicing_enabled={(self.relationship_invoicing_enabled if hasattr(self, "relationship_invoicing_enabled") else None)!r}, '
                f'schedule_subscription_cancellation_enabled={(self.schedule_subscription_cancellation_enabled if hasattr(self, "schedule_subscription_cancellation_enabled") else None)!r}, '
                f'customer_hierarchy_enabled={(self.customer_hierarchy_enabled if hasattr(self, "customer_hierarchy_enabled") else None)!r}, '
                f'whopays_enabled={(self.whopays_enabled if hasattr(self, "whopays_enabled") else None)!r}, '
                f'whopays_default_payer={(self.whopays_default_payer if hasattr(self, "whopays_default_payer") else None)!r}, '
                f'allocation_settings={(self.allocation_settings if hasattr(self, "allocation_settings") else None)!r}, '
                f'default_payment_collection_method={(self.default_payment_collection_method if hasattr(self, "default_payment_collection_method") else None)!r}, '
                f'organization_address={(self.organization_address if hasattr(self, "organization_address") else None)!r}, '
                f'tax_configuration={(self.tax_configuration if hasattr(self, "tax_configuration") else None)!r}, '
                f'net_terms={(self.net_terms if hasattr(self, "net_terms") else None)!r}, '
                f'test={(self.test if hasattr(self, "test") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'subdomain={(self.subdomain if hasattr(self, "subdomain") else None)!s}, '
                f'currency={(self.currency if hasattr(self, "currency") else None)!s}, '
                f'seller_id={(self.seller_id if hasattr(self, "seller_id") else None)!s}, '
                f'non_primary_currencies={(self.non_primary_currencies if hasattr(self, "non_primary_currencies") else None)!s}, '
                f'relationship_invoicing_enabled={(self.relationship_invoicing_enabled if hasattr(self, "relationship_invoicing_enabled") else None)!s}, '
                f'schedule_subscription_cancellation_enabled={(self.schedule_subscription_cancellation_enabled if hasattr(self, "schedule_subscription_cancellation_enabled") else None)!s}, '
                f'customer_hierarchy_enabled={(self.customer_hierarchy_enabled if hasattr(self, "customer_hierarchy_enabled") else None)!s}, '
                f'whopays_enabled={(self.whopays_enabled if hasattr(self, "whopays_enabled") else None)!s}, '
                f'whopays_default_payer={(self.whopays_default_payer if hasattr(self, "whopays_default_payer") else None)!s}, '
                f'allocation_settings={(self.allocation_settings if hasattr(self, "allocation_settings") else None)!s}, '
                f'default_payment_collection_method={(self.default_payment_collection_method if hasattr(self, "default_payment_collection_method") else None)!s}, '
                f'organization_address={(self.organization_address if hasattr(self, "organization_address") else None)!s}, '
                f'tax_configuration={(self.tax_configuration if hasattr(self, "tax_configuration") else None)!s}, '
                f'net_terms={(self.net_terms if hasattr(self, "net_terms") else None)!s}, '
                f'test={(self.test if hasattr(self, "test") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
