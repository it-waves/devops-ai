# MC15 Software Testing & QA: plan (owner rules: thorough illustrations where little CLI; UI demos planned in, unhurried and detailed)

Tools: pytest 9 + pytest-html (reports), Playwright 1.63 with real Chrome (UI tests, HTML report, trace viewer), coverage.py (HTML coverage report), GitHub Actions (CI gate UI), a small load tool for O07. Target app: CloudCart (API + health + UI) in cloudcart/.

| Lesson | Objective | Title idea | Style | UI demo |
|---|---|---|---|---|
| L135 | O01 | Test types: unit, integration, API, end-to-end, smoke, regression | Illustrated (pyramid, one real tiny example per type) | none (browser shown for e2e at the end) |
| L136 | O02 | Assertions, fixtures, mocks, test data, isolation | pytest live | none |
| L137 | O03 | Run tests, read reports, exit codes | pytest live + $? | pytest-html report page walked through |
| L138 | O03 bonus | UI tests with Playwright: report and trace viewer | Live UI | Playwright HTML report and trace viewer, every panel explained |
| L139 | O04 | API and health tests for CloudCart | pytest vs CloudCart | none |
| L140 | O05 | Coverage: use it, and its limits | pytest-cov | coverage HTML report |
| L141 | O06 | Tests in CI with pass/fail gates | GitHub Actions | Actions run page, annotations, required check |
| L142 | O07 | Performance, load and security testing: purpose | Illustrated + one small load run | none |
| L143 | O08 | Flaky and environment-dependent tests | pytest live | none |
| L144 | mastery | Testing mastery scenario (lab up/check/down, 0/N to N/N) | live | lab info on screen |

Each lesson: demo, independent task with lab (up/check/down tested 0/N to N/N), pass/fail rubric, objective ID in description. Honesty labels as always.
