import pytest
from pytest_httpserver import HTTPServer

from infobip_cpaasx import ApiClient, Configuration, SmsDestination, \
    MmsApi, MmsAdvancedRequest, MmsAdvancedMessageSegmentText, \
    MmsAdvancedMessageSegmentLink, MmsSendResult, MmsAdvancedMessage, MmsAdvancedMessageSegment, MmsMessageResult, \
    MmsStatus

mms_advanced_endpoint = "/mms/1/advanced"
api_key = "given_api_key_value"
user_agent = "infobip-cpaasx-python-client/0.0.1"
port = 8088


def test_send_link_mms_with_application_and_entity(httpserver: HTTPServer, get_api_client):
    given_bulk_id = "2034072219640523072"
    given_to = "41793026727"
    given_message_id = "2250be2d4219-3af1-78856-aabe-1362af1edfd2"
    given_from = "InfoSMS"
    given_text = "This is a sample message"
    given_group_id = 1
    given_group_name = "PENDING"
    given_status_id = 26
    given_status_name = "MESSAGE_ACCEPTED"
    given_status_description = "Message sent to next instance"
    given_application_id = "given_application_id"
    given_entity_id = "given_entity_id"

    given_text_segment_content_id = "text_content_id"
    given_text_segment_text = "given_text_segment_text"
    given_link_segment_content_id = "link_content_id"
    given_link_segment_content_type = "image/jpeg"
    given_link_segment_content_url = "https://api.infobip.com/ott/1/media/infobipLogo"

    given_request = {
        "messages": [
            {
                "destinations": [
                    {
                        "to": given_to
                    }
                ],
                "from": given_from,
                "messageSegments": [
                    {
                        "contentId": given_text_segment_content_id,
                        "text": given_text_segment_text
                    },
                    {
                        "contentId": given_link_segment_content_id,
                        "contentType": given_link_segment_content_type,
                        "contentUrl": given_link_segment_content_url
                    }
                ],
                "applicationId": given_application_id,
                "entityId": given_entity_id
            }
        ]
    }

    expected_response = {
        "bulkId": given_bulk_id,
        "messages": [{
            "to": given_to,
            "status": {
                "groupId": given_group_id,
                "groupName": given_group_name,
                "id": given_status_id,
                "name": given_status_name,
                "description": given_status_description
            },
            "messageId": given_message_id
        }],
    }

    setup_request(
        httpserver=httpserver,
        endpoint=mms_advanced_endpoint,
        expected_request=given_request,
        expected_response=expected_response,
        http_verb="POST"
    )

    mms_advanced_request = MmsAdvancedRequest(
        messages=[
            MmsAdvancedMessage(
                destinations=[
                    SmsDestination(
                        to=given_to,
                    ),
                ],
                var_from=given_from,
                text=given_text,
                message_segments=[
                    MmsAdvancedMessageSegment(actual_instance=MmsAdvancedMessageSegmentText(
                        contentId=given_text_segment_content_id,
                        text=given_text_segment_text
                    )),
                    MmsAdvancedMessageSegment(actual_instance=MmsAdvancedMessageSegmentLink(
                        contentId=given_link_segment_content_id,
                        contentType=given_link_segment_content_type,
                        contentUrl=given_link_segment_content_url
                    ))
                ],
                application_id=given_application_id,
                entity_id=given_entity_id
            )
        ])

    api_instance = MmsApi(get_api_client)
    actual_response: MmsSendResult = api_instance.send_mms_message(mms_advanced_request=mms_advanced_request)

    expected_mms_send_result = MmsSendResult(
        bulk_id=given_bulk_id,
        messages=[
            MmsMessageResult(
                message_id=given_message_id,
                status=MmsStatus(
                    groupId=given_group_id,
                    groupName=given_group_name,
                    id=given_status_id,
                    name=given_status_name,
                    description=given_status_description,
                ),
                to=given_to
            )
        ]
    )

    assert actual_response == expected_mms_send_result


def setup_request(httpserver: HTTPServer, endpoint: str, expected_request: dict = None, expected_response: dict = None,
                  http_verb: str = "GET", query_string: str = None):
    httpserver.expect_request(uri=endpoint,
                              method=http_verb,
                              json=expected_request,
                              headers={
                                  "Authorization": "App {}".format(api_key),
                                  "User-Agent": user_agent
                              },
                              query_string=query_string).respond_with_json(expected_response)


@pytest.fixture
def get_api_client():
    return ApiClient(Configuration(
        host="http://localhost:{}".format(port),
        api_key=api_key,
        api_key_prefix="App"
    ))


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return "localhost", port
