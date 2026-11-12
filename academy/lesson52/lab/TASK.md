# Lesson 52 task: a command line tool that reports with exit codes

Work only in your own Ubuntu 24.04 virtual machine, inside your virtual environment, with `pip install requests` done.

Files in this folder: `api06.py` (the lab API, standard library only) and `check52.sh` (the checker). Do not read `solution_svc_check.py` until you have tried.

Write `svc_check.py`, a tool you could call from a shell script or a pipeline:

    python3 svc_check.py URL [-t SECONDS] [-q]

1. Use `argparse`: a required `url`, an optional `-t` / `--timeout` (a number, default 2) and a `-q` / `--quiet` flag.
2. Call the URL with `requests.get(..., timeout=...)` and check the status with `raise_for_status()`.
3. Healthy (status 200): print `UP <url> 200` on standard output and exit with code 0.
4. Anything else (a 404, a 503, a refused connection, a timeout): print `DOWN <url> (<error name>)` on standard error and exit with code 1. No traceback. Catch `requests.RequestException`, never a bare `except:`.
5. With `-q` print nothing at all, but keep the same exit codes.
6. A missing URL must end with exit code 2 (argparse does this for you).
7. Finish with `sys.exit(main())` so the exit code always comes from one place.

Try it: start the lab API in one terminal with `python3 api06.py`, then run `python3 svc_check.py http://127.0.0.1:8081/health; echo $?` in another.

Check yourself: `bash check52.sh .` should print six PASS lines. The checker starts its own copy of the API on port 8099 and stops it again.

Report: copy `report_template.md` and fill it in with your commands and their output.
