RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Deploying is the moment of truth. You push a new version, and hope. If it breaks, every second counts, and a manual fix at night is how mistakes happen."),
  c('h2', "Today you build a deploy script that does three things. It releases a new version. It checks that the new version is healthy. And if it is not, it rolls back by itself."),
  c('h3', "Every demo is a real recording on Ubuntu, with a small web server running in the lab."),
 ]),
 ('layout', [
  k('l1', "First, how the files are laid out. Each version lives in its own folder, under releases. Type: L S, releases."),
  k('l2', "Three versions: v one, v two and v three. A sim link called current points to the live one. Type: L S, dash L, current."),
  k('l3', "Current points to releases slash v one. The web server serves whatever current points to. Ask it which version is live. Type: curl, dash S, local host colon eight zero eight zero, slash version."),
  k('l4', "Version one is live. Every version also has a health page. Type: curl, dash F S, local host colon eight zero eight zero, slash health."),
  c('l5', "OK. The server answers, so this version is healthy. Switching versions is just moving the sim link, which is quick, and easy to undo."),
 ]),
 ('script', [
  k('sc1', "Now the deploy script. Type: cat release dot S H."),
  k('sc2', "It remembers the old version, switches the sim link, then calls the health page. If the check passes, it reports success. If not, it points the link back to the old version, and exits with one. Check it with ShellCheck first. Type: shellcheck release dot S H, and, and, echo clean."),
  c('sc3', "Clean. A script you can trust, with a clear exit code that a pipeline can read."),
 ]),
 ('deploy', [
  k('d1', "Now deploy version two. Type: bash release dot S H, v two."),
  k('d2', "Deployed. Ask the server which version is live. Type: curl, dash S, local host colon eight zero eight zero, slash version."),
  k('d3', "Version two is live. Check where the link points. Type: read link, current."),
  k('d4', "Releases slash v two. Run the same deploy again. Type: bash release dot S H, v two."),
  c('d5', "Deployed again, with no errors. The script is idempotent, so a repeat or a retry does no harm."),
 ]),
 ('rollback', [
  k('r1', "Now the test that matters: a bad release. Version three has no health page. Deploy it. Type: bash release dot S H, v three."),
  k('r2', "The health check failed with a four oh four, and the script rolled back on its own. Check the exit code. Type: echo, dollar question mark."),
  k('r3', "One, a failure, so a pipeline would stop, and alert someone. Which version is live now? Type: curl, dash S, local host colon eight zero eight zero, slash version."),
  k('r4', "Version two, still serving users. Confirm the link. Type: read link, current."),
  k('r5', "Back on releases slash v two. You can also roll back by hand, by deploying a known good older version. Type: bash release dot S H, v one."),
  k('r6', "Deployed. Check the version. Type: curl, dash S, local host colon eight zero eight zero, slash version."),
  c('r7', "Version one is live. Rollback is just a deploy of an older release."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: if the deploy script finished, the deploy worked. No. Only a health check proves that the new version really works."),
  c('my3', "Myth two: rollback means restoring from a backup. No. With versioned releases, a rollback is moving a link."),
  c('my4', "Myth three: a deploy script only needs the happy path. No. Plan the failure first, and test it."),
  c('my5', "Myth four: health checks must be complicated. No. Start with one simple request that must succeed."),
  c('my6', "Release. Check. Roll back."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding. Six points, and you need all six."),
  c('b2', "Keep every release in its own folder, with a current link."),
  c('b3', "Switch versions by moving the link, not by editing files in place."),
  c('b4', "Check health after every deploy, with a request that must succeed."),
  c('b5', "Roll back automatically when the check fails."),
  c('b6', "Exit with a non-zero code on failure, so a pipeline can react."),
  c('b7', "Test the failure path on purpose, with a bad release."),
  c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Use a small local web server only, and nothing real."),
  c('z2', "One: make three release folders, each with a version file, and a current link to the first."),
  c('z3', "Two: start a web server on the current folder, with python three, dash M, http dot server, and request the version with curl."),
  c('z4', "Three: write the release script, with a health check and a rollback."),
  c('z5', "Four: deploy a good version, and prove with curl that it is live."),
  c('z6', "Five: deploy a bad version, with no health file, and watch it roll back."),
  c('z7', "Six: check the exit code, run ShellCheck, and stop the server when you finish."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Why keep each release in its own folder?"), c('f13', "What proves that a deploy worked?"),
  c('f14', "What should happen when the health check fails?"), c('f15', "How does a rollback work, with versioned releases?"),
  c('f16', "Objective covered: MC05-O09.", "Objective covered: M C zero five, objective nine, in the Bash scripting masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: the Bash scripting mastery scenario."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'l5': 0.5, 'sc3': 0.5, 'd5': 0.5, 'r7': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'layout': 'Releases and a link', 'script': 'The deploy script', 'deploy': 'A good deploy', 'rollback': 'A bad deploy and rollback', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
