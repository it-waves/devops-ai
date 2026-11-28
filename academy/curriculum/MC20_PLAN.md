# MC20 GitHub Actions: plan (drafted 2026-11-27, same format as MC19)

Few, comprehensive lessons (12 to 20 min), one continuous live recording per lesson, simple to advanced, state carries forward. Maven only (CloudCart cart-core from MC19), free resources only, same narrator, mastery lesson last with lab info on screen.

| Lesson | Objectives | Story and live recording |
|---|---|---|
| L177 | O01 workflows, events, jobs, steps, actions, runners; O02 build and test CloudCart | "Your first pipeline": anatomy of a workflow file, push and watch a real run on a hosted runner, setup-java, mvn verify, read the logs, fail a test on purpose, fix it |
| L178 | O03 caching, artifacts, matrices, reusable workflows; O04 branch protection, required checks | "Faster and safer": cache the Maven repo (cold vs warm), upload the jar as an artifact, Java 17/21 matrix, a reusable workflow, then a ruleset that blocks merging a red pull request |
| L179 | O05 secrets, environments, permissions; O06 OIDC; O07 approvals and promotion | "Ship without secrets": GITHUB_TOKEN least privilege, secrets vs variables, environment with required reviewer, OIDC token claims and a trust policy instead of stored keys, promote the same artifact dev to prod |
| L180 | O08 troubleshoot; mastery | "Break it, fix it, prove it": failed workflow, runner label that never starts, permission denied (403 on token), expired secret; then mastery scenario lab180.sh up/check/down |

## Decision: approved 2026-11-27 (owner said yes)
Real runs need a throwaway public repository (free hosted minutes) in the owner's GitHub account/org, driven through the owner's signed-in Chrome. Repo: cloudcart-actions-lab, created through the owner signed-in Chrome, deleted after MC20. Fallback if declined: nektos/act on a local runner (not real GitHub UI; weaker).

## Status (2026-11-27)
- Repo it-waves/cloudcart-actions-lab created (public), Claude GitHub App access granted for that one repo (owner approved via GitHub Mobile). Revoke access and delete the repo after MC20.
- Clone at /home/claude/cloudcart-actions-lab, branch main holds cart-core (pom, Cart, CartTest) and no workflow yet. Push works (a "push negotiation failed" warning is harmless).
- Next: L177 script, scenes, steps; record in the owner Chrome on github.com (signed in as it-waves).

## Status note (2026-11-27)
- GitHub asset hosts (github.githubassets.com, avatars/camo.githubusercontent.com, pipelines.actions.githubusercontent.com) still refused by the sandbox proxy even after the user said they were allowed. Headless Chrome in the workspace therefore renders GitHub unstyled.
- Fallback for MC20 recordings: GitHub UI screens captured from the user's signed-in Chrome (sharp stills/zooms with highlights, narrated step by step); terminal parts (git, mvn, yaml editing) stay live in the workspace. Recheck the hosts before each lesson; if open, record live.

## Status note (2026-11-28)
- All four GitHub hosts now open. Headed Chrome on Xvfb renders github.com/it-waves/cloudcart-actions-lab/actions fully styled (public pages need no login). Real run CI #1 (green, 15s) exists. Headless --screenshot hangs on Actions pages; use the headed recorder.
- Lesson numbers: MC20 lessons start at L180 (L177-L179 were used by MC21). Plan table L177..L180 maps to L180..L183.
- Next: L180 script (draft in /home/claude/academy/mc20_draft), scenes, steps, dry-run, live record.
