# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.price import Price


class CreateComponentPricePoint(object):

    """Implementation of the 'Create Component Price Point' model.

    TODO: type model description here.

    Attributes:
        name (str): TODO: type description here.
        handle (str): TODO: type description here.
        pricing_scheme (str): TODO: type description here.
        prices (List[Price]): TODO: type description here.
        use_site_exchange_rate (bool): Whether to use the site level exchange
            rate or define your own prices for each currency if you have
            multiple currencies defined on the site.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "pricing_scheme": 'pricing_scheme',
        "prices": 'prices',
        "handle": 'handle',
        "use_site_exchange_rate": 'use_site_exchange_rate'
    }

    _optionals = [
        'handle',
        'use_site_exchange_rate',
    ]

    def __init__(self,
                 name=None,
                 pricing_scheme=None,
                 prices=None,
                 handle=APIHelper.SKIP,
                 use_site_exchange_rate=True):
        """Constructor for the CreateComponentPricePoint class"""

        # Initialize members of the class
        self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        self.pricing_scheme = pricing_scheme 
        self.prices = prices 
        self.use_site_exchange_rate = use_site_exchange_rate 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get("name") if dictionary.get("name") else None
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else None
        prices = None
        if dictionary.get('prices') is not None:
            prices = [Price.from_dictionary(x) for x in dictionary.get('prices')]
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if dictionary.get("use_site_exchange_rate") else True
        # Return an object of this model
        return cls(name,
                   pricing_scheme,
                   prices,
                   handle,
                   use_site_exchange_rate)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.name, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.pricing_scheme, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.prices, type_callable=lambda value: Price.validate(value))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('name'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('pricing_scheme'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('prices'), type_callable=lambda value: Price.validate(value))
