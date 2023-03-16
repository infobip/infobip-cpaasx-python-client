# coding: utf-8

"""
    This class is auto generated from the Infobip OpenAPI specification
    through the OpenAPI Specification Client API libraries (Re)Generator (OSCAR),
    powered by the OpenAPI Generator (https://openapi-generator.tech).
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, conint, constr

from typing import Optional

from infobip_cpaasx.models.entity import Entity
from infobip_cpaasx.models.modify_entity import ModifyEntity
from infobip_cpaasx.models.page_entity import PageEntity

from infobip_cpaasx.api_client import ApiClient
from infobip_cpaasx.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class EntityApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_entity(self, entity: Entity, **kwargs) -> None:  # noqa: E501
        """Create entity  # noqa: E501

        Create an entity associated with the specified `entityId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_entity(entity, async_req=True)
        >>> result = thread.get()

        :param entity: (required)
        :type entity: Entity
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        return self.create_entity_with_http_info(entity, **kwargs)  # noqa: E501

    @validate_arguments
    def create_entity_with_http_info(self, entity: Entity, **kwargs):  # noqa: E501
        """Create entity  # noqa: E501

        Create an entity associated with the specified `entityId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_entity_with_http_info(entity, async_req=True)
        >>> result = thread.get()

        :param entity: (required)
        :type entity: Entity
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = ["entity"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_entity" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params["entity"]:
            _body_params = _params["entity"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = ["APIKeyHeader"]  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            "/provisioning/1/entities",
            "POST",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def get_entities(
        self,
        page: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="Results page to retrieve (0..N)."),
        ] = None,
        size: Annotated[
            Optional[conint(strict=True, le=100, ge=1)],
            Field(description="Number of records per page."),
        ] = None,
        **kwargs
    ) -> PageEntity:  # noqa: E501
        """Get entities  # noqa: E501

        Get a paginated list of entities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_entities(page, size, async_req=True)
        >>> result = thread.get()

        :param page: Results page to retrieve (0..N).
        :type page: int
        :param size: Number of records per page.
        :type size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: PageEntity
        """
        kwargs["_return_http_data_only"] = True
        return self.get_entities_with_http_info(page, size, **kwargs)  # noqa: E501

    @validate_arguments
    def get_entities_with_http_info(
        self,
        page: Annotated[
            Optional[conint(strict=True, ge=0)],
            Field(description="Results page to retrieve (0..N)."),
        ] = None,
        size: Annotated[
            Optional[conint(strict=True, le=100, ge=1)],
            Field(description="Number of records per page."),
        ] = None,
        **kwargs
    ):  # noqa: E501
        """Get entities  # noqa: E501

        Get a paginated list of entities.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_entities_with_http_info(page, size, async_req=True)
        >>> result = thread.get()

        :param page: Results page to retrieve (0..N).
        :type page: int
        :param size: Number of records per page.
        :type size: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(PageEntity, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["page", "size"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_entities" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get("page") is not None:  # noqa: E501
            _query_params.append(("page", _params["page"]))
        if _params.get("size") is not None:  # noqa: E501
            _query_params.append(("size", _params["size"]))

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["APIKeyHeader"]  # noqa: E501

        _response_types_map = {
            "200": "PageEntity",
        }

        return self.api_client.call_api(
            "/provisioning/1/entities",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def get_entity(
        self,
        entity_id: Annotated[
            constr(strict=True, max_length=255),
            Field(
                ...,
                description="Id of the entity, this `id` will be a URL path parameter, the validation on our backend will verify its validity by doing `urlEncode(id) = id` meaning if any character in the `id` would require encoding the validation will fail.",
            ),
        ],
        **kwargs
    ) -> Entity:  # noqa: E501
        """Get entity  # noqa: E501

        Get an entity for the specified `entityId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_entity(entity_id, async_req=True)
        >>> result = thread.get()

        :param entity_id: Id of the entity, this `id` will be a URL path parameter, the validation on our backend will verify its validity by doing `urlEncode(id) = id` meaning if any character in the `id` would require encoding the validation will fail. (required)
        :type entity_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Entity
        """
        kwargs["_return_http_data_only"] = True
        return self.get_entity_with_http_info(entity_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_entity_with_http_info(
        self,
        entity_id: Annotated[
            constr(strict=True, max_length=255),
            Field(
                ...,
                description="Id of the entity, this `id` will be a URL path parameter, the validation on our backend will verify its validity by doing `urlEncode(id) = id` meaning if any character in the `id` would require encoding the validation will fail.",
            ),
        ],
        **kwargs
    ):  # noqa: E501
        """Get entity  # noqa: E501

        Get an entity for the specified `entityId`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_entity_with_http_info(entity_id, async_req=True)
        >>> result = thread.get()

        :param entity_id: Id of the entity, this `id` will be a URL path parameter, the validation on our backend will verify its validity by doing `urlEncode(id) = id` meaning if any character in the `id` would require encoding the validation will fail. (required)
        :type entity_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Entity, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = ["entity_id"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_entity" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["entity_id"]:
            _path_params["entityId"] = _params["entity_id"]

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # authentication setting
        _auth_settings = ["APIKeyHeader"]  # noqa: E501

        _response_types_map = {
            "200": "Entity",
        }

        return self.api_client.call_api(
            "/provisioning/1/entities/{entityId}",
            "GET",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )

    @validate_arguments
    def modify_entity(
        self,
        entity_id: Annotated[
            constr(strict=True, max_length=255),
            Field(
                ...,
                description="Id of the entity, this `id` will be a URL path parameter, the validation on our backend will verify its validity by doing `urlEncode(id) = id` meaning if any character in the `id` would require encoding the validation will fail.",
            ),
        ],
        modify_entity: ModifyEntity,
        **kwargs
    ) -> None:  # noqa: E501
        """Modify entity  # noqa: E501

        Modify a resource `name` property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_entity(entity_id, modify_entity, async_req=True)
        >>> result = thread.get()

        :param entity_id: Id of the entity, this `id` will be a URL path parameter, the validation on our backend will verify its validity by doing `urlEncode(id) = id` meaning if any character in the `id` would require encoding the validation will fail. (required)
        :type entity_id: str
        :param modify_entity: (required)
        :type modify_entity: ModifyEntity
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        return self.modify_entity_with_http_info(
            entity_id, modify_entity, **kwargs
        )  # noqa: E501

    @validate_arguments
    def modify_entity_with_http_info(
        self,
        entity_id: Annotated[
            constr(strict=True, max_length=255),
            Field(
                ...,
                description="Id of the entity, this `id` will be a URL path parameter, the validation on our backend will verify its validity by doing `urlEncode(id) = id` meaning if any character in the `id` would require encoding the validation will fail.",
            ),
        ],
        modify_entity: ModifyEntity,
        **kwargs
    ):  # noqa: E501
        """Modify entity  # noqa: E501

        Modify a resource `name` property.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.modify_entity_with_http_info(entity_id, modify_entity, async_req=True)
        >>> result = thread.get()

        :param entity_id: Id of the entity, this `id` will be a URL path parameter, the validation on our backend will verify its validity by doing `urlEncode(id) = id` meaning if any character in the `id` would require encoding the validation will fail. (required)
        :type entity_id: str
        :param modify_entity: (required)
        :type modify_entity: ModifyEntity
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = ["entity_id", "modify_entity"]
        _all_params.extend(
            [
                "async_req",
                "_return_http_data_only",
                "_preload_content",
                "_request_timeout",
                "_request_auth",
                "_content_type",
                "_headers",
            ]
        )

        # validate the arguments
        for _key, _val in _params["kwargs"].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_entity" % _key
                )
            _params[_key] = _val
        del _params["kwargs"]

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params["entity_id"]:
            _path_params["entityId"] = _params["entity_id"]

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get("_headers", {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None
        if _params["modify_entity"]:
            _body_params = _params["modify_entity"]

        # set the HTTP header `Accept`
        _header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get(
            "_content_type",
            self.api_client.select_header_content_type(["application/json"]),
        )
        if _content_types_list:
            _header_params["Content-Type"] = _content_types_list

        # authentication setting
        _auth_settings = ["APIKeyHeader"]  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            "/provisioning/1/entities/{entityId}",
            "PUT",
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get("async_req"),
            _return_http_data_only=_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=_params.get("_preload_content", True),
            _request_timeout=_params.get("_request_timeout"),
            collection_formats=_collection_formats,
            _request_auth=_params.get("_request_auth"),
        )
