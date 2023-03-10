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
from pydantic import BaseModel, Field, StrictInt, StrictStr


class SmsBinaryContent(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    data_coding: Optional[StrictInt] = Field(
        None,
        alias="dataCoding",
        description="Binary content data coding. The default value is (`0`) for GSM7. Example: (`8`) for  Unicode data.",
    )
    esm_class: Optional[StrictInt] = Field(
        None,
        alias="esmClass",
        description="“Esm_class” parameter. Indicate special message attributes associated with the SMS. Default value is (`0`).",
    )
    hex: StrictStr = Field(
        ...,
        description="Hexadecimal string. This is the representation of your binary data. Two hex digits represent one byte. They should be separated by the space character (Example: `0f c2 4a bf 34 13 ba`).",
    )
    __properties = ["dataCoding", "esmClass", "hex"]

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
    def from_json(cls, json_str: str) -> SmsBinaryContent:
        """Create an instance of SmsBinaryContent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SmsBinaryContent:
        """Create an instance of SmsBinaryContent from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SmsBinaryContent.parse_obj(obj)

        _obj = SmsBinaryContent.parse_obj(
            {
                "data_coding": obj.get("dataCoding"),
                "esm_class": obj.get("esmClass"),
                "hex": obj.get("hex"),
            }
        )
        return _obj
