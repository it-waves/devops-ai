def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "The build fails. The screen fills with red. What do you do first?"),
  c('h2', "Most people read the last line, or the first, or the longest, and then they guess."),
  c('h3', "A Gradle failure always tells you where it happened. If you know where to look."),
  c('h4', "Today you fix a project that fails three different ways, one behind the other."),
  c('h5', "A daemon that will not start. A library that cannot be found. A task that fails."),
  c('h6', "One habit first: read what went wrong, and ask which phase broke."),
 ]),
 ('parts', [
  c('a1', "A Gradle build runs in phases. A failure belongs to one of them."),
  c('a2', "One, the daemon. Gradle starts a background Java process first. If that cannot start, nothing else happens. The message says: unable to start the daemon."),
  c('a3', "Two, dependencies. Before compiling, Gradle must download your libraries. If one cannot be found, the message says: could not resolve, or could not find."),
  c('a4', "Three, tasks. A task runs and fails: a compile error, a failing test, a failing check. The message says: execution failed for task, and the task name."),
  c('a5', "Always read from the line that says what went wrong. The first line under it is the cause. The rest is help."),
  c('a6', "Let us fix a real project, one failure at a time."),
 ]),
 ('live', [
  k('p0', "Go into the project. Type: C D, slash opt, slash lab one oh one, slash cartcore."),
  k('d1', "Build the jar, and show only the cause. Type: dot slash gradle W, jar, then two greater than ampersand one, pipe, grep, dash capital A, one, then went wrong, in quotes."),
  c('d1b', "Unable to start the daemon process. This is not about your code. Gradle could not even begin."),
  c('d1c', "And the second message says why: Java heap space. The daemon ran out of memory."),
  k('d2', "Where does the memory limit come from? Look at gradle dot properties."),
  c('d2b', "Dash capital X M X sixteen M. Sixteen megabytes. Far too small for Gradle."),
  k('d3', "Fix it. Give the daemon five hundred and twelve megabytes. Type: echo, then the setting, then greater than, gradle dot properties."),
  k('b1', "Build again, and show more of the message. Type the same command, with grep dash capital A, three."),
  c('b1b', "A new failure. The daemon started, so the first one is fixed. Now: execution failed for task compile java. Could not resolve all files. Could not find commons lang three, version three point ninety-nine point one."),
  c('b1c', "This is a dependency failure. The version does not exist."),
  k('b2', "Ask Gradle for the dependency report. Type: dot slash gradle W, dash Q, dependencies, dash dash configuration, compile class path."),
  c('b2b', "The word failed, next to the library. It confirms it. The real versions are on Maven Central. Three point twelve point oh exists."),
  k('b3', "Fix the version. Type: sed, dash I, replace three point ninety-nine point one, with three point twelve point oh, in build dot gradle."),
  k('c1', "Build the project again. The dependency is found, so the build gets further."),
  c('c1b', "A third failure, and it is different again. Execution failed for task smoke. Not compile java. A task that ran, and failed."),
  c('c1c', "And it tells you what happened. Expected total eighteen hundred. The program said: total twenty-two hundred. A discount should lower the price."),
  k('c2', "Find the line. Type: grep, dash N, percent, and the path to cart dot java."),
  c('c2b', "A plus. The discount is added, not taken off."),
  k('c3', "Fix it. Replace the plus with a minus, with sed."),
  k('c4', "Build one last time. Show only the end."),
  c('c4b', "Build successful. Three failures, three phases, three fixes. And each time, the message told you where to look."),
 ]),
 ('task', [
  c('k1', "Your task. The same project, in the lab. It will not build."),
  c('k2', "One: the daemon. Find the memory setting in gradle dot properties, and fix it."),
  c('k3', "Two: the dependency. Find the version that does not exist, and use three point twelve point oh."),
  c('k4', "Three: the task. Read what the smoke task says, and fix the Java code."),
  c('k5', "Four: dot slash gradle W, build, must pass, and produce the jar."),
  c('k6', "Five: write notes dot text, three lines: daemon, dependency, and task. What failed, and how you knew."),
 ]),
 ('labinfo', [
  c('i1x', "Here is where to find everything. Pause on this screen if you need to write it down."),
  c('i2', "The lab lives on git hub, at it dash waves, slash dev ops dash A I, in the folder academy, slash lab."),
  c('i3', "Two files: lab one oh one dot S H, and shortcuts one oh one dot S H."),
  c('i4', "Install it, in your Ubuntu virtual machine: sudo install, dash m seven five five, lab one oh one dot S H, into slash usr, slash local, slash S bin."),
  c('i5', "Load the short name with: source shortcuts one oh one dot S H. Then you can type: lab up, lab check, and lab down."),
  c('i6', "You need a J D K, curl and python three, about one gigabyte of memory, and an internet connection. The first lab up downloads Gradle, and the project needs one library from Maven Central."),
  c('i7', "Lab check runs your build on your machine. Lab down removes everything. Only run it in your own virtual machine."),
 ]),
 ('rubric', [
  c('q1x', "Pass or fail. You need all six."),
  c('q2x', "Five pass lines in lab check."), c('q3x', "The daemon starts, with enough memory in gradle dot properties."),
  c('q4x', "The dependency resolves, with a version that exists."), c('q5x', "The smoke task passes, and the build produces the jar."),
  c('q6x', "Notes dot text names the daemon, dependency and task failures, in your own words."), c('q7x', "Lab down leaves nothing behind."), c('q8x', "To pass, all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: lab up, and build. Read what went wrong, and name the phase."),
  c('z3', "Two: fix the daemon memory."),
  c('z4', "Three: fix the dependency version."),
  c('z5', "Four: fix the Java code behind the smoke task."),
  c('z6', "Five: write the notes, and run lab check."),
  c('z7', "Six: lab down, and prove nothing is left."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which three phases can a Gradle build fail in?"), c('f13', "Which words in the message tell you it is a dependency failure?"),
  c('f14', "Where in the output is the cause, and where is only help?"), c('f15', "A task failed. What do you read first?"),
  c('f16', "Objective covered: M C eleven, objective seven, diagnosing Gradle failures."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: Maven or Gradle, which one for dev ops?"), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'a6': 0.5, 'k6': 0.5, 'i7': 0.5, 'q8x': 0.5, 'z8': 14.0, 'f17': 10.0, 'p0': 1.0, 'd1': 3.0, 'd2': 1.5, 'd3': 2.5, 'b1': 3.5, 'b2': 3.0, 'b3': 2.5, 'c1': 4.0, 'c2': 2.0, 'c3': 2.5, 'c4': 3.5}
import os as _os, json as _json
_xp = '/home/claude/academy/lesson101/extra.json'
if _os.path.exists(_xp): EXTRA.update(_json.load(open(_xp)))
CHAP = {'parts': 'Three phases, three kinds of failure', 'live': 'Live: fix three failures, one by one', 'task': 'Your lab task', 'labinfo': 'Where to find the lab', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
