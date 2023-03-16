import pytest
from pytest_httpserver import HTTPServer

from infobip_cpaasx import ApiClient, Configuration, PageInfo, ResourceAssociationApi, PageResourceAssociation, \
    ResourceAssociationResponse, Channel, \
    ResourceType, ResourceAssociationRequest

resource_associations_endpoint = "/provisioning/1/associations"
resource_associations_single_endpoint = "/provisioning/1/associations/single"

api_key = "givenApiKey"
user_agent = "infobip-api-client-python/0.0.2-cpaasx"
expected_headers = {
    "Authorization": "App {}".format(api_key),
    "User-Agent": user_agent
}
port = 8088


def test_get_resource_associations(httpserver: HTTPServer, get_api_client):
    page = 1
    size = 1
    resource_type = "NUMBER"
    resource_type_enum = ResourceType.NUMBER
    channel = "SMS"
    channel_enum = Channel.SMS
    application_id = "given-application-id"
    entity_id = "given-entity-id"
    resource_id = "given-resource-id"

    expected_response = {
        "results": [
            {
                "resourceType": resource_type,
                "channel": channel,
                "applicationId": application_id,
                "entityId": entity_id,
                "resourceId": resource_id
            }
        ],
        "paging": {
            "page": page,
            "size": size,
            "totalPages": 2,
            "totalResults": 2
        }
    }

    query_string = to_query_string_without_escaping({
        "page": page,
        "size": size,
        "resourceType": resource_type,
        "channel": channel,
        "applicationId": application_id,
        "entityId": entity_id,
        "resourceId": resource_id
    })

    setup_get_request(
        httpserver=httpserver,
        endpoint=resource_associations_endpoint,
        expected_response=expected_response,
        query_string=query_string
    )

    api_instance = ResourceAssociationApi(get_api_client)
    actual_response = api_instance.get_resource_associations(
        page=page,
        size=size,
        resource_type=resource_type_enum,
        channel=channel_enum,
        application_id=application_id,
        entity_id=entity_id,
        resource_id=resource_id
    )

    expected_resource_associations_response = PageResourceAssociation(
        results=[
            ResourceAssociationResponse(
                resource_type=resource_type_enum,
                channel=channel_enum,
                application_id=application_id,
                entity_id=entity_id,
                resource_id=resource_id
            )
        ],
        paging=PageInfo(
            page=page,
            size=size,
            totalPages=2,
            totalResults=2
        )
    )

    assert actual_response == expected_resource_associations_response


def test_create_resource_associations(httpserver: HTTPServer, get_api_client):
    resource_type = "NUMBER"
    channel = "SMS"
    application_id = "given-application-id"
    entity_id = "given-entity-id"
    resource_id = "given-resource-id"

    expected_request = {
        "resourceType": resource_type,
        "channel": channel,
        "applicationId": application_id,
        "entityId": entity_id,
        "resourceId": resource_id
    }

    setup_post_request_created(
        httpserver=httpserver,
        endpoint=resource_associations_endpoint,
        expected_request=expected_request
    )

    resource_association = ResourceAssociationRequest(
        resourceType=resource_type,
        channel=channel,
        applicationId=application_id,
        entityId=entity_id,
        resourceId=resource_id
    )

    api_instance = ResourceAssociationApi(get_api_client)
    api_instance.create_resource_association(resource_association)


def test_delete_resource_associations(httpserver: HTTPServer, get_api_client):
    resource_type = "NUMBER"
    channel = "SMS"
    application_id = "given-application-id"
    entity_id = "given-entity-id"
    resource_id = "given-resource-id"

    expected_request = {
        "resourceType": resource_type,
        "channel": channel,
        "applicationId": application_id,
        "entityId": entity_id,
        "resourceId": resource_id
    }

    setup_delete_request_no_content(
        httpserver=httpserver,
        endpoint=resource_associations_endpoint,
        expected_request=expected_request
    )

    resource_association = ResourceAssociationRequest(
        resourceType=resource_type,
        channel=channel,
        applicationId=application_id,
        entityId=entity_id,
        resourceId=resource_id
    )

    api_instance = ResourceAssociationApi(get_api_client)
    api_instance.delete_resource_association(resource_association)


def test_get_resource_association(httpserver: HTTPServer, get_api_client):
    resource_type = "NUMBER"
    resource_type_enum = ResourceType.NUMBER
    channel = "SMS"
    channel_enum = Channel.SMS
    application_id = "given-application-id"
    entity_id = "given-entity-id"
    resource_id = "given-resource-id"

    expected_response = {
        "resourceType": resource_type,
        "channel": channel,
        "applicationId": application_id,
        "entityId": entity_id,
        "resourceId": resource_id
    }

    query_string = to_query_string_without_escaping({
        "resourceType": resource_type,
        "channel": channel,
        "applicationId": application_id,
        "entityId": entity_id,
        "resourceId": resource_id
    })

    setup_get_request(
        httpserver=httpserver,
        endpoint=resource_associations_single_endpoint,
        expected_response=expected_response,
        query_string=query_string
    )

    api_instance = ResourceAssociationApi(get_api_client)
    actual_response = api_instance.get_resource_association(
        resource_type=resource_type_enum,
        channel=channel_enum,
        application_id="given-application-id",
        entity_id="given-entity-id",
        resource_id="given-resource-id",
    )

    expected_resource_associations_response = ResourceAssociationResponse(
        resource_type=resource_type_enum,
        channel=channel_enum,
        application_id=application_id,
        entity_id=entity_id,
        resource_id=resource_id
    )

    assert actual_response == expected_resource_associations_response


def to_query_string_without_escaping(query_params: dict):
    if not query_params:
        return ""
    return "&".join(["{}={}".format(paramName, paramValue) for (paramName, paramValue) in query_params.items()])


def setup_get_request(httpserver: HTTPServer, endpoint: str, expected_response: dict, query_string: str):
    httpserver.expect_request(
        uri=endpoint,
        method="GET",
        headers=expected_headers,
        query_string=query_string
    ).respond_with_json(status=200, response_json=expected_response)


def setup_post_request_created(httpserver: HTTPServer, endpoint: str, expected_request: dict):
    httpserver.expect_request(
        uri=endpoint,
        method="POST",
        headers=expected_headers,
        json=expected_request
    ).respond_with_json(status=201, response_json=None)


def setup_delete_request_no_content(httpserver: HTTPServer, endpoint: str, expected_request: dict):
    httpserver.expect_request(
        uri=endpoint,
        method="DELETE",
        headers=expected_headers,
        json=expected_request
    ).respond_with_json(status=204, response_json=None)


@pytest.fixture
def get_api_client():
    return ApiClient(Configuration(
        host="http://localhost:{}".format(port),
        api_key={"APIKeyHeader": api_key},
        api_key_prefix={"APIKeyHeader": "App"},
    ))


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return "localhost", port
