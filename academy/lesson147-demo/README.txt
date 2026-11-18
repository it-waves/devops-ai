Lesson 147 demo: infrastructure as code, configuration management, automation.
Run, in order:
  sh naive.sh ; sh naive.sh ; cat naive/app.conf   (lines are doubled: not safe to repeat)
  sh apply.sh                                       (changed, changed)
  sh apply.sh                                       (ok, ok: idempotent)
  echo port=9999 > server/app.conf                  (someone edits by hand: drift)
  sh check.sh                                       (DRIFT)
  sh apply.sh ; sh check.sh                         (fixed, clean)
Answers (iac.txt): iac=infrastructure described as code;
  config=same result on every run; automation=no manual steps.
