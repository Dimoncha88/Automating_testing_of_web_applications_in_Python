import pytest
from checkPost import get_token


@pytest.fixture()
def token():
    return get_token()