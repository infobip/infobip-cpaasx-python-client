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


from pydantic import BaseModel, Field, StrictStr, conlist


class NumberRegistrationUpdateCampaignRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    number_keys: conlist(StrictStr, max_items=50, min_items=1) = Field(
        ...,
        alias="numberKeys",
        description="The numberKey(s) of the numbers to use with the campaign.",
    )
    __properties = ["numberKeys"]

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
    def from_json(cls, json_str: str) -> NumberRegistrationUpdateCampaignRequest:
        """Create an instance of NumberRegistrationUpdateCampaignRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumberRegistrationUpdateCampaignRequest:
        """Create an instance of NumberRegistrationUpdateCampaignRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NumberRegistrationUpdateCampaignRequest.parse_obj(obj)

        _obj = NumberRegistrationUpdateCampaignRequest.parse_obj(
            {"number_keys": obj.get("numberKeys")}
        )
        return _obj
