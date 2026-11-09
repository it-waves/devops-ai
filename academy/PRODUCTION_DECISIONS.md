# Standing production decisions (from the owner, 2026-11-09)
1. VOICE: consistent premium professional male American voice; chosen by listening tests, not specs. Dictionary of technical pronunciations is kept in `pronunciation.json`.
   - Status: APPROVED by owner 2026-11-09: am_eric (Kokoro) is the primary male narrator for the whole bootcamp, speed about 0.97. Final audio standard is confirmed after the SDLC pilot lesson validates it. Command rule: exact syntax on screen, long commands are not spelled out character by character, natural pauses, captions synced to the audio. Legacy RHCSA videos keep af_heart.
2. CURRICULUM: Directive v4.0, Masterclass 01 SDLC first; existing tutorials are audited (Gate A) and reused only if they meet the standard.
3. VISUALS: animated diagrams + genuine terminal/software demonstrations; navy/cyan identity; no static slideshows; no fabricated output; 3D only where it aids comprehension.
4. CLOUD: build Terraform-based labs now; label every lab VERIFIED / PARTIALLY VERIFIED / UNVERIFIED; local emulation never counts as proof of AWS/Azure; no billable deployment without cost estimate, permissions, spend guard, cleanup and owner approval.
5. EXECUTION: proceed without repeated preference questions. Interrupt only for: missing external account/permission, financial commitment, unresolvable critical decision, platform authorization, blocker.

6. LINUX PLATFORM (owner, 2026-11-09): all Linux, Bash and Linux-related academy material (MC02, MC04, MC05 and every lab that needs a Linux host) uses UBUNTU (current LTS, 24.04, GitHub runner `ubuntu-24.04` for CI labs). Consequences:
   - Package management is `apt`; firewall is `ufw` (with nftables underneath); mandatory access control is AppArmor (SELinux is no longer taught in MC04; mention it only as a comparison).
   - Service, user, permission, SSH, LVM, systemd, networking content is the same ideas on Ubuntu.
   - Prompts and outputs on screen come from real Ubuntu runs; label "Ubuntu 24.04 LTS".
   - The 62 published RHCSA EX200 videos stay on Rocky/RHEL because that exam is RHEL-specific. They are not redone.
   - Tomcat, Jenkins, Docker, etc. install on Ubuntu in later Masterclasses.

## UPDATE 2026-11-09 - Voice
Owner reverted the academy narrator to the RHCSA voice: Kokoro `af_heart`, speed 1.0. This supersedes the earlier `am_eric` (0.97) decision. Welcome and SDLC 1 are re-rendered with it. Do not ask again.

## UPDATE 2026-11-09 - Pronunciation (owner feedback)
- SonarQube is spoken "sonar cube" (say-text), JUnit "J Unit".
- Verb "lives" ("code lives in Git") must be /livz/, not /laivz/: pipe.do_tts phonemizes each cue and rewrites lˈaɪvz -> lˈɪvz for any cue containing the word "lives". Add new heteronyms to pronunciation.json and handle them the same way.
- Welcome (INTRO) now explains the program flow: 9 stages, 48 masterclasses (planned), 5 levels, ~5 min lessons, a project per level, stage exams, CloudCart journey, routes, requirements.
- New standalone video: loop/ "The DevOps Loop" (infinity symbol, 8 stages).

## Published (2026-11-09, Public, playlist DevOps Engineering Bootcamp (Full Course), order: Intro, Loop, Lesson 1)
- INTRO: g17YyNgX0Y4  (5:00)
- The DevOps Loop: hbDYFo_t-Zw  (1:26)
- LESSON 1 SDLC: 09EBDVIryE8  (4:27)
- Thumbnails: academy/thumbs/*.jpg; English captions: academy/captions/*.srt (uploaded as SRT).
- Pronunciation (sonar cube, "lives" as livz) verified in phonemes only; owner to listen.
