RB = 'REAL RECORDING  ·  Ubuntu 24.04, offline repo'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "You built a jar. You gave it to the operations team. They said, we cannot deploy that."),
  c('h2', "A web application is not a jar. A server like tomcat expects a different package, a war, with a fixed layout inside."),
  c('h3', "Today you package cloud cart as a war, open it up, and check exactly what is inside."),
  c('h4', "Then you decide which libraries go in, and which stay out."),
  c('h5', "One honest note. My recording computer cannot reach Maven Central, so the libraries come from a small local folder. The commands and the contents are what you will see."),
 ]),
 ('what', [
  c('a1', "A war is a web archive. It is a zip file, with the extension dot war."),
  c('a2', "You hand it to a servlet container, such as tomcat. The container unpacks it and serves your site."),
  c('a3', "A jar holds classes. A war holds a whole web application: pages, settings, classes and libraries."),
  c('a4', "In Maven you do not run a new tool. You change one line in the pom: the packaging."),
  c('a5', "Packaging jar, makes a jar. Packaging war, makes a war."),
 ]),
 ('inside', [
  c('b1', "A war has a strict layout. The container expects it exactly."),
  c('b2', "Files in the top folder, like index dot H T M L, are public pages."),
  c('b3', "The folder web inf is private. Browsers can never reach it."),
  c('b4', "Inside web inf: web dot X M L, the settings. Classes, your compiled code. And lib, the library jars."),
  c('b5', "Maven builds this layout for you from your source folders: source, main, webapp, plus your compiled classes and your dependencies."),
 ]),
 ('scope', [
  c('x1', "Which libraries go in the war? That depends on the scope."),
  c('x2', "Compile scope, the default. Needed to build and to run. Maven copies it into web inf lib."),
  c('x3', "Provided scope. Needed to build, but the server already has it. Maven does not package it."),
  c('x4', "A classic example is the servlet A P I. The container supplies it. If you pack your own copy, you can break the server."),
  c('x5', "So the rule: when the server supplies it, mark it provided."),
 ]),
 ('war', [
  k('w0', "Go to the demo project. Type: C D, demo."),
  c('w1', "First, build it as it is. Type: mvn -B -q clean package && ls target", "First, build it as it is. Type: M V N, dash B, dash Q, clean package, and, L S target."),
  c('w1w', "Quiet mode, so only problems print."),
  c('w1b', "A jar. Cart web, one point zero point zero, dot jar. Not deployable on a server."),
  c('w2', "Change the packaging. Type: sed -i 's/<packaging>jar/<packaging>war/' pom.xml", "Change the packaging with sed. It swaps the word jar for the word war."),
  c('w3', "Name the file. Type: sed -i '/<build>/a  <finalName>cloudcart</finalName>' pom.xml", "Next, give the file a clean name. This line adds a final name, cloud cart, inside the build block."),
  c('w4', "Build again. Type: mvn -B -q clean package && ls target", "Build again, with the same command."),
  c('w4w', "Same command as before."),
  c('w4b', "Now there is a cloud cart dot war. And a folder with the unpacked version."),
  c('w5', "Look inside. Type: unzip -Z1 target/cloudcart.war | grep -v '/$'", "Look inside. Type: unzip, dash Z one, the war, then hide the folder lines."),
  c('w5b', "The page, at the top. In web inf: web dot X M L, the compiled cart class, and two jars in lib: you till and lib A."),
  c('w6', "But lib A is supplied by the server. Mark it provided. Type: sed -i '/<artifactId>liba/a  <scope>provided</scope>' pom.xml", "But lib A is supplied by the server. This line adds the scope, provided, under lib A."),
  c('w7', "Rebuild and list again. Type: mvn -B -q clean package && unzip -Z1 target/cloudcart.war | grep -v '/$'", "Rebuild, and list the contents again, in one line."),
  c('w7w', "Almost done."),
  c('w7b', "Lib A is gone. Only you till stays in lib. The war is smaller, and cannot clash with the server."),
 ]),
 ('task', [
  c('k1', "Your lab task. Lab eighty-nine gives you a project that builds a jar. Lab check judges your work."),
  c('k2', "It lives at git hub dot com, slash it dash waves, slash dev ops dash A I, in academy, lab, lab eighty-nine dot S H."),
  c('k3', "One: set the packaging to war, and the final name to cloud cart."),
  c('k4', "Two: M V N clean package must make target, cloud cart dot war."),
  c('k5', "Three: save the contents of the war into contents dot text, with unzip dash l."),
  c('k6', "Four: you till must be inside the war. Lib A must not be, so give it provided scope."),
  c('k7', "Five: one sentence in why dot text, about why a provided library stays out. Use the words provided, and server or container."),
  c('k8', "Install a J D K, Maven and unzip first. Then lab up, lab check, and lab down. The shortcut file is shortcuts eighty-nine."),
 ]),
 ('rubric', [
  c('q1', "Pass or fail. You need all six."),
  c('q2', "Five pass lines in lab check."), c('q3', "You can explain what a war is, and what is in it."),
  c('q4', "You can state the layout: pages on top, web inf private."), c('q5', "You can explain compile and provided scope."),
  c('q6', "You can list the contents with unzip."), c('q7', "lab down, nothing left behind."), c('q8', "To pass, all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: lab up, and read the task file."),
  c('z3', "Two: change the packaging, and set the final name."),
  c('z4', "Three: build, and save contents dot text."),
  c('z5', "Four: mark lib A provided, and rebuild."),
  c('z6', "Five: write why dot text, and lab check."),
  c('z7', "Six: lab down, and prove nothing is left."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What is a war?"), c('f13', "Which folder is private?"),
  c('f14', "Which scope keeps a library out of the war?"), c('f15', "Which command lists what is inside?"),
  c('f16', "Objective covered: M C ten, objective five."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: repository mirrors and credentials."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'w1w': 6.0, 'w4w': 6.0, 'w7w': 7.0, 'a5': 0.5, 'b5': 0.5, 'x5': 0.5, 'k8': 0.5, 'q8': 0.5, 'z8': 14.0, 'f17': 10.0}
import os as _os, json as _json
_xp = '/home/claude/academy/lesson89/extra.json'
if _os.path.exists(_xp): EXTRA.update(_json.load(open(_xp)))
CHAP = {'what': 'What is a WAR', 'inside': 'Inside a WAR', 'scope': 'Compile vs provided', 'war': 'Live: build and inspect a WAR', 'task': 'Your lab task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
