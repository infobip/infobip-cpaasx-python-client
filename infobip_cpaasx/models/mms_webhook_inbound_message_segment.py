# coding: utf-8

"""
    This class is auto generated from the Infobip OpenAPI specification
    through the OpenAPI Specification Client API libraries (Re)Generator (OSCAR),
    powered by the OpenAPI Generator (https://openapi-generator.tech).
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from infobip_cpaasx.models.mms_webhook_inbound_message_segment_link import (
    MmsWebhookInboundMessageSegmentLink,
)
from infobip_cpaasx.models.mms_webhook_inbound_message_segment_text import (
    MmsWebhookInboundMessageSegmentText,
)
from typing import Any, List
from pydantic import StrictStr, Field

MMSWEBHOOKINBOUNDMESSAGESEGMENT_ANY_OF_SCHEMAS = [
    "MmsWebhookInboundMessageSegmentLink",
    "MmsWebhookInboundMessageSegmentText",
]


class MmsWebhookInboundMessageSegment(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    # data type: MmsWebhookInboundMessageSegmentText
    anyof_schema_1_validator: Optional[MmsWebhookInboundMessageSegmentText] = None
    # data type: MmsWebhookInboundMessageSegmentLink
    anyof_schema_2_validator: Optional[MmsWebhookInboundMessageSegmentLink] = None
    actual_instance: Any
    any_of_schemas: List[str] = Field(
        MMSWEBHOOKINBOUNDMESSAGESEGMENT_ANY_OF_SCHEMAS, const=True
    )

    class Config:
        validate_assignment = True

    @validator("actual_instance")
    def actual_instance_must_validate_anyof(cls, v):
        instance = cls()
        error_messages = []
        # validate data type: MmsWebhookInboundMessageSegmentText
        if type(v) is not MmsWebhookInboundMessageSegmentText:
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `MmsWebhookInboundMessageSegmentText`"
            )
        else:
            return v

        # validate data type: MmsWebhookInboundMessageSegmentLink
        if type(v) is not MmsWebhookInboundMessageSegmentLink:
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `MmsWebhookInboundMessageSegmentLink`"
            )
        else:
            return v

        if error_messages:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into MmsWebhookInboundMessageSegment with anyOf schemas: MmsWebhookInboundMessageSegmentLink, MmsWebhookInboundMessageSegmentText. Details: "
                + ", ".join(error_messages)
            )
        else:
            return v

    @classmethod
    def from_json(cls, json_str: str) -> MmsWebhookInboundMessageSegment:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        # anyof_schema_1_validator: Optional[MmsWebhookInboundMessageSegmentText] = None
        try:
            instance.actual_instance = MmsWebhookInboundMessageSegmentText.from_json(
                json_str
            )
            return instance
        except ValidationError as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[MmsWebhookInboundMessageSegmentLink] = None
        try:
            instance.actual_instance = MmsWebhookInboundMessageSegmentLink.from_json(
                json_str
            )
            return instance
        except ValidationError as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into MmsWebhookInboundMessageSegment with anyOf schemas: MmsWebhookInboundMessageSegmentLink, MmsWebhookInboundMessageSegmentText. Details: "
                + ", ".join(error_messages)
            )
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())