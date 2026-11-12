RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Welcome to the Python for DevOps masterclass. Before any code, one habit that separates a script that works on your machine from a tool a whole team can trust: the virtual environment."),
  c('h2', "Today: check your Python, create a virtual environment, install a package, record the exact versions in a requirements file, rebuild the environment from that file, and lay out a clean project."),
  c('h3', "Every terminal demo is a real recording on Ubuntu twenty-four oh four, with real installs from the Python package index."),
 ]),
 ('why', [
  c('w1', "Why not just install packages for the whole machine? Because Ubuntu itself uses Python."),
  c('w2', "The system Python belongs to the operating system. Add or upgrade packages there, and you can break the tools the system relies on."),
  c('w3', "Two projects can also need different versions of the same package. One machine, one global copy, so one of them loses."),
  c('w4', "A virtual environment solves both. It is a folder inside your project, with its own Python and its own packages. Delete the folder, and everything is gone."),
  c('w5', "The recipe has three parts. Create the environment. Activate it. Install into it. Then freeze the versions into a file, so anyone can rebuild it."),
 ]),
 ('setup', [
  k('s1', "First, check your Python. Type: python three, dash dash version."),
  k('s2', "Python three point twelve, the version that ships with Ubuntu twenty-four oh four. Where does this Python live? Ask it for its prefix. Type: python three, dash C, then a line that prints sys dot prefix."),
  k('s3', "Slash U S R. That is the system Python, owned by the operating system, so we never install packages into it. Make a project folder. Type: M K dir, inventory."),
  k('s4', "Go inside. Type: C D, inventory."),
  k('s5', "Now create a virtual environment. Type: python three, dash M, V env, dot V env. Python three, dash M, V env, builds the environment, and dot V env is the folder name."),
  k('s6', "It takes a few seconds. List the folder, including hidden files. Type: L S, dash A."),
  c('s7', "A hidden folder called dot V env now sits inside the project. It holds a private copy of Python, and a private place for packages."),
 ]),
 ('activate', [
  k('a1', "Now turn the environment on. Type: source, dot V env, slash bin, slash activate."),
  k('a2', "The prompt now starts with dot V env, in brackets. That is your reminder that the environment is active. Where is Python now? Type: which python."),
  k('a3', "The path points inside the project folder. This is the Python you are using now. Install a package. Type: pip, install, dash Q, requests."),
  k('a4', "Dash Q means quiet, so pip only prints problems. It fetched requests from the Python package index, called pie P I. List what is installed. Type: pip list."),
  k('a5', "Requests, four packages it needs, called dependencies, and pip itself. Look closer at one. Type: pip, show, requests, pipe, grep, Version."),
  c('a6', "The exact version. Versions matter, because the same code can behave differently on a different version. Next, we record them."),
 ]),
 ('deps', [
  k('d1', "To share exactly what you installed, freeze it. Type: pip, freeze."),
  k('d2', "Every package, with an exact version, joined by two equals signs. This is called pinning. Save it to a file. Type: pip, freeze, then a redirect into requirements dot text."),
  k('d3', "Nothing printed, because the output went into the file. Show the file. Type: cat, requirements dot text."),
  k('d4', "The same five lines. This file is the recipe for your environment, and it belongs in Git. Now leave the environment. Type: deactivate."),
  k('d5', "The prompt is back to normal. Now prove the isolation. Try to use requests from the system Python. Type: python three, dash C, import requests."),
  c('d6', "No module named requests. The system Python never saw it. Each project has its own packages, and nothing leaks between projects."),
 ]),
 ('repro', [
  k('r1', "Now the real test. A teammate clones your project. They get no dot V env, only your files. List the folder. Type: L S."),
  k('r2', "Just the requirements file. Create a fresh environment. Type: python three, dash M, V env, dot V env."),
  k('r3', "Activate it. Type: source, dot V env, slash bin, slash activate."),
  k('r4', "Install from the file. Type: pip, install, dash Q, dash R, requirements dot text. Dash R means: read the list from this file."),
  k('r5', "Now compare what is installed with the file. Type: pip, freeze, pipe, diff, dash, requirements dot text."),
  k('r6', "No output, which means no difference. Check the exit status. Type: echo, dollar, question mark."),
  c('r7', "Zero. The new environment matches yours exactly. That is reproducibility, and it is the whole point of the file."),
 ]),
 ('layout', [
  k('l1', "Now the project structure. Code goes in a source folder, and tests go in a tests folder. Type: M K dir, dash P, source slash inventory, and tests."),
  k('l2', "Add an init file, so Python treats the folder as a package. Type: touch, source slash inventory slash, init, dot P Y."),
  k('l3', "Tell Git to ignore the environment. You commit the recipe, never the environment itself. Type: echo, dot V env slash, redirect, dot git ignore."),
  k('l4', "Show the layout, skipping dot V env. Type: find, dot, dash path, dot slash dot V env, dash prune, dash O, dash print."),
  k('l5', "That is the shape: requirements, source, tests, and the ignore file. Now run the checker, which comes with this lesson. Type: bash, dot dot slash, check forty-seven dot S H, and a dot."),
  c('l6', "Five PASS lines. Your project is isolated, pinned, reproducible, and tidy."),
 ]),
 ('cleanup', [
  k('c1', "Cleanup, with proof. List the project first. Type: L S, dash A."),
  k('c2', "Leave the folder. Type: C D, dot dot."),
  k('c3', "Delete the whole project, environment included. Type: R M, dash R F, inventory."),
  k('c4', "Now prove it is gone. Type: L S."),
  c('c5', "Only the checker file is left. Removing a virtual environment is just deleting a folder. Nothing was installed into the system."),
 ]),
 ('task', [
  c('t1', "Here is your task, with everything you need. The files are in the repository, and in the description."),
  k('t2', "The repository is git hub dot com, slash it dash waves, slash dev ops dash A I."),
  k('t3', "In the academy slash lesson forty-seven folder you will find the task file, and the checker, check forty-seven dot S H."),
  c('t4', "You need an Ubuntu virtual machine with Python three and the venv package. On Ubuntu, that is the package called python three dash venv."),
  c('t5', "Build a project called servers. Create the environment, install one package, and pin it."),
  c('t6', "Add the layout, prove a fresh environment matches the file, run the checker, and clean up with proof."),
  c('t7', "Write your results in a report, with the commands and their output."),
 ]),
 ('rubric', [
  c('b1', "Here is how your work is judged. Six points, and you need all six."),
  c('b2', "The checker shows five pass lines."), c('b3', "The requirements file has exact, pinned versions."),
  c('b4', "A fresh environment matches the file, with no difference."), c('b5', "The environment folder is ignored by Git."),
  c('b6', "The cleanup proof shows nothing left behind."), c('b7', "You worked only in your own virtual machine, and never installed into the system Python."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: make the servers folder, and create the environment."),
  c('z3', "Two: activate it, and install one package."),
  c('z4', "Three: freeze the versions into requirements dot text."),
  c('z5', "Four: build the layout, and the ignore file."),
  c('z6', "Five: make a fresh environment, and prove it matches."),
  c('z7', "Six: run the checker, then clean up with proof."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Why do we use a virtual environment?"), c('f13', "Which command turns it on?"),
  c('f14', "What does pip freeze give you?"), c('f15', "Why is the environment folder not committed to Git?"),
  c('f16', "Objective covered: M C zero six, objective one, setting up Python, virtual environments, dependencies, and project structure."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: Python types, collections, and functions."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'w5': 0.5, 's5': 3.0, 's6': 1.0, 's7': 0.5, 'a1': 0.5, 'a3': 7.0, 'a4': 1.0, 'a6': 0.5, 'd6': 0.5, 'r2': 3.0, 'r4': 7.0, 'r7': 0.5, 'l6': 0.5, 'c5': 0.5, 't7': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'why': 'Why virtual environments', 'setup': 'Check Python and create a venv', 'activate': 'Activate and install', 'deps': 'Freeze the versions', 'repro': 'Rebuild from the file', 'layout': 'Project layout and checker', 'cleanup': 'Cleanup with proof', 'task': 'Get the lab and task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
