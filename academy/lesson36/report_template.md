# MC04 mastery scenario: Linux administration report

Name: ______________________   Date: ______________

## Setup
- Lab started with `lab up` at: ________
- Checker output at the start (paste all four lines):

```
(paste here)
```

## Fault 1
- **Symptom** (the exact message or behaviour, before any change):
- **Cause** (one sentence) and the command that proved it:
- **Fix** (the single command or edit):
- **Proof** (output after the fix):

## Fault 2
- **Symptom:**
- **Cause and proving command:**
- **Fix:**
- **Proof:**

## Fault 3
- **Symptom:**
- **Cause and proving command:**
- **Fix:**
- **Proof:**

## Fault 4
- **Symptom:**
- **Cause and proving command:**
- **Fix:**
- **Proof:**

## Final checker output (all four lines must say PASS)
```
(paste here)
```

## Where I got stuck, and what unstuck me

## Cleanup proof
```
lab down
mount | grep -c lab36                 # expect 0
pgrep -fc "http.server 8080"          # expect 0
sudo iptables -S | grep -c 8080       # expect 0
ls /opt/lab36                         # expect: No such file or directory
```
(paste the output)

## Pass / fail rubric (tick when true)
- [ ] Checker shows four PASS
- [ ] Every fault has symptom, cause, fix and proof
- [ ] One change at a time
- [ ] Report complete, including where I got stuck
- [ ] Cleanup proof shows nothing left behind
- [ ] I ran the lab only in my own virtual machine
