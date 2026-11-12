# Lesson 47 task: a reproducible Python project

Work only in your own Ubuntu 24.04 virtual machine. Never install into the system Python (no sudo pip).

1. Make a folder called `servers` and create a virtual environment named `.venv` inside it.
2. Activate it and install one package of your choice (for example `pyyaml`).
3. Save the exact versions: `pip freeze > requirements.txt`.
4. Build the layout: `src/servers/__init__.py`, a `tests` folder, and a `.gitignore` that ignores `.venv/`.
5. Prove it is reproducible: make a second environment, install with `pip install -r requirements.txt`, and show that `pip freeze | diff - requirements.txt` prints nothing.
6. Run the checker from this folder: `bash check47.sh PATH/TO/servers` (five PASS lines expected).
7. Clean up with proof: deactivate, remove the project folder, list the parent folder.

Write your answers in `report.md`: the command you ran and the output for every step, plus where you got stuck.

Pass or fail rubric (all six): 1) checker shows five PASS; 2) requirements.txt has exact pinned versions; 3) the fresh environment matches the file; 4) .venv is ignored by Git; 5) cleanup proof shows nothing left; 6) you ran everything in your own virtual machine and never installed packages into the system Python.

Status: UNVERIFIED until you run it yourself.
