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
from pydantic import BaseModel, Field, StrictStr, constr
from infobip_cpaasx.models.numbers_mo_action import NumbersMoAction
from infobip_cpaasx.models.numbers_mo_non_forward_action import (
    NumbersMoNonForwardAction,
)
from infobip_cpaasx.models.numbers_use_conversation import NumbersUseConversation


class NumbersStoredMoConfiguration(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    keyword: Optional[constr(strict=True, max_length=50, min_length=0)] = Field(
        None, description="Configuration keyword."
    )
    action: NumbersMoAction = ...
    use_conversation: Optional[NumbersUseConversation] = Field(
        None, alias="useConversation"
    )
    other_actions_details: Optional[List[NumbersMoNonForwardAction]] = Field(
        None,
        alias="otherActionsDetails",
        description="List of other configured actions on this keyword. Ignored in POST/PUT calls.",
    )
    other_actions: Optional[List[StrictStr]] = Field(
        None,
        alias="otherActions",
        description="List of other configured action types/names on this keyword. Ignored in POST/PUT calls.",
    )
    application_id: Optional[constr(strict=True, max_length=255, min_length=0)] = Field(
        None,
        alias="applicationId",
        description="ID of the Application that would be associated with the configuration.",
    )
    entity_id: Optional[constr(strict=True, max_length=255, min_length=0)] = Field(
        None,
        alias="entityId",
        description="ID of the Entity that would be associated with the configuration.",
    )
    key: StrictStr = Field(..., description="Unique ID of configuration.")
    __properties = [
        "keyword",
        "action",
        "useConversation",
        "otherActionsDetails",
        "otherActions",
        "applicationId",
        "entityId",
        "key",
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
    def from_json(cls, json_str: str) -> NumbersStoredMoConfiguration:
        """Create an instance of NumbersStoredMoConfiguration from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of action
        if self.action:
            _dict["action"] = self.action.to_dict()
        # override the default output from pydantic by calling `to_dict()` of use_conversation
        if self.use_conversation:
            _dict["useConversation"] = self.use_conversation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in other_actions_details (list)
        _items = []
        if self.other_actions_details:
            for _item in self.other_actions_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict["otherActionsDetails"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NumbersStoredMoConfiguration:
        """Create an instance of NumbersStoredMoConfiguration from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NumbersStoredMoConfiguration.parse_obj(obj)

        _obj = NumbersStoredMoConfiguration.parse_obj(
            {
                "keyword": obj.get("keyword"),
                "action": NumbersMoAction.from_dict(obj.get("action"))
                if obj.get("action") is not None
                else None,
                "use_conversation": NumbersUseConversation.from_dict(
                    obj.get("useConversation")
                )
                if obj.get("useConversation") is not None
                else None,
                "other_actions_details": [
                    NumbersMoNonForwardAction.from_dict(_item)
                    for _item in obj.get("otherActionsDetails")
                ]
                if obj.get("otherActionsDetails") is not None
                else None,
                "other_actions": obj.get("otherActions"),
                "application_id": obj.get("applicationId"),
                "entity_id": obj.get("entityId"),
                "key": obj.get("key"),
            }
        )
        return _obj
