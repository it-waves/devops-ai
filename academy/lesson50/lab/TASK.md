# Lesson 50 task: fetch the inventory from a REST API

Work only in your own Ubuntu 24.04 virtual machine, inside the virtual environment from Lesson 47, with `pip install requests` done.

Files in this folder: `api06.py` (a tiny lab API, standard library only) and `check50.sh` (the checker). Do not read `solution_fetch.py` until you have tried.

1. In one terminal start the lab API: `python3 api06.py` (it listens on 127.0.0.1:8081). Leave it running.
2. In another terminal: `export API_TOKEN=lab-token-123` (a throwaway lab token; real tokens never go on screen or into code).
3. Write `fetch.py` so that it:
   - reads the address from the environment variable `API_URL`, default `http://127.0.0.1:8081`
   - reads the token from `API_TOKEN`; if it is missing, stops with the message `API_TOKEN is not set`
   - calls `GET /servers` with the header `Authorization: Bearer <token>`, passes `timeout=5` on every call and uses `raise_for_status()`
   - follows `next_page` until it is `None`, so that all pages are collected
   - prints exactly two lines: `servers: 10` and `stopped: web-05, web-10` (the servers whose `state` is `stopped`)

Check yourself: `bash check50.sh .` should print four PASS lines. The checker starts its own copy of the API on port 8099 and stops it again.

Rules: no token in the code, a timeout on every call, and a clear error instead of a crash trace.

Report: copy `report_template.md` and fill it in with your commands and their output.
