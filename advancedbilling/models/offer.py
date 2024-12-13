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

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        site_id (int): TODO: type description here.
        product_family_id (int): TODO: type description here.
        product_id (int): TODO: type description here.
        product_price_point_id (int): TODO: type description here.
        product_revisable_number (int): TODO: type description here.
        name (str): TODO: type description here.
        handle (str): TODO: type description here.
        description (str): TODO: type description here.
        created_at (datetime): TODO: type description here.
        updated_at (datetime): TODO: type description here.
        archived_at (datetime): TODO: type description here.
        offer_items (List[OfferItem]): TODO: type description here.
        offer_discounts (List[OfferDiscount]): TODO: type description here.
        product_family_name (str): TODO: type description here.
        product_name (str): TODO: type description here.
        product_price_point_name (str): TODO: type description here.
        product_price_in_cents (long|int): TODO: type description here.
        offer_signup_pages (List[OfferSignupPage]): TODO: type description
            here.
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
