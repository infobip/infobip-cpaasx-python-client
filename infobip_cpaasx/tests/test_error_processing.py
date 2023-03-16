import json

import pytest
from pytest_httpserver import HTTPServer

from infobip_cpaasx import ApiClient, Configuration, SmsAdvancedTextualRequest, SmsTextualMessage, SmsDestination, \
    SmsApi
from infobip_cpaasx.exceptions import ApiException, ForbiddenException, NotFoundException, UnauthorizedException, \
    ServiceException

sms_advanced_textual_endpoint = "/sms/2/text/advanced"
sms_advanced_binary_endpoint = "/sms/2/binary/advanced"
sms_preview_endpoint = "/sms/1/preview"
sms_bulks_endpoint = "/sms/1/bulks"
sms_bulks_status_endpoint = "/sms/1/bulks/status"
sms_outbound_reports_endpoint = "/sms/1/reports"
sms_outbound_logs_endpoint = "/sms/1/logs"
sms_inbound_messages_endpoint = "/sms/1/inbox/reports"

port = 8088


def error_response(message_id: str, text: str) -> dict:
    return {
        "requestError": {
            "serviceException": {
                "messageId": message_id,
                "text": text
            }
        }
    }


def error_response_with_validation_errors(message_id: str, text: str, validation_errors: dict) -> dict:
    return {
        "requestError": {
            "serviceException": {
                "messageId": message_id,
                "text": text,
                "validationErrors": validation_errors
            }
        }
    }


@pytest.mark.parametrize(
    ["status_code", "error_response_json", "exception_type"],
    [
        (401, error_response("UNAUTHORIZED", "Invalid login details"), UnauthorizedException),
        (403, error_response("UNAUTHORIZED", "Unauthorized access"), ForbiddenException),
        (404, error_response("NOT_FOUND", "Requested resource not found"), NotFoundException),
        (429, error_response("TOO_MANY_REQUESTS", "Too many requests"), ApiException),
        (500, error_response("GENERAL_ERROR", "Something went wrong. Please contact support."), ServiceException),
        (400, error_response_with_validation_errors("BAD_REQUEST", "Bad Request", {"messages[0].destinations": ["must not be empty"]}), ApiException),
    ]
)
def test_error_processing(
        httpserver: HTTPServer,
        sms_api_client: SmsApi,
        status_code: int,
        error_response_json: dict,
        exception_type: type
):
    httpserver.expect_request(
        uri="/sms/2/text/advanced",
        method="POST",
    ).respond_with_json(status=status_code, response_json=error_response_json)

    sms_advanced_textual_request = SmsAdvancedTextualRequest(
        messages=[
            SmsTextualMessage(
                destinations=[SmsDestination(to="41793026727")],
                var_from="InfoSMS",
                text="This is a sample message"
            )
        ])

    with pytest.raises(ApiException) as exception:
        sms_api_client.send_sms_message(sms_advanced_textual_request=sms_advanced_textual_request)

    assert exception.type == exception_type
    assert exception.value.body == json.dumps(error_response_json, indent=4)
    assert exception.value.status == status_code


@pytest.fixture
def sms_api_client():
    return SmsApi(ApiClient(Configuration(
        host="http://localhost:{}".format(port),
        api_key="givenApiKeyValue",
        api_key_prefix="App"
    )))


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return "localhost", port
