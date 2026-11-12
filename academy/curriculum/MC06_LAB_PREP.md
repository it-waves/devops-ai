# MC06 Python for DevOps: lab and recording preparation (checked 2026-11-11)

Verified on Ubuntu 24.04.5 (the recording computer):
- Stock python3 is 3.12.3; venv and pip work (pip 24.0 inside a venv). The recording computer's default python3 was 3.13, so recordings use `mc06_prep/enter_base.sh`, which puts the stock 3.12 first on PATH inside the private recording root.
- Real `pip install` works in the recordings (through the recording computer's proxy, set invisibly in the root's rc file). Verified: requests 2.34, PyYAML 6, pytest 9, pytest-mock, boto3, moto server, Flask all install into a fresh venv.
- Real REST API available for pagination demos: api.github.com answers (unauthenticated, rate limited); a local lab API (`academy/lab/mc06/api06.py`) covers bearer-token auth (401 without the token), pagination, a flaky endpoint (503 twice, then 200) for retries, and a slow endpoint for timeouts.
- Cloud SDK lessons (O08): boto3 against a local AWS-compatible mock (moto) is free and safe; real AWS demos use only the user's free-tier resources, least-privilege read-only policies, and end with a delete reminder.
- Not available: httpbin.org (blocked). Do not rely on it.
- Terminal rules unchanged: xterm 71x19, commands up to about 52 characters, output lines under 71 columns, secrets never typed or shown.

Suggested lesson plan (9 objectives plus mastery): L47 setup and venv (O01), L48 types, collections and functions (O02), L49 files, JSON, YAML, CSV and env config (O03), L50 REST APIs: auth, timeouts, pagination (O04), L51 exceptions, logging and retries (O05), L52 CLI tools and exit codes (O06), L53 pytest and mocks (O07), L54 cloud SDKs with least privilege (O08), L55 tested inventory validation utility (O09), L56 MC06 mastery.
