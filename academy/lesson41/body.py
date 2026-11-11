RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "A command has three channels: one for input, one for normal output and one for errors. Once you control them, you can save output, hide noise and join commands together."),
  c('h2', "Today you learn four things. The three standard streams. Redirection, to send them to files. Pipes, to join commands. And safe temporary files."),
  c('h3', "Every demo is a real recording on Ubuntu."),
 ]),
 ('streams', [
  k('f1', "First, the three streams. Every command has standard in, numbered zero. Standard out, numbered one, for normal output. And standard error, numbered two, for errors. Watch both. List one file that exists, and one that does not. Type: L S, slash E T C slash hostname, space, slash nope."),
  k('f2', "Two lines on the screen. The error, and the file name. They look the same, but they travel on different streams. Now send standard out to a file with a greater than sign. Type: L S, slash E T C slash hostname, space, slash nope, greater than, out dot text."),
  k('f3', "Only the error is left on the screen. The normal output went into the file. Look inside it. Type: cat out dot text."),
  k('f4', "The file name, and no error. Now do the opposite. Two, greater than, sends the errors to a file. Type: L S, slash E T C slash hostname, space, slash nope, space, two greater than, err dot text."),
  k('f5', "Now the file name shows, and the error is gone. Check where it went. Type: cat err dot text."),
  c('f6', "The error message, saved. Stream one holds results. Stream two holds problems. Keep them apart, and each is easier to use."),
 ]),
 ('redir', [
  k('d1', "Next, more redirection. A single greater than creates the file, or replaces it. Type: echo first, greater than, log dot text."),
  k('d2', "Silent, because the output went into the file. Now two greater than signs append, and keep what is already there. Type: echo second, double greater than, log dot text."),
  k('d3', "Look at the file. Type: cat log dot text."),
  k('d4', "Both lines. A single greater than would have erased the first one, so be careful with it. A less than sign does the reverse: it feeds a file into a command as input. Count the lines. Type: W C, dash l, less than, log dot text."),
  k('d5', "Two lines. Now, a special file named slash dev slash null throws away everything written to it. Hide the error. Type: L S, slash nope, space, two greater than, slash dev slash null."),
  k('d6', "Nothing at all. But did the command succeed? Every command leaves an exit status, in the variable dollar question mark. Zero means success. Type: echo, dollar question mark."),
  c('d7', "Two, so it failed. Hiding the message did not hide the failure."),
 ]),
 ('pipes', [
  k('q1', "Now pipes. A pipe sends the standard out of one command into the standard in of the next. Here is the log again. Type: cat app dot log."),
  k('q2', "Six lines. Send them through grep, to keep only the errors. Type: cat app dot log, space, pipe, space, grep ERROR."),
  k('q3', "Two lines. Add another stage, to count them. Type: grep ERROR app dot log, space, pipe, space, W C, dash l."),
  k('q4', "Two errors. Now suppose you want to see the data and also save it. The tee command writes a copy to a file, and passes the data on. Type: grep ERROR app dot log, pipe, tee errors dot text, pipe, W C, dash l."),
  k('q5', "The count came out, and the file was written on the way. Check it. Type: cat errors dot text."),
  c('q6', "The two error lines, saved. Remember, a pipe carries standard out only. Errors still go to the screen, unless you redirect them."),
 ]),
 ('tmp', [
  k('t1', "Last, temporary files. A script often needs a scratch file. Never invent a fixed name, because it is predictable, and other users can plant a link there. Ask for a safe one with M K temp. Type: f equals dollar, open round bracket, M K temp, close round bracket."),
  k('t2', "Silent, because the name went into the variable f. Look at it. Type: echo, double quote, dollar f, double quote."),
  k('t3', "A new file in slash temp, with a random name that nobody can guess, created with private permissions. Write the errors into it. Type: grep ERROR app dot log, greater than, double quote, dollar f, double quote."),
  k('t4', "Count its lines. Type: W C, dash l, less than, double quote, dollar f, double quote."),
  k('t5', "Two lines. When you are finished, always clean up. Type: R M, double quote, dollar f, double quote."),
  k('t6', "Check that it is gone. Type: L S, double quote, dollar f, double quote."),
  c('t7', "No such file. Make, use, remove. In the next lessons, a trap will do that cleanup even when a script fails."),
 ]),
 ('build', [
  k('w1', "Now a small job that uses everything. Count the log levels, save the report, and keep the problems apart. Here is the log. Type: cat app dot log."),
  k('w2', "Count the levels, and send the report to a file. Type: awk, single quote, open brace, print dollar three, close brace, single quote, app dot log, pipe, sort, pipe, unique dash c, greater than, out dot text."),
  k('w3', "No output, because it went to the file. Look at the report. Type: cat out dot text."),
  k('w4', "Two errors, three info lines and one warning. Now run grep on a good file and a missing one, and keep the errors in their own file. Type: grep, dash c, ERROR, app dot log, missing dot log, two greater than, problems dot text."),
  k('w5', "The count for the good file. The complaint about the missing file went elsewhere. Look. Type: cat problems dot text."),
  c('w6', "Results on the screen, problems in a file. That is a script you can trust."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: greater than adds to a file. No. It replaces the file. To add, use two greater than signs."),
  c('my3', "Myth two: a pipe carries errors too. No. It carries standard out only. Errors need two greater than."),
  c('my4', "Myth three: slash dev slash null stores output. No. It throws everything away."),
  c('my5', "Myth four: a fixed name in slash temp is fine. No. It is predictable. Use M K temp."),
  c('my6', "Streams. Redirects. Pipes. Safe temp files."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding. Six points, and you need all six."),
  c('b2', "Name the three standard streams, and their numbers: zero, one and two."),
  c('b3', "Redirect output with greater than and double greater than, and input with less than."),
  c('b4', "Send errors to a file with two greater than, or discard them with slash dev slash null."),
  c('b5', "Join commands with a pipe, and save a copy with tee."),
  c('b6', "Create a temporary file with M K temp, and remove it when done."),
  c('b7', "Read the exit status, with dollar question mark."),
  c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Type every command yourself."),
  c('z2', "One: list one file that exists and one that does not, and see both streams on the screen."),
  c('z3', "Two: write a line to a file with greater than, add one with double greater than, and count with less than."),
  c('z4', "Three: send errors to a file with two greater than, then discard them with slash dev slash null, and print the exit status."),
  c('z5', "Four: build a pipeline with tee, and check the saved copy."),
  c('z6', "Five: make a temporary file with M K temp, write to it, read it back and remove it."),
  c('z7', "Six: save a report to one file, and the errors to another."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which number is standard error?"), c('f13', "What is the difference between greater than, and double greater than?"),
  c('f14', "Does a pipe carry errors?"), c('f15', "Which command makes a safe temporary file?"),
  c('f16', "Objective covered: MC05-O05.", "Objective covered: M C zero five, objective five, in the Bash scripting masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: error handling, traps, logging and exit codes."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'f6': 0.5, 'd7': 0.5, 'q6': 0.5, 't7': 0.5, 'w6': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'streams': 'The three streams', 'redir': 'Redirection', 'pipes': 'Pipes and tee', 'tmp': 'Safe temporary files', 'build': 'Put it together', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
