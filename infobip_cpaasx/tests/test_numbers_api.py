import pytest
from pytest_httpserver import HTTPServer

from infobip_cpaasx import ApiClient, Configuration, NumbersApi, \
    NumberResponse, NumbersEditPermissions, NumbersResponse, NumberPrice, NumbersVoiceSetup, \
    NumbersVoiceNumberMaskingActionDetails, NumbersPurchaseNumberRequest, NumbersForwardToIvrActionDetails

available_numbers_endpoint = "/numbers/1/numbers/available"
numbers_endpoint = "/numbers/1/numbers"
number_endpoint = "/numbers/1/numbers/{numberKey}"

api_key = "givenApiKey"
user_agent = "infobip-cpaasx-python-client/0.0.1"
expected_headers = {
    "Authorization": "App {}".format(api_key),
    "User-Agent": user_agent
}
port = 8088


def test_list_purchased_numbers(httpserver: HTTPServer, numbers_api_client):
    number_key = "6FED0BC540BFADD9B05ED7D89AAC22FA"
    number = "447860041117"
    country_code = "GB"
    country_name = "United Kingdom"
    number_type = "VIRTUAL_LONG_NUMBER"
    capability = "SMS"
    shared = False
    price_per_month = 5.0
    setup_price = 0.0
    initial_month_price = 5.0
    currency = "EUR"
    additional_setup_required = True
    can_edit_number = True
    can_edit_configuration = True
    application_id = "test-application-id"
    entity_id = "test-entity-id"
    first_keyword = "test"
    second_keyword = "stop"
    voice_setup_type = "VOICE_NUMBER_MASKING"
    voice_setup_description = "Voice number masking"
    voice_number_masking_config_key = "config-key"
    numbers_count = 1

    expected_response = {
        "numbers": [
            {
                "numberKey": number_key,
                "number": number,
                "country": country_code,
                "countryName": country_name,
                "type": number_type,
                "capabilities": [capability],
                "shared": shared,
                "price": {
                    "pricePerMonth": price_per_month,
                    "setupPrice": setup_price,
                    "initialMonthPrice": initial_month_price,
                    "currency": currency
                },
                "additionalSetupRequired": additional_setup_required,
                "editPermissions": {
                    "canEditNumber": can_edit_number,
                    "canEditConfiguration": can_edit_configuration
                },
                "applicationId": application_id,
                "entityId": entity_id,
                "keywords": [
                    first_keyword,
                    second_keyword
                ],
                "voiceSetup": {
                    "applicationId": application_id,
                    "entityId": entity_id,
                    "action": {
                        "type": voice_setup_type,
                        "description": voice_setup_description,
                        "voiceNumberMaskingConfigKey": voice_number_masking_config_key
                    }
                }
            }
        ],
        "numbersCount": numbers_count
    }

    limit = 1
    page = 0
    query_string = to_query_string_without_escaping({
        "limit": 1,
        "page": 0
    })

    setup_get_request(
        httpserver=httpserver,
        endpoint=numbers_endpoint,
        expected_response=expected_response,
        query_string=query_string
    )

    actual_response = numbers_api_client.list_purchased_numbers(limit=limit, page=page)

    expected_numbers_response = NumbersResponse(
        numbers=[
            NumberResponse(
                number_key=number_key,
                number=number,
                country=country_code,
                country_name=country_name,
                type=number_type,
                capabilities=[capability],
                shared=shared,
                price=NumberPrice(
                    price_per_month=price_per_month,
                    setup_price=setup_price,
                    initial_month_price=initial_month_price,
                    currency=currency
                ),
                additional_setup_required=additional_setup_required,
                edit_permissions=NumbersEditPermissions(
                    can_edit_number=can_edit_number,
                    can_edit_configuration=can_edit_configuration
                ),
                application_id=application_id,
                entity_id=entity_id,
                keywords=[first_keyword, second_keyword],
                voice_setup=NumbersVoiceSetup(
                    application_id=application_id,
                    entity_id=entity_id,
                    action=NumbersVoiceNumberMaskingActionDetails(
                        type=voice_setup_type,
                        description=voice_setup_description,
                        voice_number_masking_config_key=voice_number_masking_config_key
                    )
                )
            )
        ],
        numbers_count=numbers_count
    )

    assert actual_response == expected_numbers_response


