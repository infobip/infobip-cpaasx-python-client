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
from infobip_cpaasx.models.mms_advanced_message_segment_binary import (
    MmsAdvancedMessageSegmentBinary,
)
from infobip_cpaasx.models.mms_advanced_message_segment_link import (
    MmsAdvancedMessageSegmentLink,
)
from infobip_cpaasx.models.mms_advanced_message_segment_smil import (
    MmsAdvancedMessageSegmentSmil,
)
from infobip_cpaasx.models.mms_advanced_message_segment_text import (
    MmsAdvancedMessageSegmentText,
)
from infobip_cpaasx.models.mms_advanced_message_segment_upload_reference import (
    MmsAdvancedMessageSegmentUploadReference,
)
from typing import Any, List
from pydantic import StrictStr, Field

MMSADVANCEDMESSAGESEGMENT_ANY_OF_SCHEMAS = [
    "MmsAdvancedMessageSegmentBinary",
    "MmsAdvancedMessageSegmentLink",
    "MmsAdvancedMessageSegmentSmil",
    "MmsAdvancedMessageSegmentText",
    "MmsAdvancedMessageSegmentUploadReference",
]


class MmsAdvancedMessageSegment(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    # data type: MmsAdvancedMessageSegmentText
    anyof_schema_1_validator: Optional[MmsAdvancedMessageSegmentText] = None
    # data type: MmsAdvancedMessageSegmentLink
    anyof_schema_2_validator: Optional[MmsAdvancedMessageSegmentLink] = None
    # data type: MmsAdvancedMessageSegmentBinary
    anyof_schema_3_validator: Optional[MmsAdvancedMessageSegmentBinary] = None
    # data type: MmsAdvancedMessageSegmentSmil
    anyof_schema_4_validator: Optional[MmsAdvancedMessageSegmentSmil] = None
    # data type: MmsAdvancedMessageSegmentUploadReference
    anyof_schema_5_validator: Optional[MmsAdvancedMessageSegmentUploadReference] = None
    actual_instance: Any
    any_of_schemas: List[str] = Field(
        MMSADVANCEDMESSAGESEGMENT_ANY_OF_SCHEMAS, const=True
    )

    class Config:
        validate_assignment = True

    @validator("actual_instance")
    def actual_instance_must_validate_anyof(cls, v):
        instance = cls()
        error_messages = []
        # validate data type: MmsAdvancedMessageSegmentText
        if type(v) is not MmsAdvancedMessageSegmentText:
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `MmsAdvancedMessageSegmentText`"
            )
        else:
            return v

        # validate data type: MmsAdvancedMessageSegmentLink
        if type(v) is not MmsAdvancedMessageSegmentLink:
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `MmsAdvancedMessageSegmentLink`"
            )
        else:
            return v

        # validate data type: MmsAdvancedMessageSegmentBinary
        if type(v) is not MmsAdvancedMessageSegmentBinary:
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `MmsAdvancedMessageSegmentBinary`"
            )
        else:
            return v

        # validate data type: MmsAdvancedMessageSegmentSmil
        if type(v) is not MmsAdvancedMessageSegmentSmil:
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `MmsAdvancedMessageSegmentSmil`"
            )
        else:
            return v

        # validate data type: MmsAdvancedMessageSegmentUploadReference
        if type(v) is not MmsAdvancedMessageSegmentUploadReference:
            error_messages.append(
                f"Error! Input type `{type(v)}` is not `MmsAdvancedMessageSegmentUploadReference`"
            )
        else:
            return v

        if error_messages:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into MmsAdvancedMessageSegment with anyOf schemas: MmsAdvancedMessageSegmentBinary, MmsAdvancedMessageSegmentLink, MmsAdvancedMessageSegmentSmil, MmsAdvancedMessageSegmentText, MmsAdvancedMessageSegmentUploadReference. Details: "
                + ", ".join(error_messages)
            )
        else:
            return v

    @classmethod
    def from_json(cls, json_str: str) -> MmsAdvancedMessageSegment:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        # anyof_schema_1_validator: Optional[MmsAdvancedMessageSegmentText] = None
        try:
            instance.actual_instance = MmsAdvancedMessageSegmentText.from_json(json_str)
            return instance
        except ValidationError as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[MmsAdvancedMessageSegmentLink] = None
        try:
            instance.actual_instance = MmsAdvancedMessageSegmentLink.from_json(json_str)
            return instance
        except ValidationError as e:
            error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[MmsAdvancedMessageSegmentBinary] = None
        try:
            instance.actual_instance = MmsAdvancedMessageSegmentBinary.from_json(
                json_str
            )
            return instance
        except ValidationError as e:
            error_messages.append(str(e))
        # anyof_schema_4_validator: Optional[MmsAdvancedMessageSegmentSmil] = None
        try:
            instance.actual_instance = MmsAdvancedMessageSegmentSmil.from_json(json_str)
            return instance
        except ValidationError as e:
            error_messages.append(str(e))
        # anyof_schema_5_validator: Optional[MmsAdvancedMessageSegmentUploadReference] = None
        try:
            instance.actual_instance = (
                MmsAdvancedMessageSegmentUploadReference.from_json(json_str)
            )
            return instance
        except ValidationError as e:
            error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError(
                "No match found when deserializing the JSON string into MmsAdvancedMessageSegment with anyOf schemas: MmsAdvancedMessageSegmentBinary, MmsAdvancedMessageSegmentLink, MmsAdvancedMessageSegmentSmil, MmsAdvancedMessageSegmentText, MmsAdvancedMessageSegmentUploadReference. Details: "
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
