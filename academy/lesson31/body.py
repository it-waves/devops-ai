RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
SCENES = [
 ('hook', [
  c('h1', "When you log out, the server keeps working. Something has to start it, watch it, and restart it."),
  c('h2', "On Ubuntu that something is system D. It runs services, keeps their logs, and starts jobs on a schedule."),
  c('h3', "Today you read a service file, check it, read its logs, and schedule a job."),
 ]),
 ('unit', [
  c('u1', "A service is described by a unit file. Read the one for S S H. Type: head -n 14 /usr/lib/systemd/system/ssh.service.", "A service is described by a unit file. Read the one for S S H. Type: head, dash n, fourteen, slash U S R, slash lib, slash system D, slash system, slash S S H dot service."),
  c('u2', "The Unit section describes the service and when it starts. The Service section says how to run it."),
  c('u3', "Exec start is the command that system D runs. The service is that program."),
  c('u4', "Restart equals on-failure means: if it crashes, system D starts it again. That is why services come back by themselves.", "Restart equals on dash failure means: if it crashes, system D starts it again. That is why services come back by themselves."),
 ]),
 ('mine', [
  c('m1', "Now write a unit file of your own. Here is one. Type: cat web.service.", "Now a unit file of your own. Here is one. Type: cat, web dot service."),
  c('m2', "A small web server. The install section says wanted by multi-user target, which means start at normal boot.", "A small web server. The install section says wanted by multi dash user dot target, which means start at normal boot."),
  c('m3', "Check it before you use it. Type: systemd-analyze verify web.service. Grep hides one harmless warning about I P version six from this recording computer.", "Check it before you use it. Type: system D analyze, verify, web dot service. Then grep, dash v, Bind. It hides one harmless warning about I P version six from this recording computer."),
  c('m4', "No output means no problems found."),
  c('m5', "Now a file with mistakes. Type: cat bad.service.", "Now a file with mistakes. Type: cat, bad dot service."),
  c('m6', "Can you spot them? Check it the same way.", "Can you spot them? Check it the same way. Type: system D analyze, verify, bad dot service."),
  c('m7', "Two problems. An unknown key name, because Restart is misspelled. And a command that does not exist. Fix both, and verify again."),
 ]),
 ('control', [
  c('c1', "Now control a service. This needs a running system D machine, such as your virtual machine, so these screens are an illustration."),
  c('c2', "Check status first. Type: systemctl status web. Read two lines.", "Check status first. Type: system control, status, web. Read two lines."),
  c('c3', "Loaded says the file was found, and enabled means it starts at boot."),
  c('c4', "Active says running now. If it says failed, read the log lines under it."),
  c('c5', "Start, stop, restart and reload change the service right now. Use sue do."),
  c('c6', "Enable and disable control boot. Enable does not start it now. Add dash dash now to do both."),
  c('c7', "After you edit a unit file, run: systemctl daemon-reload. Then restart the service.", "After you edit a unit file, run: system control, daemon reload. Then restart the service."),
  c('c8', "Then check status again. Always confirm the change."),
 ]),
 ('journal', [
  c('j1', "When a service fails, read its log. System D keeps logs in the journal, and you read them with journal control."),
  c('j2', "Logs for one service: journalctl -u web. Add dash n to limit the lines.", "Logs for one service: journal control, dash u, web. Add dash n to limit the lines."),
  c('j3', "Read the end first. The last lines usually say why it failed."),
  c('j4', "Add dash f to follow new lines live. Control C stops it."),
  c('j5', "Filter by time with dash dash since, and by severity with dash p err."),
  c('j6', "And dash b shows only the current boot."),
 ]),
 ('boot', [
  c('b1', "How does a server start? It is a chain. Firmware starts the boot loader. The boot loader starts the kernel. The kernel starts system D, process number one."),
  c('b2', "System D then reaches a target, a group of services. A server normally reaches multi-user dot target.", "System D then reaches a target, a group of services. A server normally reaches multi dash user dot target."),
  c('b3', "To see which services slowed the boot, run: systemd-analyze blame. For the boot logs, use journal control dash b.", "To see which services slowed the boot, run: system D analyze blame. For the boot logs, use journal control dash b."),
 ]),
 ('timers', [
  c('t1', "System D can also start jobs on a schedule, with timers. First, check a schedule before you trust it. Type: systemd-analyze calendar.", "System D can also start jobs on a schedule, with timers. First, check a schedule before you trust it. Type: system D analyze, calendar, then the time in quotes."),
  c('t2', "It shows the normal form, and when it will next run. Your date and time zone will differ. Two a m, every day."),
  c('t3', "Weekday mornings. Same command, new schedule.", "Weekday mornings. Same command, new schedule. Monday to Friday at nine."),
  c('t4', "Monday to Friday, at nine. Always read the next run time before you rely on a schedule."),
 ]),
 ('cron', [
  c('k1', "The older tool is cron. One line has five time fields, then the command."),
  c('k2', "Minute thirty, hour two, any day of the month, any month, Monday to Friday. That is two thirty a m on weekdays."),
  c('k3', "Edit your table with: crontab -e. List it with: crontab -l.", "Edit your table with: cron tab, dash e. List it with: cron tab, dash l."),
  c('k4', "Cron runs with a small environment, so use full paths, and test the command by hand first."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: enable starts the service. No. Enable is for boot. Start is for now."),
  c('my3', "Myth two: edit the unit file and it applies. No. Reload system D, then restart."),
  c('my4', "Myth three: restart is the first fix. No. Read the log first, or you lose the clue."),
  c('my5', "Myth four: cron has your normal shell. No. Use full paths."),
  c('my6', "Read first. Then change."),
 ]),
 ('rubric', [
  c('r1', "Here is how you check your own understanding."), c('r2', "Read a unit file, and find the command and the restart rule."),
  c('r3', "Check a unit file with system D analyze verify.", "Check a unit file with system D analyze verify."), c('r4', "Read status, Loaded and Active."),
  c('r5', "Explain start, enable, and daemon reload."), c('r6', "Read a service log with journal control."),
  c('r7', "Write a schedule as a cron line, and check a timer schedule."), c('r8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your virtual machine. Nothing here installs or changes a service."),
  c('z2', "One: read the S S H unit file with head, and find exec start and restart."),
  c('z3', "Two: write your own web dot service in your home folder, and verify it. Then break it on purpose, and verify again.", "Two: write your own web dot service in your home folder, and verify it. Then break it on purpose, and verify again."),
  c('z4', "Three: run system control status S S H, and read Loaded and Active.", "Three: run system control status S S H, and read Loaded and Active."),
  c('z5', "Four: read the last ten lines of its log, with journal control dash u S S H dash n ten.", "Four: read the last ten lines of its log, with journal control, dash u, S S H, dash n, ten."),
  c('z6', "Five: check a timer schedule with system D analyze calendar.", "Five: check a timer schedule with system D analyze calendar."),
  c('z7', "Six: write, on paper, a cron line for two thirty a m on weekdays. Do not install it."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which line in a unit file is the command to run?"), c('f13', "Which command makes system D re-read edited unit files?"),
  c('f14', "Which tool reads service logs?"), c('f15', "Does enable start a service now?"),
  c('f16', "Objective covered: MC04-O06.", "Objective covered: M C zero four, objective six, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: installing and updating packages.", "Next lesson: installing and updating packages."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'u2': 0.4, 'u4': 0.5, 'm2': 0.4, 'm4': 0.6, 'm7': 0.5, 'c1': 0.4, 'c3': 0.5, 'c4': 0.5, 'c6': 0.4, 'c8': 0.5, 'j3': 0.5, 'j6': 0.5, 'b3': 0.6, 't2': 0.5, 't4': 0.5, 'k2': 0.5, 'k4': 0.5, 'my6': 0.5, 'r8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'unit': 'Read a unit file', 'mine': 'Write and check a unit', 'control': 'Control a service', 'journal': 'Read the journal', 'boot': 'How a server boots', 'timers': 'Timers', 'cron': 'Cron', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
