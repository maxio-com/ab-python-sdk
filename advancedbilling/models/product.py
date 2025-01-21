# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.public_signup_page import PublicSignupPage


class Product(object):

    """Implementation of the 'Product' model.

    Attributes:
        id (int): The model property of type int.
        name (str): The product name
        handle (str): The product API handle
        description (str): The product description
        accounting_code (str): E.g. Internal ID or SKU Number
        request_credit_card (bool): Deprecated value that can be ignored
            unless you have legacy hosted pages. For Public Signup Page users,
            please read this attribute from under the signup page.
        expiration_interval (int): A numerical interval for the length a
            subscription to this product will run before it expires. See the
            description of interval for a description of how this value is
            coupled with an interval unit to calculate the full interval
        expiration_interval_unit (ExpirationIntervalUnit): A string
            representing the expiration interval unit for this product, either
            month, day or never
        created_at (datetime): Timestamp indicating when this product was
            created
        updated_at (datetime): Timestamp indicating when this product was last
            updated
        price_in_cents (int): The product price, in integer cents
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this product would
            renew every 30 days
        interval_unit (IntervalUnit): A string representing the interval unit
            for this product, either month or day
        initial_charge_in_cents (int): The up front charge you have specified.
        trial_price_in_cents (int): The price of the trial period for a
            subscription to this product, in integer cents.
        trial_interval (int): A numerical interval for the length of the trial
            period of a subscription to this product. See the description of
            interval for a description of how this value is coupled with an
            interval unit to calculate the full interval
        trial_interval_unit (IntervalUnit): A string representing the trial
            interval unit for this product, either month or day
        archived_at (datetime): Timestamp indicating when this product was
            archived
        require_credit_card (bool): Boolean that controls whether a payment
            profile is required to be entered for customers wishing to sign up
            on this product.
        return_params (str): The model property of type str.
        taxable (bool): The model property of type bool.
        update_return_url (str): The url to which a customer will be returned
            after a successful account update
        initial_charge_after_trial (bool): The model property of type bool.
        version_number (int): The version of the product
        update_return_params (str): The parameters will append to the url
            after a successful account update. See [help
            documentation](https://help.chargify.com/products/product-editing.h
            tml#return-parameters-after-account-update)
        product_family (ProductFamily): The model property of type
            ProductFamily.
        public_signup_pages (List[PublicSignupPage]): The model property of
            type List[PublicSignupPage].
        product_price_point_name (str): The model property of type str.
        request_billing_address (bool): A boolean indicating whether to
            request a billing address on any Self-Service Pages that are used
            by subscribers of this product.
        require_billing_address (bool): A boolean indicating whether a billing
            address is required to add a payment profile, especially at signup.
        require_shipping_address (bool): A boolean indicating whether a
            shipping address is required for the customer, especially at
            signup.
        tax_code (str): A string representing the tax code related to the
            product type. This is especially important when using the Avalara
            service to tax based on locale. This attribute has a max length of
            10 characters.
        default_product_price_point_id (int): The model property of type int.
        use_site_exchange_rate (bool): The model property of type bool.
        item_category (str): One of the following: Business Software, Consumer
            Software, Digital Services, Physical Goods, Other
        product_price_point_id (int): The model property of type int.
        product_price_point_handle (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "handle": 'handle',
        "description": 'description',
        "accounting_code": 'accounting_code',
        "request_credit_card": 'request_credit_card',
        "expiration_interval": 'expiration_interval',
        "expiration_interval_unit": 'expiration_interval_unit',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "price_in_cents": 'price_in_cents',
        "interval": 'interval',
        "interval_unit": 'interval_unit',
        "initial_charge_in_cents": 'initial_charge_in_cents',
        "trial_price_in_cents": 'trial_price_in_cents',
        "trial_interval": 'trial_interval',
        "trial_interval_unit": 'trial_interval_unit',
        "archived_at": 'archived_at',
        "require_credit_card": 'require_credit_card',
        "return_params": 'return_params',
        "taxable": 'taxable',
        "update_return_url": 'update_return_url',
        "initial_charge_after_trial": 'initial_charge_after_trial',
        "version_number": 'version_number',
        "update_return_params": 'update_return_params',
        "product_family": 'product_family',
        "public_signup_pages": 'public_signup_pages',
        "product_price_point_name": 'product_price_point_name',
        "request_billing_address": 'request_billing_address',
        "require_billing_address": 'require_billing_address',
        "require_shipping_address": 'require_shipping_address',
        "tax_code": 'tax_code',
        "default_product_price_point_id": 'default_product_price_point_id',
        "use_site_exchange_rate": 'use_site_exchange_rate',
        "item_category": 'item_category',
        "product_price_point_id": 'product_price_point_id',
        "product_price_point_handle": 'product_price_point_handle'
    }

    _optionals = [
        'id',
        'name',
        'handle',
        'description',
        'accounting_code',
        'request_credit_card',
        'expiration_interval',
        'expiration_interval_unit',
        'created_at',
        'updated_at',
        'price_in_cents',
        'interval',
        'interval_unit',
        'initial_charge_in_cents',
        'trial_price_in_cents',
        'trial_interval',
        'trial_interval_unit',
        'archived_at',
        'require_credit_card',
        'return_params',
        'taxable',
        'update_return_url',
        'initial_charge_after_trial',
        'version_number',
        'update_return_params',
        'product_family',
        'public_signup_pages',
        'product_price_point_name',
        'request_billing_address',
        'require_billing_address',
        'require_shipping_address',
        'tax_code',
        'default_product_price_point_id',
        'use_site_exchange_rate',
        'item_category',
        'product_price_point_id',
        'product_price_point_handle',
    ]

    _nullables = [
        'handle',
        'description',
        'accounting_code',
        'expiration_interval',
        'expiration_interval_unit',
        'initial_charge_in_cents',
        'trial_price_in_cents',
        'trial_interval',
        'trial_interval_unit',
        'archived_at',
        'return_params',
        'update_return_url',
        'initial_charge_after_trial',
        'update_return_params',
        'tax_code',
        'use_site_exchange_rate',
        'item_category',
        'product_price_point_handle',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 accounting_code=APIHelper.SKIP,
                 request_credit_card=APIHelper.SKIP,
                 expiration_interval=APIHelper.SKIP,
                 expiration_interval_unit=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 price_in_cents=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 initial_charge_in_cents=APIHelper.SKIP,
                 trial_price_in_cents=APIHelper.SKIP,
                 trial_interval=APIHelper.SKIP,
                 trial_interval_unit=APIHelper.SKIP,
                 archived_at=APIHelper.SKIP,
                 require_credit_card=APIHelper.SKIP,
                 return_params=APIHelper.SKIP,
                 taxable=APIHelper.SKIP,
                 update_return_url=APIHelper.SKIP,
                 initial_charge_after_trial=APIHelper.SKIP,
                 version_number=APIHelper.SKIP,
                 update_return_params=APIHelper.SKIP,
                 product_family=APIHelper.SKIP,
                 public_signup_pages=APIHelper.SKIP,
                 product_price_point_name=APIHelper.SKIP,
                 request_billing_address=APIHelper.SKIP,
                 require_billing_address=APIHelper.SKIP,
                 require_shipping_address=APIHelper.SKIP,
                 tax_code=APIHelper.SKIP,
                 default_product_price_point_id=APIHelper.SKIP,
                 use_site_exchange_rate=APIHelper.SKIP,
                 item_category=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 product_price_point_handle=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the Product class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if description is not APIHelper.SKIP:
            self.description = description 
        if accounting_code is not APIHelper.SKIP:
            self.accounting_code = accounting_code 
        if request_credit_card is not APIHelper.SKIP:
            self.request_credit_card = request_credit_card 
        if expiration_interval is not APIHelper.SKIP:
            self.expiration_interval = expiration_interval 
        if expiration_interval_unit is not APIHelper.SKIP:
            self.expiration_interval_unit = expiration_interval_unit 
        if created_at is not APIHelper.SKIP:
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if price_in_cents is not APIHelper.SKIP:
            self.price_in_cents = price_in_cents 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 
        if initial_charge_in_cents is not APIHelper.SKIP:
            self.initial_charge_in_cents = initial_charge_in_cents 
        if trial_price_in_cents is not APIHelper.SKIP:
            self.trial_price_in_cents = trial_price_in_cents 
        if trial_interval is not APIHelper.SKIP:
            self.trial_interval = trial_interval 
        if trial_interval_unit is not APIHelper.SKIP:
            self.trial_interval_unit = trial_interval_unit 
        if archived_at is not APIHelper.SKIP:
            self.archived_at = APIHelper.apply_datetime_converter(archived_at, APIHelper.RFC3339DateTime) if archived_at else None 
        if require_credit_card is not APIHelper.SKIP:
            self.require_credit_card = require_credit_card 
        if return_params is not APIHelper.SKIP:
            self.return_params = return_params 
        if taxable is not APIHelper.SKIP:
            self.taxable = taxable 
        if update_return_url is not APIHelper.SKIP:
            self.update_return_url = update_return_url 
        if initial_charge_after_trial is not APIHelper.SKIP:
            self.initial_charge_after_trial = initial_charge_after_trial 
        if version_number is not APIHelper.SKIP:
            self.version_number = version_number 
        if update_return_params is not APIHelper.SKIP:
            self.update_return_params = update_return_params 
        if product_family is not APIHelper.SKIP:
            self.product_family = product_family 
        if public_signup_pages is not APIHelper.SKIP:
            self.public_signup_pages = public_signup_pages 
        if product_price_point_name is not APIHelper.SKIP:
            self.product_price_point_name = product_price_point_name 
        if request_billing_address is not APIHelper.SKIP:
            self.request_billing_address = request_billing_address 
        if require_billing_address is not APIHelper.SKIP:
            self.require_billing_address = require_billing_address 
        if require_shipping_address is not APIHelper.SKIP:
            self.require_shipping_address = require_shipping_address 
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code 
        if default_product_price_point_id is not APIHelper.SKIP:
            self.default_product_price_point_id = default_product_price_point_id 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 
        if item_category is not APIHelper.SKIP:
            self.item_category = item_category 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if product_price_point_handle is not APIHelper.SKIP:
            self.product_price_point_handle = product_price_point_handle 

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
        handle = dictionary.get("handle") if "handle" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        accounting_code = dictionary.get("accounting_code") if "accounting_code" in dictionary.keys() else APIHelper.SKIP
        request_credit_card = dictionary.get("request_credit_card") if "request_credit_card" in dictionary.keys() else APIHelper.SKIP
        expiration_interval = dictionary.get("expiration_interval") if "expiration_interval" in dictionary.keys() else APIHelper.SKIP
        expiration_interval_unit = dictionary.get("expiration_interval_unit") if "expiration_interval_unit" in dictionary.keys() else APIHelper.SKIP
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        price_in_cents = dictionary.get("price_in_cents") if dictionary.get("price_in_cents") else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if dictionary.get("interval_unit") else APIHelper.SKIP
        initial_charge_in_cents = dictionary.get("initial_charge_in_cents") if "initial_charge_in_cents" in dictionary.keys() else APIHelper.SKIP
        trial_price_in_cents = dictionary.get("trial_price_in_cents") if "trial_price_in_cents" in dictionary.keys() else APIHelper.SKIP
        trial_interval = dictionary.get("trial_interval") if "trial_interval" in dictionary.keys() else APIHelper.SKIP
        trial_interval_unit = dictionary.get("trial_interval_unit") if "trial_interval_unit" in dictionary.keys() else APIHelper.SKIP
        if 'archived_at' in dictionary.keys():
            archived_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("archived_at")).datetime if dictionary.get("archived_at") else None
        else:
            archived_at = APIHelper.SKIP
        require_credit_card = dictionary.get("require_credit_card") if "require_credit_card" in dictionary.keys() else APIHelper.SKIP
        return_params = dictionary.get("return_params") if "return_params" in dictionary.keys() else APIHelper.SKIP
        taxable = dictionary.get("taxable") if "taxable" in dictionary.keys() else APIHelper.SKIP
        update_return_url = dictionary.get("update_return_url") if "update_return_url" in dictionary.keys() else APIHelper.SKIP
        initial_charge_after_trial = dictionary.get("initial_charge_after_trial") if "initial_charge_after_trial" in dictionary.keys() else APIHelper.SKIP
        version_number = dictionary.get("version_number") if dictionary.get("version_number") else APIHelper.SKIP
        update_return_params = dictionary.get("update_return_params") if "update_return_params" in dictionary.keys() else APIHelper.SKIP
        product_family = ProductFamily.from_dictionary(dictionary.get('product_family')) if 'product_family' in dictionary.keys() else APIHelper.SKIP
        public_signup_pages = None
        if dictionary.get('public_signup_pages') is not None:
            public_signup_pages = [PublicSignupPage.from_dictionary(x) for x in dictionary.get('public_signup_pages')]
        else:
            public_signup_pages = APIHelper.SKIP
        product_price_point_name = dictionary.get("product_price_point_name") if dictionary.get("product_price_point_name") else APIHelper.SKIP
        request_billing_address = dictionary.get("request_billing_address") if "request_billing_address" in dictionary.keys() else APIHelper.SKIP
        require_billing_address = dictionary.get("require_billing_address") if "require_billing_address" in dictionary.keys() else APIHelper.SKIP
        require_shipping_address = dictionary.get("require_shipping_address") if "require_shipping_address" in dictionary.keys() else APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if "tax_code" in dictionary.keys() else APIHelper.SKIP
        default_product_price_point_id = dictionary.get("default_product_price_point_id") if dictionary.get("default_product_price_point_id") else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        item_category = dictionary.get("item_category") if "item_category" in dictionary.keys() else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        product_price_point_handle = dictionary.get("product_price_point_handle") if "product_price_point_handle" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   name,
                   handle,
                   description,
                   accounting_code,
                   request_credit_card,
                   expiration_interval,
                   expiration_interval_unit,
                   created_at,
                   updated_at,
                   price_in_cents,
                   interval,
                   interval_unit,
                   initial_charge_in_cents,
                   trial_price_in_cents,
                   trial_interval,
                   trial_interval_unit,
                   archived_at,
                   require_credit_card,
                   return_params,
                   taxable,
                   update_return_url,
                   initial_charge_after_trial,
                   version_number,
                   update_return_params,
                   product_family,
                   public_signup_pages,
                   product_price_point_name,
                   request_billing_address,
                   require_billing_address,
                   require_shipping_address,
                   tax_code,
                   default_product_price_point_id,
                   use_site_exchange_rate,
                   item_category,
                   product_price_point_id,
                   product_price_point_handle,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'name={self.name!r}, '
                f'handle={self.handle!r}, '
                f'description={self.description!r}, '
                f'accounting_code={self.accounting_code!r}, '
                f'request_credit_card={self.request_credit_card!r}, '
                f'expiration_interval={self.expiration_interval!r}, '
                f'expiration_interval_unit={self.expiration_interval_unit!r}, '
                f'created_at={self.created_at!r}, '
                f'updated_at={self.updated_at!r}, '
                f'price_in_cents={self.price_in_cents!r}, '
                f'interval={self.interval!r}, '
                f'interval_unit={self.interval_unit!r}, '
                f'initial_charge_in_cents={self.initial_charge_in_cents!r}, '
                f'trial_price_in_cents={self.trial_price_in_cents!r}, '
                f'trial_interval={self.trial_interval!r}, '
                f'trial_interval_unit={self.trial_interval_unit!r}, '
                f'archived_at={self.archived_at!r}, '
                f'require_credit_card={self.require_credit_card!r}, '
                f'return_params={self.return_params!r}, '
                f'taxable={self.taxable!r}, '
                f'update_return_url={self.update_return_url!r}, '
                f'initial_charge_after_trial={self.initial_charge_after_trial!r}, '
                f'version_number={self.version_number!r}, '
                f'update_return_params={self.update_return_params!r}, '
                f'product_family={self.product_family!r}, '
                f'public_signup_pages={self.public_signup_pages!r}, '
                f'product_price_point_name={self.product_price_point_name!r}, '
                f'request_billing_address={self.request_billing_address!r}, '
                f'require_billing_address={self.require_billing_address!r}, '
                f'require_shipping_address={self.require_shipping_address!r}, '
                f'tax_code={self.tax_code!r}, '
                f'default_product_price_point_id={self.default_product_price_point_id!r}, '
                f'use_site_exchange_rate={self.use_site_exchange_rate!r}, '
                f'item_category={self.item_category!r}, '
                f'product_price_point_id={self.product_price_point_id!r}, '
                f'product_price_point_handle={self.product_price_point_handle!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'name={self.name!s}, '
                f'handle={self.handle!s}, '
                f'description={self.description!s}, '
                f'accounting_code={self.accounting_code!s}, '
                f'request_credit_card={self.request_credit_card!s}, '
                f'expiration_interval={self.expiration_interval!s}, '
                f'expiration_interval_unit={self.expiration_interval_unit!s}, '
                f'created_at={self.created_at!s}, '
                f'updated_at={self.updated_at!s}, '
                f'price_in_cents={self.price_in_cents!s}, '
                f'interval={self.interval!s}, '
                f'interval_unit={self.interval_unit!s}, '
                f'initial_charge_in_cents={self.initial_charge_in_cents!s}, '
                f'trial_price_in_cents={self.trial_price_in_cents!s}, '
                f'trial_interval={self.trial_interval!s}, '
                f'trial_interval_unit={self.trial_interval_unit!s}, '
                f'archived_at={self.archived_at!s}, '
                f'require_credit_card={self.require_credit_card!s}, '
                f'return_params={self.return_params!s}, '
                f'taxable={self.taxable!s}, '
                f'update_return_url={self.update_return_url!s}, '
                f'initial_charge_after_trial={self.initial_charge_after_trial!s}, '
                f'version_number={self.version_number!s}, '
                f'update_return_params={self.update_return_params!s}, '
                f'product_family={self.product_family!s}, '
                f'public_signup_pages={self.public_signup_pages!s}, '
                f'product_price_point_name={self.product_price_point_name!s}, '
                f'request_billing_address={self.request_billing_address!s}, '
                f'require_billing_address={self.require_billing_address!s}, '
                f'require_shipping_address={self.require_shipping_address!s}, '
                f'tax_code={self.tax_code!s}, '
                f'default_product_price_point_id={self.default_product_price_point_id!s}, '
                f'use_site_exchange_rate={self.use_site_exchange_rate!s}, '
                f'item_category={self.item_category!s}, '
                f'product_price_point_id={self.product_price_point_id!s}, '
                f'product_price_point_handle={self.product_price_point_handle!s}, '
                f'additional_properties={self.additional_properties!s})')
