RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
SCENES = [
 ('hook', [
  c('h1', "A script that does the same thing every time is not very useful. Useful scripts take input: a name, a file, a number. Today you learn four ways to feed a script."),
  c('h2', "Variables, to store values. Positional arguments, to pass values in when you run the script. The read command, to ask the user. And command substitution, to capture the output of another command."),
  c('h3', "Every demo is a real recording on Ubuntu."),
 ]),
 ('vars', [
  c('a1', "Variables first. A variable is a named box for a value. Type: city=Paris. There are no spaces around the equals sign.", "Variables first. A variable is a named box for a value. Type: city equals Paris. There are no spaces around the equals sign."),
  c('a2', "Nothing printed. Read it back with a dollar sign. Type: echo, double quote, I live in dollar city, double quote.", "Nothing printed. Read it back with a dollar sign. Type: echo, double quote, I live in dollar city, double quote."),
  c('a3', "Paris. Now a trap. I want the word Parisland. Type: echo, double quote, dollar cityland, double quote.", "Paris. Now a trap. I want the word Parisland. Type: echo, double quote, dollar cityland, double quote."),
  c('a4', "An empty line. The shell looked for a variable called cityland, which does not exist. Mark where the name ends, with braces. Type: echo, double quote, dollar, open brace, city, close brace, land, double quote.", "An empty line. The shell looked for a variable called cityland, which does not exist. Mark where the name ends, with braces. Type: echo, double quote, dollar, open brace, city, close brace, land, double quote."),
  c('a5', "Parisland. Use braces whenever text touches the name. Next, a default value, for a variable that is not set. Type: echo, double quote, dollar, open brace, name, colon, dash, stranger, close brace, double quote.", "Parisland. Use braces whenever text touches the name. Next, a default value, for a variable that is not set. Type: echo, double quote, dollar, open brace, name, colon, dash, stranger, close brace, double quote."),
  c('a6', "Stranger. The variable name was never set, so the default was used. One last trap: spaces. Type: city, space, equals, space, Paris.", "Stranger. The variable name was never set, so the default was used. One last trap: spaces. Type: city, space, equals, space, Paris."),
  c('a7', "The shell treated city as a command, and failed. An assignment has no spaces. Keep it tight."),
 ]),
 ('args', [
  c('g1', "Next, positional arguments. They are the words you type after the script name. Here is a script that uses them. Type: cat greet.sh.", "Next, positional arguments. They are the words you type after the script name. Here is a script that uses them. Type: cat greet dot S H."),
  c('g2', "Dollar one is the first argument. Dollar hash is how many there are. Dollar at is all of them. Run it with one word. Type: dot slash greet dot S H, Sam.", "Dollar one is the first argument. Dollar hash is how many there are. Dollar at is all of them. Run it with one word. Type: dot slash greet dot S H, Sam."),
  c('g3', "First is Sam, and the count is one. Now three words. Type: dot slash greet dot S H, Sam Lee Kim.", "First is Sam, and the count is one. Now three words. Type: dot slash greet dot S H, Sam Lee Kim."),
  c('g4', "The count is three, and all three are listed. What if one argument has a space? Quote it, and it stays one argument. Type: dot slash greet dot S H, double quote, Sam Lee, double quote, Kim.", "The count is three, and all three are listed. What if one argument has a space? Quote it, and it stays one argument. Type: dot slash greet dot S H, double quote, Sam Lee, double quote, Kim."),
  c('g5', "First is Sam Lee, and the count is two. Quotes group words, just as before. Last case: no arguments at all. Type: dot slash greet dot S H.", "First is Sam Lee, and the count is two. Quotes group words, just as before. Last case: no arguments at all. Type: dot slash greet dot S H."),
  c('g6', "First is empty, and the count is zero. A good script checks the count before it uses an argument. You learn how in the next lesson."),
 ]),
 ('input', [
  c('i1', "Third way: ask the user. The read command waits for a line of input. Here is a short script. Type: cat ask.sh.", "Third way: ask the user. The read command waits for a line of input. Here is a short script. Type: cat ask dot S H."),
  c('i2', "Read dash p prints a prompt, then stores what the user types in a variable. Run it, and then answer the question. Type: dot slash ask dot S H.", "Read, dash p, prints a prompt, then stores what the user types in a variable. Run it, and then answer the question. Type: dot slash ask dot S H.", 6.0),
  c('i3', "Welcome, Maya. The script used my answer. Scripts also run with no person present, so input can come from a pipe. Type: echo Lee, pipe, dot slash ask dot S H.", "Welcome, Maya. The script used my answer. Scripts also run with no person present, so input can come from a pipe. Type: echo Lee, pipe, dot slash ask dot S H."),
  c('i4', "No prompt appeared, because there was no keyboard to ask. But the answer was read from the pipe. The same script works both ways."),
 ]),
 ('subst', [
  c('s1', "Fourth way: command substitution. It captures a command's output, so you can store it. Type: today equals dollar, bracket, date plus percent capital F, bracket. That format is year, month, day.", "Fourth way: command substitution. It captures a command's output, so you can store it. Type: today equals dollar, bracket, date plus percent capital F, bracket. That format is year, month, day."),
  c('s2', "Nothing printed. The output went into the variable. Use it inside a file name. Type: echo, double quote, backup dash dollar today dot tar, double quote.", "Nothing printed. The output went into the variable. Use it inside a file name. Type: echo, double quote, backup dash dollar today dot tar, double quote."),
  c('s3', "A dated file name, built by the shell. Now count things. Type: L S, pipe, W C, dash l. That counts lines.", "A dated file name, built by the shell. Now count things. Type: L S, pipe, W C, dash l. That counts lines."),
  c('s4', "Three files. Store that number. Type: count equals dollar, bracket, L S, pipe, W C, dash l, bracket.", "Three files. Store that number. Type: count equals dollar, bracket, L S, pipe, W C, dash l, bracket."),
  c('s5', "Again nothing printed. Now print a sentence with it. Type: echo, double quote, There are dollar count files, double quote.", "Again nothing printed. Now print a sentence with it. Type: echo, double quote, There are dollar count files, double quote."),
  c('s6', "There are three files. A script can now report facts about the system, not just fixed text. The older style uses backticks. It works, but brackets are easier to read, and they can be nested."),
 ]),
 ('build', [
  c('t1', "Now put it all together in one script. Type: cat backup.sh.", "Now put it all together in one script. Type: cat backup dot S H."),
  c('t2', "A default name with colon dash, a date from command substitution, and a message. Run it with no argument. Type: dot slash backup dot S H.", "A default name with colon dash, a date from command substitution, and a message. Run it with no argument. Type: dot slash backup dot S H."),
  c('t3', "It used the default name, data, and today's date. Now pass a name. Type: dot slash backup dot S H, photos.", "It used the default name, data, and today's date. Now pass a name. Type: dot slash backup dot S H, photos."),
  c('t4', "Photos. Same script, different input. That is why scripts use variables and arguments."),
 ]),
 ('myths', [
  c('my1', "Four myths to clear up."),
  c('my2', "Myth one: spaces around the equals sign are fine. No. Spaces make it a command, and it fails."),
  c('my3', "Myth two: dollar one is the script name. No. That is dollar zero. Dollar one is the first argument."),
  c('my4', "Myth three: an unquoted variable is always fine. If the value holds a space, it splits. Quote it."),
  c('my5', "Myth four: read only works with a keyboard. It also reads from pipes and files."),
  c('my6', "Set it. Pass it. Ask for it. Capture it."),
 ]),
 ('rubric', [
  c('b1', "Here is how you check your own understanding. Six points, and you need all six."),
  c('b2', "Assign and print a variable, with no spaces around the equals sign."),
  c('b3', "Use braces, and a default value with colon dash."),
  c('b4', "Name dollar zero, dollar one, dollar hash, and dollar at."),
  c('b5', "Quote an argument that contains a space."),
  c('b6', "Use read to take input, from a keyboard and from a pipe."),
  c('b7', "Capture a command's output with a dollar sign and brackets."),
  c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine. Type every command yourself."),
  c('z2', "One: set two variables, and print them in one sentence, using braces."),
  c('z3', "Two: write a script that prints its first argument, the count, and all arguments. Run it with zero, one, and three arguments."),
  c('z4', "Three: run it with an argument that contains a space, with quotes and without."),
  c('z5', "Four: write a script that asks your name with read, and greets you. Run it by hand, then from a pipe."),
  c('z6', "Five: store today's date and the number of files in your folder, and print one sentence with both."),
  c('z7', "Six: write a backup name script with a default value, and run it with and without an argument."),
  c('z8', "Mark yourself on the rubric. Pause the video, and do it now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What does dollar hash hold?"), c('f13', "How do you keep an argument with a space as one argument?"),
  c('f14', "Which command asks the user for input?"), c('f15', "What does a dollar sign with brackets do?"),
  c('f16', "Objective covered: MC05-O02.", "Objective covered: M C zero five, objective two, in the Bash scripting masterclass."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: conditions, tests, case statements, loops and functions."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'a7': 0.5, 'g6': 0.5, 'i4': 0.5, 's6': 0.5, 't4': 0.5, 'my6': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'vars': 'Variables', 'args': 'Positional arguments', 'input': 'Reading input', 'subst': 'Command substitution', 'build': 'Put it together', 'myths': 'Common myths', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
