import datetime
from typing import Union, List

import pytest
from pytest_httpserver import HTTPServer

from infobip_cpaasx import ApiClient, Configuration, NumberRegistrationApi, PageInfo, \
    NumberRegistrationPageResponseCampaign, NumberRegistrationTenDlcCampaign, NumberRegistrationNetworkStatus, \
    NumberRegistrationOptIns, NumberRegistrationKeywordOptIn, NumberRegistrationBrandPreview, \
    NumberRegistrationNumberPreview, NumberRegistrationExternalTenDlcCampaign, NumberRegistrationUpdateCampaignRequest, \
    NumberRegistrationPageResponseBrand, NumberRegistrationAddress, NumberRegistrationPageInfo, \
    NumberRegistrationBrandStatus, NumberRegistrationUpdateBrandRequest, NumberRegistrationNonProfitBrand, \
    NumberRegistrationBusinessIdentifier, NumberRegistrationPageResponseBrandVet, NumberRegistrationBrandVet

from infobip_cpaasx.models.number_registration_document_metadata import NumberRegistrationDocumentMetadata

api_key = "givenApiKey"
user_agent = "infobip-api-client-python/0.0.2-cpaasx"
expected_headers = {
    "Authorization": "App {}".format(api_key),
    "User-Agent": user_agent
}
port = 8088

# brand management
brands = "/number-registration/1/brands"
brand = "/number-registration/1/brands/{brandId}"
brand_register = "/number-registration/1/brands/{brandId}/register"
brand_update_registration = "/number-registration/1/brands/{brandId}/update-registration"
brand_registrar_statuses = "/number-registration/1/brands/{brandId}/registrar-statuses"

# brand vetting
brand_vets = "/number-registration/1/brands/{brandId}/vets"
brand_vet = "/number-registration/1/brands/{brandId}/vets/{vetId}"

# campaigns
campaigns = "/number-registration/1/campaigns"
campaign = "/number-registration/1/campaigns/{campaignId}"
campaign_register = "/number-registration/1/campaigns/{campaignId}/register"
campaign_network_statuses = "/number-registration/1/campaigns/{campaignId}/network-statuses"
campaign_deregister = "/number-registration/1/campaigns/{campaignId}/deregister"
campaign_update_registration = "/number-registration/1/campaigns/{campaignId}/update-registration"


# brand management

def test_get_brands(httpserver: HTTPServer, number_registration_api_instance):
    id = "123"

    reference_id = "customer-defined-identifier"
    var_type = "TENDLC_NON_PROFIT"
    address_city = "Seattle"
    address_state = "WA"
    address_street = "56486 915th Street"
    address_zip_code = "98061"
    legal_name = "Examples In Need"
    country_code = "US"
    name = "Examples In Need"
    support_phone = "18886679878"
    support_email = "exampl@example.com"
    vertical = "NON_PROFIT_ORGANIZATION"
    website = "https://www.example.com"
    tax_id = "62-4161762"
    business_id = "590900O3Z29E78HVXT56"
    business_type = "LEI"
    created_date = "2021-01-19T16:17:14Z"
    last_modified_date = "2021-01-19T16:17:14Z"

    page = 0
    page_size = 20
    total_pages = 1
    total_results = 1

    expected_response = {
        "results": [
            {
                "id": id,
                "referenceId": reference_id,
                "type": var_type,
                "address": {
                    "city": address_city,
                    "state": address_state,
                    "street": address_street,
                    "zipCode": address_zip_code
                },
                "alternateBusinessId": {
                    "id": business_id,
                    "type": business_type
                },
                "countryCode": country_code,
                "createdDate": created_date,
                "supportEmail": support_email,
                "lastModifiedDate": last_modified_date,
                "legalName": legal_name,
                "name": name,
                "supportPhone": support_phone,
                "vertical": vertical,
                "website": website,
                "taxId": tax_id
            }
        ],
        "paging": {
            "page": page,
            "size": page_size,
            "totalPages": total_pages,
            "totalResults": total_results
        }
    }

    setup_success_get_request(
        httpserver=httpserver,
        endpoint=brands,
        expected_response=expected_response,
        query_string=""
    )

    number_registration_brand = NumberRegistrationNonProfitBrand(
        id=id,
        reference_id=reference_id,
        type=var_type,
        address=NumberRegistrationAddress(
            city=address_city,
            state=address_state,
            street=address_street,
            zip_code=address_zip_code
        ),
        alternate_business_id=NumberRegistrationBusinessIdentifier(
            id=business_id,
            type=business_type
        ),
        country_code=country_code,
        created_date=created_date,
        support_email=support_email,
        last_modified_date=last_modified_date,
        legal_name=legal_name,
        name=name,
        support_phone=support_phone,
        vertical=vertical,
        website=website,
        tax_id=tax_id
    )

    expected_brand_response = NumberRegistrationPageResponseBrand(
        results=[
            number_registration_brand
        ],
        paging=NumberRegistrationPageInfo(
            page=page,
            size=page_size,
            total_pages=total_pages,
            total_results=total_results
        )
    )

    actual_response: NumberRegistrationPageResponseBrand = number_registration_api_instance.get_brands()

    assert actual_response == expected_brand_response


