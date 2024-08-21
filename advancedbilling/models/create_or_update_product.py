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
        name (str): The product name
        handle (str): The product API handle
        description (str): The product description
        accounting_code (str): E.g. Internal ID or SKU Number
        require_credit_card (bool): Deprecated value that can be ignored
            unless you have legacy hosted pages. For Public Signup Page users,
            please read this attribute from under the signup page.
        price_in_cents (long|int): The product price, in integer cents
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this product would
            renew every 30 days
        interval_unit (IntervalUnit): A string representing the interval unit
            for this product, either month or day
        trial_price_in_cents (long|int): The product trial price, in integer
            cents
        trial_interval (int): The numerical trial interval. i.e. an interval
            of ‘30’ coupled with a trial_interval_unit of day would mean this
            product trial would last 30 days.
        trial_interval_unit (IntervalUnit): A string representing the trial
            interval unit for this product, either month or day
        trial_type (str): TODO: type description here.
        expiration_interval (int): The numerical expiration interval. i.e. an
            expiration_interval of ‘30’ coupled with an
            expiration_interval_unit of day would mean this product would
            expire after 30 days.
        expiration_interval_unit (ExpirationIntervalUnit): A string
            representing the expiration interval unit for this product, either
            month, day or never
        auto_create_signup_page (bool): TODO: type description here.
        tax_code (str): A string representing the tax code related to the
            product type. This is especially important when using the Avalara
            service to tax based on locale. This attribute has a max length of
            10 characters.

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
        "trial_price_in_cents": 'trial_price_in_cents',
        "trial_interval": 'trial_interval',
        "trial_interval_unit": 'trial_interval_unit',
        "trial_type": 'trial_type',
        "expiration_interval": 'expiration_interval',
        "expiration_interval_unit": 'expiration_interval_unit',
        "auto_create_signup_page": 'auto_create_signup_page',
        "tax_code": 'tax_code'
    }

    _optionals = [
        'handle',
        'accounting_code',
        'require_credit_card',
        'trial_price_in_cents',
        'trial_interval',
        'trial_interval_unit',
        'trial_type',
        'expiration_interval',
        'expiration_interval_unit',
        'auto_create_signup_page',
        'tax_code',
    ]

    _nullables = [
        'trial_interval_unit',
        'expiration_interval_unit',
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
                 trial_price_in_cents=APIHelper.SKIP,
                 trial_interval=APIHelper.SKIP,
                 trial_interval_unit=APIHelper.SKIP,
                 trial_type=APIHelper.SKIP,
                 expiration_interval=APIHelper.SKIP,
                 expiration_interval_unit=APIHelper.SKIP,
                 auto_create_signup_page=APIHelper.SKIP,
                 tax_code=APIHelper.SKIP,
                 additional_properties={}):
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
        if trial_price_in_cents is not APIHelper.SKIP:
            self.trial_price_in_cents = trial_price_in_cents 
        if trial_interval is not APIHelper.SKIP:
            self.trial_interval = trial_interval 
        if trial_interval_unit is not APIHelper.SKIP:
            self.trial_interval_unit = trial_interval_unit 
        if trial_type is not APIHelper.SKIP:
            self.trial_type = trial_type 
        if expiration_interval is not APIHelper.SKIP:
            self.expiration_interval = expiration_interval 
        if expiration_interval_unit is not APIHelper.SKIP:
            self.expiration_interval_unit = expiration_interval_unit 
        if auto_create_signup_page is not APIHelper.SKIP:
            self.auto_create_signup_page = auto_create_signup_page 
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        description = dictionary.get("description") if dictionary.get("description") else None
        price_in_cents = dictionary.get("price_in_cents") if dictionary.get("price_in_cents") else None
        interval = dictionary.get("interval") if dictionary.get("interval") else None
        interval_unit = dictionary.get("interval_unit") if dictionary.get("interval_unit") else None
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        accounting_code = dictionary.get("accounting_code") if dictionary.get("accounting_code") else APIHelper.SKIP
        require_credit_card = dictionary.get("require_credit_card") if "require_credit_card" in dictionary.keys() else APIHelper.SKIP
        trial_price_in_cents = dictionary.get("trial_price_in_cents") if dictionary.get("trial_price_in_cents") else APIHelper.SKIP
        trial_interval = dictionary.get("trial_interval") if dictionary.get("trial_interval") else APIHelper.SKIP
        trial_interval_unit = dictionary.get("trial_interval_unit") if "trial_interval_unit" in dictionary.keys() else APIHelper.SKIP
        trial_type = dictionary.get("trial_type") if dictionary.get("trial_type") else APIHelper.SKIP
        expiration_interval = dictionary.get("expiration_interval") if dictionary.get("expiration_interval") else APIHelper.SKIP
        expiration_interval_unit = dictionary.get("expiration_interval_unit") if "expiration_interval_unit" in dictionary.keys() else APIHelper.SKIP
        auto_create_signup_page = dictionary.get("auto_create_signup_page") if "auto_create_signup_page" in dictionary.keys() else APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if dictionary.get("tax_code") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(name,
                   description,
                   price_in_cents,
                   interval,
                   interval_unit,
                   handle,
                   accounting_code,
                   require_credit_card,
                   trial_price_in_cents,
                   trial_interval,
                   trial_interval_unit,
                   trial_type,
                   expiration_interval,
                   expiration_interval_unit,
                   auto_create_signup_page,
                   tax_code,
                   dictionary)
