# Lesson 48 task: a small inventory script

Work only in your own Ubuntu 24.04 virtual machine (Python 3, ideally inside a virtual environment from Lesson 47).

Files in this folder: `data48.py` (the data), `expected48.txt` (the exact output wanted), `check48.sh` (the checker). Do not read `solution_inventory.py` until you have tried.

Write `inventory.py` so that `python3 inventory.py` prints exactly the contents of `expected48.txt`:

1. Import the data with `from data48 import SERVERS` (a list of dictionaries with name, env and cpu).
2. Write a function `busy(servers, limit)` that returns the list of names whose cpu is above the limit.
3. Count servers per environment with a dictionary and a for loop (do not hard-code the numbers).
4. Compute the average cpu.
5. Put the printing under `if __name__ == "__main__":` so that importing inventory prints nothing.
6. Run the checker: `bash check48.sh .` (four PASS lines expected).

Write `report.md`: your commands and their output, plus where you got stuck.

Pass or fail rubric (all six): 1) checker shows four PASS; 2) busy takes a limit parameter and returns names; 3) counts come from a dictionary and a loop, not hard-coded; 4) data is imported, not copied; 5) report is complete; 6) you worked in your own virtual machine.

Status: UNVERIFIED until you run it yourself.