def test_get_available_numbers(httpserver: HTTPServer, numbers_api_client):
    number_key = "6FED0BC540BFADD9B05ED7D89AAC22FA"
    number = "447860041117"
    country_code = "GB"
    country_name = "United Kingdom"
    number_type = "VIRTUAL_LONG_NUMBER"
    capability = "SMS"
    shared = False
    price_per_month = 5.0
    setup_price = 0.0
    initial_month_price = 5.0
    currency = "EUR"
    additional_setup_required = True
    can_edit_number = True
    can_edit_configuration = True
    application_id = "test-application-id"
    entity_id = "test-entity-id"
    numbers_count = 1

    expected_response = {
        "numbers": [
            {
                "numberKey": number_key,
                "number": number,
                "country": country_code,
                "countryName": country_name,
                "type": number_type,
                "capabilities": [capability],
                "shared": shared,
                "price": {
                    "pricePerMonth": price_per_month,
                    "setupPrice": setup_price,
                    "initialMonthPrice": initial_month_price,
                    "currency": currency
                },
                "additionalSetupRequired": additional_setup_required,
                "editPermissions": {
                    "canEditNumber": can_edit_number,
                    "canEditConfiguration": can_edit_configuration
                },
                "applicationId": application_id,
                "entityId": entity_id
            }
        ],
        "numbersCount": numbers_count
    }

    query_string = to_query_string_without_escaping({
        "capabilities": capability,
        "country": country_code,
        "number": number
    })

    setup_get_request(
        httpserver=httpserver,
        endpoint=available_numbers_endpoint,
        expected_response=expected_response,
        query_string=query_string
    )

    actual_response = numbers_api_client.get_available_numbers(
        capabilities=[capability],
        country=country_code,
        number=number
    )

    expected_numbers_response = NumbersResponse(
        numbers=[
            NumberResponse(
                number_key=number_key,
                number=number,
                country=country_code,
                country_name=country_name,
                type=number_type,
                capabilities=[capability],
                shared=shared,
                price=NumberPrice(
                    price_per_month=price_per_month,
                    setup_price=setup_price,
                    initial_month_price=initial_month_price,
                    currency=currency
                ),
                additional_setup_required=additional_setup_required,
                edit_permissions=NumbersEditPermissions(
                    can_edit_number=can_edit_number,
                    can_edit_configuration=can_edit_configuration
                ),
                application_id=application_id,
                entity_id=entity_id
            )
        ],
        numbers_count=numbers_count
    )

    assert actual_response == expected_numbers_response


def test_purchase_number(httpserver: HTTPServer, numbers_api_client):
    number_key = "6FED0BC540BFADD9B05ED7D89AAC22FA"
    number = "447860041117"
    country_code = "GB"
    country_name = "United Kingdom"
    number_type = "VIRTUAL_LONG_NUMBER"
    capability = "SMS"
    shared = False
    price_per_month = 5.0
    setup_price = 0.0
    initial_month_price = 5.0
    currency = "EUR"
    additional_setup_required = True
    can_edit_number = True
    can_edit_configuration = True
    application_id = "test-application-id"
    entity_id = "test-entity-id"

    expected_request = {
        "numberKey": number_key,
        "applicationId": application_id,
        "entityId": entity_id
    }

    expected_response = {
        "numberKey": number_key,
        "number": number,
        "country": country_code,
        "countryName": country_name,
        "type": number_type,
        "capabilities": [capability],
        "shared": shared,
        "price": {
            "pricePerMonth": price_per_month,
            "setupPrice": setup_price,
            "initialMonthPrice": initial_month_price,
            "currency": currency
        },
        "additionalSetupRequired": additional_setup_required,
        "editPermissions": {
            "canEditNumber": can_edit_number,
            "canEditConfiguration": can_edit_configuration
        },
        "applicationId": application_id,
        "entityId": entity_id
    }

    setup_post_request_ok(
        httpserver=httpserver,
        endpoint=numbers_endpoint,
        expected_request=expected_request,
        expected_response=expected_response
    )

    purchase_number_request = NumbersPurchaseNumberRequest(
        number_key=number_key,
        application_id=application_id,
        entity_id=entity_id
    )

    actual_response = numbers_api_client.purchase_number(purchase_number_request)

    expected_number_response = NumberResponse(
        number_key=number_key,
        number=number,
        country=country_code,
        country_name=country_name,
        type=number_type,
        capabilities=[capability],
        shared=shared,
        price=NumberPrice(
            price_per_month=price_per_month,
            setup_price=setup_price,
            initial_month_price=initial_month_price,
            currency=currency
        ),
        additional_setup_required=additional_setup_required,
        edit_permissions=NumbersEditPermissions(
            can_edit_number=can_edit_number,
            can_edit_configuration=can_edit_configuration
        ),
        application_id=application_id,
        entity_id=entity_id
    )

    assert actual_response == expected_number_response


