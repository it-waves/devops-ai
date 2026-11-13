RB = 'REAL RECORDING  ·  Ubuntu 24.04, offline repo'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "You get a Java project. You type M V N package. And it builds. What just happened?"),
  c('h2', "Maven read one file, the pom. It knew the project name, the folders, the libraries, and the build steps."),
  c('h3', "Today you learn to read that file, the folder layout Maven expects, and how it finds a library."),
  c('h4', "Then you fix a broken project yourself."),
  c('h5', "One honest note. My recording computer cannot reach Maven Central, so these demos use a local copy of the libraries. The commands are the same ones you will type."),
 ]),
 ('ideas', [
  c('u1', "A pom is an X M L file. Four parts matter first."),
  c('u2', "One. Coordinates. Group I D, artifact I D, and version. Together, G A V. They name your project, and every library, uniquely."),
  c('u3', "Two. Properties. Settings like the Java release, written once."),
  c('u4', "Three. Dependencies. The libraries you need. Each one is named by its own coordinates, and a scope."),
  c('u5', "Four. Build. The plugins that compile, test and package, with their versions pinned."),
  c('u6', "And one rule. Convention over configuration. Put files where Maven expects them, and you write almost nothing."),
 ]),
 ('repo', [
  c('l1', "Where do libraries live? In a repository. A repository is only folders, shown here over H T T P. This is a local copy, not Maven Central."),
  c('l2', "The group I D, org dot apache dot commons, becomes folders."),
  c('l3', "Next, the artifact I D, commons lang three."),
  c('l4', "Then the version, three point fourteen point zero."),
  c('l5', "Inside: the jar, the pom, and checksum files. Every library has its own pom, with its own coordinates."),
  c('l6', "Maven Central uses this exact layout. Same folders, same names."),
 ]),
 ('tour', [
  k('t0', "Go to the demo project. Type: C D, demo."),
  c('t1', "Read the top of the pom. Type: head -16 pom.xml", "Read the top of the pom. Type: head, dash sixteen, pom dot X M L."),
  c('t1b', "The coordinates. Com dot cloud cart, greeter demo, one point zero point zero. That is the project's name."),
  c('t2', "Maven expects standard folders. Type: find src -type f", "Maven expects standard folders. Type: find, source, dash type, F."),
  c('t2b', "Main code under source, main, java. Tests under source, test, java."),
  c('t3', "Which Maven is this? Type: mvn -v | head -1", "Which Maven is this? Type: M V N, dash V, pipe, head, dash one."),
  c('t3b', "Maven three point nine point eleven."),
  c('t4', "Build it. Type: mvn -B -q package 2>&1 | head -3", "Build it. Type: M V N, dash B, dash Q, package, then errors to the pipe, and head dash three."),
  c('t4b', "It fails. The package org dot apache dot commons dot lang three does not exist. The code imports a library the pom never declared."),
 ]),
 ('deps', [
  k('d0', "Go to the demo project. Type: C D, demo."),
  c('d1', "Where is the library used? Type: grep import src/main/java/cloudcart/Hello.java", "Where is the library used? Type: grep, import, and the path to hello dot java."),
  c('d1b', "It imports string utils from commons lang three. So the pom must declare it."),
  c('d2', "Here is the block to add. Type: cat dep.xml", "Here is the block to add. Type: cat, dep dot X M L."),
  c('d2b', "Group I D, artifact I D, version. Three coordinates. That is a dependency."),
  c('d3', "Insert it into the pom. Type: sed -i '/<dependencies>/r dep.xml' pom.xml", "Insert it into the pom. Type: sed, dash I, then a pattern that finds the dependencies line, R, the file name, and the pom."),
  c('d4', "Build again. Type: mvn -B package | grep -E 'Tests run:|BUILD'", "Build again. Type: M V N, dash B, package, pipe, grep, dash E, then the words to keep."),
  c('d4w', "While Maven works, it compiles the code, compiles and runs the test, and packs the jar. That takes a few seconds."),
  c('d4b', "One test ran, none failed. Build success."),
  c('d5', "What did it make? Type: ls target/*.jar", "What did it make? Type: L S, target, slash, star, dot jar."),
  c('d5b', "The jar is named from the coordinates. Artifact I D, dash, version."),
  c('d6', "See the dependency tree. Type: mvn -B dependency:tree | grep 'jar:'", "See the dependency tree. Type: M V N, dash B, dependency colon tree, pipe, grep, jar colon."),
  c('d6b', "Our project. One library to compile with. J unit, for tests only, with its own helper. Test scope is never shipped."),
  c('d7', "Where did that jar come from? Type: find ~/.m2 -name 'commons-lang3-3*.jar'", "Where did that jar come from? Type: find, the dot M two folder, dash name, commons lang three dash three, star, dot jar."),
  c('d7b', "Cached in your local repository, under the same folders we just browsed. The next build needs no download."),
 ]),
 ('models', [
  c('o1', "How Maven finds a library, in this order."),
  c('o2', "First, your local repository, the dot M two folder in your home. If the jar is there, it is used."),
  c('o3', "If not, a remote repository. By default, Maven Central. Maven downloads it, and keeps a copy."),
  c('o4', "The path comes from the coordinates. Same coordinates, same file, on any computer."),
  c('o5', "So pin your versions. Same version, same build."),
 ]),
 ('task', [
  c('k1', "Your lab task. Lab eighty-five gives you a project that will not build. Lab check judges your work."),
  c('k2', "It lives at git hub dot com, slash it dash waves, slash dev ops dash A I, in academy, lab, lab eighty-five dot S H."),
  c('k3', "One: set the coordinates. Com dot cloud cart, cart A P I, one point zero point zero."),
  c('k4', "Two: move the source into source, main, java, and the test into source, test, java."),
  c('k5', "Three: declare commons lang three, three point fourteen point zero, and J unit, four point thirteen point two, with scope test."),
  c('k6', "Four: M V N package. It must end in build success, and make the cart A P I jar."),
  c('k7', "Five: save the dependency tree into tree dot text."),
  c('k8', "Install a J D K and Maven first. Then lab up, lab check, and lab down. The shortcut file is shortcuts eighty-five."),
 ]),
 ('rubric', [
  c('q1', "Pass or fail. You need all six."),
  c('q2', "Five pass lines in lab check."), c('q3', "You can name the three coordinates."),
  c('q4', "You can explain the standard folders."), c('q5', "You can explain compile scope and test scope."),
  c('q6', "You can say where Maven caches a library."), c('q7', "lab down, nothing left behind."), c('q8', "To pass, all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: lab up, and read the task file."),
  c('z3', "Two: run M V N package, and read the first error."),
  c('z4', "Three: fix the coordinates and the folders."),
  c('z5', "Four: declare the two dependencies."),
  c('z6', "Five: build, save tree dot text, and lab check."),
  c('z7', "Six: lab down, and prove nothing is left."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which three values are the coordinates?"), c('f13', "Where must main code live?"),
  c('f14', "Which scope is not shipped?"), c('f15', "Where does Maven keep a downloaded library?"),
  c('f16', "Objective covered: M C ten, objective one."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: the Maven lifecycle."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'d4w': 2.5, 'd6': 0.5, 't4b': 0.5, 'd7b': 0.5, 'u6': 0.5, 'o5': 0.5, 'k8': 0.5, 'q8': 0.5, 'z8': 14.0, 'f17': 10.0}
import os as _os, json as _json
_xp = '/home/claude/academy/lesson85/extra.json'
if _os.path.exists(_xp): EXTRA.update(_json.load(open(_xp)))
CHAP = {'ideas': 'Anatomy of a pom', 'repo': 'A repository, live', 'tour': 'Layout and coordinates', 'deps': 'Dependencies', 'models': 'How Maven finds a library', 'task': 'Your lab task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
UI_LABEL = {'l1': 'A repository is just folders (local copy)', 'l2': 'groupId  org.apache.commons  becomes folders', 'l3': 'artifactId  commons-lang3', 'l4': 'version  3.14.0', 'l5': 'The jar, the pom, and checksums', 'l6': 'Maven Central uses the same layout'}
