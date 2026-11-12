
RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('y1', "You made great commits on your laptop. Now what? If the laptop dies, they are gone. And your team has never seen them."),
  c('y2', "Today you connect your repository to a shared copy, and learn the daily rhythm of team work: fetch, pull, and push."),
  c('y3', "Plus tags, which stamp a version like one point oh on a commit, so everyone can find exactly what shipped."),
  c('y4', "As always, there is a lab with a checker at the end."),
 ]),
 ('model', [
  c('d1', "A remote is just another copy of your repository, usually on a server. Git gives each remote a nickname, and the default is origin."),
  c('d2', "When you clone, Git copies everything and remembers where it came from. That source is origin."),
  c('d3', "Git also keeps a bookmark of where the remote branch was the last time you talked to it. It is called origin slash main, a remote tracking branch. It only moves when you talk to the server."),
  c('d4', "Fetch downloads new commits and moves that bookmark. It never touches your own files, so it is always safe."),
  c('d5', "Pull is fetch, plus a merge or a rebase. It updates your own branch, so it can change your files."),
  c('d6', "And push uploads your commits. Git only allows it when you will not overwrite anyone else's work."),
 ]),
 ('clone', [
  k('cl1', "Let us see it live. A team repository lives on a server, at slash S R V, slash git, slash team dot git. Clone it. Type: git clone, slash S R V, slash git, slash team dot git."),
  k('cl2', "Cloned. Go into the folder. Type: C D, team."),
  k('cl3', "List the remotes. Type: git remote, dash V."),
  k('cl4', "Origin, with an address for fetching and one for pushing. Now the branches, and what they track. Type: git branch, dash V V."),
  k('cl5', "Main tracks origin slash main, shown in square brackets. Now list every branch, including remote ones. Type: git branch, dash A."),
  c('cl6', "The remote tracking branches live under remotes slash origin. You never commit on them. They are bookmarks of the server."),
 ]),
 ('fetch', [
  k('ft1', "Now a teammate pushes while you are working. Go into your clone. Type: C D, team."),
  k('ft2', "Ask for the status. Type: git status."),
  k('ft3', "Up to date with origin slash main. But careful: that only means up to date with your last bookmark. Git has not asked the server. Ask for news. Type: git fetch."),
  k('ft4', "A new commit arrived on origin slash main. Check again. Type: git status."),
  k('ft5', "Now it knows: behind by one commit. See what is waiting, before you take it. Type: git log, dash dash one line, main, two dots, origin slash main."),
  k('ft6', "Two dots mean: commits on the right that are not on the left. One commit, from Alex. Now bring it in. Type: git pull."),
  k('ft7', "Fast forward, and your files updated. Look at the history. Type: git log, dash dash one line."),
  c('ft8', "A good habit: fetch, look, then pull. Nothing surprises you."),
 ]),
 ('push', [
  k('ps1', "Now share your own work. Go in. Type: C D, team."),
  k('ps2', "Make the start script friendlier. Type: echo, quote, echo ready, quote, two arrows, start dot S H."),
  k('ps3', "Commit it. Type: git commit, dash A M, quote, Print ready message, quote."),
  k('ps4', "Now share it. Type: git push."),
  k('ps5', "Rejected! The remote has a commit you do not have, and Git refuses to overwrite it. That is a protection, not a bug. The hint says it: fetch first. Pull your teammate's work, and replay yours on top. Type: git pull, dash dash rebase."),
  k('ps6', "Rebased. Now push again. Type: git push."),
  k('ps7', "Pushed. Look at the picture. Type: git log, dash dash one line, dash dash graph, dash dash all."),
  c('ps8', "Origin slash main and your main sit on the same commit, in a straight line. And never force push to a shared branch: it can erase your teammates' work."),
 ]),
 ('tags', [
  k('tg1', "Last skill: tags. A tag is a permanent name for one commit, like version one point oh. Go in. Type: C D, team."),
  k('tg2', "Create an annotated tag, with a message. Type: git tag, dash A, V one dot zero, dash M, quote, First release, quote."),
  k('tg3', "List the tags. Type: git tag."),
  k('tg4', "See what the tag holds. Type: git show, dash dash stat, V one dot zero."),
  k('tg5', "The tagger, the date and the message, then the commit it points to. Tags are not pushed automatically. Type: git push, origin, V one dot zero."),
  k('tg6', "Pushed as a new tag. Confirm on the server. Type: git L S dash remote, dash dash tags, origin."),
  c('tg7', "The tag is on the server. Everyone can check out exactly this version. To push all your tags at once, use git push origin dash dash tags. On GitHub, a tag becomes a release, with notes and downloads, and we will make one on screen soon."),
 ]),
 ('task', [
  c('t1', "Your task, in your own Ubuntu virtual machine."),
  k('t2', "The lab is lab sixty-one dot S H, in the academy slash lab folder of git hub dot com, slash it dash waves, slash dev ops dash A I. Install it like before, then run lab up."),
  c('t3', "It builds a shared repository, and your clone of it. While you were away, a teammate pushed a commit."),
  c('t4', "One: create release notes dot text with one line of text, and commit it."),
  c('t5', "Two: push it. Git will reject the push, so pull your teammate's work first, then push again."),
  c('t6', "Three: create an annotated tag, V one dot zero, and push it to origin."),
  c('t7', "Four: in answers dot text, write one number: how many commits origin main has now."),
  c('t8', "Then run lab check. Four pass lines. Fetch first, look, then pull."),
 ]),
 ('rubric', [
  c('rb1', "Six points, and you need all six."),
  c('rb2', "The checker shows four pass lines."), c('rb3', "You pulled before you pushed, and never used force."),
  c('rb4', "The tag is annotated and on the server."), c('rb5', "You can explain what fetch does that pull does not."),
  c('rb6', "The number in answers dot text is correct."), c('rb7', "You ran lab down to clean up."), c('rb8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: install the lab, and run lab up."),
  c('z3', "Two: commit the release notes."),
  c('z4', "Three: push, fix the rejection by pulling, and push again."),
  c('z5', "Four: tag, and push the tag."),
  c('z6', "Five: count the commits, write the number, and run lab check."),
  c('z7', "Six: run lab down."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What does fetch do that pull does not?"), c('f13', "What is origin slash main?"),
  c('f14', "Why was your first push rejected?"), c('f15', "Are tags pushed automatically?"),
  c('f16', "Objective covered: M C zero seven, objective five, remotes, fetch, pull, push, and tags."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: pull requests, reviews, and protected branches."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'y4': 0.5, 'd6': 0.5, 'cl6': 0.5, 'ft8': 0.5, 'ps8': 0.6, 'tg7': 0.6, 't8': 0.5, 'rb8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'model': 'Remotes and origin', 'clone': 'Clone and remote tracking', 'fetch': 'Fetch, then pull', 'push': 'Push and rejection', 'tags': 'Tags', 'task': 'Your lab task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
