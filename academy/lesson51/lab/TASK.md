# Lesson 51 task: a script that survives a flaky API

Work only in your own Ubuntu 24.04 virtual machine, inside your virtual environment, with `pip install requests` done.

Files in this folder: `api06.py` (the lab API, standard library only) and `check51.sh` (the checker). Do not read `solution_fetch_retry.py` until you have tried.

The lab API has an address `/flaky` that answers `503` twice and then `200` with `{"status": "recovered"}`.

1. Start the lab API in one terminal: `python3 api06.py` (it listens on 127.0.0.1:8081).
2. Write `fetch_retry.py` so that it:
   - reads the address from the environment variable `API_URL`, default `http://127.0.0.1:8081`
   - calls `GET /flaky` with `timeout=2` and checks the status with `raise_for_status()`
   - tries up to 4 times and waits longer after each failure (1 second, then 2, then 4)
   - uses the `logging` module (not `print`) for every attempt: a WARNING `attempt N failed` for a failure, an INFO `attempt N ok` for success
   - on success prints exactly `recovered` on standard output and exits with code 0
   - after the 4th failure logs an ERROR containing `gave up`, and exits with code 1 (no traceback)
   - catches `requests.RequestException`, never a bare `except:`

Check yourself: `bash check51.sh .` should print four PASS lines. The checker starts its own copy of the API on port 8099 and stops it again. One check points the script at a closed port, so it takes about 10 seconds.

Report: copy `report_template.md` and fill it in with your commands and their output.
