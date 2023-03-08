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
from pydantic import BaseModel, Field, StrictStr, conlist, validator


class NumbersDeliveryTimeWindow(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    var_from: StrictStr = Field(
        ...,
        alias="from",
        description="Exact time of day in which the sending can start. Consists of hour and minute properties, both mandatory. Time is expressed in the UTC time zone. Formatted as HH:mm.",
    )
    to: StrictStr = Field(
        ...,
        description="Exact time of day in which the sending will end. Consists of an hour and minute properties, both mandatory. Time is expressed in the UTC time zone. Formatted as HH:mm.",
    )
    days: conlist(StrictStr, max_items=7, min_items=1) = Field(
        ...,
        description="Days which are included in the delivery time window."
    )
    delivery_time_zone: Optional[StrictStr] = Field(
        None,
        alias="deliveryTimeZone",
        description="Sending time zone. If null USER_TIME_ZONE will be set.",
    )
    __properties = ["from", "to", "days", "deliveryTimeZone"]

    @validator("days")
    def days_validate_enum(cls, v):
        if v is None:
            return
        for enum_value in v:
            if enum_value not in (
                "MONDAY",
                "TUESDAY",
                "WEDNESDAY",
                "THURSDAY",
                "FRIDAY",
                "SATURDAY",
                "SUNDAY",
            ):
                raise ValueError(
                    "must validate the enum values ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY')"
                )
        return v

    @validator("delivery_time_zone")
    def delivery_time_zone_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ("USER_TIME_ZONE", "DESTINATION_TIME_ZONE"):
            raise ValueError(
                "must validate the enum values ('USER_TIME_ZONE', 'DESTINATION_TIME_ZONE')"
            )
        return v

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
    def from_json(cls, json_str: str) -> NumbersDeliveryTimeWindow:
        """Create an instance of NumbersDeliveryTimeWindow from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumbersDeliveryTimeWindow:
        """Create an instance of NumbersDeliveryTimeWindow from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NumbersDeliveryTimeWindow.parse_obj(obj)

        _obj = NumbersDeliveryTimeWindow.parse_obj(
            {
                "var_from": obj.get("from"),
                "to": obj.get("to"),
                "days": obj.get("days"),
                "delivery_time_zone": obj.get("deliveryTimeZone"),
            }
        )
        return _obj
