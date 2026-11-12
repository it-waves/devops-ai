
RB = 'REAL RECORDING  ·  Gitea server on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('y1', "Your branch is ready. But you cannot just push it into main, because main is what everyone depends on."),
  c('y2', "Today you use a pull request: a proposal to merge your branch, with a conversation and a review before anything lands."),
  c('y3', "You also protect main, so nobody can skip that review, not even by accident."),
  c('y4', "And you watch all of it live, on a real Git server running on this computer."),
 ]),
 ('model', [
  c('d1', "A pull request is a page about one branch. It says: I want to merge this branch into that one. Please take a look."),
  c('d2', "It shows the commits, the changed lines, and a conversation. GitHub calls it a pull request. GitLab calls it a merge request. Same idea."),
  c('d3', "A review has three outcomes. Comment. Approve. Or request changes."),
  c('d4', "A protected branch is a rule on the server. For example: no direct pushes to main, and at least one approval before a merge."),
  c('d5', "Our demo uses Gitea, a free Git server with the same words and almost the same screens. On GitHub, the rule lives under Settings, then Branches. We point out each difference."),
 ]),
 ('protect', [
  c('p1', "Sam opens the team app repository, and signs in."),
  c('p2', "First, protect main. Click Settings."),
  c('p3', "Then Branches, and Add New Rule."),
  c('p4', "The pattern is the branch name: main."),
  c('p5', "Scroll down. Push is disabled: nobody can push straight to main."),
  c('p6', "Now require one approval before a merge."),
  c('p7', "Save the rule. Main is protected."),
 ]),
 ('pr', [
  c('q1', "Now the work. Click Pull Requests."),
  c('q2', "New Pull Request. Merge into main. Pull from the feature branch."),
  c('q3', "Below, Git shows exactly what would change: two commits, two files."),
  c('q4', "Press New Pull Request. Give it a clear title, and a short description: what, and why."),
  c('q5', "Create Pull Request."),
  c('q6', "This is the pull request page. Conversation, Commits, and Files Changed."),
  c('q7', "And look at the merge box. This pull request does not have enough approvals yet: zero of one. The protection works."),
 ]),
 ('review', [
  c('r1', "Now Alex, a teammate, opens the pull request on his own computer, and signs in."),
  c('r2', "He opens Files Changed, and reads the difference like a reviewer."),
  c('r3', "Hover over a line, click the plus, and comment on exactly that line."),
  c('r4', "Start review, so your comments are sent together. Then open the Review menu."),
  c('r5', "Request changes, with a short summary."),
  c('r6', "Back to Sam. He fixes the code on his own machine, commits, and pushes to the same branch. No new pull request is needed."),
  c('r7', "The pull request updates by itself: one new commit appears."),
  c('r8', "Alex reads the change again, opens the Review menu, and approves."),
  c('r9', "Now the merge box turns blue. It can be merged."),
 ]),
 ('merge', [
  c('m1', "Click the arrow next to the merge button. There are several ways to merge."),
  c('m2', "A merge commit keeps every commit and adds one merge. Rebase keeps a straight line. Squash turns the whole branch into a single commit."),
  c('m3', "A team picks one rule. We choose squash, for a tidy main."),
  c('m4', "The message is filled in for you. Tick Delete Branch, because the work will live on main, then confirm the squash merge."),
  c('m5', "Merged. The pull request is closed, and the branch is gone."),
  c('m6', "Look at main: one clean commit, with the pull request number in its message."),
 ]),
 ('task', [
  c('t1', "Your task, on your own GitHub account. It is free."),
  c('t2', "The checker is lab sixty-two dot S H, in the academy slash lab folder of git hub dot com, slash it dash waves, slash dev ops dash A I."),
  c('t3', "One: create a public repository called team app, with one file, and push a branch with a small change."),
  c('t4', "Two: open a pull request from that branch into main, and leave one review comment."),
  c('t5', "Three: protect main, under Settings, Branches, so a pull request is required."),
  c('t6', "Four: merge the pull request, and delete the branch."),
  c('t7', "Then run: sh lab sixty-two dot S H, check, your user name, slash, team app. Four pass lines."),
 ]),
 ('rubric', [
  c('rb1', "Six points, and you need all six."),
  c('rb2', "The checker shows four pass lines."), c('rb3', "Main is protected, and you did not push to it directly."),
  c('rb4', "Your pull request has a clear title and description."), c('rb5', "You can explain comment, approve and request changes."),
  c('rb6', "The branch is deleted after the merge."), c('rb7', "You can say why a team protects main."), c('rb8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, on your own GitHub account."),
  c('z2', "One: create the repository and push a branch."),
  c('z3', "Two: open the pull request, and review it."),
  c('z4', "Three: protect main."),
  c('z5', "Four: merge and delete the branch."),
  c('z6', "Five: run lab check."),
  c('z7', "Six: delete the practice repository when you no longer need it."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What is a pull request?"), c('f13', "What are the three review outcomes?"),
  c('f14', "What does a protected branch stop?"), c('f15', "Why delete the branch after the merge?"),
  c('f16', "Objective covered: M C zero seven, objective six, pull requests, reviews, and protected branches."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: undoing mistakes safely, with restore, revert, and reflog."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {}
import os as _os, json as _json
_xp = '/home/claude/academy/lesson62/extra.json'
if _os.path.exists(_xp): EXTRA.update(_json.load(open(_xp)))
CHAP = {}
UI_LABEL = {
 'p1': 'Sign in as Sam', 'p2': 'Repository  ›  Settings', 'p3': 'Settings  ›  Branches  ›  Add New Rule   (GitHub: Settings  ›  Branches)', 'p4': 'Branch name pattern: main', 'p5': 'Direct push is disabled', 'p6': 'Required approvals: 1', 'p7': 'Save the rule',
 'q1': 'Pull Requests tab', 'q2': 'New Pull Request:  merge into main, pull from the feature branch', 'q3': 'The changes Git would merge', 'q4': 'A clear title and a short description', 'q5': 'Create Pull Request', 'q6': 'Conversation  ·  Commits  ·  Files Changed', 'q7': 'Merge is blocked: 0 of 1 approvals',
 'r1': 'Alex signs in on his own computer', 'r2': 'Files Changed', 'r3': 'Comment on one exact line', 'r4': 'Start review, then open Review', 'r5': 'Request changes', 'r6': 'Sam pushes a fix to the same branch', 'r7': 'The pull request updates by itself', 'r8': 'Alex approves', 'r9': 'Now the merge is allowed',
 'm1': 'Merge options', 'm2': 'Merge commit  ·  Rebase  ·  Squash', 'm3': 'Choose squash', 'm4': 'Tick Delete Branch, then confirm', 'm5': 'Merged. Branch deleted', 'm6': 'main: one clean commit'}
