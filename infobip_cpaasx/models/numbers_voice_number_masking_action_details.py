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


from pydantic import BaseModel, Field, StrictStr
from infobip_cpaasx.models.numbers_voice_action_details import NumbersVoiceActionDetails


class NumbersVoiceNumberMaskingActionDetails(NumbersVoiceActionDetails):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    voice_number_masking_config_key: StrictStr = Field(
        ..., alias="voiceNumberMaskingConfigKey"
    )
    __properties = ["type", "description", "voiceNumberMaskingConfigKey"]

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
    def from_json(cls, json_str: str) -> NumbersVoiceNumberMaskingActionDetails:
        """Create an instance of NumbersVoiceNumberMaskingActionDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumbersVoiceNumberMaskingActionDetails:
        """Create an instance of NumbersVoiceNumberMaskingActionDetails from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NumbersVoiceNumberMaskingActionDetails.parse_obj(obj)

        _obj = NumbersVoiceNumberMaskingActionDetails.parse_obj(
            {
                "type": obj.get("type"),
                "description": obj.get("description"),
                "voice_number_masking_config_key": obj.get(
                    "voiceNumberMaskingConfigKey"
                ),
            }
        )
        return _obj
