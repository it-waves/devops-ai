# MC03 mastery scenario: network diagnosis report

Name: ______________________   Date: ______________

## Setup
- Lab started with `sudo lab25.sh up` at: ________
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
sudo lab25.sh down
ip netns list | wc -l          # expect 0
pgrep -fc web25.py             # expect 0
```
(paste the output)

## Pass / fail rubric (tick when true)
- [ ] Checker shows four PASS
- [ ] Every fault has symptom, cause, fix and proof
- [ ] One change at a time, in the order I wrote them
- [ ] Cleanup proof shows 0 namespaces and 0 servers
