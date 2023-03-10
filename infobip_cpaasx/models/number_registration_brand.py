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
import infobip_cpaasx.models

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator


class NumberRegistrationBrand(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    id: Optional[StrictStr] = Field(None, description="The identifier for the brand.")
    name: constr(strict=True, max_length=100, min_length=1) = Field(
        ..., description="The customer defined name of brand."
    )
    website: constr(strict=True, max_length=255, min_length=11) = Field(
        ..., description="The website for the brand."
    )
    created_date: Optional[datetime] = Field(
        None,
        alias="createdDate",
        description="The date and time when the brand was created.",
    )
    last_modified_date: Optional[datetime] = Field(
        None,
        alias="lastModifiedDate",
        description="The date and time when the brand was last modified.",
    )
    type: StrictStr = Field(..., description="The type of brand.")
    __properties = ["id", "name", "website", "createdDate", "lastModifiedDate", "type"]

    @validator("type")
    def type_validate_enum(cls, v):
        if v not in (
            '"TENDLC_NON_PROFIT","TENDLC_PRIVATE_COMPANY","TENDLC_PUBLIC_COMPANY","TENDLC_GOVERNMENT"'
        ):
            raise ValueError(
                'must validate the enum values (\'"TENDLC_NON_PROFIT","TENDLC_PRIVATE_COMPANY","TENDLC_PUBLIC_COMPANY","TENDLC_GOVERNMENT"\')'
            )
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    # JSON field name that stores the object type
    __discriminator_property_name = "type"

    # discriminator mappings
    __discriminator_value_class_map = {
        "NumberRegistrationGovernmentBrand": "NumberRegistrationGovernmentBrand",
        "NumberRegistrationNonProfitBrand": "NumberRegistrationNonProfitBrand",
        "NumberRegistrationPrivateCompanyBrand": "NumberRegistrationPrivateCompanyBrand",
        "NumberRegistrationPublicCompanyBrand": "NumberRegistrationPublicCompanyBrand",
        "TENDLC_GOVERNMENT": "NumberRegistrationGovernmentBrand",
        "TENDLC_NON_PROFIT": "NumberRegistrationNonProfitBrand",
        "TENDLC_PRIVATE_COMPANY": "NumberRegistrationPrivateCompanyBrand",
        "TENDLC_PUBLIC_COMPANY": "NumberRegistrationPublicCompanyBrand",
    }

    @classmethod
    def get_discriminator_value(cls, obj: dict) -> str:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(
        cls, json_str: str
    ) -> Union(
        NumberRegistrationGovernmentBrand,
        NumberRegistrationNonProfitBrand,
        NumberRegistrationPrivateCompanyBrand,
        NumberRegistrationPublicCompanyBrand,
    ):
        """Create an instance of NumberRegistrationBrand from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(
        cls, obj: dict
    ) -> Union(
        NumberRegistrationGovernmentBrand,
        NumberRegistrationNonProfitBrand,
        NumberRegistrationPrivateCompanyBrand,
        NumberRegistrationPublicCompanyBrand,
    ):
        """Create an instance of NumberRegistrationBrand from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type:
            klass = getattr(infobip_cpaasx.models, object_type)
            return klass.from_dict(obj)
        else:
            raise ValueError(
                "NumberRegistrationBrand failed to lookup discriminator value from "
                + json.dumps(obj)
                + ". Discriminator property name: "
                + cls.__discriminator_property_name
                + ", mapping: "
                + json.dumps(cls.__discriminator_value_class_map)
            )
