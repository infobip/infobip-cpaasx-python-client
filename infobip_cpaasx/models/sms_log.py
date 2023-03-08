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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from infobip_cpaasx.models.sms_error import SmsError
from infobip_cpaasx.models.sms_price import SmsPrice
from infobip_cpaasx.models.sms_status import SmsStatus


class SmsLog(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    bulk_id: Optional[StrictStr] = Field(
        None,
        alias="bulkId",
        description="Unique ID assigned to the request if messaging multiple recipients or sending multiple messages via a single API request.",
    )
    done_at: Optional[datetime] = Field(
        None,
        alias="doneAt",
        description="Date and time when the Infobip services finished processing the message (i.e. delivered to the destination, delivered to the destination network, etc.). Has the following format: `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.",
    )
    error: Optional[SmsError] = None
    var_from: Optional[StrictStr] = Field(
        None, alias="from", description="Sender ID that can be alphanumeric or numeric."
    )
    mcc_mnc: Optional[StrictStr] = Field(
        None, alias="mccMnc", description="Mobile country and network codes."
    )
    message_id: Optional[StrictStr] = Field(
        None, alias="messageId", description="Unique message ID."
    )
    price: Optional[SmsPrice] = None
    sent_at: Optional[datetime] = Field(
        None,
        alias="sentAt",
        description="Date and time when the message was [scheduled](https://www.infobip.com/docs/api#channels/sms/get-scheduled-sms-messages) to be sent. Has the following format: `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.",
    )
    sms_count: Optional[StrictInt] = Field(
        None,
        alias="smsCount",
        description="The number of parts the message content was split into.",
    )
    status: Optional[SmsStatus] = None
    text: Optional[StrictStr] = Field(
        None, description="Content of the message being sent."
    )
    to: Optional[StrictStr] = Field(
        None, description="The destination address of the message."
    )
    __properties = [
        "bulkId",
        "doneAt",
        "error",
        "from",
        "mccMnc",
        "messageId",
        "price",
        "sentAt",
        "smsCount",
        "status",
        "text",
        "to",
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
    def from_json(cls, json_str: str) -> SmsLog:
        """Create an instance of SmsLog from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict["error"] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict["price"] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict["status"] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SmsLog:
        """Create an instance of SmsLog from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SmsLog.parse_obj(obj)

        _obj = SmsLog.parse_obj(
            {
                "bulk_id": obj.get("bulkId"),
                "done_at": obj.get("doneAt"),
                "error": SmsError.from_dict(obj.get("error"))
                if obj.get("error") is not None
                else None,
                "var_from": obj.get("from"),
                "mcc_mnc": obj.get("mccMnc"),
                "message_id": obj.get("messageId"),
                "price": SmsPrice.from_dict(obj.get("price"))
                if obj.get("price") is not None
                else None,
                "sent_at": obj.get("sentAt"),
                "sms_count": obj.get("smsCount"),
                "status": SmsStatus.from_dict(obj.get("status"))
                if obj.get("status") is not None
                else None,
                "text": obj.get("text"),
                "to": obj.get("to"),
            }
        )
        return _obj