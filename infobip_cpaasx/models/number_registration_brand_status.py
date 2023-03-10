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
from pydantic import BaseModel, Field, StrictStr, validator


class NumberRegistrationBrandStatus(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    registrar: Optional[StrictStr] = Field(
        None,
        description="The name of the registrar with which the brand has been registered.",
    )
    state: Optional[StrictStr] = Field(
        None, description="The state of the registration for this brand."
    )
    brand_identity_status: Optional[StrictStr] = Field(
        None,
        alias="brandIdentityStatus",
        description="The status of the brand as determined by the registrar.",
    )
    __properties = ["registrar", "state", "brandIdentityStatus"]

    @validator("registrar")
    def registrar_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ("CAMPAIGN_REGISTRY"):
            raise ValueError("must validate the enum values ('CAMPAIGN_REGISTRY')")
        return v

    @validator("state")
    def state_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ("ACTIVE", "PENDING", "REJECTED"):
            raise ValueError(
                "must validate the enum values ('ACTIVE', 'PENDING', 'REJECTED')"
            )
        return v

    @validator("brand_identity_status")
    def brand_identity_status_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ("SELF_DECLARED", "UNVERIFIED", "VERIFIED", "VETTED_VERIFIED"):
            raise ValueError(
                "must validate the enum values ('SELF_DECLARED', 'UNVERIFIED', 'VERIFIED', 'VETTED_VERIFIED')"
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
    def from_json(cls, json_str: str) -> NumberRegistrationBrandStatus:
        """Create an instance of NumberRegistrationBrandStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumberRegistrationBrandStatus:
        """Create an instance of NumberRegistrationBrandStatus from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NumberRegistrationBrandStatus.parse_obj(obj)

        _obj = NumberRegistrationBrandStatus.parse_obj(
            {
                "registrar": obj.get("registrar"),
                "state": obj.get("state"),
                "brand_identity_status": obj.get("brandIdentityStatus"),
            }
        )
        return _obj
