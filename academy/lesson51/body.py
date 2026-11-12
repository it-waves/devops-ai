RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Today your scripts learn to fail well."),
  c('h2', "Every script meets trouble: a missing file, a bad value, a server that is busy. Three habits turn a crash into a controlled result: exceptions, logging, and retries."),
  c('h3', "Every demo is typed live on Ubuntu twenty-four oh four."),
 ]),
 ('why', [
  c('w1', "When something goes wrong, Python raises an exception. If nothing catches it, the script stops with a traceback."),
  c('w2', "Try holds the risky code. Except handles one named kind of failure. Else runs when nothing failed, and finally always runs."),
  c('w3', "Logging is how a script tells operators what happened. It has levels: debug, info, warning, and error."),
  c('w4', "Retries handle temporary failures. Wait, try again, and wait longer each time."),
  c('w5', "The rule: catch what you expect, say what happened, and retry only what can recover."),
 ]),
 ('exceptions', [
  k('e1', "First, an exception. Start Python. Type: python three, dash Q."),
  k('e2', "Ask Python to turn a word into a number. Type: int, open bracket, quote, eight, quote, close bracket."),
  k('e3', "A traceback. Read it from the bottom. The last line names the exception, value error, and says why. The lines above show where it happened. Leave Python. Type: exit, open, close."),
  k('e4', "Now a script that expects trouble. Show it. Type: cat load dot P Y."),
  k('e5', "It tries to open settings dot jay son. Each except block handles one named failure. Else runs when all went well, and finally always runs. Run it, with no settings file. Type: python three, load dot P Y."),
  k('e6', "File not found, handled. The script chose defaults and carried on. Now create a valid settings file. Type: echo, then the jay son with retries five, in single quotes, redirected into settings dot jay son."),
  k('e7', "No output, the file is written. Run the script again. Type: python three, load dot P Y."),
  k('e8', "Loaded settings, finally ran, and retries is five. Now break the file on purpose. Type: echo, single quote, open brace, bad, single quote, redirected into settings dot jay son."),
  k('e9', "Run it one more time. Type: python three, load dot P Y."),
  c('e10', "Bad jay son, caught and explained, with no crash. Catch the specific exceptions you expect. A bare except hides real bugs, so avoid it."),
 ]),
 ('logging', [
  k('l1', "Now logging. Print is for users. Logging is for operators, because it has levels. Show the script. Type: cat log demo dot P Y."),
  k('l2', "The level is set to info, so the debug line will stay hidden. Log dot exception records the message and the traceback. Run it. Type: python three, log demo dot P Y."),
  k('l3', "Info, warning, error, each tagged with its level. The debug line is hidden, and the error came with its traceback, so you can find the cause. Now turn the detail down. Type: sed, dash I, quote, S slash, I N F O, slash, W A R N I N G, slash, quote, log demo dot P Y."),
  k('l4', "No output. Run it again. Type: python three, log demo dot P Y."),
  c('l5', "Now only the warning and the error appear. Same code, less noise. In production you lower the level to keep logs short, and raise the detail when you hunt a problem."),
 ]),
 ('retry', [
  k('y1', "Last, retries. A busy server or a dropped connection is temporary. This script tries up to four times, logs every attempt, and waits longer each time. Show it. Type: cat retry dot P Y."),
  k('y2', "The wait doubles: one second, two, four. That is called back off. Our lab address, flaky, fails twice and then works. Run it. Type: python three, retry dot P Y."),
  k('y3', "Two warnings, then success on attempt three. Now let it give up sooner, with only two attempts. Type: sed, dash I, quote, S slash, range, open bracket, one, comma, five, close bracket, slash, range, open bracket, one, comma, three, close bracket, slash, quote, retry dot P Y."),
  k('y4', "No output. Run it again. Type: python three, retry dot P Y."),
  k('y5', "Both attempts failed, and the script gave up with a clear message, not a crash. Now check its exit code. Type: echo, dollar sign, question mark."),
  c('y6', "One. Not zero means failure, so any caller can tell. Retry only temporary problems, like timeouts and five hundred errors. A wrong token or a missing page never fixes itself, so fail fast."),
 ]),
 ('task', [
  c('t1', "Here is your task, with everything you need. The files are in the repository, and in the description."),
  k('t2', "The repository is git hub dot com, slash it dash waves, slash dev ops dash A I."),
  k('t3', "In the academy slash lesson fifty-one folder you will find the task file, the lab A P I, and the checker, check fifty-one dot S H."),
  c('t4', "You write one file, fetch retry dot P Y. It calls the flaky address with a timeout, tries up to four times, and waits one, two, then four seconds."),
  c('t5', "Every attempt is logged with the logging module. On success it prints recovered. After four failures it logs gave up and exits with code one, with no traceback."),
  c('t6', "Do not open the solution file until you have really tried."),
  c('t7', "The checker shows four pass lines. Write your results in a report."),
 ]),
 ('rubric', [
  c('r1', "Here is how your work is judged. Six points, and you need all six."),
  c('r2', "The checker shows four pass lines."), c('r3', "Every attempt is logged at the right level."),
  c('r4', "You catch request exception, never a bare except."), c('r5', "Every call has a timeout, and the wait grows between attempts."),
  c('r6', "After the last failure: a clear message, exit code one, no traceback."), c('r7', "The report is complete, and you worked in your own virtual machine."), c('r8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: get the lesson folder, and activate your virtual environment."),
  c('z3', "Two: start the lab A P I in one terminal."),
  c('z4', "Three: write fetch retry dot P Y with a loop of four attempts and a timeout."),
  c('z5', "Four: catch request exception, and log each failure with logging."),
  c('z6', "Five: wait longer after each failure, and give up with exit code one."),
  c('z7', "Six: run the checker, and write your report."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Why is a bare except a bad idea?"), c('f13', "Which level would you use for a failed attempt?"),
  c('f14', "Why does the wait grow between retries?"), c('f15', "Which failures are worth retrying?"),
  c('f16', "Objective covered: MC06-O05, exceptions, logging, and retries."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: command line tools and exit codes."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'w5': 0.5, 'e10': 0.5, 'l5': 0.5, 'y6': 0.5, 'y2': 3.5, 'y4': 3.5, 'e1': 0.3, 'l2': 0.3, 't7': 0.5, 'r8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'why': 'Exceptions, logging, retries', 'exceptions': 'try, except, else, finally', 'logging': 'Logging levels', 'retry': 'Retries with back off', 'task': 'Get the lab and task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
