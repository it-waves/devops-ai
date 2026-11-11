RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
SCENES = [
 ('hook', [
  c('h1', "Every server runs software that someone had to install. Doing it by hand does not scale."),
  c('h2', "On Ubuntu, a package manager does it for you. A package is a program, plus the list of what it needs. Apt finds packages in repositories, and D P K G installs them."),
  c('h3', "Today you read the repository list, inspect packages, preview an install, and learn the update routine."),
 ]),
 ('repo', [
  c('q1', "Where do packages come from? From repositories, listed in one file. Type: grep ^URIs, then the path.", "Where do packages come from? From repositories, listed in one file. Type: grep, caret, U R Is, then the path. The caret keeps only lines that start with that word."),
  c('q2', "Two addresses. The main Ubuntu archive, and a separate security archive. Each one is a repository."),
  c('q3', "Now the suites. Type: grep ^Suites, and the same path.", "Now the suites. Type: grep, caret, Suites, and the same path."),
  c('q4', "Suites are release channels. Noble is Ubuntu twenty-four oh four as released. Noble dash updates carries fixes. Noble dash security carries security fixes.", "Suites are release channels. Noble is Ubuntu twenty-four oh four as released. Noble dash updates carries fixes. Noble dash security carries security fixes."),
  c('q5', "Now ask about one package. Type: apt-cache policy curl | head -n 4.", "Now ask about one package. Type: apt cache, policy, curl, pipe, head, dash n, four."),
  c('q6', "Installed is the version you have. Candidate is the newest version the repositories offer. If they differ, an update is waiting."),
 ]),
 ('installed', [
  c('d1', "What is installed? Ask the package database. Type: dpkg -s curl | head -n 4.", "What is installed? Ask the package database. Type: D P K G, dash s, curl, pipe, head, dash n, four."),
  c('d2', "Status says install ok installed. The database is the record of what is on this machine."),
  c('d3', "Which package owns a file? Type: dpkg -S /usr/bin/curl.", "Which package owns a file? Type: D P K G, dash capital S, slash U S R, slash bin, slash curl."),
  c('d4', "The curl package owns it. Use this when you find a file and wonder where it came from."),
  c('d5', "And which files does a package put on disk? Type: dpkg -L curl | grep bin.", "And which files does a package put on disk? Type: D P K G, dash capital L, curl, pipe, grep, bin."),
  c('d6', "The bin folder, and the curl program itself."),
 ]),
 ('plan', [
  c('n1', "Always preview first. Dash s means simulate, so nothing changes. Type: apt-get -s install cowsay | tail -n 6.", "Always preview first. Dash s means simulate, so nothing changes. Type: apt get, dash s, install, cowsay, pipe, tail, dash n, six."),
  c('n2', "Two packages would be installed: cowsay, and a library it depends on. Apt works out dependencies for you."),
  c('n3', "The Inst lines are the plan, and the dependency comes first."),
  c('n4', "Now preview a removal. Type: apt-get -s remove curl | tail -n 4.", "Now preview a removal. Type: apt get, dash s, remove, curl, pipe, tail, dash n, four."),
  c('n5', "It would remove curl. Read what will be removed before you agree to anything."),
  c('n6', "How many updates are waiting? Type: apt-get -s upgrade | grep, and keep the line that starts with a number.", "How many updates are waiting? Type: apt get, dash s, upgrade, pipe, grep, and keep the line that starts with a number."),
  c('n7', "The first number is how many packages could be upgraded. Your number will differ."),
 ]),
 ('manage', [
  c('a1', "Now the commands that change the system. They need sue do and a real machine, so these screens are an illustration."),
  c('a2', "First: sudo apt update. It refreshes the package lists from the repositories. It installs nothing."),
  c('a3', "Then: sudo apt install, and the package name. Apt shows the plan, and asks you to confirm."),
  c('a4', "To bring everything current: sudo apt upgrade. Update first, then upgrade."),
  c('a5', "Remove takes the program away. Purge also deletes its configuration files."),
  c('a6', "Then: sudo apt autoremove. It removes dependencies that nothing needs any more."),
  c('a7', "Add repositories only from sources you trust. Read the plan, then answer yes."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: apt update installs updates. No. Update refreshes the list. Upgrade installs."),
  c('my3', "Myth two: remove deletes everything. No. Purge also deletes the configuration."),
  c('my4', "Myth three: any download is safe if it installs. No. Use trusted repositories."),
  c('my5', "Myth four: answer yes to every prompt. No. Read the plan first."),
  c('my6', "Update, read the plan, then upgrade."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding."), c('b2', "Read the repository list, and say where packages come from."),
  c('b3', "Compare the installed and candidate versions."), c('b4', "Find which package owns a file, with D P K G."),
  c('b5', "Preview an install with a simulation, and read the plan."), c('b6', "Explain update, upgrade, remove, purge and autoremove."),
  c('b7', "Say how to add software safely."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your virtual machine. These tasks only read, or simulate. Nothing is installed."),
  c('z2', "One: read your repository list, and name the suites."),
  c('z3', "Two: run apt-cache policy for a package, and compare installed with candidate."),
  c('z4', "Three: use D P K G dash s and dash capital S on a program you use."),
  c('z5', "Four: simulate an install of a small package, with dash s, and read the plan."),
  c('z6', "Five: run sudo apt update, then apt list dash dash upgradable. Update only refreshes the lists.", "Five: run sue do apt update, then apt list, dash dash upgradable. Update only refreshes the lists."),
  c('z7', "Six: simulate a removal, and say what purge would add."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which command refreshes the package lists?"), c('f13', "Which flag simulates an install?"),
  c('f14', "Which D P K G option finds the owner of a file?"), c('f15', "Does remove delete configuration files?"),
  c('f16', "Objective covered: MC04-O07.", "Objective covered: M C zero four, objective seven, in the Linux administration masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: disks, filesystems and mounts."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'q3': 1.0, 'h3': 0.5, 'q2': 0.4, 'q4': 0.5, 'q6': 0.5, 'd2': 0.4, 'd4': 0.4, 'd6': 0.5, 'n2': 0.4, 'n3': 0.4, 'n5': 0.4, 'n7': 0.5, 'a1': 0.4, 'a2': 0.4, 'a5': 0.4, 'a7': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'repo': 'Repositories and versions', 'installed': 'Inspect installed packages', 'plan': 'Preview before you change', 'manage': 'Install, update, remove', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