def test_create_brand(httpserver: HTTPServer, number_registration_api_instance):
    id = "79ff0424-7201-45ca-bcbe-9989535fa2ec"

    reference_id = "customer-defined-identifier"
    type = "TENDLC_NON_PROFIT"
    address_city = "Seattle"
    address_state = "WA"
    address_street = "56486 915th Street"
    address_zip_code = "98061"
    legal_name = "Examples In Need"
    country_code = "US"
    name = "Examples In Need"
    support_phone = "18886679878"
    support_email = "exampl@example.com"
    vertical = "NON_PROFIT_ORGANIZATION"
    website = "https://www.example.com"
    tax_id = "62-4161762"
    business_id = "590900O3Z29E78HVXT56"
    business_type = "LEI"
    created_date = "2021-01-19T16:17:14Z"
    last_modified_date = "2021-01-19T16:17:14Z"

    expected_request = {
        "referenceId": reference_id,
        "type": type,
        "address": {
            "city": address_city,
            "state": address_state,
            "street": address_street,
            "zipCode": address_zip_code
        },
        "alternateBusinessId": {
            "id": business_id,
            "type": business_type
        },
        "countryCode": country_code,
        "supportEmail": support_email,
        "legalName": legal_name,
        "name": name,
        "supportPhone": support_phone,
        "vertical": vertical,
        "website": website,
        "taxId": tax_id
    }

    expected_response = {
        "id": id,
        "referenceId": reference_id,
        "type": type,
        "address": {
            "city": address_city,
            "state": address_state,
            "street": address_street,
            "zipCode": address_zip_code
        },
        "alternateBusinessId": {
            "id": business_id,
            "type": business_type
        },
        "countryCode": country_code,
        "createdDate": created_date,
        "supportEmail": support_email,
        "lastModifiedDate": last_modified_date,
        "legalName": legal_name,
        "name": name,
        "supportPhone": support_phone,
        "vertical": vertical,
        "website": website,
        "taxId": tax_id
    }

    setup_created_post_request(
        httpserver=httpserver,
        endpoint=brands,
        expected_request=expected_request,
        expected_response=expected_response
    )

    number_registration_brand = NumberRegistrationNonProfitBrand(
        reference_id=reference_id,
        type=type,
        address=NumberRegistrationAddress(
            city=address_city, state=address_state, street=address_street,
            zip_code=address_zip_code
        ),
        alternate_business_id=NumberRegistrationBusinessIdentifier(id=business_id, type=business_type),
        country_code=country_code,
        support_email=support_email,
        legal_name=legal_name,
        name=name,
        support_phone=support_phone,
        vertical=vertical,
        website=website,
        tax_id=tax_id
    )

    actual_response = number_registration_api_instance.create_brand(
        number_registration_brand=number_registration_brand
    )

    expected_brand_response = NumberRegistrationNonProfitBrand(
        id=id,
        reference_id=reference_id,
        type=type,
        address=NumberRegistrationAddress(
            city=address_city, state=address_state, street=address_street,
            zip_code=address_zip_code
        ),
        alternate_business_id=NumberRegistrationBusinessIdentifier(id=business_id, type=business_type),
        country_code=country_code,
        created_date="2021-01-19T16:17:14Z",
        support_email=support_email,
        last_modified_date="2021-01-19T16:17:14Z",
        legal_name=legal_name,
        name=name,
        support_phone=support_phone,
        vertical=vertical,
        website=website,
        tax_id=tax_id
    )

    assert actual_response == expected_brand_response


def test_get_brand(httpserver: HTTPServer, number_registration_api_instance):
    id = "79ff0424-7201-45ca-bcbe-9989535fa2ec"

    reference_id = "customer-defined-identifier"
    type = "TENDLC_NON_PROFIT"
    address_city = "Seattle"
    address_state = "WA"
    address_street = "56486 915th Street"
    address_zip_code = "98061"
    legal_name = "Examples In Need"
    country_code = "US"
    name = "Examples In Need"
    support_phone = "18886679878"
    support_email = "exampl@example.com"
    vertical = "NON_PROFIT_ORGANIZATION"
    website = "https://www.example.com"
    tax_id = "62-4161762"
    business_id = "590900O3Z29E78HVXT56"
    business_type = "LEI"

    expected_response = {
        "id": id,
        "referenceId": reference_id,
        "type": type,
        "address": {
            "city": address_city,
            "state": address_state,
            "street": address_street,
            "zipCode": address_zip_code
        },
        "alternateBusinessId": {
            "id": business_id,
            "type": business_type
        },
        "countryCode": country_code,
        "createdDate": "2021-01-19T16:17:14Z",
        "supportEmail": support_email,
        "lastModifiedDate": "2021-01-19T16:17:14Z",
        "legalName": legal_name,
        "name": name,
        "supportPhone": support_phone,
        "vertical": vertical,
        "website": website,
        "taxId": tax_id
    }

    setup_success_get_request(
        httpserver=httpserver,
        endpoint=brand.replace("{brandId}", id),
        expected_response=expected_response
    )

    actual_response: NumberRegistrationNonProfitBrand = number_registration_api_instance.get_brand(brand_id=id)

    expected_brand_response = NumberRegistrationNonProfitBrand(
        id=id,
        reference_id=reference_id,
        type=type,
        address=NumberRegistrationAddress(
            city=address_city, state=address_state, street=address_street,
            zip_code=address_zip_code
        ),
        alternate_business_id=NumberRegistrationBusinessIdentifier(id=business_id, type=business_type),
        country_code=country_code,
        created_date="2021-01-19T16:17:14Z",
        support_email=support_email,
        last_modified_date="2021-01-19T16:17:14Z",
        legal_name=legal_name,
        name=name,
        support_phone=support_phone,
        vertical=vertical,
        website=website,
        tax_id=tax_id
    )

    assert expected_brand_response == actual_response


