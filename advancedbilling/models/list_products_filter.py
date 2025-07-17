# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.prepaid_product_price_point_filter import PrepaidProductPricePointFilter


class ListProductsFilter(object):

    """Implementation of the 'List Products Filter' model.

    Attributes:
        ids (List[int]): Allows fetching products with matching id based on
            provided values. Use in query `filter[ids]=1,2,3`.
        prepaid_product_price_point (PrepaidProductPricePointFilter): Allows
            fetching products only if a prepaid product price point is present
            or not. To use this filter you also have to include the following
            param in the request `include=prepaid_product_price_point`. Use in
            query
            `filter[prepaid_product_price_point][product_price_point_id]=not_nu
            ll`.
        use_site_exchange_rate (bool): Allows fetching products with matching
            use_site_exchange_rate based on provided value (refers to default
            price point). Use in query `filter[use_site_exchange_rate]=true`.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ids": 'ids',
        "prepaid_product_price_point": 'prepaid_product_price_point',
        "use_site_exchange_rate": 'use_site_exchange_rate'
    }

    _optionals = [
        'ids',
        'prepaid_product_price_point',
        'use_site_exchange_rate',
    ]

    def __init__(self,
                 ids=APIHelper.SKIP,
                 prepaid_product_price_point=APIHelper.SKIP,
                 use_site_exchange_rate=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ListProductsFilter class"""

        # Initialize members of the class
        if ids is not APIHelper.SKIP:
            self.ids = ids 
        if prepaid_product_price_point is not APIHelper.SKIP:
            self.prepaid_product_price_point = prepaid_product_price_point 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 

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
        ids = dictionary.get("ids") if dictionary.get("ids") else APIHelper.SKIP
        prepaid_product_price_point = PrepaidProductPricePointFilter.from_dictionary(dictionary.get('prepaid_product_price_point')) if 'prepaid_product_price_point' in dictionary.keys() else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(ids,
                   prepaid_product_price_point,
                   use_site_exchange_rate,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'ids={(self.ids if hasattr(self, "ids") else None)!r}, '
                f'prepaid_product_price_point={(self.prepaid_product_price_point if hasattr(self, "prepaid_product_price_point") else None)!r}, '
                f'use_site_exchange_rate={(self.use_site_exchange_rate if hasattr(self, "use_site_exchange_rate") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'ids={(self.ids if hasattr(self, "ids") else None)!s}, '
                f'prepaid_product_price_point={(self.prepaid_product_price_point if hasattr(self, "prepaid_product_price_point") else None)!s}, '
                f'use_site_exchange_rate={(self.use_site_exchange_rate if hasattr(self, "use_site_exchange_rate") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
