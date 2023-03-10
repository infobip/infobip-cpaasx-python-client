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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr


class MessageError(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    description: Optional[StrictStr] = Field(
        None, description="Human-readable description of the error."
    )
    permanent: Optional[StrictBool] = Field(
        None, description="Indicates whether the error is permanent."
    )
    name: Optional[StrictStr] = Field(None, description="Error name.")
    id: Optional[StrictInt] = Field(None, description="Error ID.")
    group_name: Optional[StrictStr] = Field(
        None, alias="groupName", description="Error group name."
    )
    group_id: Optional[StrictInt] = Field(
        None, alias="groupId", description="Error group ID."
    )
    __properties = ["description", "permanent", "name", "id", "groupName", "groupId"]

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
    def from_json(cls, json_str: str) -> MessageError:
        """Create an instance of MessageError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MessageError:
        """Create an instance of MessageError from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MessageError.parse_obj(obj)

        _obj = MessageError.parse_obj(
            {
                "description": obj.get("description"),
                "permanent": obj.get("permanent"),
                "name": obj.get("name"),
                "id": obj.get("id"),
                "group_name": obj.get("groupName"),
                "group_id": obj.get("groupId"),
            }
        )
        return _obj
