# Lesson 55 task: a tested inventory validation utility

Work only in your own Ubuntu 24.04 virtual machine, inside your virtual environment, with `pip install pytest` done. This task puts together the whole Python for DevOps masterclass: data files, functions, a command line tool with exit codes, and tests.

Files in this folder: `check55.sh` (the checker), `broken_invcheck.py` (a deliberately wrong version used by the checker) and `report_template.md`. Do not read `solution_invcheck.py` until you have tried.

Write two files.

1. `invcheck.py`, a tool that validates a JSON inventory file, a list of server objects like `{"name": "web-01", "env": "prod", "ip": "10.0.0.5"}`.
   - `validate(servers)` returns a list of error strings, one per problem. An empty list means valid.
   - The rules: `name` is a non-empty string and unique in the list; `env` is one of `dev`, `staging`, `prod`; `ip` is a valid IPv4 address (the `ipaddress` module helps).
   - One problem gives one error: a server with a bad `env` and a bad `ip` gives two errors. A missing field is a problem for that field.
   - Command line: `python3 invcheck.py FILE`. Print each error on its own line, then exit 0 if valid, 1 if there are problems, 2 if the file cannot be read or is not valid JSON.

2. `test_invcheck.py`, at least 6 tests, all passing against your `invcheck.py`, and strict enough to fail against `broken_invcheck.py` (which accepts duplicate names, accepts a bad IP and ignores `env`). Use `parametrize` at least once.

Check yourself: `bash check55.sh .` should print six PASS lines. The checker needs no server and no cloud account.

Report: copy `report_template.md` and fill it in with your commands and their output.