def test_update_brand(httpserver: HTTPServer, number_registration_api_instance):
    id = "79ff0424-7201-45ca-bcbe-9989535fa2ec"

    reference_id = "customer-defined-identifier"
    var_type = "TENDLC_NON_PROFIT"
    address_city = "Seattle"
    address_state = "WA"
    address_street = "56486 915th Street"
    address_zip_code = "98061"
    legal_name = "Examples In Need"
    country_code = "US"
    name = "Examples In Need"
    support_phone = "18886679878"
    support_email = "exampl@example.com"
    vertical = "NON_PROFIT_ORGANIZATION"
    website = "https://www.example.com"
    tax_id = "62-4161762"
    business_id = "590900O3Z29E78HVXT56"
    business_type = "LEI"
    created_date = "2021-01-19T16:17:14Z"
    last_modified_date = "2021-01-19T16:17:14Z"

    expected_request = {
        "referenceId": reference_id,
        "type": var_type,
        "address": {
            "city": address_city,
            "state": address_state,
            "street": address_street,
            "zipCode": address_zip_code
        },
        "alternateBusinessId": {
            "id": business_id,
            "type": business_type
        },
        "countryCode": country_code,
        "supportEmail": support_email,
        "legalName": legal_name,
        "name": name,
        "supportPhone": support_phone,
        "vertical": vertical,
        "website": website,
        "taxId": tax_id
    }

    expected_response = {
        "id": id,
        "referenceId": reference_id,
        "type": var_type,
        "address": {
            "city": address_city,
            "state": address_state,
            "street": address_street,
            "zipCode": address_zip_code
        },
        "alternateBusinessId": {
            "id": business_id,
            "type": business_type
        },
        "countryCode": country_code,
        "createdDate": created_date,
        "supportEmail": support_email,
        "lastModifiedDate": last_modified_date,
        "legalName": legal_name,
        "name": name,
        "supportPhone": support_phone,
        "vertical": vertical,
        "website": website,
        "taxId": tax_id
    }

    setup_success_put_request(
        httpserver=httpserver,
        endpoint=brand.replace("{brandId}", id),
        expected_request=expected_request,
        expected_response=expected_response
    )

    number_registration_brand = NumberRegistrationNonProfitBrand(
        reference_id=reference_id,
        type=var_type,
        address=NumberRegistrationAddress(
            city=address_city, state=address_state, street=address_street, zip_code=address_zip_code
        ),
        alternate_business_id=NumberRegistrationBusinessIdentifier(id=business_id, type=business_type),
        country_code=country_code,
        support_email=support_email,
        legal_name=legal_name,
        name=name,
        support_phone=support_phone,
        vertical=vertical,
        website=website,
        tax_id=tax_id
    )

    actual_response = number_registration_api_instance.update_brand(
        brand_id=id,
        number_registration_brand=number_registration_brand
    )

    expected_brand_response = NumberRegistrationNonProfitBrand(
        id=id,
        reference_id=reference_id,
        type=var_type,
        address=NumberRegistrationAddress(
            city=address_city, state=address_state, street=address_street,
            zip_code=address_zip_code
        ),
        alternate_business_id=NumberRegistrationBusinessIdentifier(id=business_id, type=business_type),
        country_code=country_code,
        created_date="2021-01-19T16:17:14Z",
        support_email=support_email,
        last_modified_date="2021-01-19T16:17:14Z",
        legal_name=legal_name,
        name=name,
        support_phone=support_phone,
        vertical=vertical,
        website=website,
        tax_id=tax_id
    )

    assert actual_response == expected_brand_response


def test_register_brand(httpserver: HTTPServer, number_registration_api_instance):
    id = "123"

    setup_accepted_post_request_no_request_body(
        httpserver=httpserver,
        endpoint=brand_register.replace("{brandId}", id),
    )

    number_registration_api_instance.register_brand(id)


def test_update_registration(httpserver: HTTPServer, number_registration_api_instance):
    brand_id = "123"
    request = {
        "address": {
            "city": "string",
            "state": "string",
            "street": "string",
            "zipCode": "string"
        },
        "countryCode": "string",
        "legalName": "string",
        "name": "string",
        "supportEmail": "string",
        "supportPhone": "string",
        "referenceId": "string",
        "taxId": "string",
        "vertical": "string",
        "website": "string",
        "stockExchange": "string",
        "stockSymbol": "string"
    }

    setup_accepted_post_request(
        httpserver=httpserver,
        endpoint=brand_update_registration.replace("{brandId}", brand_id),
        expected_request=request
    )

    number_registration_update_brand_request = NumberRegistrationUpdateBrandRequest(
        address=NumberRegistrationAddress(city="string", state="string", street="string", zip_code="string"),
        country_code="string", legal_name="string", name="string", support_email="string", support_phone="string",
        reference_id="string", tax_id="string", vertical="string", website="string", stock_exchange="string",
        stock_symbol="string"
    )

    number_registration_api_instance.update_registered_brand(
        brand_id=brand_id,
        number_registration_update_brand_request=number_registration_update_brand_request
    )


def test_registrar_statuses(httpserver: HTTPServer, number_registration_api_instance):
    brand_id = "123"
    registrar = "CAMPAIGN_REGISTRY"
    state = "ACTIVE"
    brand_identity_status = "SELF_DECLARED"

    expected_response = [
        {
            "registrar": registrar,
            "state": state,
            "brandIdentityStatus": brand_identity_status
        }
    ]

    setup_success_get_request_array_response(
        httpserver=httpserver,
        endpoint=brand_registrar_statuses.replace("{brandId}", brand_id),
        expected_response=expected_response,
        query_string=""
    )

    actual_response = number_registration_api_instance.get_brand_registrar_statuses(brand_id=brand_id)

    expected_brand_response = [NumberRegistrationBrandStatus(
        registrar=registrar, state=state, brand_identity_status=brand_identity_status
    )]

    assert expected_brand_response == actual_response


# brand vetting

