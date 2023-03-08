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
from pydantic import BaseModel, Field, StrictInt
from infobip_cpaasx.models.mms_webhook_inbound_report import MmsWebhookInboundReport


class MmsWebhookInboundReportResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    results: Optional[List[MmsWebhookInboundReport]] = None
    message_count: Optional[StrictInt] = Field(
        None,
        alias="messageCount",
        description="Number of returned messages in this request.",
    )
    pending_message_count: Optional[StrictInt] = Field(
        None,
        alias="pendingMessageCount",
        description="Number of remaining new messages on Infobip servers ready to be returned in the next request.",
    )
    __properties = ["results", "messageCount", "pendingMessageCount"]

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
    def from_json(cls, json_str: str) -> MmsWebhookInboundReportResponse:
        """Create an instance of MmsWebhookInboundReportResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict["results"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MmsWebhookInboundReportResponse:
        """Create an instance of MmsWebhookInboundReportResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MmsWebhookInboundReportResponse.parse_obj(obj)

        _obj = MmsWebhookInboundReportResponse.parse_obj(
            {
                "results": [
                    MmsWebhookInboundReport.from_dict(_item)
                    for _item in obj.get("results")
                ]
                if obj.get("results") is not None
                else None,
                "message_count": obj.get("messageCount"),
                "pending_message_count": obj.get("pendingMessageCount"),
            }
        )
        return _obj
