# MC08 mastery scenario: Application Architecture and APIs report

Name: ______________________   Date: ______________

## Setup
- Lab started with `lab up` at: ________
- Checker output at the start (paste all four lines):

```
(paste here)
```

## Fault 1 (the API does not answer)
- **Symptom** (the exact output, before any change):
- **Cause** (one sentence) and the command that proved it:
- **Fix** (the single command or edit):
- **Proof** (output after the fix):

## Fault 2 (the shop is not ready)
- **Symptom:**
- **Cause and proving command:**
- **Fix:**
- **Proof:**

## Fault 3 (secrets are not private)
- **Symptom:**
- **Cause and proving command:**
- **Fix:**
- **Proof:**

## Fault 4 (no traced request)
- **Symptom:**
- **Cause and proving command:**
- **Fix** (the requests you sent and the search you ran):
- **Proof** (contents of trace.txt):

## Final checker output (all four lines must say PASS)
```
(paste here)
```

## Where I got stuck, and what unstuck me

## Cleanup proof
```
lab down
ls /opt/lab75                          # expect: No such file or directory
ls /opt | grep -c lab75                # expect 0
sudo rm /usr/local/sbin/lab75.sh
ls /usr/local/sbin | wc -l             # expect 0 if nothing else is installed there
ss -ltn | grep -c 8080                 # expect 0: nothing still listening
```
(paste the output)

## Pass / fail rubric (tick when true)
- [ ] Checker shows four PASS
- [ ] Every fault has symptom, cause, fix and proof
- [ ] One change at a time
- [ ] Report complete, including where I got stuck
- [ ] Cleanup proof shows nothing left behind and nothing listening
- [ ] I ran the lab only in my own virtual machine
