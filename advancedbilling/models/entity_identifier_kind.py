"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class EntityIdentifierKind(object):
    """Implementation of the 'Entity Identifier Kind' enum.

    The kind of tax or business identifier held by the customer:
    - `vat_eu`: an EU VAT number. Requires `vat_country` to be an EU member state
    code or `GB`.
    - `national_tax`: a national tax ID registered outside the EU. Requires
    `vat_country` to be one of `AL`, `AM`, `AR`, `AU`, `BR`, `CA`, `CH`, `DZ`, `IN`,
    `MX`, `NO`, `NZ`, or `ZA`.
    - `company_reg`: a company registration number, such as a French SIREN. No
    `vat_country` is required.
    - `gln`: a Global Location Number. The value must be 13 digits.
    - `duns`: a D-U-N-S Number. The value must be 9 digits.
    - `lei`: a Legal Entity Identifier. The value must be 20 characters: 18 letters
    or digits followed by 2 digits.
    A customer holds one identifier at a time. Saving an identifier of a different
    kind replaces the existing one.

    Attributes:
        VAT_EU: The enum member of type str.
        NATIONAL_TAX: The enum member of type str.
        COMPANY_REG: The enum member of type str.
        GLN: The enum member of type str.
        DUNS: The enum member of type str.
        LEI: The enum member of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    _all_values = ["vat_eu", "national_tax", "company_reg", "gln", "duns", "lei"]
    VAT_EU = "vat_eu"

    NATIONAL_TAX = "national_tax"

    COMPANY_REG = "company_reg"

    GLN = "gln"

    DUNS = "duns"

    LEI = "lei"

    @classmethod
    def validate(cls, value):
        """Validate value contains in enum

        Args:
            value: the value to be validated

        Returns:
            boolean : if value is valid enum values.

        """
        return value in cls._all_values

    @classmethod
    def from_value(cls, value, default=None):
        """Return the matching enum value for the given input."""
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
