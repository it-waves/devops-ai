
RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('y1', "Open a project's history and it looks like a tangled ball of string. Merge, merge, merge, and nobody can read the story."),
  c('y2', "Last lesson you merged branches. Today you learn the other tool: rebasing, which replays your work on top of the latest code, so history stays a straight line."),
  c('y3', "Three skills. Amend, to fix your last commit. Rebase, to move a branch onto new work. And rebase conflicts, which are just merge conflicts in slow motion."),
  c('y4', "And one golden rule that keeps you out of trouble. As always, there is a lab with a checker at the end."),
 ]),
 ('model', [
  c('d1', "Here is the situation. You branched from main, and did two commits. Meanwhile, someone added a commit to main. The branches have diverged."),
  c('d2', "Merging joins them with a merge commit. Safe, and it keeps the real order of events, but the history now has a fork and a join."),
  c('d3', "Rebasing does something different. Git takes your commits, sets them aside, moves your branch to the tip of main, and replays your commits on top, one at a time."),
  c('d4', "The result is a straight line, as if you had started your work today. But there is a catch."),
  c('d5', "Your commits are copied. They have the same changes, but they are new commits, with new hashes. Rebasing rewrites history."),
  c('d6', "Remember this: rebase rewrites. Amend rewrites too. So everything we do today applies to your own work, not to work other people already have."),
 ]),
 ('amend', [
  k('am1', "First the smallest rewrite: fixing the last commit. This project has a last commit with a lazy message. Go in. Type: C D, site."),
  k('am2', "Look at the history. Type: git log, dash dash one line."),
  k('am3', "The top commit says wip. Work in progress tells your team nothing. Rewrite it. Type: git commit, dash dash amend, dash M, quote, Add owner line, quote."),
  k('am4', "Amend replaces the last commit with a new one. Look again. Type: git log, dash dash one line."),
  c('am5', "Same position, better message, and the hash changed. That is the proof that a new commit replaced the old one. Forgot a file? Stage it, then amend with dash dash no dash edit, and it joins the last commit. Only amend commits you have not shared yet."),
 ]),
 ('rebase', [
  k('rb1', "Now a real rebase. In this project, you are on a feature branch that diverged from main. Go in. Type: C D, site."),
  k('rb2', "Look at the picture. Type: git log, dash dash one line, dash dash graph, dash dash all."),
  k('rb3', "Main has one commit that your branch does not have, and your branch has two that main does not have. Now rebase your branch onto main. You stay on your branch, and name the base. Type: git rebase, main."),
  k('rb4', "Successfully rebased. Git replayed your two commits. Look at the picture again. Type: git log, dash dash one line, dash dash graph, dash dash all."),
  k('rb5', "One straight line. Notice the two commits have new hashes. Now bring it home. Type: git switch, main."),
  k('rb6', "On main. Merge the feature. Type: git merge, feature."),
  k('rb7', "Fast forward! Because the branch now sits right on top of main, there is nothing to combine, so Git just moves the pointer. Final check. Type: git log, dash dash one line, dash dash graph."),
  c('rb8', "A perfectly linear history, with no merge commit. That is why teams love rebase."),
 ]),
 ('rconf', [
  k('rc1', "Rebase can conflict too, just like merge. Here both sides changed the port line. Go in. Type: C D, site."),
  k('rc2', "Rebase onto main. Type: git rebase, main."),
  k('rc3', "Conflict, in app dot conf. Git replays your commits one at a time, and stopped at the first one that does not fit. Ask Git where you are. Type: git status."),
  k('rc4', "Look at the first line: rebase in progress, and the hint tells you what to do. Open the file. Type: cat, app dot conf."),
  k('rc5', "Careful, in a rebase the sides are swapped. Head is main, the code you are rebasing onto. The other side is your own commit being replayed. The team wants port eight thousand eighty. Write the final file. Type: printf, the text in single quotes, port equals eight thousand eighty, backslash N, timeout equals five, backslash N, redirect into app dot conf."),
  k('rc6', "Stage it. Type: git add, app dot conf."),
  k('rc7', "Now tell Git to carry on. Type: git rebase, dash dash continue."),
  k('rc8', "Git may open your editor to confirm the commit message. Just save and close it. In this recording that step is accepted automatically. Your second commit applied cleanly. Check the history. Type: git log, dash dash one line, dash dash graph."),
  c('rc9', "A straight line again. And if you ever panic mid rebase, git rebase dash dash abort takes you back to exactly where you started."),
 ]),
 ('golden', [
  c('g1', "Now the golden rule. Never rebase commits that other people already have."),
  c('g2', "Rebasing creates new commits. If a teammate already built on your old ones, their history and yours no longer match, and fixing that is painful."),
  c('g3', "So: rebase your own local branch before you share it, to keep it clean and current. Once it is pushed and others use it, merge instead."),
  c('g4', "A simple guide. Private work, rebase is fine. Shared work, merge. And when in doubt, merge, because merging never rewrites anything."),
 ]),
 ('task', [
  c('t1', "Your task, in your own Ubuntu virtual machine."),
  k('t2', "The lab is lab sixty dot S H, in the academy slash lab folder of git hub dot com, slash it dash waves, slash dev ops dash A I. Install it like before, then run lab up."),
  c('t3', "It builds a repository with a feature branch that diverged from main. The last commit on the feature says wip."),
  c('t4', "One: on the feature branch, amend the last commit to a clear message."),
  c('t5', "Two: rebase the feature branch onto main."),
  c('t6', "Three: switch to main and merge the feature, so main has all the work, with no merge commit."),
  c('t7', "Four: in answers dot text, write one number: how many commits main has now."),
  c('t8', "Then run lab check. Four pass lines. Remember: only rebase your own unshared work."),
 ]),
 ('rubric', [
  c('rb9', "Six points, and you need all six."),
  c('rb10', "The checker shows four pass lines."), c('rb11', "The history is a straight line, with no merge commit."),
  c('rb12', "The last commit has a clear message, not wip."), c('rb13', "You can explain why rebasing changes the hashes."),
  c('rb14', "The number in answers dot text is correct."), c('rb15', "You ran lab down to clean up."), c('rb16', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: install the lab, and run lab up."),
  c('z3', "Two: amend the last commit message."),
  c('z4', "Three: rebase the feature branch onto main."),
  c('z5', "Four: switch to main, and merge the feature."),
  c('z6', "Five: count the commits, write the number, and run lab check."),
  c('z7', "Six: run lab down."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What does rebase do to your commits?"), c('f13', "Why does the hash change after an amend?"),
  c('f14', "Which commits are safe to rebase?"), c('f15', "How do you back out of a rebase?"),
  c('f16', "Objective covered: M C zero seven, objective four, rebasing."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: remotes, fetch, pull, push, tags, and releases."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'y4': 0.5, 'd6': 0.5, 'am5': 0.5, 'rb8': 0.5, 'rc9': 0.6, 'g4': 0.5, 't8': 0.5, 'rb16': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'model': 'Rebase versus merge', 'amend': 'Fix the last commit', 'rebase': 'Rebase onto main', 'rconf': 'Rebase conflicts', 'golden': 'The golden rule', 'task': 'Your lab task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