def test_get_brand_vets(httpserver: HTTPServer, number_registration_api_instance):
    # issue with dates in model NumberRegistrationBrandVet

    brand_id = "132"
    vet_id = "12345"
    score = 0
    vetted_date = "2023-03-08T16:59:52Z"
    enhanced_vetted_date = "2023-03-08T16:57:52Z"
    var_type = "STANDARD"
    page = 0
    page_size = 1
    total_pages = 0
    total_results = 0

    expected_response = {
        "results": [
            {
                "vetId": vet_id,
                "brandId": brand_id,
                "score": score,
                "vettedDate": vetted_date,
                "enhancedVettedDate": enhanced_vetted_date,
                "type": var_type
            }
        ],
        "paging": {
            "page": page,
            "size": page_size,
            "totalPages": total_pages,
            "totalResults": total_results
        }
    }

    sort = "createdDate,desc"

    query_string = to_query_string_without_escaping([
        ("page", page),
        ("size", page_size),
        ("sort", sort)
    ])

    setup_success_get_request(
        httpserver=httpserver,
        endpoint=brand_vets.replace("{brandId}", brand_id),
        expected_response=expected_response,
        query_string=query_string
    )

    actual_response = number_registration_api_instance.get_brand_vets(
        brand_id=brand_id,
        sort=[sort],
        page=page,
        size=page_size
    )

    number_registration_vet = NumberRegistrationBrandVet(
        vet_id=vet_id,
        brand_id=brand_id,
        score=score,
        vetted_date=vetted_date,
        enhanced_vetted_date=enhanced_vetted_date,
        type=var_type
    )

    expected_vets_response = NumberRegistrationPageResponseBrandVet(
        results=[number_registration_vet],
        paging=NumberRegistrationPageInfo(
            page=page,
            size=page_size,
            total_pages=total_pages,
            total_results=total_results
        )
    )

    assert actual_response == expected_vets_response


def test_vet_brand(httpserver: HTTPServer, number_registration_api_instance):
    # issue with dates in model NumberRegistrationBrandVet

    brand_id = "string"
    vet_id = "string"
    score = 0
    vetted_date = "2023-03-08T16:57:52Z"
    enhanced_vetted_date = "2023-03-08T16:57:52Z"
    var_type = "STANDARD"

    expected_request = {
        "type": var_type
    }

    expected_response = {
        "vetId": vet_id,
        "brandId": brand_id,
        "score": score,
        "vettedDate": vetted_date,
        "enhancedVettedDate": enhanced_vetted_date,
        "type": var_type
    }

    setup_accepted_post_request(
        httpserver=httpserver,
        endpoint=brand_vets.replace("{brandId}", brand_id),
        expected_request=expected_request,
        expected_response=expected_response
    )

    number_registration_brand_vet = NumberRegistrationBrandVet(
        type=var_type
    )

    actual_response: NumberRegistrationBrandVet = number_registration_api_instance.vet_brand(
        brand_id=brand_id,
        number_registration_brand_vet=number_registration_brand_vet
    )

    expected_vet_brand_response = NumberRegistrationBrandVet(
        vet_id=vet_id,
        brand_id=brand_id,
        score=score,
        vetted_date=vetted_date,
        enhanced_vetted_date=enhanced_vetted_date,
        type=var_type
    )

    assert actual_response == expected_vet_brand_response


def test_get_brand_vet(httpserver: HTTPServer, number_registration_api_instance):
    brand_id = "string"
    vet_id = "string"
    score = 0
    vetted_date = "2023-03-08T16:57:52Z"
    enhanced_vetted_date = "2023-03-08T16:57:52Z"
    var_type = "STANDARD"

    expected_response = {
        "vetId": vet_id,
        "brandId": brand_id,
        "score": score,
        "vettedDate": vetted_date,
        "enhancedVettedDate": enhanced_vetted_date,
        "type": var_type
    }

    setup_success_get_request(
        httpserver=httpserver,
        endpoint=brand_vet.replace("{brandId}", brand_id).replace("{vetId}", vet_id),
        expected_response=expected_response
    )

    actual_response: NumberRegistrationBrandVet = number_registration_api_instance.get_brand_vet(
        brand_id=brand_id,
        vet_id=vet_id
    )

    expected_brand_vet_response = NumberRegistrationBrandVet(
        vet_id=vet_id,
        brand_id=brand_id,
        score=score,
        vetted_date=vetted_date,
        enhanced_vetted_date=enhanced_vetted_date,
        type=var_type
    )

    assert expected_brand_vet_response == actual_response


def test_update_brand_vet(httpserver: HTTPServer, number_registration_api_instance):
    brand_id = "123"
    vet_id = "string"
    score = 0
    vetted_date = "2023-03-08T16:57:52Z"
    enhanced_vetted_date = "2023-03-08T16:57:52Z"
    var_type = "STANDARD"

    expected_response = {
        "vetId": vet_id,
        "brandId": brand_id,
        "score": score,
        "vettedDate": vetted_date,
        "enhancedVettedDate": enhanced_vetted_date,
        "type": var_type
    }

    expected_request = {
        "type": var_type
    }

    setup_success_put_request(
        httpserver=httpserver,
        endpoint=brand_vet.replace("{brandId}", brand_id).replace("{vetId}", vet_id),
        expected_request=expected_request,
        expected_response=expected_response
    )

    number_registration_brand_vet = NumberRegistrationBrandVet(
        type=var_type
    )

    actual_response: NumberRegistrationBrandVet = number_registration_api_instance.update_brand_vet(
        brand_id=brand_id, vet_id=vet_id, number_registration_brand_vet=number_registration_brand_vet
    )

    expected_brand_vet_response = NumberRegistrationBrandVet(
        vet_id=vet_id,
        brand_id=brand_id,
        score=score,
        vetted_date=vetted_date,
        enhanced_vetted_date=enhanced_vetted_date,
        type=var_type
    )

    assert expected_brand_vet_response == actual_response


