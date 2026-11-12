import pytest
from svccheck import validate
OK = {"name": "web", "port": 80, "proto": "tcp"}

def test_valid_and_edge():
    assert validate([OK, {**OK, "name": "x", "port": 65535}]) == []

@pytest.mark.parametrize("port", [0, 65536, "80", None])
def test_port(port):
    assert validate([{**OK, "port": port}])

def test_duplicate():
    assert validate([OK, OK]) == ["web: duplicate"]

def test_no_name():
    errs = validate([{"port": 80, "proto": "tcp"}])
    assert errs == ["#0: name missing"]
