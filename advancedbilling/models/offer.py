# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.offer_discount import OfferDiscount
from advancedbilling.models.offer_item import OfferItem
from advancedbilling.models.offer_signup_page import OfferSignupPage


class Offer(object):

    """Implementation of the 'Offer' model.

    Attributes:
        id (int): The model property of type int.
        site_id (int): The model property of type int.
        product_family_id (int): The model property of type int.
        product_id (int): The model property of type int.
        product_price_point_id (int): The model property of type int.
        product_revisable_number (int): The model property of type int.
        name (str): The model property of type str.
        handle (str): The model property of type str.
        description (str): The model property of type str.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        archived_at (datetime): The model property of type datetime.
        offer_items (List[OfferItem]): The model property of type
            List[OfferItem].
        offer_discounts (List[OfferDiscount]): The model property of type
            List[OfferDiscount].
        product_family_name (str): The model property of type str.
        product_name (str): The model property of type str.
        product_price_point_name (str): The model property of type str.
        product_price_in_cents (int): The model property of type int.
        offer_signup_pages (List[OfferSignupPage]): The model property of type
            List[OfferSignupPage].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "site_id": 'site_id',
        "product_family_id": 'product_family_id',
        "product_id": 'product_id',
        "product_price_point_id": 'product_price_point_id',
        "product_revisable_number": 'product_revisable_number',
        "name": 'name',
        "handle": 'handle',
        "description": 'description',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "archived_at": 'archived_at',
        "offer_items": 'offer_items',
        "offer_discounts": 'offer_discounts',
        "product_family_name": 'product_family_name',
        "product_name": 'product_name',
        "product_price_point_name": 'product_price_point_name',
        "product_price_in_cents": 'product_price_in_cents',
        "offer_signup_pages": 'offer_signup_pages'
    }

    _optionals = [
        'id',
        'site_id',
        'product_family_id',
        'product_id',
        'product_price_point_id',
        'product_revisable_number',
        'name',
        'handle',
        'description',
        'created_at',
        'updated_at',
        'archived_at',
        'offer_items',
        'offer_discounts',
        'product_family_name',
        'product_name',
        'product_price_point_name',
        'product_price_in_cents',
        'offer_signup_pages',
    ]

    _nullables = [
        'description',
        'archived_at',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 site_id=APIHelper.SKIP,
                 product_family_id=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 product_revisable_number=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 archived_at=APIHelper.SKIP,
                 offer_items=APIHelper.SKIP,
                 offer_discounts=APIHelper.SKIP,
                 product_family_name=APIHelper.SKIP,
                 product_name=APIHelper.SKIP,
                 product_price_point_name=APIHelper.SKIP,
                 product_price_in_cents=APIHelper.SKIP,
                 offer_signup_pages=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Offer class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if site_id is not APIHelper.SKIP:
            self.site_id = site_id 
        if product_family_id is not APIHelper.SKIP:
            self.product_family_id = product_family_id 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if product_revisable_number is not APIHelper.SKIP:
            self.product_revisable_number = product_revisable_number 
        if name is not APIHelper.SKIP:
            self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if description is not APIHelper.SKIP:
            self.description = description 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if archived_at is not APIHelper.SKIP:
            self.archived_at = APIHelper.apply_datetime_converter(archived_at, APIHelper.RFC3339DateTime) if archived_at else None 
        if offer_items is not APIHelper.SKIP:
            self.offer_items = offer_items 
        if offer_discounts is not APIHelper.SKIP:
            self.offer_discounts = offer_discounts 
        if product_family_name is not APIHelper.SKIP:
            self.product_family_name = product_family_name 
        if product_name is not APIHelper.SKIP:
            self.product_name = product_name 
        if product_price_point_name is not APIHelper.SKIP:
            self.product_price_point_name = product_price_point_name 
        if product_price_in_cents is not APIHelper.SKIP:
            self.product_price_in_cents = product_price_in_cents 
        if offer_signup_pages is not APIHelper.SKIP:
            self.offer_signup_pages = offer_signup_pages 

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
        site_id = dictionary.get("site_id") if dictionary.get("site_id") else APIHelper.SKIP
        product_family_id = dictionary.get("product_family_id") if dictionary.get("product_family_id") else APIHelper.SKIP
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        product_revisable_number = dictionary.get("product_revisable_number") if dictionary.get("product_revisable_number") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        if 'archived_at' in dictionary.keys():
            archived_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("archived_at")).datetime if dictionary.get("archived_at") else None
        else:
            archived_at = APIHelper.SKIP
        offer_items = None
        if dictionary.get('offer_items') is not None:
            offer_items = [OfferItem.from_dictionary(x) for x in dictionary.get('offer_items')]
        else:
            offer_items = APIHelper.SKIP
        offer_discounts = None
        if dictionary.get('offer_discounts') is not None:
            offer_discounts = [OfferDiscount.from_dictionary(x) for x in dictionary.get('offer_discounts')]
        else:
            offer_discounts = APIHelper.SKIP
        product_family_name = dictionary.get("product_family_name") if dictionary.get("product_family_name") else APIHelper.SKIP
        product_name = dictionary.get("product_name") if dictionary.get("product_name") else APIHelper.SKIP
        product_price_point_name = dictionary.get("product_price_point_name") if dictionary.get("product_price_point_name") else APIHelper.SKIP
        product_price_in_cents = dictionary.get("product_price_in_cents") if dictionary.get("product_price_in_cents") else APIHelper.SKIP
        offer_signup_pages = None
        if dictionary.get('offer_signup_pages') is not None:
            offer_signup_pages = [OfferSignupPage.from_dictionary(x) for x in dictionary.get('offer_signup_pages')]
        else:
            offer_signup_pages = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   site_id,
                   product_family_id,
                   product_id,
                   product_price_point_id,
                   product_revisable_number,
                   name,
                   handle,
                   description,
                   created_at,
                   updated_at,
                   archived_at,
                   offer_items,
                   offer_discounts,
                   product_family_name,
                   product_name,
                   product_price_point_name,
                   product_price_in_cents,
                   offer_signup_pages,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!r}, '
                f'site_id={(self.site_id if hasattr(self, "site_id") else None)!r}, '
                f'product_family_id={(self.product_family_id if hasattr(self, "product_family_id") else None)!r}, '
                f'product_id={(self.product_id if hasattr(self, "product_id") else None)!r}, '
                f'product_price_point_id={(self.product_price_point_id if hasattr(self, "product_price_point_id") else None)!r}, '
                f'product_revisable_number={(self.product_revisable_number if hasattr(self, "product_revisable_number") else None)!r}, '
                f'name={(self.name if hasattr(self, "name") else None)!r}, '
                f'handle={(self.handle if hasattr(self, "handle") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!r}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!r}, '
                f'archived_at={(self.archived_at if hasattr(self, "archived_at") else None)!r}, '
                f'offer_items={(self.offer_items if hasattr(self, "offer_items") else None)!r}, '
                f'offer_discounts={(self.offer_discounts if hasattr(self, "offer_discounts") else None)!r}, '
                f'product_family_name={(self.product_family_name if hasattr(self, "product_family_name") else None)!r}, '
                f'product_name={(self.product_name if hasattr(self, "product_name") else None)!r}, '
                f'product_price_point_name={(self.product_price_point_name if hasattr(self, "product_price_point_name") else None)!r}, '
                f'product_price_in_cents={(self.product_price_in_cents if hasattr(self, "product_price_in_cents") else None)!r}, '
                f'offer_signup_pages={(self.offer_signup_pages if hasattr(self, "offer_signup_pages") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={(self.id if hasattr(self, "id") else None)!s}, '
                f'site_id={(self.site_id if hasattr(self, "site_id") else None)!s}, '
                f'product_family_id={(self.product_family_id if hasattr(self, "product_family_id") else None)!s}, '
                f'product_id={(self.product_id if hasattr(self, "product_id") else None)!s}, '
                f'product_price_point_id={(self.product_price_point_id if hasattr(self, "product_price_point_id") else None)!s}, '
                f'product_revisable_number={(self.product_revisable_number if hasattr(self, "product_revisable_number") else None)!s}, '
                f'name={(self.name if hasattr(self, "name") else None)!s}, '
                f'handle={(self.handle if hasattr(self, "handle") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'created_at={(self.created_at if hasattr(self, "created_at") else None)!s}, '
                f'updated_at={(self.updated_at if hasattr(self, "updated_at") else None)!s}, '
                f'archived_at={(self.archived_at if hasattr(self, "archived_at") else None)!s}, '
                f'offer_items={(self.offer_items if hasattr(self, "offer_items") else None)!s}, '
                f'offer_discounts={(self.offer_discounts if hasattr(self, "offer_discounts") else None)!s}, '
                f'product_family_name={(self.product_family_name if hasattr(self, "product_family_name") else None)!s}, '
                f'product_name={(self.product_name if hasattr(self, "product_name") else None)!s}, '
                f'product_price_point_name={(self.product_price_point_name if hasattr(self, "product_price_point_name") else None)!s}, '
                f'product_price_in_cents={(self.product_price_in_cents if hasattr(self, "product_price_in_cents") else None)!s}, '
                f'offer_signup_pages={(self.offer_signup_pages if hasattr(self, "offer_signup_pages") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
