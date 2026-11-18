Lesson 151 demo: finding the bottleneck
Files: stages.csv (hours of work and of waiting for each pipeline stage), stages_after.csv (after the fix), bottleneck.sh
Run:   sh bottleneck.sh stages.csv      then      sh bottleneck.sh stages_after.csv
Answers (stages.csv): total 70.0 h (work 10.5, waiting 59.5); slowest stage approval, 30.5 h, 44 percent; flow efficiency 15 percent
Answers (stages_after.csv): total 26.0 h; slowest stage is now code, 8.0 h; flow efficiency 40 percent. The bottleneck moved.
Note: the numbers are example data and bottleneck.sh is a teaching stand-in. Real teams get these times from their pipeline, review and ticket tools.
