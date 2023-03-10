# coding: utf-8

"""
    This class is auto generated from the Infobip OpenAPI specification
    through the OpenAPI Specification Client API libraries (Re)Generator (OSCAR),
    powered by the OpenAPI Generator (https://openapi-generator.tech).
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator
from infobip_cpaasx.models.number_registration_address import NumberRegistrationAddress
from infobip_cpaasx.models.number_registration_brand import NumberRegistrationBrand
from infobip_cpaasx.models.number_registration_business_identifier import (
    NumberRegistrationBusinessIdentifier,
)


class NumberRegistrationPublicCompanyBrand(NumberRegistrationBrand):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    reference_id: Optional[StrictStr] = Field(
        None,
        alias="referenceId",
        description="Unique user defined ID for the brand. While not required, it is recommended to supply a referenceId as the uniqueness constraint will help ensure a brand is not accidentally created multiple times. Subsequent create requests with the same referenceId will be rejected with an error.",
    )
    legal_name: constr(strict=True, max_length=255, min_length=1) = Field(
        ..., alias="legalName", description="The legal name of the brand."
    )
    address: NumberRegistrationAddress = ...
    country_code: constr(strict=True, max_length=2, min_length=1) = Field(
        ..., alias="countryCode", description="The country where the brand is located."
    )
    alternate_business_id: Optional[NumberRegistrationBusinessIdentifier] = Field(
        None, alias="alternateBusinessId"
    )
    support_email: constr(strict=True, max_length=100, min_length=1) = Field(
        ...,
        alias="supportEmail",
        description="The business email address to contact about brand compliance issues. Must be a well formed email address that does not include a '=' character.",
    )
    support_phone: constr(strict=True, max_length=16, min_length=3) = Field(
        ...,
        alias="supportPhone",
        description="The business phone number to contact about brand compliance issues.",
    )
    vertical: StrictStr = Field(
        ..., description="The vertical in which the brand operates."
    )
    tax_id: constr(strict=True, max_length=21, min_length=1) = Field(
        ..., alias="taxId", description="The tax identifier (EIN) for the brand."
    )
    stock_exchange: StrictStr = Field(
        ...,
        alias="stockExchange",
        description="The stock exchange where brand is listed.",
    )
    stock_symbol: constr(strict=True, max_length=30, min_length=1) = Field(
        ...,
        alias="stockSymbol",
        description="The ticker symbol for the brand on the exchange where it is listed.",
    )
    __properties = [
        "id",
        "name",
        "website",
        "createdDate",
        "lastModifiedDate",
        "type",
        "referenceId",
        "legalName",
        "address",
        "countryCode",
        "alternateBusinessId",
        "supportEmail",
        "supportPhone",
        "vertical",
        "taxId",
        "stockExchange",
        "stockSymbol",
    ]

    @validator("support_phone")
    def support_phone_validate_regular_expression(cls, v):
        if not re.match(r"\+?[1-9]\d{1,14}", v):
            raise ValueError(r"must validate the regular expression /\+?[1-9]\d{1,14}/")
        return v

    @validator("vertical")
    def vertical_validate_enum(cls, v):
        if v not in (
            "AGRICULTURE",
            "CONSTRUCTION_AND_MATERIALS",
            "EDUCATION",
            "ENERGY_AND_UTILITIES",
            "ENTERTAINMENT",
            "FINANCIAL_SERVICES",
            "GAMBLING_AND_LOTTERY",
            "HEALTHCARE_AND_LIFESCIENCES",
            "HOSPITALITY",
            "INFORMATION_TECHNOLOGY_SERVICES",
            "INSURANCE",
            "MANUFACTURING",
            "MASS_MEDIA_AND_COMMUNICATION",
            "NON_PROFIT_ORGANIZATION",
            "PUBLIC_SECTOR",
            "REAL_ESTATE",
            "RETAIL_AND_CONSUMER_PRODUCTS",
        ):
            raise ValueError(
                "must validate the enum values ('AGRICULTURE', 'CONSTRUCTION_AND_MATERIALS', 'EDUCATION', 'ENERGY_AND_UTILITIES', 'ENTERTAINMENT', 'FINANCIAL_SERVICES', 'GAMBLING_AND_LOTTERY', 'HEALTHCARE_AND_LIFESCIENCES', 'HOSPITALITY', 'INFORMATION_TECHNOLOGY_SERVICES', 'INSURANCE', 'MANUFACTURING', 'MASS_MEDIA_AND_COMMUNICATION', 'NON_PROFIT_ORGANIZATION', 'PUBLIC_SECTOR', 'REAL_ESTATE', 'RETAIL_AND_CONSUMER_PRODUCTS')"
            )
        return v

    @validator("stock_exchange")
    def stock_exchange_validate_enum(cls, v):
        if v not in (
            "AMEX",
            "AMX",
            "ASX",
            "B3",
            "BME",
            "BSE",
            "FRA",
            "ICEX",
            "JPX",
            "JSE",
            "KRX",
            "LON",
            "NASDAQ",
            "NSE",
            "NYSE",
            "OMX",
            "SEHK",
            "SGX",
            "SSE",
            "STO",
            "SWX",
            "SZSE",
            "TSX",
            "TWSE",
            "VSE",
        ):
            raise ValueError(
                "must validate the enum values ('AMEX', 'AMX', 'ASX', 'B3', 'BME', 'BSE', 'FRA', 'ICEX', 'JPX', 'JSE', 'KRX', 'LON', 'NASDAQ', 'NSE', 'NYSE', 'OMX', 'SEHK', 'SGX', 'SSE', 'STO', 'SWX', 'SZSE', 'TSX', 'TWSE', 'VSE')"
            )
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> NumberRegistrationPublicCompanyBrand:
        """Create an instance of NumberRegistrationPublicCompanyBrand from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict["address"] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of alternate_business_id
        if self.alternate_business_id:
            _dict["alternateBusinessId"] = self.alternate_business_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumberRegistrationPublicCompanyBrand:
        """Create an instance of NumberRegistrationPublicCompanyBrand from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NumberRegistrationPublicCompanyBrand.parse_obj(obj)

        _obj = NumberRegistrationPublicCompanyBrand.parse_obj(
            {
                "id": obj.get("id"),
                "name": obj.get("name"),
                "website": obj.get("website"),
                "created_date": obj.get("createdDate"),
                "last_modified_date": obj.get("lastModifiedDate"),
                "type": obj.get("type"),
                "reference_id": obj.get("referenceId"),
                "legal_name": obj.get("legalName"),
                "address": NumberRegistrationAddress.from_dict(obj.get("address"))
                if obj.get("address") is not None
                else None,
                "country_code": obj.get("countryCode"),
                "alternate_business_id": NumberRegistrationBusinessIdentifier.from_dict(
                    obj.get("alternateBusinessId")
                )
                if obj.get("alternateBusinessId") is not None
                else None,
                "support_email": obj.get("supportEmail"),
                "support_phone": obj.get("supportPhone"),
                "vertical": obj.get("vertical"),
                "tax_id": obj.get("taxId"),
                "stock_exchange": obj.get("stockExchange"),
                "stock_symbol": obj.get("stockSymbol"),
            }
        )
        return _obj
