import pytest
from pytest_httpserver import HTTPServer

from infobip_cpaasx import ApiClient, Configuration, PageInfo, ApplicationApi, PageApplication, Application, \
    ModifyApplication

applications_endpoint = "/provisioning/1/applications"
application_endpoint = "/provisioning/1/applications/{applicationId}"

api_key = "givenApiKey"
user_agent = "infobip-cpaasx-python-client/0.0.1"
port = 8088


def test_get_applications(httpserver: HTTPServer, get_api_client):
    application_name = "Test application"
    application_id = "test-application"
    another_application_name = "Another test application"
    another_application_id = "another-test-application"

    expected_response = {
        "results": [
            {
                "applicationName": application_name,
                "applicationId": application_id
            },
            {
                "applicationName": another_application_name,
                "applicationId": another_application_id
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
        endpoint=applications_endpoint,
        expected_response=expected_response,
    )

    api_instance = ApplicationApi(get_api_client)
    actual_response = api_instance.get_applications()

    expected_applications_response = PageApplication(
        results=[
            Application(application_name=application_name, application_id=application_id),
            Application(application_name=another_application_name, application_id=another_application_id),
        ],
        paging=PageInfo(
            page=0,
            size=2,
            totalPages=1,
            totalResults=2
        )
    )

    assert actual_response == expected_applications_response


def test_get_application(httpserver: HTTPServer, get_api_client):
    application_name = "Test application"
    application_id = "test-application"

    expected_response = {
        "applicationName": application_name,
        "applicationId": application_id
    }

    setup_get_request(
        httpserver=httpserver,
        endpoint=application_endpoint.replace("{applicationId}", application_id),
        expected_response=expected_response,
    )

    api_instance = ApplicationApi(get_api_client)
    actual_response = api_instance.get_application(application_id=application_id)

    expected_application_response = Application(application_name=application_name, application_id=application_id)

    assert actual_response == expected_application_response


def test_create_application(httpserver: HTTPServer, get_api_client):
    application_name = "Test application"
    application_id = "test-application"

    expected_request = {
        "applicationName": application_name,
        "applicationId": application_id
    }

    setup_post_request_created(
        httpserver=httpserver,
        endpoint=applications_endpoint,
        expected_request=expected_request
    )

    application = Application(application_name=application_name, application_id=application_id)

    api_instance = ApplicationApi(get_api_client)
    api_instance.create_application(application=application)


def test_modify_application(httpserver: HTTPServer, get_api_client):
    application_name = "Modified application"
    application_id = "test-application"

    expected_request = {
        "applicationName": application_name,
    }

    setup_put_request_no_content(
        httpserver=httpserver,
        endpoint=application_endpoint.replace("{applicationId}", application_id),
        expected_request=expected_request
    )

    application = ModifyApplication(application_name=application_name)

    api_instance = ApplicationApi(get_api_client)
    api_instance.modify_application(modify_application=application, application_id=application_id)


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
