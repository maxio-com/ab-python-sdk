# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class UpdateComponent(object):

    """Implementation of the 'Update Component' model.

    Attributes:
        handle (str): The model property of type str.
        name (str): The name of the Component, suitable for display on
            statements. i.e. Text Messages.
        description (str): The description of the component.
        accounting_code (str): The model property of type str.
        taxable (bool): Boolean flag describing whether a component is taxable
            or not.
        tax_code (str): A string representing the tax code related to the
            component type. This is especially important when using the
            Avalara service to tax based on locale. This attribute has a max
            length of 10 characters.
        item_category (ItemCategory): One of the following: Business Software,
            Consumer Software, Digital Services, Physical Goods, Other
        display_on_hosted_page (bool): The model property of type bool.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
        'accounting_code',
        'tax_code',
        'item_category',
        'upgrade_charge',
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
                 upgrade_charge=APIHelper.SKIP,
                 additional_properties=None):
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
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        accounting_code = dictionary.get("accounting_code") if "accounting_code" in dictionary.keys() else APIHelper.SKIP
        taxable = dictionary.get("taxable") if "taxable" in dictionary.keys() else APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if "tax_code" in dictionary.keys() else APIHelper.SKIP
        item_category = dictionary.get("item_category") if "item_category" in dictionary.keys() else APIHelper.SKIP
        display_on_hosted_page = dictionary.get("display_on_hosted_page") if "display_on_hosted_page" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(handle,
                   name,
                   description,
                   accounting_code,
                   taxable,
                   tax_code,
                   item_category,
                   display_on_hosted_page,
                   upgrade_charge,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'handle={(self.handle if hasattr(self, "handle") else None)!r}, '
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r}, '
                f'accounting_code={(self.accounting_code if hasattr(self, "accounting_code") else None)!r}, '
                f'taxable={(self.taxable if hasattr(self, "taxable") else None)!r}, '
                f'tax_code={(self.tax_code if hasattr(self, "tax_code") else None)!r}, '
                f'item_category={(self.item_category if hasattr(self, "item_category") else None)!r}, '
                f'display_on_hosted_page={(self.display_on_hosted_page if hasattr(self, "display_on_hosted_page") else None)!r}, '
                f'upgrade_charge={(self.upgrade_charge if hasattr(self, "upgrade_charge") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'handle={(self.handle if hasattr(self, "handle") else None)!s}, '
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'accounting_code={(self.accounting_code if hasattr(self, "accounting_code") else None)!s}, '
                f'taxable={(self.taxable if hasattr(self, "taxable") else None)!s}, '
                f'tax_code={(self.tax_code if hasattr(self, "tax_code") else None)!s}, '
                f'item_category={(self.item_category if hasattr(self, "item_category") else None)!s}, '
                f'display_on_hosted_page={(self.display_on_hosted_page if hasattr(self, "display_on_hosted_page") else None)!s}, '
                f'upgrade_charge={(self.upgrade_charge if hasattr(self, "upgrade_charge") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
