# Lesson 54 task: cloud SDK code with least privilege

Work only in your own Ubuntu 24.04 virtual machine, inside your virtual environment, with `pip install boto3 moto` done. Everything runs against moto, a free mock of AWS, so you need no cloud account and nothing costs money. If you later try this on a real cloud account, use free-tier resources only and delete everything you created when you finish.

Files in this folder: `check54.sh` (the checker) and `report_template.md`. Do not read `solution_s3tools.py` or `solution_policy.json` until you have tried.

Write two files.

1. `policy.json`, an IAM policy that gives read-only access to one bucket named `devops-lab`:
   - `Effect` is `Allow` in every statement.
   - The only actions are `s3:ListBucket` (on the bucket itself) and `s3:GetObject` (on the objects inside it).
   - No `*` anywhere in `Action`, and no bare `*` in `Resource`. Resources are `arn:aws:s3:::devops-lab` and `arn:aws:s3:::devops-lab/*`.

2. `s3tools.py` with one function: `big_files(s3, bucket, min_size)`.
   - `s3` is a boto3 S3 client that the caller passes in (so tests can pass a mocked one).
   - It returns a sorted list of the keys whose size is at least `min_size` bytes.
   - It must handle buckets with more than 1000 objects (use a paginator, because one call returns at most 1000).
   - An empty bucket returns an empty list.

Check yourself: `bash check54.sh .` should print six PASS lines. The checker needs no cloud account.

Report: copy `report_template.md` and fill it in with your commands and their output. End the report with the line `Cleanup: nothing to delete, moto only`, or, if you tried a real account, list what you deleted.
