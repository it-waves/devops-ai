RB = 'REAL RECORDING  ·  Ubuntu 24.04, local repo'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Your build runs on your laptop, and fails on the server, with a four oh one. Unauthorized."),
  c('h2', "Your company keeps its libraries in a private repository. It needs a login. And that login must never end up in git."),
  c('h3', "Today you learn what a mirror is, where Maven looks for credentials, and how to hand over a password safely."),
  c('h4', "Then you set it up yourself."),
  c('h5', "One honest note. The company repository in this lesson is a small local server I started, with a login. The real thing is a repository manager like nexus or artifactory, but Maven sees the same four oh one."),
 ]),
 ('what', [
  c('a1', "A repository is where Maven downloads libraries from. Your pom can name one, with a repository block."),
  c('a2', "A mirror is a detour. Maven asks the mirror, instead of the original address."),
  c('a3', "Companies use mirrors for speed, for control, and because the mirror can cache everything."),
  c('a4', "A mirror matches by id. Mirror of libs means: every request for the repository with the id libs goes to the mirror."),
  c('a5', "So the pom keeps the public address, and each developer's settings decide where it really goes."),
 ]),
 ('settings', [
  c('b1', "Two files configure Maven. The pom belongs to the project, and lives in git."),
  c('b2', "The settings dot X M L file belongs to you. It lives in your home folder, in dot m two. Not in git."),
  c('b3', "Mirrors go here, and so do servers. A server block holds a user name and a password."),
  c('b4', "The link between them is the id. The server with the id corp, matches the mirror with the id corp."),
  c('b5', "If the ids differ by one letter, Maven sends no password, and you get the four oh one."),
 ]),
 ('secrets', [
  c('x1', "Where does the password itself go? Three rules."),
  c('x2', "One. Never in the pom, and never in any file in git. Anyone who can read the project can read the password."),
  c('x3', "Two. In settings, refer to an environment variable. Dollar, brace, env dot, the name. The real value stays outside the file."),
  c('x4', "Three. Lock down the files. C H mod six hundred means: only you can read the file."),
  c('x5', "Maven can also encrypt passwords with a master password. It is better than plain text, but an environment variable from a secret store is better still."),
 ]),
 ('mirror', [
  k('m0', "Go to the demo project. Type: C D, demo."),
  c('m1', "Look at the settings file. Type: cat, tilde, slash, dot m two, slash settings dot X M L.", "Look at the settings file. Type: cat, tilde slash dot m two slash settings dot X M L."),
  c('m1b', "A server, with the id corp, and the password as an environment variable. And a mirror, with the same id, corp, for the repository libs."),
  c('m2', "Now build, without the password. Type: mvn -B -q clean package, then filter the error.", "Now build, without giving the password. Maven, quiet mode, clean package, and then we keep only the line about corp."),
  c('m2w', "Maven asks the mirror for the libraries."),
  c('m2b', "Four oh one. Unauthorized. The server exists, but Maven has no password to send."),
  c('m3', "Give it the password, from a locked file. Type: export REPO_PASS= dollar, parenthesis, cat tilde slash dot corp dash pass.", "Read the password from a locked file into the variable. Type: export, repo pass, equals, then cat, the file, in a dollar parenthesis."),
  c('m4', "Build again. Type: mvn -B -q clean package && ls target slash star dot jar", "Build again, with the same command, and list the jar."),
  c('m4w', "Now it downloads, with the login."),
  c('m4b', "A jar. The build works, and the password never appeared in a command, or a file."),
  c('m5', "Prove it. Search every file here for the password.", "Prove it. This searches the project and the settings file for the password, and prints a message if it finds nothing."),
  c('m5b', "Nothing found. The password lives only in the variable, and in the locked file."),
  c('m6', "Last, lock the settings file. Type: chmod 600, then stat, to show the permissions.", "Last, lock the settings file with C H mod six hundred, and show the permissions of both files with stat."),
  c('m6b', "Dash, r w, and dashes. Only the owner can read or write. Both files are locked."),
 ]),
 ('task', [
  c('k1', "Your lab task. Lab ninety gives you a project and a repository with a login. Lab check judges your work."),
  c('k2', "It lives at git hub dot com, slash it dash waves, slash dev ops dash A I, in academy, lab, lab ninety dot S H."),
  c('k3', "One: in settings dot X M L, add a server with the id corp, the user dev, and the password from the environment variable corp pass."),
  c('k4', "Two: add a mirror with the id corp, for the repository libs, with the address on port eight zero nine one."),
  c('k5', "Three: lock the file with C H mod six hundred."),
  c('k6', "Four: set the variable from the password file, and build with dash s settings dot X M L. It must end in build success."),
  c('k7', "Five: one sentence in why dot text, about why the password must not be in the pom. Use the words pom, and git or commit."),
  c('k8', "Install a J D K and Maven first. Then lab up, lab check, and lab down. The shortcut file is shortcuts ninety. The check downloads plugins, so be online."),
 ]),
 ('rubric', [
  c('q1', "Pass or fail. You need all six."),
  c('q2', "Five pass lines in lab check."), c('q3', "You can explain a mirror, and what mirror of means."),
  c('q4', "You can explain why server and mirror ids must match."), c('q5', "No password in any file, only in the environment."),
  c('q6', "The settings file is locked, mode six hundred."), c('q7', "lab down, nothing left behind."), c('q8', "To pass, all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: lab up, and read the task file."),
  c('z3', "Two: write the server and the mirror."),
  c('z4', "Three: lock the file."),
  c('z5', "Four: set the variable, and build."),
  c('z6', "Five: write why dot text, and lab check."),
  c('z7', "Six: lab down, and prove nothing is left."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What does a mirror do?"), c('f13', "Which file holds credentials?"),
  c('f14', "How do you keep a password out of the file?"), c('f15', "What does four oh one mean?"),
  c('f16', "Objective covered: M C ten, objective six."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: publish snapshot and release artifacts."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'m2w': 6.0, 'm4w': 7.0, 'a5': 0.5, 'b5': 0.5, 'x5': 0.5, 'k8': 0.5, 'q8': 0.5, 'z8': 14.0, 'f17': 10.0}
import os as _os, json as _json
_xp = '/home/claude/academy/lesson90/extra.json'
if _os.path.exists(_xp): EXTRA.update(_json.load(open(_xp)))
CHAP = {'what': 'Repositories and mirrors', 'settings': 'settings.xml vs the pom', 'secrets': 'Keeping passwords safe', 'mirror': 'Live: mirror, login and 401', 'task': 'Your lab task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
