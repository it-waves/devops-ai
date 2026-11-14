RB = 'REAL RECORDING  ·  Ubuntu 24.04, offline repo'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Same code. Same pom. You build twice. And you get two different jars. Why?"),
  c('h2', "Because a build has loose ends: dates inside the jar, settings that differ per machine, and tools that change version."),
  c('h3', "Today you tighten them. Plug ins, properties, profiles, and reproducible builds."),
  c('h4', "You will see each one live, then fix a project yourself."),
  c('h5', "One honest note. My recording computer cannot reach Maven Central, so the demos use a local copy of the plug ins. The commands are the same ones you will type."),
 ]),
 ('plug', [
  c('a1', "Maven itself does almost nothing. Plug ins do the work."),
  c('a2', "Every phase you saw last time runs a plug in goal. Compiler, sure fire, jar."),
  c('a3', "You tune a plug in with a configuration block, inside the plug in. For example, tell the jar plug in which class starts the program."),
  c('a4', "That goes in the manifest, as the main class. Then java dash jar knows where to begin."),
  c('a5', "And pin every plug in version. A plug in that updates by itself can change your build."),
 ]),
 ('props', [
  c('r1', "Properties. A value, defined once, used many times."),
  c('r2', "Write it inside the properties block. Then use it anywhere with dollar, curly braces, and its name."),
  c('r3', "Maven has its own too. Project dot version is the version of your project."),
  c('r4', "Resource filtering copies a file into the jar, and fills in the dollar names on the way."),
  c('r5', "And a value given on the command line, with dash capital D, always beats the pom."),
 ]),
 ('prof', [
  c('f1', "Profiles. A named set of changes, switched on only when you ask."),
  c('f2', "Switch one on with dash capital P, and the profile name."),
  c('f3', "Use profiles for differences, like dev and prod. Keep them few, and keep them small."),
  c('f4', "Never put passwords in a profile in the pom. The pom is shared. We handle secrets in a later lesson."),
 ]),
 ('cfg', [
  k('p0', "Go to the demo project. Type: C D, demo."),
  c('p1', "Read the settings. Type: sed -n 8,19p pom.xml", "Read the settings. Type: sed, dash N, eight comma nineteen P, pom dot X M L."),
  c('p1b', "Two properties, the environment and the greeting. And a profile named prod, which changes the environment."),
  c('p2', "The file that uses them. Type: cat src/main/resources/app.properties", "The file that uses them. Type: cat, and the path to app dot properties."),
  c('p2b', "Two dollar names. Maven will fill them in when it copies the file."),
  c('p3', "Build, then run. Type: mvn -B -q package && java -jar target/shop-1.0.0.jar", "Build, then run. Type: M V N, dash B, dash Q, package, and, java, dash jar, and the jar."),
  c('p3w', "Quiet mode, so only errors print. A few seconds."),
  c('p3b', "Dev. The jar ran, because the plug in set the main class. And both names were filled in."),
  c('p4', "Now the prod profile. Type: mvn -B -q clean package -Pprod && java -jar target/shop-1.0.0.jar", "Now the prod profile. Type: M V N, dash B, dash Q, clean, package, dash capital P, prod, and run the jar."),
  c('p4w', "Same code, different profile."),
  c('p4b', "Prod. One switch changed the build."),
  c('p5', "And the command line wins. Type: mvn -B -q clean package -Dapp.greeting=Hi && java -jar target/shop-1.0.0.jar", "And the command line wins. Type: M V N, dash B, dash Q, clean, package, dash capital D, app dot greeting, equals, hi, and run the jar."),
  c('p5w', "One more build."),
  c('p5b', "The greeting is now Hi. The command line beat the pom."),
  c('p6', "Check the plug in's work. Type: unzip -p target/shop-1.0.0.jar META-INF/MANIFEST.MF | grep Main", "Check the plug in's work. Type: unzip, dash P, the jar, the manifest file, then grep for main."),
  c('p6b', "There is the main class, written by the jar plug in."),
 ]),
 ('repro', [
  k('y0', "Go to the demo project. Type: C D, demo."),
  c('y1', "Build, and take a fingerprint of the jar. Type: mvn -B -q clean package; sha256sum target/shop-1.0.0.jar | cut -c1-16", "Build, and take a fingerprint of the jar. Type: M V N, clean, package, then shaw two fifty-six sum of the jar, cut to sixteen characters."),
  c('y1w', "A fingerprint, called a hash, changes if even one byte changes."),
  c('y1b', "Remember the start of that fingerprint."),
  c('y2', "Again, the same. Type: mvn -B -q clean package; sha256sum target/shop-1.0.0.jar | cut -c1-16", "Build the same thing again, and fingerprint it."),
  c('y2w', "Nothing in the code changed."),
  c('y2b', "A different fingerprint. The jar stores the build time, so every build is different."),
  c('y3', "Fix it. Type: sed -i '8a\\    <project.build.outputTimestamp>2024-01-01T00:00:00Z</project.build.outputTimestamp>' pom.xml; sed -n 8,10p pom.xml", "Fix it with a fixed date. Type: sed, dash I, a command that appends a line after line eight, and then show lines eight to ten."),
  c('y3b', "One property, project dot build dot output time stamp. A fixed date, stored in every file."),
  c('y4', "Build, and fingerprint. Type: mvn -B -q clean package; sha256sum target/shop-1.0.0.jar | cut -c1-16", "Build, and fingerprint."),
  c('y4w', "Once more."),
  c('y4b', "Note the start of this fingerprint."),
  c('y5', "Again, the same. Type: mvn -B -q clean package; sha256sum target/shop-1.0.0.jar | cut -c1-16", "And one more time, the same command."),
  c('y5w', "The same again."),
  c('y5b', "The same fingerprint, twice. A reproducible build. Same input, same bytes, anywhere."),
 ]),
 ('task', [
  c('k1', "Your lab task. Lab eighty-seven gives you a jar that cannot run, with settings not set. Lab check judges your work."),
  c('k2', "It lives at git hub dot com, slash it dash waves, slash dev ops dash A I, in academy, lab, lab eighty-seven dot S H."),
  c('k3', "One: configure the jar plug in so the main class is cloud cart dot hello, and java dash jar prints a line."),
  c('k4', "Two: add the two properties, and turn on filtering. The jar must print dev, welcome."),
  c('k5', "Three: add a profile called prod, that sets the environment to prod."),
  c('k6', "Four: add the output time stamp property, so two builds make an identical jar."),
  c('k7', "Five: build, and save the fingerprint into shaw dot text."),
  c('k8', "Install a J D K and Maven first. Then lab up, lab check, and lab down. The shortcut file is shortcuts eighty-seven."),
 ]),
 ('rubric', [
  c('q1', "Pass or fail. You need all six."),
  c('q2', "Five pass lines in lab check."), c('q3', "You can say what a plug in configuration block does."),
  c('q4', "You can explain why the command line beats the pom."), c('q5', "You can switch a profile on."),
  c('q6', "You can say why two builds differ, and the fix."), c('q7', "lab down, nothing left behind."), c('q8', "To pass, all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: lab up, and read the task file."),
  c('z3', "Two: fix the manifest, and run the jar."),
  c('z4', "Three: add the properties and filtering."),
  c('z5', "Four: add the prod profile, and the time stamp."),
  c('z6', "Five: build, save the fingerprint, and lab check."),
  c('z7', "Six: lab down, and prove nothing is left."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What does a plug in configuration block do?"), c('f13', "Which wins: the pom, or dash capital D?"),
  c('f14', "How do you switch a profile on?"), c('f15', "What makes a build reproducible?"),
  c('f16', "Objective covered: M C ten, objective three."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: dependency trees and version conflicts."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'y2': 4.0, 'y3': 3.2, 'y4': 5.0, 'y5': 4.3, 'p3w': 6.0, 'p4w': 7.0, 'p5w': 7.0, 'y1w': 4.0, 'y2w': 5.0, 'y4w': 5.0, 'y5w': 5.0, 'a5': 0.5, 'f4': 0.5, 'k8': 0.5, 'q8': 0.5, 'z8': 14.0, 'f17': 10.0}
import os as _os, json as _json
_xp = '/home/claude/academy/lesson87/extra.json'
if _os.path.exists(_xp): EXTRA.update(_json.load(open(_xp)))
CHAP = {'plug': 'Plugins', 'props': 'Properties', 'prof': 'Profiles', 'cfg': 'Live: plugin, property, profile', 'repro': 'Reproducible builds', 'task': 'Your lab task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
