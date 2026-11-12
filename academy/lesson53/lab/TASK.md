# Lesson 53 task: test a module, and fake the network

Work only in your own Ubuntu 24.04 virtual machine, inside your virtual environment, with `pip install requests pytest` done.

Files in this folder: `inventory_tools.py` (the code you will test) and `check53.sh` (the checker). Do not read `solution_test_tools.py` until you have tried.

Write `test_tools.py` for `inventory_tools.py`, which has two functions:

- `count_by_env(servers)` takes a list of dicts like `{"name": "web-01", "env": "prod"}` and returns a dict that counts servers per environment, for example `{"prod": 2, "staging": 1}`. A server without an `env` key raises `KeyError`.
- `api_status(url)` calls `requests.get(url, timeout=2)`, checks the status with `raise_for_status()`, and returns the `"status"` value of the JSON answer.

Your `test_tools.py` must:

1. Contain at least 5 tests, and all of them pass: `python3 -m pytest -q`.
2. Use `@pytest.mark.parametrize` at least once.
3. Use `pytest.raises` to test the `KeyError`.
4. Fake the network with `unittest.mock` (`Mock` and `patch`), the `monkeypatch` fixture, or `pytest-mock`. No test may need a real server: `api_status` is tested for an OK answer and for an HTTP error (a fake response whose `raise_for_status` raises `requests.HTTPError`).
5. Be strict enough to catch bugs: the checker breaks the module on purpose, three different ways, and your tests must fail each time.

Check yourself: `bash check53.sh .` should print six PASS lines. The checker needs no server.

Report: copy `report_template.md` and fill it in with your commands and their output.
