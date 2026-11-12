# Lesson 49 task: a config-driven report

Work only in your own Ubuntu 24.04 virtual machine, inside the virtual environment from Lesson 47. Install the YAML package first: `pip install pyyaml`.

Files in this folder: `servers49.csv` (the servers), `config49.yaml` (the settings), `check49.sh` (the checker). Do not read `solution_report.py` until you have tried.

Write `report.py` so that running `APP_ENV=prod python3 report.py` creates `report.json` containing exactly these four keys:

1. `env`: the value of the environment variable `APP_ENV`, with the default `dev` when it is not set.
2. `limit`: the number `limit` read from `config49.yaml` with `yaml.safe_load`.
3. `count`: how many servers are in `servers49.csv` (read it with `csv.DictReader`).
4. `busy`: the list of server names whose `cpu` is above the limit (the CSV gives text, so convert with `int`).

Write the file with `with open("report.json", "w")` and `json.dump`, and print `wrote report.json`.

Check yourself: `bash check49.sh .` should print four PASS lines. The checker works in a temporary copy and changes nothing.

Rules: never put a real secret in a file or a command; the limit must come from the YAML file, not from the code.

Report: copy `report_template.md` and fill it in with your commands and their output.
