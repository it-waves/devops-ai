SCENES = [
 ('hook', [
  c('h1', "A server is never idle. Something is always running."),
  c('h2', "A process is a running program. When one misbehaves, you need to find it, read it, and stop it."),
  c('h3', "Today you list processes, send signals, and check how busy the machine is."),
 ]),
 ('ps', [
  c('p1', "Start with the simplest list. Type: ps.", "Start with the simplest list. Type: P S."),
  c('p2', "Only your own shell, and P S itself. Every process has a number, the P I D, and a name."),
  c('p3', "Now every process on the system, with the columns you choose. Type: ps -eo pid,user,comm.", "Now every process on the system, with the columns you choose. Type: P S, dash e o, pid, comma, user, comma, comm."),
  c('p4', "Three columns: the P I D, the owner, and the command. Process number one is the parent of everything else."),
  c('p5', "Add C P U and memory. Type: ps -eo pid,pcpu,pmem,comm.", "Add C P U and memory. Type: P S, dash e o, pid, comma, P C P U, comma, P mem, comma, comm."),
  c('p6', "Percent of one C P U, and percent of memory. Those two columns find a hungry process fast."),
 ]),
 ('signals', [
  c('s1', "Start a program in the background. Type: sleep 300 &. The ampersand returns your prompt at once.", "Start a program in the background. Type: sleep, three hundred, ampersand. The ampersand returns your prompt at once."),
  c('s2', "Bracket one is the job number. The next number is its P I D. Check with: jobs.", "Bracket one is the job number. The next number is its P I D. Check with: jobs."),
  c('s3', "Stop it politely. Type: kill %1. That sends the term signal, number fifteen. The program may clean up, then exit.", "Stop it politely. Type: kill, percent one. That sends the term signal, number fifteen. The program may clean up, then exit."),
  c('s4', "Check again with: jobs. Terminated.", "Check again with: jobs. Terminated."),
  c('s5', "Now a runaway program. Type: yes > /dev/null &. It burns a whole C P U doing nothing.", "Now a runaway program. Type: yes, greater than, slash dev slash null, ampersand. It burns a whole C P U doing nothing."),
  c('s6', "Find it. Sort by C P U, and show the top three. Type: ps -eo pid,pcpu,comm --sort=-pcpu | head -n 4.", "Find it. Sort by C P U, and show the top three. Type: P S, dash e o, pid, comma, P C P U, comma, comm, dash dash sort equals dash P C P U, pipe, head, dash n, four."),
  c('s7', "Yes is at the top, near one hundred percent. Stop it with: kill -9 %1. Signal nine cannot be ignored. Use it last.", "Yes is at the top, near one hundred percent. Stop it with: kill, dash nine, percent one. Signal nine cannot be ignored. Use it last."),
  c('s8', "Order of force: term first, kill only if term fails. Control C sends the int signal from your keyboard."),
 ]),
 ('resources', [
  c('r1', "How busy is the machine? Type: uptime.", "How busy is the machine? Type: up time."),
  c('r2', "The three numbers are the load average, over one, five and fifteen minutes. Compare them with the number of C P U cores."),
  c('r3', "Count the cores. Type: nproc.", "Count the cores. Type: N proc."),
  c('r4', "A load above the core count means work is waiting. Now memory. Type: free -h | column -t. Column tidies the table.", "A load above the core count means work is waiting. Now memory. Type: free, dash h, pipe, column, dash t. Column tidies the table."),
  c('r5', "Look at the available column, not free. Linux uses spare memory as cache, and gives it back when needed."),
 ]),
 ('running', [
  c('u1', "Is a program running? Start one. Type: sleep 300 &.", "Is a program running? Start one. Type: sleep, three hundred, ampersand."),
  c('u2', "Now ask by name. Type: pgrep -a sleep. It prints the P I D and the command.", "Now ask by name. Type: P grep, dash a, sleep. It prints the P I D and the command."),
  c('u3', "Stop everything with that name. Type: pkill sleep.", "Stop everything with that name. Type: P kill, sleep."),
  c('u4', "Ask again. Type: pgrep sleep. No output.", "Ask again. Type: P grep, sleep. No output."),
  c('u5', "Read the exit status. Type: echo $?.", "Read the exit status. Type: echo, dollar, question mark."),
  c('u6', "One means nothing matched. Zero means found. Scripts and monitoring tools use this exit status to test whether a service is up."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: kill dash nine is the normal way to stop a program. No. Term first, so it can clean up."),
  c('my3', "Myth two: high memory use means a problem. Not always. Linux caches. Read available."),
  c('my4', "Myth three: a process with a high load is the only suspect. Check the load against the core count."),
  c('my5', "Myth four: kill only kills. It sends signals, and most signals ask politely."),
  c('my6', "Term first. Kill last."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "List processes with P I D, user and command.", "List processes with P I D, user and command."),
  c('b3', "Start a job in the background, and find it."), c('b4', "Stop it with term, and say when kill dash nine is needed.", "Stop it with term, and say when kill dash nine is needed."),
  c('b5', "Find the process using the most C P U."), c('b6', "Read the load average against the core count."),
  c('b7', "Check if a program runs with P grep, and read its exit status.", "Check if a program runs with P grep, and read its exit status."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your virtual machine. These commands are safe, but only stop programs you started."),
  c('z2', "One: list processes with P I D, user and command, and find process number one."),
  c('z3', "Two: start a sleep in the background, and find it with jobs and with P grep."),
  c('z4', "Three: stop it with a normal kill, and confirm it is gone."),
  c('z5', "Four: start yes, sent to dev null, find it at the top by C P U, then stop it."),
  c('z6', "Five: read uptime and nproc, and say in one sentence if your machine is busy."),
  c('z7', "Six: check free dash h, and explain the difference between free and available.", "Six: check free, dash h, and explain the difference between free and available."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which character starts a command in the background?"), c('f13', "Which signal does a plain kill send?"),
  c('f14', "Which memory column should you read?"), c('f15', "What exit status means a process was found?"),
  c('f16', "Objective covered: MC04-O05.", "Objective covered: M C zero four, objective five, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: system D services, logs and scheduled jobs.", "Next lesson: system D services, logs and scheduled jobs."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'p2': 0.4, 'p4': 0.4, 'p6': 0.5, 's4': 0.5, 's7': 0.5, 's8': 0.5, 'r2': 0.5, 'r5': 0.5, 'u6': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'ps': 'List processes', 'signals': 'Background jobs and signals', 'resources': 'Load and memory', 'running': 'Is it running?', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
