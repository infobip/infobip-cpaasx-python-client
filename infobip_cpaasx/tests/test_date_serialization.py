import datetime

import pytest
from dateutil import parser
from dateutil.tz import tzutc, tzoffset
from urllib3 import HTTPResponse

from infobip_cpaasx import Configuration, ApiClient
from infobip_cpaasx.rest import RESTResponse


@pytest.mark.parametrize(
    "serialized_date_time, date_time",
    [
        ('2023-08-03T12:07:42.777000+00:00', parser.parse('2023-08-03T12:07:42.777000+00:00')),
        ('2023-08-03T13:07:42.777000+01:00', parser.parse('2023-08-03T13:07:42.777000+01:00')),
        ('2023-08-03T11:07:42.777000-01:00', parser.parse('2023-08-03T11:07:42.777000-01:00')),
        ('2023-08-03T13:37:42.777000+01:30', parser.parse('2023-08-03T13:37:42.777000+01:30')),
        ('2023-08-03T10:37:42.777000-01:30', parser.parse('2023-08-03T10:37:42.777000-01:30')),
        ('2023-08-03T17:07:42.777000+05:00', parser.parse('2023-08-03T17:07:42.777000+05:00')),
        ('2023-08-03T07:07:42.777000-05:00', parser.parse('2023-08-03T07:07:42.777000-05:00')),
        ('2023-08-03T17:37:42.777000+05:30', parser.parse('2023-08-03T17:37:42.777000+05:30')),
        ('2023-08-03T06:37:42.777000-05:30', parser.parse('2023-08-03T06:37:42.777000-05:30')),
        ('2023-08-03T12:07:42.777000+00:00', datetime.datetime(2023, 8, 3, 12, 7, 42, 777000, tzinfo=tzutc())),
        ('2023-08-03T13:07:42.777000+01:00', datetime.datetime(2023, 8, 3, 13, 7, 42, 777000, tzinfo=tzoffset(None, 3600))),
        ('2023-08-03T11:07:42.777000-01:00', datetime.datetime(2023, 8, 3, 11, 7, 42, 777000, tzinfo=tzoffset(None, -3600))),
        ('2023-08-03T13:37:42.777000+01:30', datetime.datetime(2023, 8, 3, 13, 37, 42, 777000, tzinfo=tzoffset(None, 5400))),
        ('2023-08-03T10:37:42.777000-01:30', datetime.datetime(2023, 8, 3, 10, 37, 42, 777000, tzinfo=tzoffset(None, -5400))),
        ('2023-08-03T17:07:42.777000+05:00', datetime.datetime(2023, 8, 3, 17, 7, 42, 777000, tzinfo=tzoffset(None, 18000))),
        ('2023-08-03T07:07:42.777000-05:00', datetime.datetime(2023, 8, 3, 7, 7, 42, 777000, tzinfo=tzoffset(None, -18000))),
        ('2023-08-03T17:37:42.777000+05:30', datetime.datetime(2023, 8, 3, 17, 37, 42, 777000, tzinfo=tzoffset(None, 19800))),
        ('2023-08-03T06:37:42.777000-05:30', datetime.datetime(2023, 8, 3, 6, 37, 42, 777000, tzinfo=tzoffset(None, -19800))),
        ('2023-08-03T12:07:42.777000+00:00', parser.parse('2023-08-03T12:07:42.777+0000')),
        ('2023-08-03T13:07:42.777000+01:00', parser.parse('2023-08-03T13:07:42.777+0100')),
        ('2023-08-03T11:07:42.777000-01:00', parser.parse('2023-08-03T11:07:42.777-0100')),
        ('2023-08-03T13:37:42.777000+01:30', parser.parse('2023-08-03T13:37:42.777+0130')),
        ('2023-08-03T10:37:42.777000-01:30', parser.parse('2023-08-03T10:37:42.777-0130')),
        ('2023-08-03T17:07:42.777000+05:00', parser.parse('2023-08-03T17:07:42.777+0500')),
        ('2023-08-03T07:07:42.777000-05:00', parser.parse('2023-08-03T07:07:42.777-0500')),
        ('2023-08-03T17:37:42.777000+05:30', parser.parse('2023-08-03T17:37:42.777+0530')),
        ('2023-08-03T06:37:42.777000-05:30', parser.parse('2023-08-03T06:37:42.777-0530')),
        ('2023-08-03T06:37:42.777000+00:00', parser.parse('2023-08-03T06:37:42.777Z')),
    ]
)
def test_supported_datetime_format_serialization(get_api_client, serialized_date_time, date_time):
    assert get_api_client.sanitize_for_serialization(date_time) == serialized_date_time


@pytest.mark.parametrize(
    "date_time_string, deserialized_date_time",
    [
        ('2023-08-03T12:07:42.777+00:00', parser.parse('2023-08-03T12:07:42.777000+00:00')),
        ('2023-08-03T13:07:42.777+01:00', parser.parse('2023-08-03T13:07:42.777000+01:00')),
        ('2023-08-03T13:37:42.777+01:30', parser.parse('2023-08-03T13:37:42.777000+01:30')),
        ('2023-08-03T10:37:42.777-01:00', parser.parse('2023-08-03T10:37:42.777000-01:00')),
        ('2023-08-03T10:37:42.777-01:30', parser.parse('2023-08-03T10:37:42.777000-01:30')),
        ('2023-08-03T12:07:42.777+0000', parser.parse('2023-08-03T12:07:42.777000+00:00')),
        ('2023-08-03T13:07:42.777+0100', parser.parse('2023-08-03T13:07:42.777000+01:00')),
        ('2023-08-03T11:07:42.777-0100', parser.parse('2023-08-03T11:07:42.777000-01:00')),
        ('2023-08-03T13:07:42.777+0130', parser.parse('2023-08-03T13:07:42.777000+01:30')),
        ('2023-08-03T11:07:42.777-0130', parser.parse('2023-08-03T11:07:42.777000-01:30')),
        ('2023-08-03T06:37:42.777Z', parser.parse('2023-08-03T06:37:42.777000+00:00')),
    ]
)
def test_supported_datetime_format_deserialization(get_api_client, date_time_string, deserialized_date_time):
    assert get_api_client.deserialize(RESTResponse(HTTPResponse(body=date_time_string)), datetime.datetime) == deserialized_date_time


@pytest.fixture
def get_api_client():
    return ApiClient(Configuration(
        host="http://localhost:8088",
        api_key={'APIKeyHeader': 'givenApiKey'},
        api_key_prefix={'APIKeyHeader': 'App'},
    ))
