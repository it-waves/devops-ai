RB = 'REAL RECORDING  ·  Ubuntu 24.04, local repo'
SCENES = [
 ('hook', [
  c('h1', "Your build works. The jar sits on your laptop. And your teammate cannot use it."),
  c('h2', "Until you publish it, to the repository your whole company shares. That step is called deploy."),
  c('h3', "Today you learn the two kinds of version, snapshot and release, and the one rule that surprises everybody."),
  c('h4', "Then you publish, and break the rule on purpose."),
  c('h5', "One honest note. The company repository in this lesson is a small local server I started, that accepts uploads with a login. The real thing is a repository manager like nexus or artifactory, but Maven uploads to it the same way."),
 ]),
 ('what', [
  c('a1', "Install copies your jar into your own dot m two folder. Deploy uploads it to a remote repository, so others can download it."),
  c('a2', "A repository manager usually has two repositories. One for snapshots, and one for releases."),
  c('a3', "A snapshot is work in progress. The version ends with dash snapshot. You may publish it again and again."),
  c('a4', "A release is final. The version has no snapshot. Once published, it can never be replaced."),
  c('a5', "The pom says where to upload. In the block distribution management, one address for snapshots, and one for releases."),
 ]),
 ('rule', [
  c('b1', "Why can a release never be replaced? Because other people built on it."),
  c('b2', "If the jar for one dot zero dot zero changed tomorrow, an old build could not be repeated. The same version would mean different code."),
  c('b3', "So the repository refuses. It answers four oh nine, conflict. The right fix is never to overwrite. Publish one dot zero dot one."),
  c('b4', "A snapshot is different. Maven adds a time stamp, so each upload is a new file, and the newest one wins."),
  c('b5', "And the login? The same as last lesson. A server block, with the same id, and the password from an environment variable."),
 ]),
 ('deploy', [
  k('d0', "Go to the demo project. Type: C D, demo."),
  c('d1', "Look at the upload addresses in the pom. Type: sed, dash n, eleven comma twenty-two, p, pom dot X M L.", "Look at the upload addresses in the pom. Type: sed, dash n, eleven comma twenty-two p, pom dot X M L."),
  c('d1b', "Two repositories, snapshots and releases. Both with the id corp, so one login serves both."),
  c('d2', "Set the password from the locked file. Type: export REPO_PASS equals dollar, parenthesis, cat, tilde, slash, dot corp dash pass.", "Set the password from the locked file, as you learned last lesson."),
  c('d3', "Deploy the snapshot. Type: mvn dash B dash q deploy, then list the snapshot folder.", "Deploy the snapshot, in quiet mode, and then list the jar files in the snapshot repository."),
  c('d3w', "Maven builds, then uploads."),
  c('d3b', "One jar, with a time stamp in its name."),
  c('d4', "Deploy it again. The same command.", "Deploy again, with the same command, and list the jar files once more."),
  c('d4w', "A second upload."),
  c('d4b', "Two jars now. Each upload is a new file, and nothing was refused."),
  c('d5', "Now make it a release. Remove the word snapshot from the version, with sed.", "Now make it a release. This removes dash snapshot from the version, and shows the version line."),
  c('d5b', "Version one dot zero dot zero. No snapshot."),
  c('d6', "Deploy it. Type: mvn dash B dash q deploy, then list the release folder.", "Deploy the release, and list the jar files in the release repository."),
  c('d6w', "Uploading the release."),
  c('d6b', "The release is published."),
  c('d7', "Now the rule. Deploy the same version again, and keep only the error.", "Now the rule. Deploy the same release again, and keep only the line with the status code."),
  c('d7w', "Same version, second time."),
  c('d7b', "Four oh nine. Conflict. The repository protects the release. To change anything, you need a new version."),
 ]),
 ('task', [
  c('k1', "Your lab task. Lab ninety-one gives you a project and a repository that accepts uploads. Lab check judges your work."),
  c('k2', "It lives at git hub dot com, slash it dash waves, slash dev ops dash A I, in academy, lab, lab ninety-one dot S H."),
  c('k3', "One: set the variable corp pass from the password file, and deploy the snapshot, with dash s settings dot X M L."),
  c('k4', "Two: change the version to one dot zero dot zero, and deploy the release."),
  c('k5', "Three: deploy it again. It must fail. Save the error line into conflict dot text."),
  c('k6', "Four: change the version to one dot zero dot one, and deploy that."),
  c('k7', "Five: one sentence in why dot text, about why a release is never published twice. Use the word release."),
  c('k8', "Install a J D K, Maven and python three first. Then lab up, lab check, and lab down. The shortcut file is shortcuts ninety-one. The check downloads plugins once, so be online."),
 ]),
 ('rubric', [
  c('q1', "Pass or fail. You need all six."),
  c('q2', "Five pass lines in lab check."), c('q3', "You can explain snapshot and release."),
  c('q4', "You can explain why the second release deploy fails."), c('q5', "The fix is a new version, never an overwrite."),
  c('q6', "The password stays out of every file."), c('q7', "lab down, nothing left behind."), c('q8', "To pass, all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: lab up, and read the task file."),
  c('z3', "Two: deploy the snapshot."),
  c('z4', "Three: deploy the release, then deploy it again, and save the error."),
  c('z5', "Four: publish one dot zero dot one."),
  c('z6', "Five: write why dot text, and lab check."),
  c('z7', "Six: lab down, and prove nothing is left."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What is the difference between install and deploy?"), c('f13', "Snapshot or release: which can be uploaded twice?"),
  c('f14', "What does four oh nine mean?"), c('f15', "What do you do when a release has a bug?"),
  c('f16', "Objective covered: M C ten, objective seven."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: diagnose offline, checksum, login and test failures."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'d3w': 7.0, 'd4w': 6.0, 'd6w': 6.0, 'd7w': 6.0, 'a5': 0.5, 'b5': 0.5, 'k8': 0.5, 'q8': 0.5, 'z8': 14.0, 'f17': 10.0}
import os as _os, json as _json
_xp = '/home/claude/academy/lesson91/extra.json'
if _os.path.exists(_xp): EXTRA.update(_json.load(open(_xp)))
CHAP = {'what': 'Install vs deploy, snapshot vs release', 'rule': 'Why a release is immutable', 'deploy': 'Live: deploy snapshot, release, 409', 'task': 'Your lab task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
