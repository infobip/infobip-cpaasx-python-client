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
from pydantic import BaseModel, Field, StrictStr, constr


class NumbersPurchaseNumberRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    number_key: Optional[StrictStr] = Field(None, alias="numberKey")
    number: Optional[StrictStr] = None
    application_id: Optional[constr(strict=True, max_length=255, min_length=0)] = Field(
        None,
        alias="applicationId",
        description="ID of the Application that would be associated with the number.",
    )
    entity_id: Optional[constr(strict=True, max_length=255, min_length=0)] = Field(
        None,
        alias="entityId",
        description="ID of the Entity that would be associated with the number.",
    )
    __properties = ["numberKey", "number", "applicationId", "entityId"]

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
    def from_json(cls, json_str: str) -> NumbersPurchaseNumberRequest:
        """Create an instance of NumbersPurchaseNumberRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumbersPurchaseNumberRequest:
        """Create an instance of NumbersPurchaseNumberRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NumbersPurchaseNumberRequest.parse_obj(obj)

        _obj = NumbersPurchaseNumberRequest.parse_obj(
            {
                "number_key": obj.get("numberKey"),
                "number": obj.get("number"),
                "application_id": obj.get("applicationId"),
                "entity_id": obj.get("entityId"),
            }
        )
        return _obj