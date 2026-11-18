Lesson 146 demo: CI, continuous delivery, continuous deployment.
Run:   sh pipeline.sh ci
       sh pipeline.sh delivery          (stops: waits for a human)
       sh pipeline.sh delivery approve  (a human says go)
       sh pipeline.sh deployment        (no human: tests decide)
Break it: sed -i 's/\*/+/' src/shop.py   then run deployment again.
Answers (modes.txt): ci=build and test every commit;
  delivery=always ready, a human approves; deployment=automatic.
After the break, prod must still hold exactly 2 releases.
