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
                f'id={self.id!r}, '
                f'site_id={self.site_id!r}, '
                f'product_family_id={self.product_family_id!r}, '
                f'product_id={self.product_id!r}, '
                f'product_price_point_id={self.product_price_point_id!r}, '
                f'product_revisable_number={self.product_revisable_number!r}, '
                f'name={self.name!r}, '
                f'handle={self.handle!r}, '
                f'description={self.description!r}, '
                f'created_at={self.created_at!r}, '
                f'updated_at={self.updated_at!r}, '
                f'archived_at={self.archived_at!r}, '
                f'offer_items={self.offer_items!r}, '
                f'offer_discounts={self.offer_discounts!r}, '
                f'product_family_name={self.product_family_name!r}, '
                f'product_name={self.product_name!r}, '
                f'product_price_point_name={self.product_price_point_name!r}, '
                f'product_price_in_cents={self.product_price_in_cents!r}, '
                f'offer_signup_pages={self.offer_signup_pages!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'site_id={self.site_id!s}, '
                f'product_family_id={self.product_family_id!s}, '
                f'product_id={self.product_id!s}, '
                f'product_price_point_id={self.product_price_point_id!s}, '
                f'product_revisable_number={self.product_revisable_number!s}, '
                f'name={self.name!s}, '
                f'handle={self.handle!s}, '
                f'description={self.description!s}, '
                f'created_at={self.created_at!s}, '
                f'updated_at={self.updated_at!s}, '
                f'archived_at={self.archived_at!s}, '
                f'offer_items={self.offer_items!s}, '
                f'offer_discounts={self.offer_discounts!s}, '
                f'product_family_name={self.product_family_name!s}, '
                f'product_name={self.product_name!s}, '
                f'product_price_point_name={self.product_price_point_name!s}, '
                f'product_price_in_cents={self.product_price_in_cents!s}, '
                f'offer_signup_pages={self.offer_signup_pages!s}, '
                f'additional_properties={self.additional_properties!s})')
