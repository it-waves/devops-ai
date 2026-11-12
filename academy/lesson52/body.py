RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Today your scripts learn to speak to the command line."),
  c('h2', "Run by a person, a script can explain itself. Run by a pipeline, it only has a number. Three habits make a script a proper tool: arguments with argparse, exit codes, and two output channels."),
  c('h3', "Every demo is typed live on Ubuntu twenty-four oh four."),
 ]),
 ('why', [
  c('w1', "A script you run by hand can talk to you. A script that runs in a pipeline cannot. So it needs a clear way to take input, and a clear way to report the result."),
  c('w2', "Input comes from the command line. Arguments are what the tool needs, flags are options. Argparse reads them, checks their types, and even writes the help for you."),
  c('w3', "The result is the exit code. Zero means success. Anything else means failure. By convention, one is a failure, and two means the command was used wrongly."),
  c('w4', "And output has two channels. Standard out carries results. Standard error carries problems. A pipeline can keep one and show you the other."),
  c('w5', "The rule: arguments in, exit code out, and problems to standard error."),
 ]),
 ('cli', [
  k('a1', "Let's build a real tool, one you could drop into a pipeline. It checks whether a network port is open. Show the script. Type: cat, port check dot P Y."),
  k('a2', "Sixteen lines. Argparse reads the command line: a host, a port that must be a number, and an optional dash Q flag. The try and except decides the result, and the number the script returns becomes the exit code. Ask the tool how to use it. Type: dot slash, port check dot P Y, dash H."),
  k('a3', "Free documentation, written by argparse: the usage line, the two arguments, and the dash Q option. Now use it, on the lab A P I. Type: dot slash, port check dot P Y, local host, eighty eighty-one."),
  k('a4', "Open. The port answers, and the result went to standard out. But the script also left a number for the shell. Ask for it. Type: echo, dollar sign, question mark."),
  k('a5', "Zero. Zero means success. Now a port where nothing is listening. Type: dot slash, port check dot P Y, local host, one."),
  k('a6', "Closed, connection refused, and no traceback. The problem went to standard error. Ask for the exit code. Type: echo, dollar sign, question mark."),
  k('a7', "One. Failure. Any caller can tell, without reading a single word. Now a mistake by the user: a port that is not a number. Type: dot slash, port check dot P Y, local host, A B C."),
  k('a8', "Argparse refused it, printed the usage, and gave a clear error, all by itself, and the script never ran. What exit code? Type: echo, dollar sign, question mark."),
  c('a9', "Two. By convention: zero is success, one is failure, and two means the command was used wrongly. Three outcomes, three numbers, and a caller can react to each."),
 ]),
 ('shell', [
  k('b1', "Now the part that makes exit codes powerful: the shell. Our closed message was an error, so it travelled on standard error. Throw standard error away, with two, greater than, slash dev, slash null. Type: dot slash, port check dot P Y, local host, one, space, two, greater than, slash dev, slash null."),
  k('b2', "Nothing on screen. The message is gone, but the exit code is still one. Now the dash Q flag, with the double ampersand, which means: run the next command only if this one succeeded. Type: dot slash, port check dot P Y, dash Q, local host, eighty eighty-one, space, ampersand, ampersand, space, echo up."),
  k('b3', "Up. The shell read a zero and chose. Now the opposite. The double pipe means: run the next command only if this one failed. Type: dot slash, port check dot P Y, dash Q, local host, one, space, pipe, pipe, space, echo down."),
  c('b4', "Down. The tool said nothing, and the shell still chose, from the exit code alone. This is how pipelines, cron jobs and C I systems decide whether to go on. They never read your messages. They read the number. A tool that always exits zero lies to its pipeline."),
 ]),
 ('task', [
  c('t1', "Here is your task, with everything you need. The files are in the repository, and in the description."),
  k('t2', "The repository is git hub dot com, slash it dash waves, slash dev ops dash A I."),
  k('t3', "In the academy slash lesson fifty-two folder you will find the task file, the lab A P I, and the checker, check fifty-two dot S H."),
  c('t4', "You write one file, service check dot P Y. It takes a U R L, calls it with a timeout, and prints up when the page answers two hundred."),
  c('t5', "Any failure prints down on standard error and exits with code one, with no traceback. A missing U R L must exit with code two. And dash Q makes it silent, with the same exit codes."),
  c('t6', "Do not open the solution file until you have really tried."),
  c('t7', "The checker shows six pass lines. Write your results in a report."),
 ]),
 ('rubric', [
  c('r1', "Here is how your work is judged. Six points, and you need all six."),
  c('r2', "The checker shows six pass lines."), c('r3', "Exit codes are right: zero, one, and two."),
  c('r4', "Results go to standard out, and problems go to standard error."), c('r5', "You use argparse, and every call has a timeout."),
  c('r6', "No traceback, and never a bare except."), c('r7', "The report is complete, and you worked in your own virtual machine."), c('r8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: get the lesson folder, and activate your virtual environment."),
  c('z3', "Two: start the lab A P I in one terminal."),
  c('z4', "Three: write service check dot P Y with argparse: a U R L, a timeout, and a quiet flag."),
  c('z5', "Four: call the U R L with a timeout, and catch request exception."),
  c('z6', "Five: print up on standard out, or down on standard error, and return zero or one."),
  c('z7', "Six: run the checker, and write your report."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What does exit code zero mean?"), c('f13', "Which channel carries the problems?"),
  c('f14', "What exit code means the command was used wrongly?"), c('f15', "Why does a pipeline read the exit code, not your messages?"),
  c('f16', "Objective covered: MC06-O06, command line tools and exit codes."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: tests with pytest and mocks."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'w5': 0.5, 'a9': 0.5, 'b4': 0.5, 'a1': 0.3, 't7': 0.5, 'r8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'why': 'Arguments, exit codes, two channels', 'cli': 'argparse and exit codes', 'shell': 'Exit codes in the shell', 'task': 'Get the lab and task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
