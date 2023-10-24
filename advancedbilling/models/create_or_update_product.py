# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateOrUpdateProduct(object):

    """Implementation of the 'Create or Update Product' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        handle (str): TODO: type description here.
        description (str): TODO: type description here.
        accounting_code (str): TODO: type description here.
        require_credit_card (bool): TODO: type description here.
        price_in_cents (int): TODO: type description here.
        interval (int): TODO: type description here.
        interval_unit (str): TODO: type description here.
        auto_create_signup_page (bool): TODO: type description here.
        tax_code (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "description": 'description',
        "price_in_cents": 'price_in_cents',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "handle": 'handle',
        "accounting_code": 'accounting_code',
        "require_credit_card": 'require_credit_card',
        "auto_create_signup_page": 'auto_create_signup_page',
        "tax_code": 'tax_code'
    }

    _optionals = [
        'handle',
        'accounting_code',
        'require_credit_card',
        'auto_create_signup_page',
        'tax_code',
    ]

    def __init__(self,
                 name=None,
                 description=None,
                 price_in_cents=None,
                 interval=None,
                 interval_unit=None,
                 handle=APIHelper.SKIP,
                 accounting_code=APIHelper.SKIP,
                 require_credit_card=APIHelper.SKIP,
                 auto_create_signup_page=APIHelper.SKIP,
                 tax_code=APIHelper.SKIP):
        """Constructor for the CreateOrUpdateProduct class"""

        # Initialize members of the class
        self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        self.description = description 
        if accounting_code is not APIHelper.SKIP:
            self.accounting_code = accounting_code 
        if require_credit_card is not APIHelper.SKIP:
            self.require_credit_card = require_credit_card 
        self.price_in_cents = price_in_cents 
        self.interval = interval 
        self.interval_unit = interval_unit 
        if auto_create_signup_page is not APIHelper.SKIP:
            self.auto_create_signup_page = auto_create_signup_page 
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        price_in_cents = dictionary.get("price_in_cents") if dictionary.get("price_in_cents") else None
        interval = dictionary.get("interval") if dictionary.get("interval") else None
        interval_unit = dictionary.get("interval_unit") if dictionary.get("interval_unit") else None
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        accounting_code = dictionary.get("accounting_code") if dictionary.get("accounting_code") else APIHelper.SKIP
        require_credit_card = dictionary.get("require_credit_card") if "require_credit_card" in dictionary.keys() else APIHelper.SKIP
        auto_create_signup_page = dictionary.get("auto_create_signup_page") if "auto_create_signup_page" in dictionary.keys() else APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if dictionary.get("tax_code") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   description,
                   price_in_cents,
                   interval,
                   interval_unit,
                   handle,
                   accounting_code,
                   require_credit_card,
                   auto_create_signup_page,
                   tax_code)
