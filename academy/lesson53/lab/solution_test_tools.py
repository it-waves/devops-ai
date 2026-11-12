import pytest
import requests
from unittest.mock import Mock, patch

from inventory_tools import api_status, count_by_env

SERVERS = [
    {"name": "web-01", "env": "prod"},
    {"name": "web-02", "env": "prod"},
    {"name": "db-01", "env": "staging"},
]


def test_count_by_env():
    assert count_by_env(SERVERS) == {"prod": 2, "staging": 1}


def test_count_empty():
    assert count_by_env([]) == {}


@pytest.mark.parametrize("n", [1, 3, 5])
def test_count_many(n):
    servers = [{"name": f"s{i}", "env": "dev"} for i in range(n)]
    assert count_by_env(servers) == {"dev": n}


def test_missing_env_raises():
    with pytest.raises(KeyError):
        count_by_env([{"name": "x"}])


def test_api_status_ok():
    fake = Mock()
    fake.json.return_value = {"status": "ok"}
    with patch("inventory_tools.requests.get", return_value=fake):
        assert api_status("http://example.test/health") == "ok"


def test_api_status_http_error():
    fake = Mock()
    fake.raise_for_status.side_effect = requests.HTTPError("503")
    with patch("inventory_tools.requests.get", return_value=fake):
        with pytest.raises(requests.HTTPError):
            api_status("http://example.test/health")
