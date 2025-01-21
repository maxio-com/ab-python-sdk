# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.component_price_point_item import ComponentPricePointItem


class OnOffComponent(object):

    """Implementation of the 'On/Off Component' model.

    Attributes:
        name (str): A name for this component that is suitable for showing
            customers and displaying on billing statements, ie. "Minutes".
        description (str): A description for the component that will be
            displayed to the user on the hosted signup page.
        handle (str): A unique identifier for your use that can be used to
            retrieve this component is subsequent requests.  Must start with a
            letter or number and may only contain lowercase letters, numbers,
            or the characters '.', ':', '-', or '_'.
        taxable (bool): Boolean flag describing whether a component is taxable
            or not.
        upgrade_charge (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        downgrade_credit (CreditType): The type of credit to be created when
            upgrading/downgrading. Defaults to the component and then site
            setting if one is not provided. Available values: `full`,
            `prorated`, `none`.
        price_points (List[ComponentPricePointItem]): The model property of
            type List[ComponentPricePointItem].
        unit_price (str | float): This is the amount that the customer will be
            charged when they turn the component on for the subscription. The
            price can contain up to 8 decimal places. i.e. 1.00 or 0.0012 or
            0.00000065
        tax_code (str): A string representing the tax code related to the
            component type. This is especially important when using the
            Avalara service to tax based on locale. This attribute has a max
            length of 10 characters.
        hide_date_range_on_invoice (bool): (Only available on Relationship
            Invoicing sites) Boolean flag describing if the service date range
            should show for the component on generated invoices.
        display_on_hosted_page (bool): The model property of type bool.
        allow_fractional_quantities (bool): The model property of type bool.
        public_signup_page_ids (List[int]): The model property of type
            List[int].
        interval (int): The numerical interval. i.e. an interval of ‘30’
            coupled with an interval_unit of day would mean this component's
            default price point would renew every 30 days. This property is
            only available for sites with Multifrequency enabled.
        interval_unit (IntervalUnit): A string representing the interval unit
            for this component's default price point, either month or day.
            This property is only available for sites with Multifrequency
            enabled.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "unit_price": 'unit_price',
        "description": 'description',
        "handle": 'handle',
        "taxable": 'taxable',
        "upgrade_charge": 'upgrade_charge',
        "downgrade_credit": 'downgrade_credit',
        "price_points": 'price_points',
        "tax_code": 'tax_code',
        "hide_date_range_on_invoice": 'hide_date_range_on_invoice',
        "display_on_hosted_page": 'display_on_hosted_page',
        "allow_fractional_quantities": 'allow_fractional_quantities',
        "public_signup_page_ids": 'public_signup_page_ids',
        "interval": 'interval',
        "interval_unit": 'interval_unit'
    }

    _optionals = [
        'description',
        'handle',
        'taxable',
        'upgrade_charge',
        'downgrade_credit',
        'price_points',
        'tax_code',
        'hide_date_range_on_invoice',
        'display_on_hosted_page',
        'allow_fractional_quantities',
        'public_signup_page_ids',
        'interval',
        'interval_unit',
    ]

    _nullables = [
        'upgrade_charge',
        'downgrade_credit',
        'interval_unit',
    ]

    def __init__(self,
                 name=None,
                 unit_price=None,
                 description=APIHelper.SKIP,
                 handle=APIHelper.SKIP,
                 taxable=APIHelper.SKIP,
                 upgrade_charge=APIHelper.SKIP,
                 downgrade_credit=APIHelper.SKIP,
                 price_points=APIHelper.SKIP,
                 tax_code=APIHelper.SKIP,
                 hide_date_range_on_invoice=APIHelper.SKIP,
                 display_on_hosted_page=APIHelper.SKIP,
                 allow_fractional_quantities=APIHelper.SKIP,
                 public_signup_page_ids=APIHelper.SKIP,
                 interval=APIHelper.SKIP,
                 interval_unit=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the OnOffComponent class"""

        # Initialize members of the class
        self.name = name 
        if description is not APIHelper.SKIP:
            self.description = description 
        if handle is not APIHelper.SKIP:
            self.handle = handle 
        if taxable is not APIHelper.SKIP:
            self.taxable = taxable 
        if upgrade_charge is not APIHelper.SKIP:
            self.upgrade_charge = upgrade_charge 
        if downgrade_credit is not APIHelper.SKIP:
            self.downgrade_credit = downgrade_credit 
        if price_points is not APIHelper.SKIP:
            self.price_points = price_points 
        self.unit_price = unit_price 
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code 
        if hide_date_range_on_invoice is not APIHelper.SKIP:
            self.hide_date_range_on_invoice = hide_date_range_on_invoice 
        if display_on_hosted_page is not APIHelper.SKIP:
            self.display_on_hosted_page = display_on_hosted_page 
        if allow_fractional_quantities is not APIHelper.SKIP:
            self.allow_fractional_quantities = allow_fractional_quantities 
        if public_signup_page_ids is not APIHelper.SKIP:
            self.public_signup_page_ids = public_signup_page_ids 
        if interval is not APIHelper.SKIP:
            self.interval = interval 
        if interval_unit is not APIHelper.SKIP:
            self.interval_unit = interval_unit 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get("name") if dictionary.get("name") else None
        unit_price = APIHelper.deserialize_union_type(UnionTypeLookUp.get('OnOffComponentUnitPrice'), dictionary.get('unit_price'), False) if dictionary.get('unit_price') is not None else None
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        handle = dictionary.get("handle") if dictionary.get("handle") else APIHelper.SKIP
        taxable = dictionary.get("taxable") if "taxable" in dictionary.keys() else APIHelper.SKIP
        upgrade_charge = dictionary.get("upgrade_charge") if "upgrade_charge" in dictionary.keys() else APIHelper.SKIP
        downgrade_credit = dictionary.get("downgrade_credit") if "downgrade_credit" in dictionary.keys() else APIHelper.SKIP
        price_points = None
        if dictionary.get('price_points') is not None:
            price_points = [ComponentPricePointItem.from_dictionary(x) for x in dictionary.get('price_points')]
        else:
            price_points = APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if dictionary.get("tax_code") else APIHelper.SKIP
        hide_date_range_on_invoice = dictionary.get("hide_date_range_on_invoice") if "hide_date_range_on_invoice" in dictionary.keys() else APIHelper.SKIP
        display_on_hosted_page = dictionary.get("display_on_hosted_page") if "display_on_hosted_page" in dictionary.keys() else APIHelper.SKIP
        allow_fractional_quantities = dictionary.get("allow_fractional_quantities") if "allow_fractional_quantities" in dictionary.keys() else APIHelper.SKIP
        public_signup_page_ids = dictionary.get("public_signup_page_ids") if dictionary.get("public_signup_page_ids") else APIHelper.SKIP
        interval = dictionary.get("interval") if dictionary.get("interval") else APIHelper.SKIP
        interval_unit = dictionary.get("interval_unit") if "interval_unit" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(name,
                   unit_price,
                   description,
                   handle,
                   taxable,
                   upgrade_charge,
                   downgrade_credit,
                   price_points,
                   tax_code,
                   hide_date_range_on_invoice,
                   display_on_hosted_page,
                   allow_fractional_quantities,
                   public_signup_page_ids,
                   interval,
                   interval_unit,
                   additional_properties)

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.name,
                                           type_callable=lambda value: isinstance(value, str)) \
                and UnionTypeLookUp.get('OnOffComponentUnitPrice').validate(dictionary.unit_price).is_valid

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('name'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and UnionTypeLookUp.get('OnOffComponentUnitPrice').validate(dictionary.get('unit_price')).is_valid

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!r}, '
                f'description={self.description!r}, '
                f'handle={self.handle!r}, '
                f'taxable={self.taxable!r}, '
                f'upgrade_charge={self.upgrade_charge!r}, '
                f'downgrade_credit={self.downgrade_credit!r}, '
                f'price_points={self.price_points!r}, '
                f'unit_price={self.unit_price!r}, '
                f'tax_code={self.tax_code!r}, '
                f'hide_date_range_on_invoice={self.hide_date_range_on_invoice!r}, '
                f'display_on_hosted_page={self.display_on_hosted_page!r}, '
                f'allow_fractional_quantities={self.allow_fractional_quantities!r}, '
                f'public_signup_page_ids={self.public_signup_page_ids!r}, '
                f'interval={self.interval!r}, '
                f'interval_unit={self.interval_unit!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'name={self.name!s}, '
                f'description={self.description!s}, '
                f'handle={self.handle!s}, '
                f'taxable={self.taxable!s}, '
                f'upgrade_charge={self.upgrade_charge!s}, '
                f'downgrade_credit={self.downgrade_credit!s}, '
                f'price_points={self.price_points!s}, '
                f'unit_price={self.unit_price!s}, '
                f'tax_code={self.tax_code!s}, '
                f'hide_date_range_on_invoice={self.hide_date_range_on_invoice!s}, '
                f'display_on_hosted_page={self.display_on_hosted_page!s}, '
                f'allow_fractional_quantities={self.allow_fractional_quantities!s}, '
                f'public_signup_page_ids={self.public_signup_page_ids!s}, '
                f'interval={self.interval!s}, '
                f'interval_unit={self.interval_unit!s}, '
                f'additional_properties={self.additional_properties!s})')
