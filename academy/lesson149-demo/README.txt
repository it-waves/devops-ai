Lesson 149 demo: a security gate and an error budget.
Run in this order:
  cat data/requests.csv
  sh scan.sh                 FAIL: a password is in the code
  sed -i 's/"hunter2"/ENV/' src/config.py
  sh scan.sh                 PASS
  sh budget.sh 99.9          SHIP    (47% of the budget used)
  sh budget.sh 99.95         CAREFUL (94% used)
  sh budget.sh 99.99         FREEZE  (budget spent)
Answers for ops.txt: devsecops=security checks inside the pipeline / sre=reliability measured with an error budget / platform=a paved road other teams reuse
