import pytest
from unittest.mock import MagicMock
from src.askSage.sage_client import SageAPI


@pytest.fixture
def sage_api():
    email = 'test@example.com'
    password = 'test'
    get_token_url = 'http://get.token.url'
    query_url = 'http://query.url'
    train_url = 'http://train.url'

    return SageAPI(email, password, get_token_url, query_url, train_url)


@pytest.fixture
def mock_requests(mocker):
    mock = mocker.patch('requests.post')
    return mock


@pytest.fixture
def mock_redis(mocker):
    mock = mocker.patch('redis.Redis.from_url')
    return mock


def test_sage_request(sage_api, mock_requests, mock_redis):
    mock_requests.return_value.ok = True
    mock_requests.return_value.json.return_value = {'response': 'Token is valid'}
    mock_redis.return_value.get.return_value = 'token'.encode('utf-8')

    data = {'message': 'test message'}
    assert sage_api.sage_request(data)


def test_check_token(sage_api, mock_requests, mock_redis):
    mock_redis.return_value.get.return_value = 'new_token'.encode('utf-8')

    sage_api.check_token()
    assert sage_api.token == 'new_token'


def test_request_new_token(sage_api, mock_requests, mock_redis):
    mock_requests.return_value.ok = True
    mock_requests.return_value.json.return_value = {'response': {'access_token': 'new_token'}}

    sage_api.request_new_token()
    assert sage_api.token == 'new_token'


def test_query_sage(sage_api, mock_requests, mock_redis):
    mock_requests.return_value.ok = True
    mock_requests.return_value.json.return_value = {'response': 'query response'}
    mock_redis.return_value.get.return_value = 'token'.encode('utf-8')

    message = 'test message'
    assert sage_api.query_sage(message)