# campaigns

def test_get_campaigns(httpserver: HTTPServer, number_registration_api_instance):
    campaign_id = "4d3601ed-c632-4979-ae22-43854ef4ffaf"
    reference_id = "customer-defined-identifier"
    name = "Example Promo"
    campaign_type = "EXTERNAL_TEN_DIGIT_LONG_CODE"
    created_date_string = "2019-08-24T14:15:22Z"
    created_datetime = datetime.datetime(2019, 8, 24, 14, 15, 22, 0, tzinfo=datetime.timezone.utc)
    external_campaign_id = "CAM1234"
    number_key = "D79C1785A82A2BC6FC0B867DCD055215"

    expected_response = {
        "results": [{
            "id": campaign_id,
            "referenceId": reference_id,
            "name": name,
            "type": campaign_type,
            "createdDate": created_date_string,
            "lastModifiedDate": created_date_string,
            "externalCampaignId": external_campaign_id,
            "numberKeys": [number_key]
        }],
        "paging": {
            "page": 0,
            "size": 1,
            "totalPages": 1,
            "totalResults": 1
        }
    }

    expected_campaign = NumberRegistrationExternalTenDlcCampaign(
        id=campaign_id,
        reference_id=reference_id,
        name=name,
        type=campaign_type,
        created_date=created_datetime,
        last_modified_date=created_datetime,
        external_campaign_id=external_campaign_id,
        number_keys=[number_key]
    )

    sort = "createdDate,desc"
    name_like = "Example"
    not_existing_campaign_id = "100"

    query_string = to_query_string_without_escaping([
        ("id", campaign_id),
        ("id", not_existing_campaign_id),
        ("nameLike", name_like),
        ("sort", sort)
    ])

    setup_success_get_request(
        httpserver=httpserver,
        endpoint=campaigns,
        expected_response=expected_response,
        query_string=query_string
    )

    actual_response = number_registration_api_instance.get_campaigns(
        id=[campaign_id, not_existing_campaign_id],
        name_like=name_like,
        sort=[sort]
    )

    expected_campaigns_response = NumberRegistrationPageResponseCampaign(
        results=[expected_campaign],
        paging=PageInfo(page=0, size=1, total_pages=1, total_results=1)
    )

    assert expected_campaigns_response == actual_response


def test_get_campaign(httpserver: HTTPServer, number_registration_api_instance):
    campaign_id = "4d3601ed-c632-4979-ae22-43854ef4ffaf"
    reference_id = "customer-defined-identifier"
    name = "Example Promo"
    campaign_type = "TEN_DIGIT_LONG_CODE"
    brand_id = "a0c63335-f841-4d43-9ef8-e0765a233f29"
    program_summary = "A mix of promotional and informational messaging."
    customer_care_email = "examples@example.com"
    customer_care_phone = "18889997777"
    confirmation_message = "Example promotional-marketing. Msg&data rates may apply."
    example_message = "Come in today and get 10% OFF today!"
    help_message = "Example promotional-marketing: Help at textsupport@example.com or 18889997777."
    stop_message = "Example promotional-marketing: You have been unsubscribed, no more messages will be sent."
    first_message_type = "SMS"
    second_message_type = "MMS"
    terms_and_conditions_url = "https://www.example.com/terms-and-conditions"
    terms_and_conditions_document_id = "100"
    keyword_call_to_action = "Text MESSAGE to subscribe"
    keyword = "MESSAGE"
    low_volume = False
    use_case = "PROMOTIONAL_MARKETING"
    number_key = "D79C1785A82A2BC6FC0B867DCD055215"
    number = "447860041117"

    expected_response = {
        "id": campaign_id,
        "referenceId": reference_id,
        "name": name,
        "type": campaign_type,
        "brandId": brand_id,
        "programSummary": program_summary,
        "customerCareEmail": customer_care_email,
        "customerCarePhone": customer_care_phone,
        "confirmationMessage": confirmation_message,
        "exampleMessages": [example_message],
        "helpMessage": help_message,
        "stopMessage": stop_message,
        "messageTypes": [first_message_type, second_message_type],
        "termsAndConditionsUrl": terms_and_conditions_url,
        "termsAndConditionsDocumentId": terms_and_conditions_document_id,
        "termsAndConditionsDocumentPreview": {
            "documentId": terms_and_conditions_document_id
        },
        "optIns": {
            "keyword": {
                "callToAction": keyword_call_to_action,
                "keywords": [keyword]
            }
        },
        "brandPreview": {
            "brandId": brand_id
        },
        "lowVolume": low_volume,
        "useCase": use_case,
        "numberKeys": [number_key],
        "numberPreviews": [{
            "number": number
        }]
    }

    expected_campaign = NumberRegistrationTenDlcCampaign(
        id=campaign_id,
        reference_id=reference_id,
        name=name,
        type=campaign_type,
        brand_id=brand_id,
        program_summary=program_summary,
        customer_care_email=customer_care_email,
        customer_care_phone=customer_care_phone,
        confirmation_message=confirmation_message,
        example_messages=[example_message],
        help_message=help_message,
        stop_message=stop_message,
        message_types=[first_message_type, second_message_type],
        terms_and_conditions_url=terms_and_conditions_url,
        terms_and_conditions_document_id=terms_and_conditions_document_id,
        terms_and_conditions_document_preview=NumberRegistrationDocumentMetadata(
            document_id=terms_and_conditions_document_id
        ),
        opt_ins=NumberRegistrationOptIns(
            keyword=NumberRegistrationKeywordOptIn(
                call_to_action=keyword_call_to_action,
                keywords=[keyword]
            )
        ),
        brand_preview=NumberRegistrationBrandPreview(
            brand_id=brand_id
        ),
        low_volume=low_volume,
        use_case=use_case,
        number_keys=[number_key],
        number_previews=[
            NumberRegistrationNumberPreview(
                number=number
            )
        ]
    )

    setup_success_get_request(
        httpserver=httpserver,
        endpoint=campaign.replace("{campaignId}", campaign_id),
        expected_response=expected_response,
        query_string=""
    )

    actual_response = number_registration_api_instance.get_campaign(campaign_id=campaign_id)

    assert actual_response == expected_campaign


