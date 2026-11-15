def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Maven or Gradle? Which one should your team use?"),
  c('h2', "Ask ten engineers and you get ten loud answers. Most of them have only ever used one."),
  c('h3', "Today you build the same project with both, side by side, and see for yourself."),
  c('h4', "Same code. Same library. Same jar at the end."),
  c('h5', "Then you decide, with evidence, and not with a feeling."),
 ]),
 ('parts', [
  c('a1', "Both tools do the same job. They compile your code, run your tests, fetch libraries, and make a jar."),
  c('a2', "Maven describes the project in a file called pom dot X M L. It is data: you say what the project is."),
  c('a3', "Gradle describes it in build dot gradle. It is a small program: you can also say how to build it."),
  c('a4', "Maven follows one fixed life cycle: compile, test, package. Gradle builds a graph of tasks, and runs only the tasks that must run."),
  c('a5', "They share the same libraries. Both download from Maven Central, with the same names and versions."),
  c('a6', "The output goes to different folders. Maven writes to target. Gradle writes to build, slash libs."),
 ]),
 ('live', [
  k('p0', "Go into the project. Type: C D, slash opt, slash lab one oh two, slash cartcore."),
  k('w1', "Two build files, in one project. Count the lines in each. Type: grep, dash C, a dot, then pom dot X M L, and build dot gradle."),
  c('w1b', "Twelve lines of X M L, ten lines of Gradle. Similar size. One is data, the other is code."),
  k('w2', "Both need the same library. Look at the Maven version of it. Type: cat, dot dot slash demo, slash dep dot X M L."),
  c('w2b', "Five lines of X M L: a group, an artifact, and a version. Those three words are the library's name on Maven Central."),
  k('m1', "Add it to the pom. Type: sed, dash I, and insert the file after the dependencies line, in pom dot X M L."),
  k('m2', "Build with Maven. Type: M V N, package, and show only the result."),
  c('m2b', "Build success. Maven did it in about two seconds."),
  k('m3', "Look for the jar. Type: L S, target, slash star dot jar."),
  k('g1', "Now the same library in Gradle. One line, inside the dependencies block. Type the sed command."),
  k('g2', "Build with Gradle. Type: dot slash gradle W, build, and show the result."),
  c('g2b', "Build successful, in about a second. Two tasks executed. The Gradle daemon was already warm, so this run is quick."),
  k('g3', "And its jar. Type: L S, build, slash libs."),
  c('g3b', "Same name, same version, a different folder."),
  k('r1', "Now the second run, and nothing has changed. Maven first."),
  c('r1b', "Maven noticed: nothing to compile, all classes are up to date. Maven can skip work too."),
  k('r2', "And Gradle."),
  c('r2b', "Every task says up to date. Gradle lists each step, and tells you which ones it skipped. That list is what makes a slow build easy to understand."),
 ]),
 ('decide', [
  c('v1', "So which one? Honestly, both work. Here is how to choose."),
  c('v2', "Pick Maven when you want a standard layout that every Java engineer already knows, and a build file anyone can read."),
  c('v3', "Pick Gradle when the build needs custom steps, or when a large project needs faster builds through its cache."),
  c('v4', "On a small project like this one, both finish in seconds. Do not choose by a speed claim you have not measured."),
  c('v5', "In this bootcamp, we build with Maven, and we use Gradle only where a lesson says so."),
 ]),
 ('task', [
  c('k1', "Your task. One project, with both build files. It does not build yet."),
  c('k2', "One: add commons lang three, version three point twelve point oh, to the pom. Maven must build the jar."),
  c('k3', "Two: add the same library to build dot gradle. Gradle must build its jar."),
  c('k4', "Three: run Gradle a second time, and save the output. It must say up to date."),
  c('k5', "Four: both jars must contain the same classes."),
  c('k6', "Five: write decision dot text, three lines: maven, gradle, and your choice, with a reason."),
 ]),
 ('labinfo', [
  c('i1x', "Here is where to find everything. Pause on this screen if you need to write it down."),
  c('i2', "The lab lives on git hub, at it dash waves, slash dev ops dash A I, in the folder academy, slash lab."),
  c('i3', "Two files: lab one oh two dot S H, and shortcuts one oh two dot S H."),
  c('i4', "Install it, in your Ubuntu virtual machine: sudo install, dash m seven five five, lab one oh two dot S H, into slash usr, slash local, slash S bin."),
  c('i5', "Load the short name with: source shortcuts one oh two dot S H. Then you can type: lab up, lab check, and lab down."),
  c('i6', "You need a J D K, Maven, curl and python three, about one gigabyte of memory, and an internet connection. The first lab up downloads Gradle."),
  c('i7', "Lab check builds your project on your machine. Lab down removes everything. Only run it in your own virtual machine."),
 ]),
 ('rubric', [
  c('q1x', "Pass or fail. You need all six."),
  c('q2x', "Five pass lines in lab check."), c('q3x', "Maven builds the jar, with the library in the pom."),
  c('q4x', "Gradle builds the jar, with the library in build dot gradle."), c('q5x', "The second Gradle run is saved, and says up to date."),
  c('q6x', "Decision dot text has your maven, gradle and choice lines, in your own words."), c('q7x', "Lab down leaves nothing behind."), c('q8x', "To pass, all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: lab up, and look at both build files."),
  c('z3', "Two: add the library to the pom, and build with Maven."),
  c('z4', "Three: add it to build dot gradle, and build with Gradle."),
  c('z5', "Four: run Gradle again, and save the second run."),
  c('z6', "Five: write your decision, and run lab check."),
  c('z7', "Six: lab down, and prove nothing is left."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which file describes a Maven project, and which one a Gradle project?"), c('f13', "Where does each tool put the jar?"),
  c('f14', "What does up to date mean in a Gradle build?"), c('f15', "When would you choose Maven, and when Gradle?"),
  c('f16', "Objective covered: M C eleven, objective eight, comparing Maven and Gradle."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: the Gradle mastery lesson, the whole domain in one lab."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'a6': 0.5, 'k6': 0.5, 'i7': 0.5, 'q8x': 0.5, 'z8': 14.0, 'f17': 10.0, 'p0': 1.0, 'w1': 2.5, 'w2': 2.0, 'm1': 3.0, 'm2': 4.0, 'm3': 2.0, 'g1': 3.0, 'g2': 7.0, 'g3': 2.0, 'r1': 3.0, 'r2': 4.0}
import os as _os, json as _json
_xp = '/home/claude/academy/lesson102/extra.json'
if _os.path.exists(_xp): EXTRA.update(_json.load(open(_xp)))
CHAP = {'parts': 'Same job, two tools', 'live': 'Live: the same project, built both ways', 'decide': 'How to choose', 'task': 'Your lab task', 'labinfo': 'Where to find the lab', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
