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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr
from infobip_cpaasx.models.mms_message_result import MmsMessageResult


class MmsSendResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    bulk_id: Optional[StrictStr] = Field(
        None, alias="bulkId", description="Unique bulk identifier."
    )
    messages: List[MmsMessageResult] = Field(
        ..., description="Array of sent message objects, one object per every message."
    )
    error_message: Optional[StrictStr] = Field(
        None, alias="errorMessage", description="General error description."
    )
    __properties = ["bulkId", "messages", "errorMessage"]

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
    def from_json(cls, json_str: str) -> MmsSendResult:
        """Create an instance of MmsSendResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item in self.messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict["messages"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MmsSendResult:
        """Create an instance of MmsSendResult from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MmsSendResult.parse_obj(obj)

        _obj = MmsSendResult.parse_obj(
            {
                "bulk_id": obj.get("bulkId"),
                "messages": [
                    MmsMessageResult.from_dict(_item) for _item in obj.get("messages")
                ]
                if obj.get("messages") is not None
                else None,
                "error_message": obj.get("errorMessage"),
            }
        )
        return _obj