def test_create_campaign(httpserver: HTTPServer, number_registration_api_instance):
    campaign_id = "4d3601ed-c632-4979-ae22-43854ef4ffaf"
    reference_id = "customer-defined-identifier"
    name = "Example Promo"
    campaign_type = "TEN_DIGIT_LONG_CODE"
    brand_id = "a0c63335-f841-4d43-9ef8-e0765a233f29"
    program_summary = "A mix of promotional and informational messaging."
    customer_care_email = "examples@example.com"
    customer_care_phone = "18889997777"
    confirmation_message = "Example promotional-marketing. Msg&data rates may apply."
    example_message = "Come in today and get 10% OFF today!"
    help_message = "Example promotional-marketing: Help at textsupport@example.com or 18889997777."
    stop_message = "Example promotional-marketing: You have been unsubscribed, no more messages will be sent."
    first_message_type = "SMS"
    second_message_type = "MMS"
    terms_and_conditions_url = "https://www.example.com/terms-and-conditions"
    terms_and_conditions_document_id = "100"
    keyword_call_to_action = "Text MESSAGE to subscribe"
    keyword = "MESSAGE"
    low_volume = False
    use_case = "PROMOTIONAL_MARKETING"
    number_key = "D79C1785A82A2BC6FC0B867DCD055215"

    expected_request = {
        "referenceId": reference_id,
        "name": name,
        "type": campaign_type,
        "brandId": brand_id,
        "programSummary": program_summary,
        "customerCareEmail": customer_care_email,
        "customerCarePhone": customer_care_phone,
        "confirmationMessage": confirmation_message,
        "exampleMessages": [example_message],
        "helpMessage": help_message,
        "stopMessage": stop_message,
        "messageTypes": [first_message_type, second_message_type],
        "termsAndConditionsUrl": terms_and_conditions_url,
        "termsAndConditionsDocumentId": terms_and_conditions_document_id,
        "termsAndConditionsDocumentPreview": {
            "documentId": terms_and_conditions_document_id
        },
        "optIns": {
            "keyword": {
                "callToAction": keyword_call_to_action,
                "keywords": [keyword]
            }
        },
        "brandPreview": {
            "brandId": brand_id
        },
        "lowVolume": low_volume,
        "useCase": use_case,
        "numberKeys": [number_key]
    }

    expected_response = {
        "id": campaign_id,
        "referenceId": reference_id,
        "name": name,
        "type": campaign_type,
        "brandId": brand_id,
        "programSummary": program_summary,
        "customerCareEmail": customer_care_email,
        "customerCarePhone": customer_care_phone,
        "confirmationMessage": confirmation_message,
        "exampleMessages": [example_message],
        "helpMessage": help_message,
        "stopMessage": stop_message,
        "messageTypes": [first_message_type, second_message_type],
        "termsAndConditionsUrl": terms_and_conditions_url,
        "termsAndConditionsDocumentId": terms_and_conditions_document_id,
        "termsAndConditionsDocumentPreview": {
            "documentId": terms_and_conditions_document_id
        },
        "optIns": {
            "keyword": {
                "callToAction": keyword_call_to_action,
                "keywords": [keyword]
            }
        },
        "brandPreview": {
            "brandId": brand_id
        },
        "lowVolume": low_volume,
        "useCase": use_case,
        "numberKeys": [number_key]
    }

    setup_created_post_request(
        httpserver,
        endpoint=campaigns,
        expected_request=expected_request,
        expected_response=expected_response
    )

    campaign_request = NumberRegistrationTenDlcCampaign(
        reference_id=reference_id,
        name=name,
        type=campaign_type,
        brand_id=brand_id,
        program_summary=program_summary,
        customer_care_email=customer_care_email,
        customer_care_phone=customer_care_phone,
        confirmation_message=confirmation_message,
        example_messages=[example_message],
        help_message=help_message,
        stop_message=stop_message,
        message_types=[first_message_type, second_message_type],
        terms_and_conditions_url=terms_and_conditions_url,
        terms_and_conditions_document_id=terms_and_conditions_document_id,
        terms_and_conditions_document_preview=NumberRegistrationDocumentMetadata(
            document_id=terms_and_conditions_document_id
        ),
        opt_ins=NumberRegistrationOptIns(
            keyword=NumberRegistrationKeywordOptIn(
                call_to_action=keyword_call_to_action,
                keywords=[keyword]
            )
        ),
        brand_preview=NumberRegistrationBrandPreview(
            brand_id=brand_id
        ),
        low_volume=low_volume,
        use_case=use_case,
        number_keys=[number_key]
    )

    expected_campaign = NumberRegistrationTenDlcCampaign(
        id=campaign_id,
        reference_id=reference_id,
        name=name,
        type=campaign_type,
        brand_id=brand_id,
        program_summary=program_summary,
        customer_care_email=customer_care_email,
        customer_care_phone=customer_care_phone,
        confirmation_message=confirmation_message,
        example_messages=[example_message],
        help_message=help_message,
        stop_message=stop_message,
        message_types=[first_message_type, second_message_type],
        terms_and_conditions_url=terms_and_conditions_url,
        terms_and_conditions_document_id=terms_and_conditions_document_id,
        terms_and_conditions_document_preview=NumberRegistrationDocumentMetadata(
            document_id=terms_and_conditions_document_id
        ),
        opt_ins=NumberRegistrationOptIns(
            keyword=NumberRegistrationKeywordOptIn(
                call_to_action=keyword_call_to_action,
                keywords=[keyword]
            )
        ),
        brand_preview=NumberRegistrationBrandPreview(
            brand_id=brand_id
        ),
        low_volume=low_volume,
        use_case=use_case,
        number_keys=[number_key]
    )

    actual_response = number_registration_api_instance.create_campaign(campaign_request)

    assert actual_response == expected_campaign


