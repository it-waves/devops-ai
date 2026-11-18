Lesson 153 demo: the DevOps Fundamentals mastery scenario (CloudCart delivery review)
Files: shop_deploys.csv (10 deploys in 2 weeks), shop_stages.csv (hours per stage), metrics.sh, bottleneck.sh, plan.sh, check.sh
Your job: run the tools, find and fix the bad row, write report.txt and plan.txt, clean up, then run  sh check.sh
Run:   sh metrics.sh shop_deploys.csv 2     sh bottleneck.sh shop_stages.csv     sh check.sh
report.txt format (key=value): frequency, lead, failure, restore, bottleneck, flow, found
Answers: frequency 5.0 per week; lead time 21.2 hours; failure rate 20 percent; time to restore 3.0 hours (after fixing d07: restored 2026-02-11T14:00, it was written as 09:00, before the deploy); bottleneck review (11.0 h, 37 percent); flow efficiency 31 percent.
Hint if restore looks too good (0.5 hours): look at the failed rows with  grep yes shop_deploys.csv  and check each restored time against its deployed time.
Cleanup: if you make a scratch folder, remove it. check.sh fails while a folder named scratch exists.
Note: the numbers are example data; metrics.sh, bottleneck.sh, plan.sh and check.sh are teaching stand-ins.
