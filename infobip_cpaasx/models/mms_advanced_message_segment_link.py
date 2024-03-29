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
from pydantic import BaseModel, Field, StrictStr


class MmsAdvancedMessageSegmentLink(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    content_id: Optional[StrictStr] = Field(
        None,
        alias="contentId",
        description="Unique identifier within single message. `[a-zA-Z]` up to 20 characters. Using other characters (e.g. spaces) may cause your message to be rejected by some mobile carriers.",
    )
    content_type: Optional[StrictStr] = Field(
        None,
        alias="contentType",
        description="Content type for media, for example `image/png`.",
    )
    content_url: StrictStr = Field(
        ..., alias="contentUrl", description="URL of externally hosted content."
    )
    __properties = ["contentId", "contentType", "contentUrl"]

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
    def from_json(cls, json_str: str) -> MmsAdvancedMessageSegmentLink:
        """Create an instance of MmsAdvancedMessageSegmentLink from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MmsAdvancedMessageSegmentLink:
        """Create an instance of MmsAdvancedMessageSegmentLink from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MmsAdvancedMessageSegmentLink.parse_obj(obj)

        _obj = MmsAdvancedMessageSegmentLink.parse_obj(
            {
                "content_id": obj.get("contentId"),
                "content_type": obj.get("contentType"),
                "content_url": obj.get("contentUrl"),
            }
        )
        return _obj
