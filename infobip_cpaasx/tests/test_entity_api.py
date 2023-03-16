import pytest
from pytest_httpserver import HTTPServer

from infobip_cpaasx import ApiClient, Configuration, EntityApi, PageEntity, Entity, PageInfo, ModifyEntity

entities_endpoint = "/provisioning/1/entities"
entity_endpoint = "/provisioning/1/entities/{entityId}"

api_key = "givenApiKey"
user_agent = "infobip-api-client-python/0.0.2-cpaasx"
port = 8088


def test_get_entities(httpserver: HTTPServer, get_api_client):
    entity_name = "Test entity"
    entity_id = "test-entity"
    another_entity_name = "Another test entity"
    another_entity_id = "another-test-entity"

    expected_response = {
        "results": [
            {
                "entityName": entity_name,
                "entityId": entity_id
            },
            {
                "entityName": another_entity_name,
                "entityId": another_entity_id
            }
        ],
        "paging": {
            "page": 0,
            "size": 2,
            "totalPages": 1,
            "totalResults": 2
        }
    }

    setup_get_request(
        httpserver=httpserver,
        endpoint=entities_endpoint,
        expected_response=expected_response,
    )

    api_instance = EntityApi(get_api_client)
    actual_response = api_instance.get_entities()

    expected_entities_response = PageEntity(
        results=[
            Entity(entity_name=entity_name, entity_id=entity_id),
            Entity(entity_name=another_entity_name, entity_id=another_entity_id),
        ],
        paging=PageInfo(
            page=0,
            size=2,
            totalPages=1,
            totalResults=2
        )
    )

    assert actual_response == expected_entities_response


def test_get_entity(httpserver: HTTPServer, get_api_client):
    entity_name = "Test entity"
    entity_id = "test-entity"

    expected_response = {
        "entityName": entity_name,
        "entityId": entity_id
    }

    setup_get_request(
        httpserver=httpserver,
        endpoint=entity_endpoint.replace("{entityId}", entity_id),
        expected_response=expected_response,
    )

    api_instance = EntityApi(get_api_client)
    actual_response = api_instance.get_entity(entity_id=entity_id)

    expected_entity_response = Entity(entity_name=entity_name, entity_id=entity_id)

    assert actual_response == expected_entity_response


def test_create_entity(httpserver: HTTPServer, get_api_client):
    entity_name = "Test entity"
    entity_id = "test-entity"

    expected_request = {
        "entityName": entity_name,
        "entityId": entity_id
    }

    setup_post_request_created(
        httpserver=httpserver,
        endpoint=entities_endpoint,
        expected_request=expected_request
    )

    entity = Entity(entity_name=entity_name, entity_id=entity_id)

    api_instance = EntityApi(get_api_client)
    api_instance.create_entity(entity=entity)


def test_modify_entity(httpserver: HTTPServer, get_api_client):
    entity_name = "Modified entity"
    entity_id = "test-entity"

    expected_request = {
        "entityName": entity_name,
    }

    setup_put_request_no_content(
        httpserver=httpserver,
        endpoint=entity_endpoint.replace("{entityId}", entity_id),
        expected_request=expected_request
    )

    entity = ModifyEntity(entity_name=entity_name)

    api_instance = EntityApi(get_api_client)
    api_instance.modify_entity(modify_entity=entity, entity_id=entity_id)


def setup_get_request(httpserver: HTTPServer, endpoint: str, expected_response: dict):
    httpserver.expect_request(
        uri=endpoint,
        method="GET",
        headers={
            "Authorization": "App {}".format(api_key),
            "User-Agent": user_agent
        },
    ).respond_with_json(status=200, response_json=expected_response)


def setup_post_request_created(httpserver: HTTPServer, endpoint: str, expected_request: dict):
    httpserver.expect_request(
        uri=endpoint,
        method="POST",
        headers={
            "Authorization": "App {}".format(api_key),
            "User-Agent": user_agent
        },
        json=expected_request
    ).respond_with_json(status=201, response_json=None)


def setup_put_request_no_content(httpserver: HTTPServer, endpoint: str, expected_request: dict):
    httpserver.expect_request(
        uri=endpoint,
        method="PUT",
        headers={
            "Authorization": "App {}".format(api_key),
            "User-Agent": user_agent
        },
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
