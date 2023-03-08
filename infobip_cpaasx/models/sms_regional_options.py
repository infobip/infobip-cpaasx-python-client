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
from pydantic import BaseModel, Field
from infobip_cpaasx.models.sms_india_dlt_options import SmsIndiaDltOptions
from infobip_cpaasx.models.sms_turkey_iys_options import SmsTurkeyIysOptions


class SmsRegionalOptions(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    india_dlt: Optional[SmsIndiaDltOptions] = Field(None, alias="indiaDlt")
    turkey_iys: Optional[SmsTurkeyIysOptions] = Field(None, alias="turkeyIys")
    __properties = ["indiaDlt", "turkeyIys"]

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
    def from_json(cls, json_str: str) -> SmsRegionalOptions:
        """Create an instance of SmsRegionalOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of india_dlt
        if self.india_dlt:
            _dict["indiaDlt"] = self.india_dlt.to_dict()
        # override the default output from pydantic by calling `to_dict()` of turkey_iys
        if self.turkey_iys:
            _dict["turkeyIys"] = self.turkey_iys.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SmsRegionalOptions:
        """Create an instance of SmsRegionalOptions from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SmsRegionalOptions.parse_obj(obj)

        _obj = SmsRegionalOptions.parse_obj(
            {
                "india_dlt": SmsIndiaDltOptions.from_dict(obj.get("indiaDlt"))
                if obj.get("indiaDlt") is not None
                else None,
                "turkey_iys": SmsTurkeyIysOptions.from_dict(obj.get("turkeyIys"))
                if obj.get("turkeyIys") is not None
                else None,
            }
        )
        return _obj