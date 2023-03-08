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


from pydantic import BaseModel, Field, constr


class NumberRegistrationWebOptIn(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    call_to_action: constr(strict=True, max_length=1024, min_length=20) = Field(
        ...,
        alias="callToAction",
        description="The message sent to the user to tell them how to subscribe.",
    )
    url: constr(strict=True, max_length=255, min_length=11) = ...
    __properties = ["callToAction", "url"]

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
    def from_json(cls, json_str: str) -> NumberRegistrationWebOptIn:
        """Create an instance of NumberRegistrationWebOptIn from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumberRegistrationWebOptIn:
        """Create an instance of NumberRegistrationWebOptIn from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NumberRegistrationWebOptIn.parse_obj(obj)

        _obj = NumberRegistrationWebOptIn.parse_obj(
            {"call_to_action": obj.get("callToAction"), "url": obj.get("url")}
        )
        return _obj