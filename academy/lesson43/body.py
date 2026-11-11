RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "A script is only as safe as what it handles. Passwords and tokens. Who is allowed to run it. What a user types in. And what the shell does with that text. Get one of them wrong, and a small script becomes a hole."),
  c('h2', "Today you learn four habits. Keep secrets out of the script. Lock down permissions. Validate every input. And never let input become code."),
  c('h3', "Every demo is a real recording on Ubuntu. Every secret you see is fake, made up for this lesson."),
 ]),
 ('secrets', [
  k('se1', "First, secrets. Never write a password inside a script. Here is a bad example. Type: cat bad dot S H."),
  k('se2', "The password sits in the file. Anyone who can read the script, or the repository it lands in, can read the password. The better way is a separate file. Check the permissions of this one. Type: L S, dash L, dot E N V."),
  k('se3', "Read the first column. R W, then R, then R. The owner can write, but everyone else can read it. That is too open for a secret. Fix it. Type: chmod, six hundred, dot E N V."),
  k('se4', "Six, zero, zero means the owner can read and write, and nobody else gets anything. Check again. Type: L S, dash L, dot E N V."),
  k('se5', "Now only the owner has access. Next, a script that loads the secret from that file, instead of holding it. Type: cat good dot S H."),
  k('se6', "It reads the file with source, and prints only the last four characters of the token. Never print a whole secret into a log. Run it. Type: bash good dot S H."),
  c('se7', "The script works, and the secret never appears in it. Keep that file out of version control, with an entry in dot git ignore."),
 ]),
 ('perms', [
  k('pe1', "Second, permissions on the script itself. A new file is not executable by default. Look at this deploy script. Type: L S, dash L, deploy dot S H."),
  k('pe2', "There is no X in the permissions, so it cannot be run directly. Try it. Type: dot slash deploy dot S H."),
  k('pe3', "Permission denied. Do not reach for chmod seven seven seven, which gives everyone full control. Give the owner only what is needed. Type: chmod, U plus X, deploy dot S H."),
  k('pe4', "That adds execute for the owner only. Check it. Type: L S, dash L, deploy dot S H."),
  k('pe5', "Now the owner has R W X, and nobody else has anything extra. Run it. Type: dot slash deploy dot S H."),
  k('pe6', "It runs. One more habit. The umask decides the permissions of every new file. Set it to zero seven seven, and files you create are private. Type: umask zero seven seven, semicolon, touch priv dot T X T, semicolon, L S, dash L, priv dot T X T."),
  c('pe7', "R W for the owner, and nothing for the group or for others. Use a tight umask whenever a script writes secrets or reports."),
 ]),
 ('validate', [
  k('va1', "Third, input validation. Never trust what a user passes in. Here is a script that accepts a server name. Type: cat validate dot S H."),
  k('va2', "It allows only lowercase letters, digits, dash and underscore, up to twenty characters. Anything else is refused, with exit code two. Run it with a good name. Type: bash validate dot S H, web zero one."),
  k('va3', "Accepted. Now a hostile input, with a space, a semicolon and a delete command. Type: bash validate dot S H, and then in quotes: web zero one, semicolon, R M, dash R F, slash."),
  k('va4', "Refused. Nothing ran, because the input never passed the check. Look at the exit code. Type: echo, dollar question mark."),
  k('va5', "Two. A clear refusal, and a clear signal for whoever called the script. One more attack, a path that climbs out of the folder. Type: bash validate dot S H, dot dot slash E T C."),
  c('va6', "Refused as well. Allow what you expect, and reject everything else. That is safer than trying to list everything bad."),
 ]),
 ('inject', [
  k('in1', "Fourth, injection. If a script lets input become code, the user controls your machine. Here is a risky script, using eval. Type: cat danger dot S H."),
  k('in2', "Eval runs its text as a command. Pass it a file name, with a second command hidden after a semicolon. The hidden command is harmless here. It only prints a word. Type: bash danger dot S H, and then in quotes: app dot log, semicolon, echo INJECTED."),
  k('in3', "The word INJECTED appeared. The hidden command ran, as if you had typed it. Now the safe version. Type: cat quoted dot S H."),
  k('in4', "No eval, and the variable is in double quotes, with two dashes before it, so it can only be a file name. Run it with the same input. Type: bash quoted dot S H, and then in quotes: app dot log, semicolon, echo INJECTED."),
  c('in5', "Nothing was injected. The whole text was treated as one file name, which does not exist. Quote your variables, and never use eval on input."),
 ]),
 ('build', [
  k('bu1', "Now put the four habits together, in one script. Type: cat secure dot S H."),
  k('bu2', "A tight umask. Input checked against an allow list. The secret loaded from its own file. And a temporary file, removed by a trap. Run it with a good name. Type: bash secure dot S H, web zero one."),
  k('bu3', "It works, and it shows only the last four characters of the token. Now a hostile name. Type: bash secure dot S H, and then in quotes: web zero one, semicolon, I D."),
  k('bu4', "Refused. Check the exit code. Type: echo, dollar question mark."),
  c('bu5', "Two. Safe against the common mistakes, and honest about the result. That is a script you can hand to a team."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: a secret in a private repository is safe. No. Repositories get shared, cloned and leaked. Keep secrets out of the code."),
  c('my3', "Myth two: chmod seven seven seven fixes permission errors. No. It gives everyone full control. Grant only what is needed."),
  c('my4', "Myth three: quotes are optional. No. Without quotes, spaces and special characters split or change your commands. Quote every variable."),
  c('my5', "Myth four: blocking bad input is enough. No. Allow only what you expect, and reject the rest."),
  c('my6', "Secrets. Permissions. Validation. No eval."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding. Six points, and you need all six."),
  c('b2', "Keep secrets out of scripts, in a file only you can read."),
  c('b3', "Set permissions with chmod. Six hundred for secrets, and never seven seven seven."),
  c('b4', "Use umask zero seven seven for private output."),
  c('b5', "Validate input with an allow list, and exit with a clear code."),
  c('b6', "Quote every variable, and never use eval on input."),
  c('b7', "Never print a whole secret. At most, the last few characters."),
  c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Type every command yourself. Use fake secrets only."),
  c('z2', "One: create a dot E N V file with a fake token, and lock it with chmod six hundred."),
  c('z3', "Two: write a script that loads it with source, and prints only the last four characters."),
  c('z4', "Three: create a script without execute permission, see it fail, then add execute for the owner only."),
  c('z5', "Four: set umask zero seven seven, create a file, and read its permissions."),
  c('z6', "Five: add input validation with a regular expression, and prove that a name with a semicolon is refused."),
  c('z7', "Six: write a script that passes a quoted variable to L S, with two dashes, and show that a hostile name is not run as code."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Where does a password belong?"), c('f13', "Which mode locks a secret file to its owner?"),
  c('f14', "What does an allow list do?"), c('f15', "Why avoid eval on input?"),
  c('f16', "Objective covered: MC05-O07.", "Objective covered: M C zero five, objective seven, in the Bash scripting masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: idempotent scripts and ShellCheck."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'se7': 0.5, 'pe7': 0.5, 'va6': 0.5, 'in5': 0.5, 'bu5': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'secrets': 'Keep secrets out', 'perms': 'Permissions', 'validate': 'Validate input', 'inject': 'Injection', 'build': 'Put it together', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
