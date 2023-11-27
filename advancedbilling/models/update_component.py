# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class UpdateComponent(object):

    """Implementation of the 'Update Component' model.

    TODO: type model description here.

    Attributes:
        handle (str): TODO: type description here.
        name (str): The name of the Component, suitable for display on
            statements. i.e. Text Messages.
        description (str): The description of the component.
        accounting_code (str): TODO: type description here.
        taxable (bool): Boolean flag describing whether a component is taxable
            or not.
        tax_code (str): A string representing the tax code related to the
            component type. This is especially important when using the
            Avalara service to tax based on locale. This attribute has a max
            length of 10 characters.
        item_category (ItemCategory): One of the following: Business Software,
            Consumer Software, Digital Services, Physical Goods, Other
        display_on_hosted_page (bool): TODO: type description here.
        upgrade_charge (CreditType): The type of charge to be applied when a
            component is upgraded. Valid values are: `prorated`, `full`,
            `none`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "handle": 'handle',
        "name": 'name',
        "description": 'description',
        "accounting_code": 'accounting_code',
        "taxable": 'taxable',
        "tax_code": 'tax_code',
        "item_category": 'item_category',
        "display_on_hosted_page": 'display_on_hosted_page',
        "upgrade_charge": 'upgrade_charge'
    }

    _optionals = [
        'handle',
        'name',
        'description',
        'accounting_code',
        'taxable',
        'tax_code',
        'item_category',
        'display_on_hosted_page',
        'upgrade_charge',
    ]

    _nullables = [
        'description',
        'tax_code',
        'item_category',
    ]

    def __init__(self,
                 handle=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 accounting_code=APIHelper.SKIP,
                 taxable=APIHelper.SKIP,
                 tax_code=APIHelper.SKIP,
                 item_category=APIHelper.SKIP,
                 display_on_hosted_page=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP):
        """Constructor for the UpdateComponent class"""

        # Initialize members of the class
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if name is not APIHelper.SKIP:
            self.name = name 
        if description is not APIHelper.SKIP:
            self.description = description 
        if accounting_code is not APIHelper.SKIP:
            self.accounting_code = accounting_code 
        if taxable is not APIHelper.SKIP:
            self.taxable = taxable 
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code 
        if item_category is not APIHelper.SKIP:
            self.item_category = item_category 
        if display_on_hosted_page is not APIHelper.SKIP:
            self.display_on_hosted_page = display_on_hosted_page 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 

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
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        accounting_code = dictionary.get("accounting_code") if dictionary.get("accounting_code") else APIHelper.SKIP
        taxable = dictionary.get("taxable") if "taxable" in dictionary.keys() else APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if "tax_code" in dictionary.keys() else APIHelper.SKIP
        item_category = dictionary.get("item_category") if "item_category" in dictionary.keys() else APIHelper.SKIP
        display_on_hosted_page = dictionary.get("display_on_hosted_page") if "display_on_hosted_page" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if dictionary.get("upgrade_charge") else APIHelper.SKIP
        # Return an object of this model
        return cls(handle,
                   name,
                   description,
                   accounting_code,
                   taxable,
                   tax_code,
                   item_category,
                   display_on_hosted_page,
                   upgrade_charge)
