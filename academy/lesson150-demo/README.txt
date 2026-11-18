Lesson 150 demo: the four key DevOps metrics
Files: deploys.csv (a healthy team, 4 weeks), deploys_slow.csv (a team that ships in big batches), metrics.sh
Run:   sh metrics.sh deploys.csv      then      sh metrics.sh deploys_slow.csv
Answers (deploys.csv): 12 deploys / 3.0 per week; lead time 15.5 hours; failure rate 17% (2 of 12); time to restore 2.2 hours
Answers (deploys_slow.csv): 4 deploys / 1.0 per week; lead time 262.5 hours; failure rate 50% (2 of 4); time to restore 39.5 hours
Note: the data is example data and metrics.sh is a teaching stand-in. Real teams read these numbers from their pipeline and incident tools.
