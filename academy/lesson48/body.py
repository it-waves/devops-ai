RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Last lesson you built a clean Python project. Today you write the code that goes inside it."),
  c('h2', "Five building blocks. Types. Collections. Conditions and loops. Functions. And modules."),
  c('h3', "Every demo is typed live on Ubuntu twenty-four oh four, so you can follow along."),
 ]),
 ('why', [
  c('w1', "Why Python for DevOps? Shell is great for gluing commands together."),
  c('w2', "But the moment your data has structure, a list of servers, a map of settings, an answer from an A P I, shell gets painful."),
  c('w3', "Python gives you clear data types, readable errors, and code you can test."),
  c('w4', "And a lot of DevOps data is already in the shape Python understands: lists and dictionaries."),
  c('w5', "So these five building blocks are the base for every tool in this masterclass."),
 ]),
 ('repl', [
  k('r1', "First, types. Start Python's interactive mode, called the R E P L. Type: python three, dash Q."),
  k('r2', "Three greater-than signs is the Python prompt. Store a port number. Type: port, equals, eight zero eight zero."),
  k('r3', "Nothing printed, the value is stored. Every value has a type. Ask Python. Type: type, open bracket, port, close bracket."),
  k('r4', "Class int, a whole number. Now some text. Type: name, equals, quote, web one, quote."),
  k('r5', "Text goes in quotes. Ask its type. Type: type, open bracket, name, close bracket."),
  k('r6', "Class str, a string. Now a trap that bites DevOps engineers all the time: environment variables are always strings. Compare the number with the text. Type: port, equals equals, quote, eight zero eight zero, quote."),
  k('r7', "False. The number eight thousand eighty is not equal to the text eight thousand eighty. Convert the text. Type: int, open bracket, quote, eight zero eight zero, quote, close bracket, plus one."),
  k('r8', "Eight thousand eighty-one. Int turns text into a number. Leave the R E P L. Type: exit, open bracket, close bracket."),
  c('r9', "Remember: types matter. Use int to turn text into a number, and str to turn a number into text."),
 ]),
 ('coll', [
  k('c1', "Next, collections. Start Python again. Type: python three, dash Q."),
  k('c2', "A list holds items in order. Type: ports, equals, square bracket, eighty, comma, four forty-three, comma, eighty eighty, close square bracket."),
  k('c3', "Add an item. Type: ports dot append, open bracket, twenty-two, close bracket."),
  k('c4', "Look at the list. Type: ports."),
  k('c5', "Four items. Counting starts at zero, so the first item is index zero. Type: ports, square bracket, zero."),
  k('c6', "Eighty. Now a dictionary: names paired with values, in curly braces. Type: server, equals, brace, quote name quote, colon, quote web one quote, comma, quote C P U quote, colon, seventy-two, close brace."),
  k('c7', "Look up a value by its name. Type: server, square bracket, quote C P U quote, close square bracket."),
  k('c8', "Seventy-two. What if a key is missing? Square brackets raise an error, so use get with a default value. Type: server dot get, open bracket, quote mem quote, comma, quote N slash A quote, close bracket."),
  k('c9', "N slash A, the default. Now the error version. Type: server, square bracket, quote mem quote, close square bracket."),
  c('c10', "A key error. Python names exactly what is missing. Lists keep order, and dictionaries look things up by name. You will use both constantly, because the answer from an A P I is made of exactly these."),
 ]),
 ('script', [
  k('p1', "Now a real script, with a condition and a loop. Here is a file called check dot P Y. Type: cat check dot P Y."),
  k('p2', "A list of pairs: a server name and its C P U. A for loop visits each pair. Inside, if the C P U is above eighty, print busy, else print okay. Notice there are no braces. Python uses indentation, four spaces, to show what belongs inside. Run it. Type: python three, check dot P Y."),
  c('p3', "Web two is busy, and the others are okay. The loop ran three times, and the if chose a branch each time."),
  c('p4', "Two rules to remember. A colon opens every block, and the indented lines under it belong to it."),
 ]),
 ('func', [
  k('f1', "Functions package logic so you can reuse it. Here is funcs dot P Y. Type: cat funcs dot P Y."),
  k('f2', "Def starts a function. Busy takes two inputs, a list of servers and a limit. It builds a list of names, and returns it. The last block runs only when the file is run directly. Run it. Type: python three, funcs dot P Y."),
  c('f3', "Only web two. Change the limit, and the answer changes. One function, many uses."),
  c('f4', "A function should do one job, take its inputs as parameters, and give back a result with return. That makes it easy to test, which we do in a later lesson."),
 ]),
 ('mod', [
  k('m1', "Finally, modules: files of ready-made code. Python ships with many, called the standard library. Use J S O N to turn a dictionary into text. Type: python three, dash C, then import json, semicolon, print, json dot dumps."),
  k('m2', "J S O N text, with double quotes, ready to send to an A P I. Your own files are modules too. Import funcs. Type: python three, dash C, import funcs."),
  k('m3', "Nothing printed. The if name equals main guard kept the demo code from running on import. That is why we wrote it. Now import something that does not exist. Type: python three, dash C, import nothere."),
  c('m4', "Module not found. Inside a virtual environment, that usually means a missing pip install, or an environment that is not active. Last lesson's habit pays off."),
 ]),
 ('task', [
  c('t1', "Here is your task, with everything you need. The files are in the repository, and in the description."),
  k('t2', "The repository is git hub dot com, slash it dash waves, slash dev ops dash A I."),
  k('t3', "In the academy slash lesson forty-eight folder you will find the task file, the data, the expected output, and the checker, check forty-eight dot S H."),
  c('t4', "You write one file, inventory dot P Y. It imports the data, counts servers per environment with a dictionary, finds the busy ones with a function, and prints an average."),
  c('t5', "The checker runs it and compares with the expected output. Four pass lines to finish."),
  c('t6', "Do not open the solution file until you have really tried."),
  c('t7', "Write your results in a report, with the commands and their output."),
 ]),
 ('rubric', [
  c('b1', "Here is how your work is judged. Six points, and you need all six."),
  c('b2', "The checker shows four pass lines."), c('b3', "Busy takes a limit, and returns names."),
  c('b4', "The counts come from a dictionary and a loop, not hard-coded numbers."), c('b5', "The data is imported, not copied."),
  c('b6', "The report is complete, including where you got stuck."), c('b7', "You worked in your own virtual machine."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: get the lesson folder, and activate your virtual environment."),
  c('z3', "Two: start inventory dot P Y, and import the data."),
  c('z4', "Three: write busy, with a limit."),
  c('z5', "Four: count servers per environment with a dictionary."),
  c('z6', "Five: print the four lines, under the main guard."),
  c('z7', "Six: run the checker, and write your report."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Why does port equals equals quote eight zero eight zero quote give false?"), c('f13', "How do you get a dictionary value with a default?"),
  c('f14', "What shows which lines belong inside a loop?"), c('f15', "Why use the if name equals main guard?"),
  c('f16', "Objective covered: M C zero six, objective two, types, collections, conditions, loops, functions, and modules."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: files, J S O N, Y A M L, C S V, and environment configuration."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'w5': 0.5, 'r1': 1.0, 'r8': 0.6, 'r9': 0.5, 'c1': 1.0, 'c10': 0.5, 'p4': 0.5, 'f4': 0.5, 'm4': 0.5, 't7': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'why': 'Why Python for DevOps', 'repl': 'Types in the REPL', 'coll': 'Lists and dictionaries', 'script': 'Conditions and loops', 'func': 'Functions', 'mod': 'Modules and imports', 'task': 'Get the lab and task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
