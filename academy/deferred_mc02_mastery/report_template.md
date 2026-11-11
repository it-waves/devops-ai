# MC02 mastery scenario: shop server report

Name: ______________________   Date: ______________

## Setup
- Lab started with `./lab26.sh up` at: ________
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
./lab26.sh down
ls /tmp/lab26                 # expect: No such file or directory
pgrep -fc /tmp/lab26          # expect 0
```
(paste the output)

## Pass / fail rubric (tick when true)
- [ ] Checker shows four PASS
- [ ] Every fault has symptom, cause, fix and proof
- [ ] One change at a time, in the order I wrote them
- [ ] Cleanup proof shows the folder gone and nothing running
