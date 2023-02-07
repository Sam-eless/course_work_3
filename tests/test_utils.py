import pytest

from utils.func import get_data


def test_get_data(test_url, test_url_wrong, test_url_pikabu, test_url_status):
    assert len(get_data(test_url)[0]) > 0
    assert get_data(test_url_wrong) == (None, "ERROR: requests.exceptions.ConnectionError")
    assert get_data(test_url_pikabu) == (None, "ERROR: requests.exceptions.JSONDecodeError")
    assert get_data(test_url_status) == (None, "ERROR: status_code: 404")



