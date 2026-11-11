RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Scripts fail. A disk fills up, a file is missing, a server does not answer. The question is whether your script notices, stops safely, cleans up and tells you what happened."),
  c('h2', "Today you learn four things. Exit codes. Strict mode, to stop on the first failure. Traps, to clean up. And logging, to leave a clear record."),
  c('h3', "Every demo is a real recording on Ubuntu."),
 ]),
 ('exitcodes', [
  k('e1', "First, exit codes. Every command ends with a number. Zero means success, and anything else means failure. Run a command that works. Type: L S, slash E T C slash hostname."),
  k('e2', "It printed the file name. Now ask for its exit code, with dollar question mark. Type: echo, dollar question mark."),
  k('e3', "Zero, success. Now a command that fails. Type: L S, slash nope."),
  k('e4', "An error message. Ask for the exit code again. Type: echo, dollar question mark."),
  k('e5', "Two. Not zero, so the command failed. Your own scripts can return a code too, with the exit command. Here is a small check script. Type: cat check dot S H."),
  k('e6', "If the log contains the word ERROR, the script prints a message and exits with one. Otherwise it prints clean, and exits with zero. Run it. Type: bash check dot S H."),
  k('e7', "It found errors. Check the code. Type: echo, dollar question mark."),
  c('e8', "One. Other tools, like pipelines and schedulers, read this number, to decide what to do next."),
 ]),
 ('strict', [
  k('s1', "Next, strict mode. By default, bash carries on after an error, and that can be dangerous. Here is a loose script. Type: cat loose dot S H."),
  k('s2', "It tries to change into a folder that does not exist, and then carries on. Run it. Type: bash loose dot S H."),
  k('s3', "The cd failed, but the script went on. It reported a folder that is not the one it wanted, and used a variable that was never set. Now a strict version. Type: cat strict dot S H."),
  k('s4', "The set line has three options. Dash E stops at the first failing command. Dash U treats an unset variable as an error. And pipe fail makes a pipeline fail if any stage fails. Run it. Type: bash strict dot S H."),
  k('s5', "It stopped at the failed cd, and nothing after it ran. Check the exit code. Type: echo, dollar question mark."),
  k('s6', "One. Now see what dash U does. Here is a script that uses a variable that was never set. Type: cat unset dot S H."),
  k('s7', "Run it. Type: bash unset dot S H."),
  c('s8', "Unbound variable. Without dash U, the script would have printed an empty name, and gone on."),
 ]),
 ('trap', [
  k('t1', "Stopping early is good, but a script that stops can leave a mess. A trap runs a command when something happens. Here is a script with a trap on the word EXIT. Type: cat trap dot S H."),
  k('t2', "It makes a temporary file, and sets a trap that removes the file and prints a message. Then a command fails. Run it. Type: bash trap dot S H."),
  k('t3', "The script stopped at the failure, and the trap still ran. Check the exit code. Type: echo, dollar question mark."),
  k('t4', "One, still a failure. Now check that nothing was left behind in slash temp. Type: L S, slash temp."),
  c('t5', "Empty. The trap on EXIT runs however the script ends: success, failure or an interrupt. That is how you clean up safely."),
 ]),
 ('logging', [
  k('l1', "Next, logging. A good script says what it is doing, and when. Here is a small log function. Type: cat log dot S H."),
  k('l2', "The function prints the time, a level and a message, to standard error, with the redirect, greater than ampersand two. Run it. Type: bash log dot S H."),
  k('l3', "Messages with times, on the screen. Because they went to standard error, you can capture them without touching the normal output. Type: bash log dot S H, space, two greater than, run dot log."),
  k('l4', "Silent, because the log went into the file. Look inside. Type: cat run dot log."),
  c('l5', "A timestamped record. Results on standard out, and logs on standard error, so each can go to its own place."),
 ]),
 ('build', [
  k('w1', "Now put it all together, in one safe script. Strict mode, a temporary file, a trap, and an exit code. Type: cat safe dot S H."),
  k('w2', "Notice or true after grep. When grep finds no match, it exits with one, and strict mode would stop the script. Or true says: that is allowed. Run it. Type: bash safe dot S H."),
  k('w3', "Two errors. The script then exits with one, to tell the caller. Check it. Type: echo, dollar question mark."),
  c('w4', "Strict, clean, and honest about the result. That is a script you can run from a scheduler, and trust."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: exit code zero means failure. No. Zero means success. Anything else is a failure."),
  c('my3', "Myth two: set dash E catches every error. No. Commands inside an if test, or before or or, are exempt."),
  c('my4', "Myth three: a trap only runs on control C. No. A trap on EXIT runs however the script ends."),
  c('my5', "Myth four: logs belong on standard out. No. Put results on standard out, and logs on standard error."),
  c('my6', "Exit codes. Strict mode. Traps. Logs."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding. Six points, and you need all six."),
  c('b2', "Read an exit code with dollar question mark, and know that zero means success."),
  c('b3', "Return your own exit code with the exit command."),
  c('b4', "Use set dash E U O pipe fail, and explain each option."),
  c('b5', "Clean up with a trap on EXIT."),
  c('b6', "Write timestamped log lines to standard error."),
  c('b7', "Allow an expected failure with or true."),
  c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Type every command yourself."),
  c('z2', "One: run a command that works and one that fails, and print each exit code."),
  c('z3', "Two: write a script that exits with one when a file contains a word, and zero when it does not."),
  c('z4', "Three: add set dash E U O pipe fail, and prove that it stops at the first failure."),
  c('z5', "Four: add a trap on EXIT that removes a temporary file, and check that none is left."),
  c('z6', "Five: add a log function that writes timestamps to standard error, and save them to a file."),
  c('z7', "Six: run grep on a file with no match, and make the script survive with or true."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which exit code means success?"), c('f13', "What does set dash U do?"),
  c('f14', "When does a trap on EXIT run?"), c('f15', "Where should log messages go?"),
  c('f16', "Objective covered: MC05-O06.", "Objective covered: M C zero five, objective six, in the Bash scripting masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: secrets, permissions, input validation and injection risks."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'e8': 0.5, 's8': 0.5, 't5': 0.5, 'l5': 0.5, 'w4': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'exitcodes': 'Exit codes', 'strict': 'Strict mode', 'trap': 'Clean up with trap', 'logging': 'Logging', 'build': 'Put it together', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
