def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Last lesson you published a jar. A real repository wants a password."),
  c('h2', "Where does that password go? Not in your build script. Not in a file that goes to git."),
  c('h3', "Gradle has a clean path for settings, and another for secrets."),
  c('h4', "You will see a password leak from a file, remove it, and bring it back through the environment."),
  c('h5', "Then you do it alone, and a checker judges your result."),
  c('h6', "One idea first: settings go in files. Secrets go in the environment."),
 ]),
 ('parts', [
  c('a1', "Four ideas keep a Gradle build configurable, and safe."),
  c('a2', "One, settings live in gradle dot properties. Not secret, and shared by the whole team."),
  c('a3', "Two, a flag on the command line overrides a setting, for one run. The flag is dash capital P."),
  c('a4', "Three, a secret never goes in a file that is committed. It comes from the environment, or a secret store."),
  c('a5', "Four, read it, but never print it. A build log is public, and a leaked line stays forever."),
  c('a6', "Real Nexus needs a user and a password. This is how they reach your build. Let us see it live."),
 ]),
 ('live', [
  k('p0', "Go into the project. Type: C D, slash opt, slash lab ninety-eight, slash cartcore."),
  c('f1', "First, look at the settings file. Type: cat, gradle dot properties.", "First, look at the settings file. Type: cat, gradle dot properties."),
  c('f1b', "One line. Repo password, equals, Pa55-plain. A real password, in a plain file. If this goes to git, everyone who can read the repository can read it.", "One line. Repo password, equals, pa fifty-five dash plain. A real password, in a plain file. If this goes to git, everyone who can read the repository can read it."),
  c('s1', "What does the build see? Run the show config task, in quiet mode. Type: dot slash gradle W, dash Q, show config.", "What does the build see? Run the show config task, in quiet mode. Type: dot slash gradle W, dash Q, show config."),
  c('s1b', "Greeting, unset. Password, set. The build found the password in the file. Notice what the task prints: set, never the value. A build log is public. Never print a secret."),
  c('r1', "Take the secret out of the file. Delete every line with repo password. Type: sed, dash I, then the delete command, and gradle dot properties.", "Take the secret out of the file. Delete every line with repo password. Type: sed, dash I, then the delete command, and gradle dot properties."),
  c('s2', "Ask again. Same command.", "Ask again. Same command."),
  c('s2b', "Password, missing. The build no longer has it, and nothing leaks. Now we must give it back, the safe way."),
  c('g1', "A setting that is not secret belongs in the file. Add a greeting. Type: echo, the greeting, double greater than, gradle dot properties.", "A setting that is not secret belongs in the file. Add a greeting. Type: echo, the greeting, double greater than, gradle dot properties."),
  c('g2', "Ask the build.", "Ask the build."),
  c('g2b', "Greeting: Welcome to CloudCart. The setting lives in a file, so everyone on the team gets the same value."),
  c('o1', "Sometimes you need a different value, once. Override it on the command line, with dash capital P. Type: show config, then dash capital P, greeting equals Hello.", "Sometimes you need a different value, once. Override it on the command line, with dash capital P. Type: show config, then dash capital P, greeting equals Hello."),
  c('o1b', "Greeting: Hello. The command line wins over the file, and the file did not change."),
  c('e1', "Now the secret, the safe way: the environment. A variable named O R G, underscore, gradle, underscore, project, underscore, then the property name. Set it for this one command.", "Now the secret, the safe way: the environment. A variable named O R G, underscore, gradle, underscore, project, underscore, then the property name. Set it for this one command."),
  c('e1b', "Password: set. Gradle turned the variable into the property. The value came from the environment, so it never touched a file. In a pipeline, the secret store provides it."),
  c('c1', "Prove it. Search every file for the value, and count the matches. Type: grep dash R, the value, dot, then pipe, W C dash L.", "Prove it. Search every file for the value, and count the matches. Type: grep dash R, the value, dot, then pipe, W C dash L."),
  c('c1b', "Zero. The secret was used, and left no trace in the project. That is the goal."),
 ]),
 ('task', [
  c('k1', "Your task. The same journey, on your own project, in the lab."),
  c('k2', "One: the password sits in gradle dot properties. Take it out. No file may contain it.", "One: the password sits in gradle dot properties. Take it out. No file may contain it."),
  c('k3', "Two: add a greeting to gradle dot properties, and see it in show config."),
  c('k4', "Three: override the greeting with dash capital P, and save the output in override dot text."),
  c('k5', "Four: give the password through the environment, and save the output in secret dot text. It must say password, set.", "Four: give the password through the environment, and save the output in secret dot text. It must say password, set."),
  c('k6', "Five: write notes dot text, three lines: where, why, and override."),
 ]),
 ('labinfo', [
  c('i1x', "Here is where to find everything. Pause on this screen if you need to write it down."),
  c('i2', "The lab lives on git hub, at it dash waves, slash dev ops dash A I, in the folder academy, slash lab."),
  c('i3', "Two files: lab ninety-eight dot S H, and shortcuts ninety-eight dot S H."),
  c('i4', "Install it, in your Ubuntu virtual machine: sudo install, dash m seven five five, lab ninety-eight dot S H, into slash usr, slash local, slash S bin."),
  c('i5', "Load the short name with: source shortcuts ninety-eight dot S H. Then you can type: lab up, lab check, and lab down."),
  c('i6', "You need a J D K, curl and python three, about one gigabyte of memory, and an internet connection. The first lab up downloads Gradle."),
  c('i7', "Lab down removes everything. Only run it in your own virtual machine."),
 ]),
 ('rubric', [
  c('q1x', "Pass or fail. You need all six."),
  c('q2x', "Five pass lines in lab check."), c('q3x', "The password text is in no file."),
  c('q4x', "The greeting is in the file, and the override works from the command line."), c('q5x', "The secret came from the environment, and show config says set."),
  c('q6x', "Notes dot text answers where, why, and override, in your own words."), c('q7x', "Lab down leaves nothing behind."), c('q8x', "To pass, all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: lab up, and read the task file."),
  c('z3', "Two: take the password out of the file."),
  c('z4', "Three: add the greeting, and override it once."),
  c('z5', "Four: pass the secret through the environment."),
  c('z6', "Five: write the notes, and run lab check."),
  c('z7', "Six: lab down, and prove nothing is left."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Where do settings go, and where do secrets go?"), c('f13', "Which flag overrides a property for one run?"),
  c('f14', "How does an environment variable become a Gradle property?"), c('f15', "Why does show config print set, and not the value?"),
  c('f16', "Objective covered: M C eleven, objective four, Gradle environment settings and secrets."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: the build cache, and reproducible builds."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'a6': 0.5, 'k6': 0.5, 'i7': 0.5, 'q8x': 0.5, 'z8': 14.0, 'f17': 10.0, 'f1': 1.5, 's1': 1.5, 'r1': 1.5, 's2': 1.5, 'g1': 1.5, 'g2': 2.0, 'o1': 1.5, 'e1': 1.5, 'c1': 1.5}
import os as _os, json as _json
_xp = '/home/claude/academy/lesson98/extra.json'
if _os.path.exists(_xp): EXTRA.update(_json.load(open(_xp)))
CHAP = {'parts': 'Four ideas: settings, flags, secrets, no printing', 'live': 'Live: remove a secret, override a setting', 'task': 'Your lab task', 'labinfo': 'Where to find the lab', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
