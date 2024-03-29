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
from infobip_cpaasx.models.mms_error import MmsError
from infobip_cpaasx.models.mms_price import MmsPrice
from infobip_cpaasx.models.mms_status import MmsStatus


class MmsReport(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    bulk_id: Optional[StrictStr] = Field(None, alias="bulkId", description="Bulk ID.")
    message_id: Optional[StrictStr] = Field(
        None, alias="messageId", description="Message ID."
    )
    to: Optional[StrictStr] = Field(None, description="Destination address.")
    var_from: Optional[StrictStr] = Field(
        None, alias="from", description="Sender ID that can be alphanumeric or numeric."
    )
    sent_at: Optional[datetime] = Field(
        None,
        alias="sentAt",
        description="Indicates whether the MMS was sent. Has the following format: `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.",
    )
    done_at: Optional[datetime] = Field(
        None,
        alias="doneAt",
        description="Indicates Whether the MMS was finished processing by Infobip (i.e., delivered to the destination, delivered to the destination network, etc.). Has the following format: `yyyy-MM-dd'T'HH:mm:ss.SSSZ`.",
    )
    mms_count: Optional[StrictInt] = Field(
        None,
        alias="mmsCount",
        description="The number of parts the sent MMS was split into.",
    )
    mcc_mnc: Optional[StrictStr] = Field(
        None, alias="mccMnc", description="Mobile country and network codes."
    )
    callback_data: Optional[StrictStr] = Field(
        None,
        alias="callbackData",
        description="Callback data sent through `callbackData` field in fully featured MMS message.",
    )
    price: Optional[MmsPrice] = None
    status: Optional[MmsStatus] = None
    error: Optional[MmsError] = None
    entity_id: Optional[StrictStr] = Field(
        None, alias="entityId", description="Entity used in MMS request."
    )
    application_id: Optional[StrictStr] = Field(
        None, alias="applicationId", description="Application used in MMS request."
    )
    __properties = [
        "bulkId",
        "messageId",
        "to",
        "from",
        "sentAt",
        "doneAt",
        "mmsCount",
        "mccMnc",
        "callbackData",
        "price",
        "status",
        "error",
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
    def from_json(cls, json_str: str) -> MmsReport:
        """Create an instance of MmsReport from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict["price"] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict["status"] = self.status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict["error"] = self.error.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MmsReport:
        """Create an instance of MmsReport from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MmsReport.parse_obj(obj)

        _obj = MmsReport.parse_obj(
            {
                "bulk_id": obj.get("bulkId"),
                "message_id": obj.get("messageId"),
                "to": obj.get("to"),
                "var_from": obj.get("from"),
                "sent_at": obj.get("sentAt"),
                "done_at": obj.get("doneAt"),
                "mms_count": obj.get("mmsCount"),
                "mcc_mnc": obj.get("mccMnc"),
                "callback_data": obj.get("callbackData"),
                "price": MmsPrice.from_dict(obj.get("price"))
                if obj.get("price") is not None
                else None,
                "status": MmsStatus.from_dict(obj.get("status"))
                if obj.get("status") is not None
                else None,
                "error": MmsError.from_dict(obj.get("error"))
                if obj.get("error") is not None
                else None,
                "entity_id": obj.get("entityId"),
                "application_id": obj.get("applicationId"),
            }
        )
        return _obj
