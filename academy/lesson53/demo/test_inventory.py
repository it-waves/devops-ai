import pytest
from inventory import running

SERVERS = [{"name": "web-01", "state": "running"},
           {"name": "web-02", "state": "stopped"}]

def test_running():
    assert running(SERVERS) == ["web-01"]

def test_none_running():
    assert running([]) == []

@pytest.mark.parametrize("state", ["stopped", "failed"])
def test_not_running(state):
    assert running([{"name": "x", "state": state}]) == []
