def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Last lesson you read a Gradle project. Today it does real work: it tests your code, and it pulls in libraries."),
  c('h2', "And real work breaks. A test fails. Two libraries want different versions of a third."),
  c('h3', "Gradle gives you three commands to find the cause: build, test, and dependencies."),
  c('h4', "You will watch a real failing test get fixed, then see exactly which library version Gradle chose, and why."),
  c('h5', "Then you do it alone, and a checker judges your result."),
  c('h6', "One idea first: when something fails, ask Gradle. It will tell you."),
 ]),
 ('parts', [
  c('a1', "Four ideas turn a Gradle build into something you can trust."),
  c('a2', "One, the build chain. Build runs check, check runs test, and test runs your tests. A failing test stops the whole build."),
  c('a3', "Two, the test task. It runs J unit, and writes two results: an X M L file for machines, and an H T M L report for people."),
  c('a4', "Three, dependencies. Implementation is for code that ships. Test implementation is for code that only tests use."),
  c('a5', "Four, inspection. The dependencies task prints the tree. Dependency insight explains one library. When versions clash, Gradle picks the highest."),
  c('a6', "Maven does this with plug ins and the dependency tree goal. Gradle does it with tasks. Let us see it live."),
 ]),
 ('live', [
  k('p0', "Go into the project. Type: C D, slash opt, slash lab ninety-six, slash cartcore."),
  c('p1', "Find the code. Type: find, src, dash name, quote, star dot java, quote.", "Find the code. Type: find, src, dash name, quote, star dot java, quote."),
  c('p1b', "Three files. Cart and Main are the program, in S R C, main. Cart test is the test, in S R C, test. Gradle keeps them apart."),
  c('d1', "Now the libraries. Show the dependencies block of the build script. Type: grep, dash capital A five, quote, caret, dependencies, quote, build dot gradle.", "Now the libraries. Show the dependencies block of the build script. Type: grep, dash capital A five, quote, caret, dependencies, quote, build dot gradle."),
  c('d1b', "Implementation means: ships with the program. Commons text, and commons lang three, at version three point nine. Below them, test implementation: J unit, used only by tests. Keep commons lang three in mind."),
  c('b1', "Run the build. Keep the lines about failures. Type: dot slash gradle W, build, then two, greater than, ampersand one, and grep.", "Run the build. Keep the lines about failures. Type: dot slash gradle W, build, then two, greater than, ampersand one, and grep."),
  c('b1b', "Task test failed. Cart test, ten percent discount, failed. Three tests ran, one failed, so the whole build failed. That is the build chain at work."),
  c('b2', "What went wrong? Run the tests, and keep only the word expected, and what follows. Type: dot slash gradle W, test, and grep dash O, expected.", "What went wrong? Run the tests, and keep only the word expected, and what follows. Type: dot slash gradle W, test, and grep dash O, expected."),
  c('b2b', "Expected forty-five, but the code gave forty. Fifty dollars, with ten percent off, should be forty-five. We got fifty minus ten."),
  c('c1', "Find the code behind it. Type: grep dash N, dash capital A two, total with, then the path to cart dot java.", "Find the code behind it. Type: grep dash N, dash capital A two, total with, then the path to cart dot java."),
  c('c1b', "Line twenty-two. It subtracts the percent, as if ten percent meant ten dollars. The bug is in the program, not in the test. We fix the program."),
  c('f1', "Fix it with sed. Subtract the percentage of the total, instead of the number.", "Fix it with sed. Subtract the percentage of the total, instead of the number."),
  c('t2', "Run the tests again. Keep the failed and build lines.", "Run the tests again. Keep the failed and build lines."),
  c('t2b', "Build successful. No failures. The test that was red is green, and the test file did not change."),
  c('x1', "Machines read the X M L result. Pull out the counts. Type: grep, dash O H, then the pattern, and the results folder.", "Machines read the X M L result. Pull out the counts. Type: grep, dash O H, then the pattern, and the results folder."),
  c('x1b', "Tests three, skipped zero, failures zero. A build server reads exactly this file, to decide pass or fail."),
  c('r1', "People read the H T M L report. List its folder. Type: L S, build, slash reports, slash tests, slash test.", "People read the H T M L report. List its folder. Type: L S, build, slash reports, slash tests, slash test."),
  c('r1b', "Index dot H T M L is the report. In your own virtual machine you open it in a browser. It lists every test, with its time and result."),
  c('y1', "Now the dependency tree. Show the runtime class path, and keep the commons lines. Type: dot slash gradle W, dependencies, dash dash configuration, runtime class path, and grep.", "Now the dependency tree. Show the runtime class path, and keep the commons lines. Type: dot slash gradle W, dependencies, dash dash configuration, runtime class path, and grep."),
  c('y1b', "Commons text brings commons lang three, version three point twelve. But our script asked for three point nine. The arrow says it all: three point nine, becomes three point twelve. Gradle took the higher one."),
  c('i1', "Ask Gradle why. Type: dot slash gradle W, dependency insight, dash dash dependency, commons lang three, the configuration, and grep.", "Ask Gradle why. Type: dot slash gradle W, dependency insight, dash dash dependency, commons lang three, the configuration, and grep."),
  c('i1b', "Selection reasons: by conflict resolution, between three point twelve and three point nine. Not a guess. Gradle told you which version, and why. Look here first, whenever a library behaves strangely."),
 ]),
 ('task', [
  c('k1', "Your task. The same journey, on your own project, in the lab."),
  c('k2', "One: run the tests. One fails. Fix the bug in the program, not in the test, until all three pass.", "One: run the tests. One fails. Fix the bug in the program, not in the test, until all three pass."),
  c('k3', "Two: find the H T M L test report, and note its path."),
  c('k4', "Three: save the runtime class path tree in deps dot text."),
  c('k5', "Four: save the dependency insight for commons lang three in insight dot text.", "Four: save the dependency insight for commons lang three in insight dot text."),
  c('k6', "Five: write notes dot text, three lines: version, why, and report."),
 ]),
 ('labinfo', [
  c('i1x', "Here is where to find everything. Pause on this screen if you need to write it down."),
  c('i2', "The lab lives on git hub, at it dash waves, slash dev ops dash A I, in the folder academy, slash lab."),
  c('i3', "Two files: lab ninety-six dot S H, and shortcuts ninety-six dot S H."),
  c('i4', "Install it, in your Ubuntu virtual machine: sudo install, dash m seven five five, lab ninety-six dot S H, into slash usr, slash local, slash S bin."),
  c('i5', "Load the short name with: source shortcuts ninety-six dot S H. Then you can type: lab up, lab check, and lab down."),
  c('i6', "You need a J D K, curl and python three, about one gigabyte of memory, and an internet connection. The first lab up downloads Gradle, and the libraries."),
  c('i7', "Lab down removes everything. Only run it in your own virtual machine."),
 ]),
 ('rubric', [
  c('q1', "Pass or fail. You need all six."),
  c('q2', "Five pass lines in lab check."), c('q3', "The bug is fixed in the program, and the test file is untouched."),
  c('q4', "You used the wrapper, not another Gradle."), c('q5', "Deps dot text and insight dot text come from real Gradle runs."),
  c('q6', "Notes dot text names the real version, in your own words."), c('q7', "Lab down leaves nothing behind."), c('q8', "To pass, all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: lab up, and read the task file."),
  c('z3', "Two: run the tests, and read the failure."),
  c('z4', "Three: fix the program, and run the tests again."),
  c('z5', "Four: print the dependency tree, and ask for the insight."),
  c('z6', "Five: write the notes, and run lab check."),
  c('z7', "Six: lab down, and prove nothing is left."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Why does a failing test stop the build?"), c('f13', "Which file does a build server read, and which does a person read?"),
  c('f14', "What is the difference between implementation and test implementation?"), c('f15', "Two libraries want different versions. Which does Gradle pick, and which command proves it?"),
  c('f16', "Objective covered: M C eleven, objective two, Gradle build, test and dependency inspection."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: dependencies, repositories and plug ins in depth."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'a6': 0.5, 'k6': 0.5, 'i7': 0.5, 'q8': 0.5, 'z8': 14.0, 'f17': 10.0, 'b1': 1.5, 'b2': 1.5, 't2': 1.5, 'x1': 1.5, 'r1': 1.5, 'y1': 1.8, 'i1': 1.8, 'f1': 1.5}
import os as _os, json as _json
_xp = '/home/claude/academy/lesson96/extra.json'
if _os.path.exists(_xp): EXTRA.update(_json.load(open(_xp)))
CHAP = {'parts': 'Four ideas: chain, tests, libraries, inspection', 'live': 'Live: fix a failing test, read the dependency tree', 'task': 'Your lab task', 'labinfo': 'Where to find the lab', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
