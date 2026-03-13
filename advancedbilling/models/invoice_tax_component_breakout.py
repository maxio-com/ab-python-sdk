"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
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
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "tax_rule_id": "tax_rule_id",
        "percentage": "percentage",
        "country_code": "country_code",
        "subdivision_code": "subdivision_code",
        "tax_amount": "tax_amount",
        "taxable_amount": "taxable_amount",
        "tax_exempt_amount": "tax_exempt_amount",
        "non_taxable_amount": "non_taxable_amount",
        "tax_name": "tax_name",
        "tax_type": "tax_type",
        "rate_type": "rate_type",
        "tax_authority_type": "tax_authority_type",
        "state_assigned_no": "state_assigned_no",
        "tax_sub_type": "tax_sub_type",
    }

    _optionals = [
        "tax_rule_id",
        "percentage",
        "country_code",
        "subdivision_code",
        "tax_amount",
        "taxable_amount",
        "tax_exempt_amount",
        "non_taxable_amount",
        "tax_name",
        "tax_type",
        "rate_type",
        "tax_authority_type",
        "state_assigned_no",
        "tax_sub_type",
    ]

    def __init__(
        self,
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
        """Initialize a InvoiceTaxComponentBreakout instance."""
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
        """Create an instance of this model from a dictionary

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
        tax_rule_id =\
            dictionary.get("tax_rule_id")\
            if dictionary.get("tax_rule_id")\
                else APIHelper.SKIP
        percentage =\
            dictionary.get("percentage")\
            if dictionary.get("percentage")\
                else APIHelper.SKIP
        country_code =\
            dictionary.get("country_code")\
            if dictionary.get("country_code")\
                else APIHelper.SKIP
        subdivision_code =\
            dictionary.get("subdivision_code")\
            if dictionary.get("subdivision_code")\
                else APIHelper.SKIP
        tax_amount =\
            dictionary.get("tax_amount")\
            if dictionary.get("tax_amount")\
                else APIHelper.SKIP
        taxable_amount =\
            dictionary.get("taxable_amount")\
            if dictionary.get("taxable_amount")\
                else APIHelper.SKIP
        tax_exempt_amount =\
            dictionary.get("tax_exempt_amount")\
            if dictionary.get("tax_exempt_amount")\
                else APIHelper.SKIP
        non_taxable_amount =\
            dictionary.get("non_taxable_amount")\
            if dictionary.get("non_taxable_amount")\
                else APIHelper.SKIP
        tax_name =\
            dictionary.get("tax_name")\
            if dictionary.get("tax_name")\
                else APIHelper.SKIP
        tax_type =\
            dictionary.get("tax_type")\
            if dictionary.get("tax_type")\
                else APIHelper.SKIP
        rate_type =\
            dictionary.get("rate_type")\
            if dictionary.get("rate_type")\
                else APIHelper.SKIP
        tax_authority_type =\
            dictionary.get("tax_authority_type")\
            if dictionary.get("tax_authority_type")\
                else APIHelper.SKIP
        state_assigned_no =\
            dictionary.get("state_assigned_no")\
            if dictionary.get("state_assigned_no")\
                else APIHelper.SKIP
        tax_sub_type =\
            dictionary.get("tax_sub_type")\
            if dictionary.get("tax_sub_type")\
                else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

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
        """Validate dictionary against class required properties

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
        """Return a unambiguous string representation."""
        _tax_rule_id=(
            self.tax_rule_id
            if hasattr(self, "tax_rule_id")
            else None
        )
        _percentage=(
            self.percentage
            if hasattr(self, "percentage")
            else None
        )
        _country_code=(
            self.country_code
            if hasattr(self, "country_code")
            else None
        )
        _subdivision_code=(
            self.subdivision_code
            if hasattr(self, "subdivision_code")
            else None
        )
        _tax_amount=(
            self.tax_amount
            if hasattr(self, "tax_amount")
            else None
        )
        _taxable_amount=(
            self.taxable_amount
            if hasattr(self, "taxable_amount")
            else None
        )
        _tax_exempt_amount=(
            self.tax_exempt_amount
            if hasattr(self, "tax_exempt_amount")
            else None
        )
        _non_taxable_amount=(
            self.non_taxable_amount
            if hasattr(self, "non_taxable_amount")
            else None
        )
        _tax_name=(
            self.tax_name
            if hasattr(self, "tax_name")
            else None
        )
        _tax_type=(
            self.tax_type
            if hasattr(self, "tax_type")
            else None
        )
        _rate_type=(
            self.rate_type
            if hasattr(self, "rate_type")
            else None
        )
        _tax_authority_type=(
            self.tax_authority_type
            if hasattr(self, "tax_authority_type")
            else None
        )
        _state_assigned_no=(
            self.state_assigned_no
            if hasattr(self, "state_assigned_no")
            else None
        )
        _tax_sub_type=(
            self.tax_sub_type
            if hasattr(self, "tax_sub_type")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"tax_rule_id={_tax_rule_id!r}, "
            f"percentage={_percentage!r}, "
            f"country_code={_country_code!r}, "
            f"subdivision_code={_subdivision_code!r}, "
            f"tax_amount={_tax_amount!r}, "
            f"taxable_amount={_taxable_amount!r}, "
            f"tax_exempt_amount={_tax_exempt_amount!r}, "
            f"non_taxable_amount={_non_taxable_amount!r}, "
            f"tax_name={_tax_name!r}, "
            f"tax_type={_tax_type!r}, "
            f"rate_type={_rate_type!r}, "
            f"tax_authority_type={_tax_authority_type!r}, "
            f"state_assigned_no={_state_assigned_no!r}, "
            f"tax_sub_type={_tax_sub_type!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _tax_rule_id=(
            self.tax_rule_id
            if hasattr(self, "tax_rule_id")
            else None
        )
        _percentage=(
            self.percentage
            if hasattr(self, "percentage")
            else None
        )
        _country_code=(
            self.country_code
            if hasattr(self, "country_code")
            else None
        )
        _subdivision_code=(
            self.subdivision_code
            if hasattr(self, "subdivision_code")
            else None
        )
        _tax_amount=(
            self.tax_amount
            if hasattr(self, "tax_amount")
            else None
        )
        _taxable_amount=(
            self.taxable_amount
            if hasattr(self, "taxable_amount")
            else None
        )
        _tax_exempt_amount=(
            self.tax_exempt_amount
            if hasattr(self, "tax_exempt_amount")
            else None
        )
        _non_taxable_amount=(
            self.non_taxable_amount
            if hasattr(self, "non_taxable_amount")
            else None
        )
        _tax_name=(
            self.tax_name
            if hasattr(self, "tax_name")
            else None
        )
        _tax_type=(
            self.tax_type
            if hasattr(self, "tax_type")
            else None
        )
        _rate_type=(
            self.rate_type
            if hasattr(self, "rate_type")
            else None
        )
        _tax_authority_type=(
            self.tax_authority_type
            if hasattr(self, "tax_authority_type")
            else None
        )
        _state_assigned_no=(
            self.state_assigned_no
            if hasattr(self, "state_assigned_no")
            else None
        )
        _tax_sub_type=(
            self.tax_sub_type
            if hasattr(self, "tax_sub_type")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"tax_rule_id={_tax_rule_id!s}, "
            f"percentage={_percentage!s}, "
            f"country_code={_country_code!s}, "
            f"subdivision_code={_subdivision_code!s}, "
            f"tax_amount={_tax_amount!s}, "
            f"taxable_amount={_taxable_amount!s}, "
            f"tax_exempt_amount={_tax_exempt_amount!s}, "
            f"non_taxable_amount={_non_taxable_amount!s}, "
            f"tax_name={_tax_name!s}, "
            f"tax_type={_tax_type!s}, "
            f"rate_type={_rate_type!s}, "
            f"tax_authority_type={_tax_authority_type!s}, "
            f"state_assigned_no={_state_assigned_no!s}, "
            f"tax_sub_type={_tax_sub_type!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