def test_update_campaign(httpserver: HTTPServer, number_registration_api_instance):
    campaign_id = "4d3601ed-c632-4979-ae22-43854ef4ffaf"
    reference_id = "customer-defined-identifier"
    name = "Example Promo"
    campaign_type = "TEN_DIGIT_LONG_CODE"
    brand_id = "a0c63335-f841-4d43-9ef8-e0765a233f29"
    program_summary = "A mix of promotional and informational messaging."
    customer_care_email = "examples@example.com"
    customer_care_phone = "18889997777"
    confirmation_message = "Example promotional-marketing. Msg&data rates may apply."
    example_message = "Come in today and get 10% OFF today!"
    help_message = "Example promotional-marketing: Help at textsupport@example.com or 18889997777."
    stop_message = "Example promotional-marketing: You have been unsubscribed, no more messages will be sent."
    first_message_type = "SMS"
    second_message_type = "MMS"
    terms_and_conditions_url = "https://www.example.com/terms-and-conditions"
    terms_and_conditions_document_id = "100"
    keyword_call_to_action = "Text MESSAGE to subscribe"
    keyword = "MESSAGE"
    low_volume = False
    use_case = "PROMOTIONAL_MARKETING"
    number_key = "D79C1785A82A2BC6FC0B867DCD055215"

    expected_request = {
        "referenceId": reference_id,
        "name": name,
        "type": campaign_type,
        "brandId": brand_id,
        "programSummary": program_summary,
        "customerCareEmail": customer_care_email,
        "customerCarePhone": customer_care_phone,
        "confirmationMessage": confirmation_message,
        "exampleMessages": [example_message],
        "helpMessage": help_message,
        "stopMessage": stop_message,
        "messageTypes": [first_message_type, second_message_type],
        "termsAndConditionsUrl": terms_and_conditions_url,
        "termsAndConditionsDocumentId": terms_and_conditions_document_id,
        "termsAndConditionsDocumentPreview": {
            "documentId": terms_and_conditions_document_id
        },
        "optIns": {
            "keyword": {
                "callToAction": keyword_call_to_action,
                "keywords": [keyword]
            }
        },
        "brandPreview": {
            "brandId": brand_id
        },
        "lowVolume": low_volume,
        "useCase": use_case,
        "numberKeys": [number_key]
    }

    expected_response = {
        "id": campaign_id,
        "referenceId": reference_id,
        "name": name,
        "type": campaign_type,
        "brandId": brand_id,
        "programSummary": program_summary,
        "customerCareEmail": customer_care_email,
        "customerCarePhone": customer_care_phone,
        "confirmationMessage": confirmation_message,
        "exampleMessages": [example_message],
        "helpMessage": help_message,
        "stopMessage": stop_message,
        "messageTypes": [first_message_type, second_message_type],
        "termsAndConditionsUrl": terms_and_conditions_url,
        "termsAndConditionsDocumentId": terms_and_conditions_document_id,
        "termsAndConditionsDocumentPreview": {
            "documentId": terms_and_conditions_document_id
        },
        "optIns": {
            "keyword": {
                "callToAction": keyword_call_to_action,
                "keywords": [keyword]
            }
        },
        "brandPreview": {
            "brandId": brand_id
        },
        "lowVolume": low_volume,
        "useCase": use_case,
        "numberKeys": [number_key]
    }

    setup_success_put_request(
        httpserver,
        endpoint=campaign.replace("{campaignId}", campaign_id),
        expected_request=expected_request,
        expected_response=expected_response
    )

    campaign_request = NumberRegistrationTenDlcCampaign(
        reference_id=reference_id,
        name=name,
        type=campaign_type,
        brand_id=brand_id,
        program_summary=program_summary,
        customer_care_email=customer_care_email,
        customer_care_phone=customer_care_phone,
        confirmation_message=confirmation_message,
        example_messages=[example_message],
        help_message=help_message,
        stop_message=stop_message,
        message_types=[first_message_type, second_message_type],
        terms_and_conditions_url=terms_and_conditions_url,
        terms_and_conditions_document_id=terms_and_conditions_document_id,
        terms_and_conditions_document_preview=NumberRegistrationDocumentMetadata(
            document_id=terms_and_conditions_document_id
        ),
        opt_ins=NumberRegistrationOptIns(
            keyword=NumberRegistrationKeywordOptIn(
                call_to_action=keyword_call_to_action,
                keywords=[keyword]
            )
        ),
        brand_preview=NumberRegistrationBrandPreview(
            brand_id=brand_id
        ),
        low_volume=low_volume,
        use_case=use_case,
        number_keys=[number_key]
    )

    expected_campaign = NumberRegistrationTenDlcCampaign(
        id=campaign_id,
        reference_id=reference_id,
        name=name,
        type=campaign_type,
        brand_id=brand_id,
        program_summary=program_summary,
        customer_care_email=customer_care_email,
        customer_care_phone=customer_care_phone,
        confirmation_message=confirmation_message,
        example_messages=[example_message],
        help_message=help_message,
        stop_message=stop_message,
        message_types=[first_message_type, second_message_type],
        terms_and_conditions_url=terms_and_conditions_url,
        terms_and_conditions_document_id=terms_and_conditions_document_id,
        terms_and_conditions_document_preview=NumberRegistrationDocumentMetadata(
            document_id=terms_and_conditions_document_id
        ),
        opt_ins=NumberRegistrationOptIns(
            keyword=NumberRegistrationKeywordOptIn(
                call_to_action=keyword_call_to_action,
                keywords=[keyword]
            )
        ),
        brand_preview=NumberRegistrationBrandPreview(
            brand_id=brand_id
        ),
        low_volume=low_volume,
        use_case=use_case,
        number_keys=[number_key]
    )

    actual_response = number_registration_api_instance.update_campaign(campaign_id, campaign_request)

    assert actual_response == expected_campaign


