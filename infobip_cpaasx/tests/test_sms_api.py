import datetime

import pytest
from dateutil.tz import tzoffset
from pytest_httpserver import HTTPServer

from infobip_cpaasx import ApiClient, Configuration, SmsAdvancedTextualRequest, SmsTextualMessage, SmsDestination, \
    SmsApi, SmsResponse, SmsResponseDetails, SmsStatus, SmsBulkResponse, SmsBulkStatusResponse, SmsBulkStatus, \
    SmsBulkRequest, SmsUpdateStatusRequest, SmsDeliveryResult, SmsWebhookInboundReportResponse, \
    SmsWebhookOutboundReportResponse

sms_advanced_endpoint = "/sms/2/text/advanced"
sms_bulks_endpoint = "/sms/1/bulks"
sms_bulks_status_endpoint = "/sms/1/bulks/status"

api_key = "givenApiKeyValue"
user_agent = "infobip-cpaasx-python-client/0.0.1"
expected_headers = {
    "Authorization": "App {}".format(api_key),
    "User-Agent": user_agent
}
port = 8088


def test_send_basic_sms_with_application_and_entity(httpserver: HTTPServer, sms_api_client):
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

    given_request = {
        "messages": [
            {
                "destinations": [
                    {
                        "to": given_to
                    }
                ],
                "flash": False,
                "text": given_text,
                "from": given_from,
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

    setup_post_request_ok(
        httpserver=httpserver,
        endpoint=sms_advanced_endpoint,
        expected_request=given_request,
        expected_response=expected_response
    )

    sms_advanced_textual_request = SmsAdvancedTextualRequest(
        messages=[
            SmsTextualMessage(
                destinations=[
                    SmsDestination(
                        to=given_to,
                    ),
                ],
                var_from=given_from,
                text=given_text,
                application_id=given_application_id,
                entity_id=given_entity_id
            )
        ])

    actual_response: SmsResponse = sms_api_client.send_sms_message(
        sms_advanced_textual_request=sms_advanced_textual_request)

    expected_sms_response = SmsResponse(
        bulk_id=given_bulk_id,
        messages=[
            SmsResponseDetails(
                message_id=given_message_id,
                status=SmsStatus(
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

    assert actual_response == expected_sms_response


def test_get_scheduled_sms_messages(httpserver: HTTPServer, sms_api_client):
    given_bulk_id = "BULK-ID-123-xyz"
    given_send_at_message = "2023-03-08T17:42:05.390+0100"

    expected_response = {
        "bulkId": given_bulk_id,
        "sendAt": given_send_at_message
    }

    query_string = to_query_string_without_escaping({"bulkId": given_bulk_id})

    setup_get_request(
        httpserver=httpserver,
        endpoint=sms_bulks_endpoint,
        expected_response=expected_response,
        query_string=query_string
    )

    actual_response: SmsBulkResponse = sms_api_client.get_scheduled_sms_messages(bulk_id=given_bulk_id)

    expected_sms_bulk_response = SmsBulkResponse(
        bulk_id=given_bulk_id,
        send_at=datetime.datetime(2023, 3, 8, 17, 42, 5, 390000, tzinfo=tzoffset(None, 3600))
    )

    assert actual_response == expected_sms_bulk_response


def test_reschedule_sms_messages(httpserver: HTTPServer, sms_api_client):
    given_bulk_id = "BULK-ID-123-xyz"
    given_send_at_message_request = "2023-03-08T17:42:05.390000+01:00"
    given_send_at_message_response = "2023-03-08T17:42:05.390+0100"
    given_send_at_message_datetime = datetime.datetime(2023, 3, 8, 17, 42, 5, 390000, tzinfo=tzoffset(None, 3600))

    expected_request = {
        "sendAt": given_send_at_message_request
    }

    expected_response = {
        "bulkId": given_bulk_id,
        "sendAt": given_send_at_message_response
    }

    query_string = to_query_string_without_escaping({"bulkId": given_bulk_id})

    setup_put_request_ok(
        httpserver=httpserver,
        endpoint=sms_bulks_endpoint,
        expected_request=expected_request,
        expected_response=expected_response,
        query_string=query_string
    )

    sms_bulk_request = SmsBulkRequest(
        send_at=given_send_at_message_datetime
    )

    actual_response: SmsBulkResponse = sms_api_client.reschedule_sms_messages(
        bulk_id=given_bulk_id,
        sms_bulk_request=sms_bulk_request
    )

    expected_sms_bulk_response = SmsBulkResponse(
        bulk_id=given_bulk_id,
        send_at=given_send_at_message_datetime
    )

    assert actual_response == expected_sms_bulk_response


def test_get_scheduled_sms_messages_status(httpserver: HTTPServer, sms_api_client):
    given_bulk_id = "BULK-ID-123-xyz"
    given_status = "PAUSED"

    expected_response = {
        "bulkId": given_bulk_id,
        "status": given_status
    }

    query_string = to_query_string_without_escaping({"bulkId": given_bulk_id})

    setup_get_request(
        httpserver=httpserver,
        endpoint=sms_bulks_status_endpoint,
        expected_response=expected_response,
        query_string=query_string
    )

    actual_response: SmsBulkStatusResponse = sms_api_client.get_scheduled_sms_messages_status(bulk_id=given_bulk_id)

    expected_sms_bulk_status_response = SmsBulkStatusResponse(
        bulk_id=given_bulk_id,
        status=SmsBulkStatus.PAUSED
    )

    assert actual_response == expected_sms_bulk_status_response


def test_update_scheduled_sms_messages_status(httpserver: HTTPServer, sms_api_client):
    given_bulk_id = "BULK-ID-123-xyz"
    given_status = "CANCELED"

    expected_request = {
        "status": given_status
    }

    expected_response = {
        "bulkId": given_bulk_id,
        "status": given_status
    }

    query_string = to_query_string_without_escaping({"bulkId": given_bulk_id})

    setup_put_request_ok(
        httpserver=httpserver,
        endpoint=sms_bulks_status_endpoint,
        expected_request=expected_request,
        expected_response=expected_response,
        query_string=query_string
    )

    sms_update_status_request = SmsUpdateStatusRequest(
        status=SmsBulkStatus.CANCELED
    )

    actual_response: SmsBulkStatusResponse = sms_api_client.update_scheduled_sms_messages_status(
        bulk_id=given_bulk_id,
        sms_update_status_request=sms_update_status_request
    )

    expected_sms_bulk_response = SmsBulkStatusResponse(
        bulk_id=given_bulk_id,
        status=SmsBulkStatus.CANCELED
    )

    assert actual_response == expected_sms_bulk_response


def test_delivery_results():
    delivery_result_payload = """
    {
        "results": [
        {
            "bulkId": "BULK-ID-123-xyz",
            "messageId": "MESSAGE-ID-123-xyz",
            "to": "41793026727",
            "sentAt": "2019-11-09T16:00:00.000+0000",
            "doneAt": "2019-11-09T16:00:00.000+0000",
            "smsCount": 1,
            "price": {
                "pricePerMessage": 0.01,
                "currency": "EUR"
            },
            "status": {
                "groupId": 3,
                "groupName": "DELIVERED",
                "id": 5,
                "name": "DELIVERED_TO_HANDSET",
                "description": "Message delivered to handset"
            },
            "error": {
                "groupId": 0,
                "groupName": "Ok",
                "id": 0,
                "name": "NO_ERROR",
                "description": "No Error",
                "permanent": false
            }
        }
        ]
    }
    """

    delivery_results = SmsDeliveryResult.from_json(delivery_result_payload)

    results = delivery_results.results

    assert len(results) == 1

    assert results[0].bulk_id == 'BULK-ID-123-xyz'
    assert results[0].message_id == 'MESSAGE-ID-123-xyz'
    assert results[0].to == '41793026727'
    assert results[0].sms_count == 1
    assert results[0].price.price_per_message == 0.01
    assert results[0].price.currency == 'EUR'
    assert results[0].status.group_id == 3
    assert results[0].status.group_name == 'DELIVERED'
    assert results[0].status.group_name == 'DELIVERED'
    assert results[0].status.id == 5
    assert results[0].status.name == 'DELIVERED_TO_HANDSET'
    assert results[0].status.description == 'Message delivered to handset'

    assert results[0].error.group_id == 0
    assert results[0].error.group_name == 'Ok'
    assert results[0].error.id == 0
    assert results[0].error.name == 'NO_ERROR'
    assert results[0].error.description == 'No Error'
    assert results[0].error.permanent is False


def test_inbound_reports():
    inbound_report_payload = """
    {
        "results": [
        {
            "messageId": "817790313235066447",
            "from": "385916242493",
            "to": "385921004026",
            "text": "QUIZ Correct answer is Paris",
            "cleanText": "Correct answer is Paris",
            "keyword": "QUIZ",
            "receivedAt": "2016-10-06T09:28:39.220+0000",
            "smsCount": 1,
            "price": {
                "pricePerMessage": 0.00,
                "currency": "EUR"
            },
            "callbackData": "callbackData"
        }
        ],
        "messageCount": 1,
        "pendingMessageCount": 0
    }
    """

    inbound_report_results = SmsWebhookInboundReportResponse.from_json(inbound_report_payload)

    results = inbound_report_results.results

    assert len(results) == 1

    assert inbound_report_results.message_count == 1
    assert inbound_report_results.pending_message_count == 0

    assert results[0].message_id == '817790313235066447'
    assert results[0].var_from == '385916242493'
    assert results[0].to == '385921004026'
    assert results[0].text == 'QUIZ Correct answer is Paris'
    assert results[0].clean_text == 'Correct answer is Paris'
    assert results[0].keyword == 'QUIZ'
    assert results[0].sms_count == 1
    assert results[0].price.price_per_message == 0.00
    assert results[0].price.currency == 'EUR'
    assert results[0].callback_data == 'callbackData'


def test_outbound_reports():
    outbound_report_payload = """
    {
        "results": [
        {
            "bulkId": "BULK-ID-123-xyz",
            "messageId": "MESSAGE-ID-123-xyz",
            "to": "41793026727",
            "sentAt": "2019-11-09T16:00:00.000+0000",
            "doneAt": "2019-11-09T16:00:00.000+0000",
            "smsCount": 1,
            "price": {
                "pricePerMessage": 0.01,
                "currency": "EUR"
            },
            "status": {
                "groupId": 3,
                "groupName": "DELIVERED",
                "id": 5,
                "name": "DELIVERED_TO_HANDSET",
                "description": "Message delivered to handset"
            },
            "error": {
                "groupId": 0,
                "groupName": "Ok",
                "id": 0,
                "name": "NO_ERROR",
                "description": "No Error",
                "permanent": false
            }
        }
        ]
    }
    """

    outbound_report_results = SmsWebhookOutboundReportResponse.from_json(outbound_report_payload)

    results = outbound_report_results.results

    assert len(results) == 1

    assert results[0].bulk_id == 'BULK-ID-123-xyz'
    assert results[0].message_id == 'MESSAGE-ID-123-xyz'
    assert results[0].to == '41793026727'
    assert results[0].sms_count == 1
    assert results[0].price.price_per_message == 0.01
    assert results[0].price.currency == 'EUR'
    assert results[0].status.group_id == 3
    assert results[0].status.group_name == 'DELIVERED'
    assert results[0].status.group_name == 'DELIVERED'
    assert results[0].status.id == 5
    assert results[0].status.name == 'DELIVERED_TO_HANDSET'
    assert results[0].status.description == 'Message delivered to handset'

    assert results[0].error.group_id == 0
    assert results[0].error.group_name == 'Ok'
    assert results[0].error.id == 0
    assert results[0].error.name == 'NO_ERROR'
    assert results[0].error.description == 'No Error'
    assert results[0].error.permanent is False


def to_query_string_without_escaping(query_params: dict):
    if not query_params:
        return ""
    return "&".join(["{}={}".format(paramName, paramValue) for (paramName, paramValue) in query_params.items()])


def setup_post_request_ok(httpserver: HTTPServer, endpoint: str, expected_request: dict = None,
                          expected_response: dict = None):
    httpserver.expect_request(
        uri=endpoint,
        method="POST",
        json=expected_request,
        headers=expected_headers) \
        .respond_with_json(expected_response)


def setup_get_request(httpserver: HTTPServer, endpoint: str, expected_response: dict, query_string: str = None):
    httpserver.expect_request(
        uri=endpoint,
        method="GET",
        headers=expected_headers,
        query_string=query_string
    ).respond_with_json(status=200, response_json=expected_response)


def setup_put_request_ok(
        httpserver: HTTPServer,
        endpoint: str,
        expected_request: dict,
        expected_response: dict,
        query_string: str
):
    httpserver.expect_request(
        uri=endpoint,
        method="PUT",
        headers=expected_headers,
        json=expected_request,
        query_string=query_string
    ).respond_with_json(status=200, response_json=expected_response)


@pytest.fixture
def sms_api_client():
    return SmsApi(ApiClient(Configuration(
        host="http://localhost:{}".format(port),
        api_key=api_key,
        api_key_prefix="App"
    )))


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return "localhost", port