def test_get_single_purchased_number(httpserver: HTTPServer, numbers_api_client):
    number_key = "6FED0BC540BFADD9B05ED7D89AAC22FA"
    number = "447860041117"
    country_code = "GB"
    country_name = "United Kingdom"
    number_type = "VIRTUAL_LONG_NUMBER"
    capability = "SMS"
    shared = False
    price_per_month = 5.0
    setup_price = 0.0
    initial_month_price = 5.0
    currency = "EUR"
    additional_setup_required = True
    can_edit_number = True
    can_edit_configuration = True
    application_id = "test-application-id"
    entity_id = "test-entity-id"
    first_keyword = "test"
    second_keyword = "stop"
    voice_setup_type = "FORWARD_TO_IVR"
    voice_setup_description = "Forward to IVR"
    scenario_key = "config-key"

    expected_response = {
        "numberKey": number_key,
        "number": number,
        "country": country_code,
        "countryName": country_name,
        "type": number_type,
        "capabilities": [capability],
        "shared": shared,
        "price": {
            "pricePerMonth": price_per_month,
            "setupPrice": setup_price,
            "initialMonthPrice": initial_month_price,
            "currency": currency
        },
        "additionalSetupRequired": additional_setup_required,
        "editPermissions": {
            "canEditNumber": can_edit_number,
            "canEditConfiguration": can_edit_configuration
        },
        "applicationId": application_id,
        "entityId": entity_id,
        "keywords": [
            first_keyword,
            second_keyword
        ],
        "voiceSetup": {
            "applicationId": application_id,
            "entityId": entity_id,
            "action": {
                "type": voice_setup_type,
                "description": voice_setup_description,
                "scenarioKey": scenario_key
            }
        }
    }

    setup_get_request(
        httpserver=httpserver,
        endpoint=number_endpoint.replace("{numberKey}", number_key),
        expected_response=expected_response
    )

    actual_response = numbers_api_client.get_single_purchased_number(number_key)

    expected_number_response = NumberResponse(
        number_key=number_key,
        number=number,
        country=country_code,
        country_name=country_name,
        type=number_type,
        capabilities=[capability],
        shared=shared,
        price=NumberPrice(
            price_per_month=price_per_month,
            setup_price=setup_price,
            initial_month_price=initial_month_price,
            currency=currency
        ),
        additional_setup_required=additional_setup_required,
        edit_permissions=NumbersEditPermissions(
            can_edit_number=can_edit_number,
            can_edit_configuration=can_edit_configuration
        ),
        application_id=application_id,
        entity_id=entity_id,
        keywords=[first_keyword, second_keyword],
        voice_setup=NumbersVoiceSetup(
            application_id=application_id,
            entity_id=entity_id,
            action=NumbersForwardToIvrActionDetails(
                type=voice_setup_type,
                description=voice_setup_description,
                scenario_key=scenario_key
            )
        )
    )

    assert actual_response == expected_number_response


def test_cancel_number(httpserver: HTTPServer, numbers_api_client):
    number_key = "6FED0BC540BFADD9B05ED7D89AAC22FA"

    setup_delete_request_no_content(
        httpserver=httpserver,
        endpoint=number_endpoint.replace("{numberKey}", number_key)
    )

    numbers_api_client.cancel_number(number_key)


def to_query_string_without_escaping(query_params: dict):
    if not query_params:
        return ""
    return "&".join(["{}={}".format(paramName, paramValue) for (paramName, paramValue) in query_params.items()])


def setup_get_request(httpserver: HTTPServer, endpoint: str, expected_response: dict, query_string: str = None):
    httpserver.expect_request(
        uri=endpoint,
        method="GET",
        headers=expected_headers,
        query_string=query_string
    ).respond_with_json(status=200, response_json=expected_response)


def setup_post_request_ok(httpserver: HTTPServer, endpoint: str, expected_request: dict, expected_response: dict):
    httpserver.expect_request(
        uri=endpoint,
        method="POST",
        headers={
            "Authorization": "App {}".format(api_key),
            "User-Agent": user_agent
        },
        json=expected_request
    ).respond_with_json(status=200, response_json=expected_response)


def setup_delete_request_no_content(httpserver: HTTPServer, endpoint: str):
    httpserver.expect_request(
        uri=endpoint,
        method="DELETE",
        headers=expected_headers
    ).respond_with_json(status=204, response_json=None)


@pytest.fixture
def numbers_api_client():
    return NumbersApi(ApiClient(Configuration(
        host="http://localhost:{}".format(port),
        api_key={"APIKeyHeader": api_key},
        api_key_prefix={"APIKeyHeader": "App"},
    )))


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return "localhost", port