def test_get_campaign_network_statuses(httpserver: HTTPServer, number_registration_api_instance):
    campaign_id = "test-campaign"

    network = "ATT"
    state = "ACTIVE"
    message_class = "message-class"

    expected_response = [{
        "network": network,
        "state": state,
        "messageClass": message_class
    }]

    setup_success_get_request(
        httpserver=httpserver,
        endpoint=campaign_network_statuses.replace("{campaignId}", campaign_id),
        expected_response=expected_response,
        query_string=""
    )

    actual_response = number_registration_api_instance.get_campaign_network_statuses(campaign_id)

    expected_network_status = [
        NumberRegistrationNetworkStatus(network=network, state=state, message_class=message_class)
    ]

    assert expected_network_status == actual_response


def test_register_campaign(httpserver: HTTPServer, number_registration_api_instance):
    campaign_id = "test-campaign"

    setup_accepted_post_request_no_request_body(
        httpserver=httpserver,
        endpoint=campaign_register.replace("{campaignId}", campaign_id)
    )

    number_registration_api_instance.register_campaign(campaign_id)


def test_deregister_campaign(httpserver: HTTPServer, number_registration_api_instance):
    campaign_id = "test-campaign"

    setup_accepted_post_request_no_request_body(
        httpserver=httpserver,
        endpoint=campaign_deregister.replace("{campaignId}", campaign_id)
    )

    number_registration_api_instance.deregister_campaign(campaign_id)


def test_update_registered_campaign(httpserver: HTTPServer, number_registration_api_instance):
    campaign_id = "test-campaign"

    first_number_key = "ABC100"
    second_number_key = "ABC200"

    expected_request = {
        "numberKeys": [
            first_number_key,
            second_number_key
        ]
    }

    setup_accepted_post_request(
        httpserver=httpserver,
        endpoint=campaign_update_registration.replace("{campaignId}", campaign_id),
        expected_request=expected_request
    )

    update_registered_campaign_request = NumberRegistrationUpdateCampaignRequest(
        number_keys=[first_number_key, second_number_key]
    )

    number_registration_api_instance.update_registered_campaign(campaign_id, update_registered_campaign_request)


# PUT


def setup_success_put_request(httpserver: HTTPServer, endpoint: str, expected_request: dict = None,
                              expected_response: dict = None):
    httpserver.expect_request(
        uri=endpoint,
        method="PUT",
        json=expected_request,
        headers=expected_headers
    ).respond_with_json(status=200, response_json=expected_response)


# POST

def setup_accepted_post_request(
        httpserver: HTTPServer,
        endpoint: str,
        expected_request: dict = None,
        expected_response: dict = None
):
    httpserver.expect_request(
        uri=endpoint,
        method="POST",
        json=expected_request,
        headers=expected_headers
    ).respond_with_json(status=202, response_json=expected_response)


def setup_accepted_post_request_no_request_body(httpserver: HTTPServer, endpoint: str):
    httpserver.expect_request(
        uri=endpoint,
        method="POST",
        headers=expected_headers
    ).respond_with_json(status=202, response_json=None)


def setup_accepted_post_request_no_response_body(httpserver: HTTPServer, endpoint: str, expected_request: dict = None):
    httpserver.expect_request(
        uri=endpoint,
        method="POST",
        json=expected_request,
        headers=expected_headers
    ).respond_with_json(status=202, response_json=None)


def setup_created_post_request(
        httpserver: HTTPServer,
        endpoint: str,
        expected_request: dict = None,
        expected_response: dict = None
):
    httpserver.expect_request(
        uri=endpoint,
        method="POST",
        json=expected_request,
        headers=expected_headers
    ).respond_with_json(status=201, response_json=expected_response)


# GET

def setup_success_get_request(httpserver: HTTPServer, endpoint: str, expected_response: dict, query_string: str = None):
    httpserver.expect_request(
        uri=endpoint,
        method="GET",
        headers=expected_headers,
        query_string=query_string
    ).respond_with_json(status=200, response_json=expected_response)


def setup_success_get_request_array_response(
        httpserver: HTTPServer, endpoint: str, expected_response: List = None, query_string: str = None):
    httpserver.expect_request(
        uri=endpoint,
        method="GET",
        headers=expected_headers,
        query_string=query_string
    ).respond_with_json(expected_response)


def to_query_string_without_escaping(query_params: list[tuple[str, str]]):
    if not query_params:
        return ""
    return "&".join(["{}={}".format(paramName, paramValue) for (paramName, paramValue) in query_params])


@pytest.fixture
def number_registration_api_instance():
    return NumberRegistrationApi(ApiClient(Configuration(
        host="http://localhost:{}".format(port),
        api_key={"APIKeyHeader": api_key},
        api_key_prefix={"APIKeyHeader": "App"},
    )))


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return "localhost", port
