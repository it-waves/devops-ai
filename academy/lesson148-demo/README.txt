Lesson 148 demo: build once, promote the same artifact.
Run in this order:
  sh naive.sh            three builds, three different fingerprints (the mistake)
  sh build.sh            ONE build, one fingerprint
  sh promote.sh dev      same artifact, dev config
  sh promote.sh test
  sh promote.sh prod
  echo x >> artifacts/shop-1.4.0.tar     tamper with the artifact
  sh promote.sh prod     the check stops it
  sh build.sh            a clean build restores trust
Answers for promo.txt: artifact=one build, never rebuilt / config=changes per environment, outside the artifact / promote=move the same artifact up, after checks
