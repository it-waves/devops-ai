# Lesson 47 report (Python setup, venv, requirements)

For every step, paste the command you typed and its output.

1. Python version and sys.prefix of the system Python
2. Create the environment: python3 -m venv .venv, then ls -a
3. Activate, which python, pip install (package of your choice), pip list
4. pip freeze > requirements.txt, then cat requirements.txt
5. Layout: src/servers/__init__.py, tests, .gitignore
6. Fresh environment: pip install -r requirements.txt, then pip freeze | diff - requirements.txt, then echo $?
7. Checker output (five PASS lines expected)
8. Cleanup proof: deactivate, remove the project folder, list the parent folder
9. Where I got stuck, and what unstuck me
