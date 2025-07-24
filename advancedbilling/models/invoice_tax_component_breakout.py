# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class InvoiceTaxComponentBreakout(object):

    """Implementation of the 'Invoice Tax Component Breakout' model.

    Attributes:
        tax_rule_id (int): The model property of type int.
        percentage (str): The model property of type str.
        country_code (str): The model property of type str.
        subdivision_code (str): The model property of type str.
        tax_amount (str): The model property of type str.
        taxable_amount (str): The model property of type str.
        tax_exempt_amount (str): The model property of type str.
        non_taxable_amount (str): The model property of type str.
        tax_name (str): The model property of type str.
        tax_type (str): The model property of type str.
        rate_type (str): The model property of type str.
        tax_authority_type (int): The model property of type int.
        state_assigned_no (str): The model property of type str.
        tax_sub_type (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tax_rule_id": 'tax_rule_id',
        "percentage": 'percentage',
        "country_code": 'country_code',
        "subdivision_code": 'subdivision_code',
        "tax_amount": 'tax_amount',
        "taxable_amount": 'taxable_amount',
        "tax_exempt_amount": 'tax_exempt_amount',
        "non_taxable_amount": 'non_taxable_amount',
        "tax_name": 'tax_name',
        "tax_type": 'tax_type',
        "rate_type": 'rate_type',
        "tax_authority_type": 'tax_authority_type',
        "state_assigned_no": 'state_assigned_no',
        "tax_sub_type": 'tax_sub_type'
    }

    _optionals = [
        'tax_rule_id',
        'percentage',
        'country_code',
        'subdivision_code',
        'tax_amount',
        'taxable_amount',
        'tax_exempt_amount',
        'non_taxable_amount',
        'tax_name',
        'tax_type',
        'rate_type',
        'tax_authority_type',
        'state_assigned_no',
        'tax_sub_type',
    ]

    def __init__(self,
                 tax_rule_id=APIHelper.SKIP,
                 percentage=APIHelper.SKIP,
                 country_code=APIHelper.SKIP,
                 subdivision_code=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP,
                 taxable_amount=APIHelper.SKIP,
                 tax_exempt_amount=APIHelper.SKIP,
                 non_taxable_amount=APIHelper.SKIP,
                 tax_name=APIHelper.SKIP,
                 tax_type=APIHelper.SKIP,
                 rate_type=APIHelper.SKIP,
                 tax_authority_type=APIHelper.SKIP,
                 state_assigned_no=APIHelper.SKIP,
                 tax_sub_type=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoiceTaxComponentBreakout class"""

        # Initialize members of the class
        if tax_rule_id is not APIHelper.SKIP:
            self.tax_rule_id = tax_rule_id 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 
        if country_code is not APIHelper.SKIP:
            self.country_code = country_code 
        if subdivision_code is not APIHelper.SKIP:
            self.subdivision_code = subdivision_code 
        if tax_amount is not APIHelper.SKIP:
            self.tax_amount = tax_amount 
        if taxable_amount is not APIHelper.SKIP:
            self.taxable_amount = taxable_amount 
        if tax_exempt_amount is not APIHelper.SKIP:
            self.tax_exempt_amount = tax_exempt_amount 
        if non_taxable_amount is not APIHelper.SKIP:
            self.non_taxable_amount = non_taxable_amount 
        if tax_name is not APIHelper.SKIP:
            self.tax_name = tax_name 
        if tax_type is not APIHelper.SKIP:
            self.tax_type = tax_type 
        if rate_type is not APIHelper.SKIP:
            self.rate_type = rate_type 
        if tax_authority_type is not APIHelper.SKIP:
            self.tax_authority_type = tax_authority_type 
        if state_assigned_no is not APIHelper.SKIP:
            self.state_assigned_no = state_assigned_no 
        if tax_sub_type is not APIHelper.SKIP:
            self.tax_sub_type = tax_sub_type 

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
        tax_rule_id = dictionary.get("tax_rule_id") if dictionary.get("tax_rule_id") else APIHelper.SKIP
        percentage = dictionary.get("percentage") if dictionary.get("percentage") else APIHelper.SKIP
        country_code = dictionary.get("country_code") if dictionary.get("country_code") else APIHelper.SKIP
        subdivision_code = dictionary.get("subdivision_code") if dictionary.get("subdivision_code") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        taxable_amount = dictionary.get("taxable_amount") if dictionary.get("taxable_amount") else APIHelper.SKIP
        tax_exempt_amount = dictionary.get("tax_exempt_amount") if dictionary.get("tax_exempt_amount") else APIHelper.SKIP
        non_taxable_amount = dictionary.get("non_taxable_amount") if dictionary.get("non_taxable_amount") else APIHelper.SKIP
        tax_name = dictionary.get("tax_name") if dictionary.get("tax_name") else APIHelper.SKIP
        tax_type = dictionary.get("tax_type") if dictionary.get("tax_type") else APIHelper.SKIP
        rate_type = dictionary.get("rate_type") if dictionary.get("rate_type") else APIHelper.SKIP
        tax_authority_type = dictionary.get("tax_authority_type") if dictionary.get("tax_authority_type") else APIHelper.SKIP
        state_assigned_no = dictionary.get("state_assigned_no") if dictionary.get("state_assigned_no") else APIHelper.SKIP
        tax_sub_type = dictionary.get("tax_sub_type") if dictionary.get("tax_sub_type") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(tax_rule_id,
                   percentage,
                   country_code,
                   subdivision_code,
                   tax_amount,
                   taxable_amount,
                   tax_exempt_amount,
                   non_taxable_amount,
                   tax_name,
                   tax_type,
                   rate_type,
                   tax_authority_type,
                   state_assigned_no,
                   tax_sub_type,
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

        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'tax_rule_id={(self.tax_rule_id if hasattr(self, "tax_rule_id") else None)!r}, '
                f'percentage={(self.percentage if hasattr(self, "percentage") else None)!r}, '
                f'country_code={(self.country_code if hasattr(self, "country_code") else None)!r}, '
                f'subdivision_code={(self.subdivision_code if hasattr(self, "subdivision_code") else None)!r}, '
                f'tax_amount={(self.tax_amount if hasattr(self, "tax_amount") else None)!r}, '
                f'taxable_amount={(self.taxable_amount if hasattr(self, "taxable_amount") else None)!r}, '
                f'tax_exempt_amount={(self.tax_exempt_amount if hasattr(self, "tax_exempt_amount") else None)!r}, '
                f'non_taxable_amount={(self.non_taxable_amount if hasattr(self, "non_taxable_amount") else None)!r}, '
                f'tax_name={(self.tax_name if hasattr(self, "tax_name") else None)!r}, '
                f'tax_type={(self.tax_type if hasattr(self, "tax_type") else None)!r}, '
                f'rate_type={(self.rate_type if hasattr(self, "rate_type") else None)!r}, '
                f'tax_authority_type={(self.tax_authority_type if hasattr(self, "tax_authority_type") else None)!r}, '
                f'state_assigned_no={(self.state_assigned_no if hasattr(self, "state_assigned_no") else None)!r}, '
                f'tax_sub_type={(self.tax_sub_type if hasattr(self, "tax_sub_type") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'tax_rule_id={(self.tax_rule_id if hasattr(self, "tax_rule_id") else None)!s}, '
                f'percentage={(self.percentage if hasattr(self, "percentage") else None)!s}, '
                f'country_code={(self.country_code if hasattr(self, "country_code") else None)!s}, '
                f'subdivision_code={(self.subdivision_code if hasattr(self, "subdivision_code") else None)!s}, '
                f'tax_amount={(self.tax_amount if hasattr(self, "tax_amount") else None)!s}, '
                f'taxable_amount={(self.taxable_amount if hasattr(self, "taxable_amount") else None)!s}, '
                f'tax_exempt_amount={(self.tax_exempt_amount if hasattr(self, "tax_exempt_amount") else None)!s}, '
                f'non_taxable_amount={(self.non_taxable_amount if hasattr(self, "non_taxable_amount") else None)!s}, '
                f'tax_name={(self.tax_name if hasattr(self, "tax_name") else None)!s}, '
                f'tax_type={(self.tax_type if hasattr(self, "tax_type") else None)!s}, '
                f'rate_type={(self.rate_type if hasattr(self, "rate_type") else None)!s}, '
                f'tax_authority_type={(self.tax_authority_type if hasattr(self, "tax_authority_type") else None)!s}, '
                f'state_assigned_no={(self.state_assigned_no if hasattr(self, "state_assigned_no") else None)!s}, '
                f'tax_sub_type={(self.tax_sub_type if hasattr(self, "tax_sub_type") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
