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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, constr
from infobip_cpaasx.models.mms_advanced_message_segment import MmsAdvancedMessageSegment
from infobip_cpaasx.models.mms_delivery_time_window import MmsDeliveryTimeWindow
from infobip_cpaasx.models.mms_destination import MmsDestination


class MmsAdvancedMessage(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    callback_data: Optional[constr(strict=True, max_length=4000, min_length=0)] = Field(
        None,
        alias="callbackData",
        description="Additional client data to be sent over the notifyUrl. The maximum value is 4000 characters.",
    )
    delivery_time_window: Optional[MmsDeliveryTimeWindow] = Field(
        None, alias="deliveryTimeWindow"
    )
    destinations: List[MmsDestination] = Field(
        ...,
        description="An array of destination objects for where messages are being sent. A valid destination is required.",
    )
    var_from: Optional[StrictStr] = Field(
        None,
        alias="from",
        description="The sender ID which can be alphanumeric or numeric (e.g., `CompanyName`).",
    )
    intermediate_report: Optional[StrictBool] = Field(
        None,
        alias="intermediateReport",
        description="The [real-time intermediate delivery report](https://www.infobip.com/docs/api/channels/mms/get-outbound-mms-message-delivery-reports) containing GSM error codes, messages status, pricing, network and country codes, etc., which will be sent on your callback server. Defaults to `false`.",
    )
    notify_url: Optional[StrictStr] = Field(
        None,
        alias="notifyUrl",
        description="The URL on your call back server on to which a delivery report will be sent.",
    )
    message_segments: List[MmsAdvancedMessageSegment] = Field(
        ..., alias="messageSegments", description="Content of the message being sent."
    )
    validity_period: Optional[StrictInt] = Field(
        None,
        alias="validityPeriod",
        description="The message validity period in minutes. When the period expires, it will not be allowed for the message to be sent. Validity period longer than 48h is not supported. Any bigger value will automatically default back to `2880`.",
    )
    title: Optional[constr(strict=True, max_length=66, min_length=0)] = None
    entity_id: Optional[constr(strict=True, max_length=50, min_length=0)] = Field(
        None,
        alias="entityId",
        description="Required for entity use in a send request for outbound traffic. Returned in notification events.",
    )
    application_id: Optional[constr(strict=True, max_length=50, min_length=0)] = Field(
        None,
        alias="applicationId",
        description="Required for application use in a send request for outbound traffic. Returned in notification events.",
    )
    __properties = [
        "callbackData",
        "deliveryTimeWindow",
        "destinations",
        "from",
        "intermediateReport",
        "notifyUrl",
        "messageSegments",
        "validityPeriod",
        "title",
        "entityId",
        "applicationId",
    ]

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
    def from_json(cls, json_str: str) -> MmsAdvancedMessage:
        """Create an instance of MmsAdvancedMessage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of delivery_time_window
        if self.delivery_time_window:
            _dict["deliveryTimeWindow"] = self.delivery_time_window.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in destinations (list)
        _items = []
        if self.destinations:
            for _item in self.destinations:
                if _item:
                    _items.append(_item.to_dict())
            _dict["destinations"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in message_segments (list)
        _items = []
        if self.message_segments:
            for _item in self.message_segments:
                if _item:
                    _items.append(_item.to_dict())
            _dict["messageSegments"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MmsAdvancedMessage:
        """Create an instance of MmsAdvancedMessage from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MmsAdvancedMessage.parse_obj(obj)

        _obj = MmsAdvancedMessage.parse_obj(
            {
                "callback_data": obj.get("callbackData"),
                "delivery_time_window": MmsDeliveryTimeWindow.from_dict(
                    obj.get("deliveryTimeWindow")
                )
                if obj.get("deliveryTimeWindow") is not None
                else None,
                "destinations": [
                    MmsDestination.from_dict(_item) for _item in obj.get("destinations")
                ]
                if obj.get("destinations") is not None
                else None,
                "var_from": obj.get("from"),
                "intermediate_report": obj.get("intermediateReport"),
                "notify_url": obj.get("notifyUrl"),
                "message_segments": [
                    MmsAdvancedMessageSegment.from_dict(_item)
                    for _item in obj.get("messageSegments")
                ]
                if obj.get("messageSegments") is not None
                else None,
                "validity_period": obj.get("validityPeriod"),
                "title": obj.get("title"),
                "entity_id": obj.get("entityId"),
                "application_id": obj.get("applicationId"),
            }
        )
        return _obj
