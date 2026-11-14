RB = 'REAL RECORDING  ·  Ubuntu 24.04, offline repo'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Your build worked yesterday. Today it fails, and you changed nothing. A library you never asked for just changed version."),
  c('h2', "That is the world of transitive dependencies. Libraries pull in other libraries, and sometimes two of them want different versions of the same one."),
  c('h3', "Today you learn to read the dependency tree, see the conflict, understand how Maven chooses, and fix it."),
  c('h4', "Then you solve a conflict yourself."),
  c('h5', "One honest note. My recording computer cannot reach Maven Central, so the demos use two tiny libraries I built in a local folder. The commands and the tree are exactly what you will see."),
 ]),
 ('trans', [
  c('a1', "A direct dependency is one you write in your pom."),
  c('a2', "A transitive dependency is one your dependency needs. You never wrote it. Maven brings it for you."),
  c('a3', "Your project asks for lib A and lib B. Lib A needs you till, version one. Lib B needs you till, version two."),
  c('a4', "Only one version can go on the class path. So Maven must choose."),
  c('a5', "That clash is a version conflict. It is common, and it is quiet, until something breaks."),
 ]),
 ('rules', [
  c('b1', "How Maven chooses. Rule one: nearest wins. The version closest to your project in the tree is used."),
  c('b2', "Rule two: if two are the same distance, the first one declared wins."),
  c('b3', "In our case, you till is two levels away, through lib A, and also two levels away, through lib B. A tie. Lib A is declared first, so version one wins."),
  c('b4', "The newest version does not win. The nearest does, or the first. That surprises many people."),
  c('b5', "Version one is chosen, but our code needs a method that only exists in version two."),
 ]),
 ('fixes', [
  c('x1', "Three ways to fix a conflict."),
  c('x2', "One. Dependency management. Pin the version for the whole project, in one place. This is the best habit."),
  c('x3', "Two. An exclusion. Tell Maven: from this dependency, leave that library out."),
  c('x4', "Three. Declare it yourself, directly. A direct dependency is nearest, so it wins. Quick, but easy to forget."),
  c('x5', "We will use the first one, dependency management. Then prove it with the tree."),
 ]),
 ('tree', [
  k('t0', "Go to the demo project. Type: C D, demo."),
  c('t1', "Print the tree. Type: mvn -B dependency:tree | grep 'jar:' | cut -c8-", "Print the tree. Type: M V N, dash B, dependency colon tree, then grep for the jar lines, and cut away the first seven characters."),
  c('t1w', "Maven reads every pom, direct and transitive. A few seconds."),
  c('t1b', "Read it like folders. Our project at the top. Lib A, and under it, you till one. Then lib B."),
  c('t2', "Now ask for the details. Type: mvn -B dependency:tree -Dverbose | grep omitted | cut -c8-", "Now ask for the details. Type: M V N, dash B, dependency colon tree, dash capital D verbose, then grep for the word omitted."),
  c('t2w', "Verbose mode also lists what Maven left out."),
  c('t2b', "There it is. You till two point zero, omitted for conflict with one point zero. Lib B wanted version two, and lost."),
  c('t3', "Focus on one library. Type: mvn -B dependency:tree -Dincludes=com.cloudcart.lib:util | grep 'jar:' | cut -c8-", "Focus on one library. Type: M V N, dependency colon tree, dash capital D includes, the group and you till, then the same filter."),
  c('t3w', "Includes keeps only the path to one library. Useful in a big tree."),
  c('t3b', "Only the path to you till. Version one, through lib A."),
  c('t4', "Now the build. Type: mvn -B -q compile 2>&1 | head -4", "Now the build. Type: M V N, dash B, dash Q, compile, then errors to the pipe, and head dash four."),
  c('t4w', "Quiet mode, so only errors show."),
  c('t4b', "It fails. Cannot find symbol, shout. That method is only in you till two point zero. The conflict is now a real error."),
  c('t5', "Here is the fix, as a block. Type: cat dm.xml", "Here is the fix, as a block. Type: cat, D M dot X M L."),
  c('t5b', "Dependency management, with you till pinned to two point zero. No jar is added. It only sets the version, wherever you till appears."),
  c('t6', "Insert it into the pom. Type: sed -i '/<\\/properties>/r dm.xml' pom.xml", "Insert it after the properties block. Type: sed, dash I, a pattern that finds the end of the properties, R, the file name, and the pom."),
  c('t7', "Print the tree again. Type: mvn -B dependency:tree | grep 'jar:' | cut -c8-", "Print the tree again, with the same filter."),
  c('t7w', "Same command as before."),
  c('t7b', "You till is now two point zero, under lib A. Lib A did not change. The pin did."),
  c('t8', "Build again. Type: mvn -B -q compile && echo built", "Build again. Type: M V N, dash B, dash Q, compile, and, echo, built."),
  c('t8w', "Almost there."),
  c('t8b', "Built. Conflict found, understood, and fixed."),
 ]),
 ('task', [
  c('k1', "Your lab task. Lab eighty-eight gives you a build with a version conflict. Lab check judges your work."),
  c('k2', "It lives at git hub dot com, slash it dash waves, slash dev ops dash A I, in academy, lab, lab eighty-eight dot S H."),
  c('k3', "One: before you fix anything, save the verbose tree lines with omitted into conflict dot text."),
  c('k4', "Two: pin you till to two point zero, with a dependency management block. Do not delete lib A or lib B."),
  c('k5', "Three: M V N clean package must end in build success."),
  c('k6', "Four: save the new tree into tree dot text. It must show you till two point zero, and no one point zero."),
  c('k7', "Five: write one sentence in why dot text, about the rule Maven used to pick version one. Use the word nearest, or first."),
  c('k8', "Install a J D K and Maven first. Then lab up, lab check, and lab down. The shortcut file is shortcuts eighty-eight."),
 ]),
 ('rubric', [
  c('q1', "Pass or fail. You need all six."),
  c('q2', "Five pass lines in lab check."), c('q3', "You can read a dependency tree, direct and transitive."),
  c('q4', "You can state the two rules: nearest wins, then first declared."), c('q5', "You can name three ways to fix a conflict."),
  c('q6', "You can find a conflict with dash capital D verbose."), c('q7', "lab down, nothing left behind."), c('q8', "To pass, all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: lab up, and read the task file."),
  c('z3', "Two: save the conflict into conflict dot text, before any fix."),
  c('z4', "Three: add the dependency management block."),
  c('z5', "Four: build, and save tree dot text."),
  c('z6', "Five: write why dot text, and lab check."),
  c('z7', "Six: lab down, and prove nothing is left."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What is a transitive dependency?"), c('f13', "Which version wins in a conflict?"),
  c('f14', "Name two ways to fix a conflict."), c('f15', "Which flag shows what was omitted?"),
  c('f16', "Objective covered: M C ten, objective four."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: package the cloud cart app as a war."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'t1w': 5.0, 't2w': 6.0, 't3w': 6.0, 't4w': 6.0, 't7w': 5.0, 't8w': 6.0, 'a5': 0.5, 'b5': 0.5, 'x5': 0.5, 'k8': 0.5, 'q8': 0.5, 'z8': 14.0, 'f17': 10.0}
import os as _os, json as _json
_xp = '/home/claude/academy/lesson88/extra.json'
if _os.path.exists(_xp): EXTRA.update(_json.load(open(_xp)))
CHAP = {'trans': 'Transitive dependencies', 'rules': 'How Maven chooses', 'fixes': 'Three ways to fix it', 'tree': 'Live: find and fix a conflict', 'task': 'Your lab task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
