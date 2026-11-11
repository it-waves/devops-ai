RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Scripts get run again. A scheduler fires twice. A deploy fails halfway, and someone runs it again. If your script only works the first time, the second run can break things."),
  c('h2', "Today you learn two skills. Idempotent scripts, which give the same result, however many times they run. And ShellCheck, a free tool that finds mistakes before you run anything."),
  c('h3', "Every demo is a real recording on Ubuntu."),
 ]),
 ('idem', [
  k('id1', "First, what goes wrong when a script runs twice. Here is a setup script. Type: cat bad dot S H."),
  k('id2', "It makes a folder, and adds a setting to a file. Run it once. Type: bash bad dot S H."),
  k('id3', "Silent, so it worked. Now run it a second time. Type: bash bad dot S H."),
  k('id4', "An error. The folder already exists. And what about the settings file? Type: cat app dot conf."),
  c('id5', "The line is there twice. Run it ten times, and you get ten lines. A script like this makes a mess when it is repeated, or retried after a crash."),
 ]),
 ('fix', [
  k('g1', "Now the better version. Type: cat good dot S H."),
  k('g2', "Three changes. M K dir with dash P creates the folder only if it is missing. The grep check adds the setting only if it is not there already. And the strict mode line stops the script on any real failure. Run it. Type: bash good dot S H."),
  k('g3', "Run it again, with the same command. Type: bash good dot S H."),
  k('g4', "No error, and no output. Nothing needed doing. Check the file. Type: cat app dot conf."),
  c('g5', "One line, however many times you run it. That is idempotent. Running it again changes nothing."),
 ]),
 ('state', [
  k('st1', "Bash gives you repeat-safe switches built in. First, M K dir with dash P, run twice, then print the exit code. Type: mkdir dash P logs, semicolon, mkdir dash P logs, semicolon, echo dollar question mark."),
  k('st2', "Zero. No error on the second run. Next, R M with dash F, which does not complain when the file is missing. Type: R M dash F, nothing dot T X T, semicolon, echo dollar question mark."),
  k('st3', "Zero again. Last, L N with dash S F N, which replaces a link if it exists, and creates it if not. Run it twice, then look. Type: L N dash S F N, logs, cur, semicolon, again, semicolon, L S dash L, cur."),
  c('st4', "One link, and no error. Prefer these forms, so a second run is harmless."),
 ]),
 ('finds', [
  k('fi1', "Next, ShellCheck, a free tool that reads your script and finds mistakes before you run it. Here is a script with a typo. Type: cat typo dot S H."),
  k('fi2', "The variable is called name, but the echo line says N M A E. Bash would quietly print nothing. Let ShellCheck look. Type: shellcheck typo dot S H."),
  k('fi3', "ShellCheck shows the line, the problem and a code, S C twenty one fifty four. The variable is referenced, but not assigned. Check its exit code. Type: echo, dollar question mark."),
  c('fi4', "One. A non-zero exit, so a pipeline can fail the build when ShellCheck finds problems. On Ubuntu, install it with sudo apt install shellcheck."),
 ]),
 ('fixes', [
  k('d1', "ShellCheck can often fix the problem for you. Here is a script that breaks on file names with spaces. Type: cat buggy dot S H."),
  k('d2', "Without quotes, the file name my file dot T X T splits into two words. Ask ShellCheck for a diff. Type: shellcheck, dash F, diff, buggy dot S H."),
  k('d3', "Lines starting with a minus are removed, and lines starting with a plus are added. The fix is quotes around the variable. Apply it with the patch command. Type: shellcheck dash F diff buggy dot S H, pipe, patch buggy dot S H."),
  k('d4', "Patched. Look at the script again. Type: cat buggy dot S H."),
  k('d5', "Quotes added. Now run ShellCheck again, and print clean only if it finds nothing. Type: shellcheck buggy dot S H, and, and, echo clean."),
  c('d6', "Clean. Always read a patch before you trust it. But this is a fast way to learn the fixes."),
 ]),
 ('build', [
  k('bu1', "Now one script that is idempotent, and clean under ShellCheck. Type: cat site dot S H."),
  k('bu2', "It ensures a folder, a setting and a link, all safe to repeat. Check it with ShellCheck first. Type: shellcheck site dot S H, and, and, echo clean."),
  k('bu3', "Clean. Now run it. Type: bash site dot S H."),
  k('bu4', "It ensured everything. Run it again, and count the lines in the file. Type: bash site dot S H, semicolon, W C, dash L, conf slash app dot conf."),
  c('bu5', "Still one line. Safe to run, safe to retry, and safe to schedule."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: if a script worked once, it is fine. No. Run it twice, and it may fail, or repeat its work."),
  c('my3', "Myth two: ShellCheck finds every bug. No. It finds many common mistakes, but it cannot know what you meant."),
  c('my4', "Myth three: a clean ShellCheck means safe for production. No. Test the script on a copy first."),
  c('my5', "Myth four: idempotent means the script does nothing. No. It does the work the first time, and then finds nothing left to do."),
  c('my6', "Same result. Check first. Lint first."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding. Six points, and you need all six."),
  c('b2', "Explain idempotent in one sentence: the same result, however many times it runs."),
  c('b3', "Use M K dir dash P, R M dash F and L N dash S F N, so repeats are harmless."),
  c('b4', "Check before you change a file, so a setting is never added twice."),
  c('b5', "Run ShellCheck, and read the code and the line number of each finding."),
  c('b6', "Fix the findings, with quotes or the diff output, and run ShellCheck until it is clean."),
  c('b7', "Prove it: run the script twice, and show that the second run changes nothing."),
  c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Install ShellCheck first, with sudo apt install shellcheck. Type every command yourself."),
  c('z2', "One: write a script that makes a folder and appends a line, and run it twice to watch it break."),
  c('z3', "Two: make it repeat-safe with M K dir dash P and a grep check, and run it three times."),
  c('z4', "Three: try M K dir dash P, R M dash F and L N dash S F N twice each, and read the exit codes."),
  c('z5', "Four: write a script with a typo in a variable name, and let ShellCheck find it."),
  c('z6', "Five: write a script with an unquoted variable, and fix it with shellcheck dash F diff and patch."),
  c('z7', "Six: run ShellCheck on a script from earlier in this course, and fix every finding."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What does idempotent mean?"), c('f13', "Which flag makes M K dir safe to repeat?"),
  c('f14', "What exit code does ShellCheck give, when it finds problems?"), c('f15', "How do you prove a script is idempotent?"),
  c('f16', "Objective covered: MC05-O08.", "Objective covered: M C zero five, objective eight, in the Bash scripting masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: a deploy, health check and rollback script."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'id5': 0.5, 'g5': 0.5, 'st4': 0.5, 'fi4': 0.5, 'd6': 0.5, 'bu5': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'idem': 'Why repeats break', 'fix': 'The idempotent version', 'state': 'Repeat-safe commands', 'finds': 'ShellCheck', 'fixes': 'Fix with ShellCheck', 'build': 'Put it together', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
