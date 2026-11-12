
RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('y1', "One password in the wrong place can cost a company its whole cloud account. Bots scan public repositories for secrets, often within minutes."),
  c('y2', "Today you learn how secrets leak into Git, what to do the moment one does, and how to give people and programs only the access they need."),
  c('y3', "You will use a leaked password, an S S H key, an access token, and repository roles."),
  c('y4', "As always, there is a lab with a checker at the end."),
 ]),
 ('model', [
  c('d1', "A secret is anything that proves who you are: a password, an A P I key, a token, a private key."),
  c('d2', "Git never forgets. Once a secret is committed, it lives in the history, even if you delete the file in the next commit."),
  c('d3', "Rule one: keep secrets out. Use environment variables, a dot E N V file that Git ignores, or a secret manager."),
  c('d4', "Rule two: if one leaks, assume it is stolen. Rotate it first, which means make a new one and kill the old one. Only then clean the history."),
  c('d5', "Rule three: least access. An S S H key pair has a private half that never leaves your computer, and a public half you share. Tokens should have the smallest scope, and roles the smallest permission."),
 ]),
 ('leak', [
  k('lk1', "A real mistake, live. A small app repository. Go in. Type: C D, app."),
  k('lk2', "Look at the history. Type: git log, dash dash one line."),
  k('lk3', "Add database settings. That sounds risky. Look at the file. Type: cat, dot E N V."),
  c('lk4', "A database password, committed. This one is fake, but the mistake is real. First rotate it, in real life. Then stop tracking the file. Type: echo, quote, dot E N V, quote, two arrows, dot git ignore.", "A database password, committed. This one is fake, but the mistake is real. In real life, rotate it first. Then ignore the file. Type: echo, quote, dot E N V, quote, two arrows, dot git ignore."),
  k('lk5', "Remove it from Git, but keep the file on disk. Type: git R M, dash dash cached, dot E N V."),
  k('lk6', "Stage the ignore file. Type: git add, dot git ignore."),
  k('lk7', "Commit. Type: git commit, dash M, quote, Stop tracking dot E N V, quote."),
  c('lk8', "Fixed? Search the whole history for the password. Type: git log, dash S, demo dash secret, dash dash one line.", "Fixed? Search the whole history for the password. Type: git log, dash S, demo dash secret, dash dash one line."),
  c('lk9', "Still there! The old commit still holds the secret, and anyone with a copy can read it. This is why rotating comes first. Now rewrite history without that file. Type: git filter dash repo, dash dash path, dot E N V, dash dash invert dash paths, dash dash force.", "Still there! The old commit still holds the secret, and anyone with a copy can read it. Rewrite history without that file. Type: git filter dash repo, dash dash path, dot E N V, dash dash invert dash paths, dash dash force."),
  k('lk10', "Search again. Type: git log, dash S, demo dash secret, dash dash one line."),
  k('lk11', "Nothing found. Check the history. Type: git log, dash dash one line."),
  c('lk12', "The secret commit is gone. On a real shared repository, everyone must re-clone, and the old password must stay dead. The force flag is only safe here because this is a practice repository."),
 ]),
 ('ssh', [
  k('ss1', "Now S S H keys: log in without a password, safely. Make the folder. Type: M K dir, dash P, tilde slash dot S S H."),
  c('ss2', "Generate a key pair. Type: S S H dash key gen, dash T, E D two five five one nine, dash C, sam at example dot com, dash F, tilde slash dot S S H slash lab sixty-four underscore key, dash N, two quotes.", "Generate a key pair. Type: S S H key gen, dash T, E D two five five one nine, dash C, sam at example dot com, dash F, the key path, and dash N, two quotes, for no passphrase."),
  c('ss3', "Two files were made. Look. Type: L S, tilde slash dot S S H.", "Two files were made. Look. Type: L S, tilde slash dot S S H."),
  c('ss4', "The one ending in dot pub is the public key. This is the one you paste into git hub. Type: cat, the key path, dot pub.", "The one ending in dot pub is the public key. This is the one you paste into git hub. Type: cat, the key path, dot pub."),
  c('ss5', "The other file is the private key. Never share it, never commit it. Peek at its first line only. Type: head, dash N one, the key path.", "The other file is the private key. Never share it. Peek at its first line only. Type: head, dash N one, the key path."),
  c('ss6', "In real life, always set a passphrase on your key. We skipped it only to keep this demo short."),
 ]),
 ('token', [
  c('tk1', "Programs need access too. On git hub it is a personal access token. This demo is on Gitea, which has the same idea. Open your settings, then Applications."),
  c('tk2', "Give the token a name that says what it is for: C I read only."),
  c('tk3', "Now the scopes. Everything starts at No Access. Give the one thing it needs: repository, read only."),
  c('tk4', "Generate the token. It is shown once. Copy it into your secret store now, because you will never see it again."),
  c('tk5', "Treat it like a password: never in code, never in a chat. And revoke it when the job is done."),
 ]),
 ('access', [
  c('ac1', "Now people. Open the repository, then Settings, then Collaborators."),
  c('ac2', "Alex can write. That is right for a teammate who pushes. For a reviewer who only reads, we use Read."),
  c('ac3', "Change Alex to Read. The menu offers Read, Write, and Admin."),
  c('ac4', "Give people the smallest role that lets them do their job. Admin can delete the repository, so keep it for very few people."),
 ]),
 ('task', [
  c('t1', "Your task, in your own Ubuntu virtual machine."),
  k('t2', "The lab is lab sixty-four dot S H, in the academy slash lab folder of git hub dot com, slash it dash waves, slash dev ops dash A I. Install it like before, then run lab up."),
  c('t3', "It builds a repository where a fake password was committed by mistake."),
  c('t4', "One: stop tracking dot E N V, and list it in dot git ignore."),
  c('t5', "Two: rewrite the history so the secret is gone."),
  c('t6', "Three: make an E D two five five one nine S S H key named lab sixty-four underscore key."),
  c('t7', "Four: in answers dot text, write the first thing you do when a secret leaks: the word rotate."),
  c('t8', "Then run lab check. Four pass lines. Rotate, then clean."),
 ]),
 ('rubric', [
  c('rb1', "Six points, and you need all six."),
  c('rb2', "The checker shows four pass lines."), c('rb3', "The secret is gone from every commit."),
  c('rb4', "Your private key stays private, and is never committed."), c('rb5', "You can explain why rotate comes before cleaning history."),
  c('rb6', "You can name the smallest token scope or role for a job."), c('rb7', "You ran lab down to clean up."), c('rb8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: install the lab, and run lab up."),
  c('z3', "Two: ignore and untrack dot E N V."),
  c('z4', "Three: rewrite history with git filter repo."),
  c('z5', "Four: generate the S S H key."),
  c('z6', "Five: write the answer, and run lab check."),
  c('z7', "Six: run lab down."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Why does deleting a file not remove a secret from Git?"), c('f13', "What do you do first when a secret leaks?"),
  c('f14', "Which half of an S S H key pair do you share?"), c('f15', "What is least access?"),
  c('f16', "Objective covered: M C zero seven, objective eight, secrets, credentials, and repository access."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: a team release workflow with automated checks."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'y4': 0.5, 'd5': 0.5, 'lk12': 0.5, 'ss6': 0.5, 'tk5': 0.5, 'ac4': 0.5, 't8': 0.5, 'rb8': 0.5, 'z8': 14.0, 'f17': 10.0}
import os as _os, json as _json
_xp = '/home/claude/academy/lesson64/extra.json'
if _os.path.exists(_xp): EXTRA.update(_json.load(open(_xp)))
CHAP = {'model': 'Secrets, and three rules', 'leak': 'A leaked password', 'ssh': 'SSH keys', 'token': 'Access tokens', 'access': 'Repository roles', 'task': 'Your lab task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
UI_LABEL = {
 'tk1': 'Settings  ›  Applications   (GitHub: Developer settings)', 'tk2': 'Name the token for its job', 'tk3': 'Scope: repository, read only. Everything else: No Access', 'tk4': 'Generate. Shown once: store it now', 'tk5': 'Never in code. Revoke when done',
 'ac1': 'Repository  ›  Settings  ›  Collaborators', 'ac2': 'Alex has Write', 'ac3': 'Change to Read   (Read · Write · Admin)', 'ac4': 'Smallest role that does the job',
}
