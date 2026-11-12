import pytest
from invcheck import validate

OK = {"name": "web-01", "env": "prod", "ip": "10.0.0.5"}

def test_valid():
    assert validate([OK]) == []

def test_duplicate():
    assert len(validate([OK, OK])) == 1

@pytest.mark.parametrize("ip", ["999.1.1.1", "10.0.0", "abc", None])
def test_bad_ip(ip):
    assert len(validate([{**OK, "ip": ip}])) == 1

@pytest.mark.parametrize("env", ["test", "", None])
def test_bad_env(env):
    assert len(validate([{**OK, "env": env}])) == 1

def test_missing_name():
    assert len(validate([{"env": "dev", "ip": "10.0.0.1"}])) == 1

def test_two_problems():
    assert len(validate([{**OK, "env": "x", "ip": "y"}])) == 2
