RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Today your Python talks to the outside world."),
  c('h2', "A REST API is how tools, clouds and servers answer questions over HTTP. Three habits make your calls safe: authentication, timeouts, and pagination."),
  c('h3', "Every demo is typed live on Ubuntu twenty-four oh four, against a small lab API that runs on this computer."),
 ]),
 ('why', [
  c('w1', "A REST API is a web address that answers with data, usually JSON."),
  c('w2', "You ask with a method. GET reads data. POST creates data. And you get back a status code."),
  c('w3', "Two hundred means success. Four oh one means you are not logged in. Five hundred and up means the server has a problem."),
  c('w4', "Python's requests library turns this into three lines of code."),
  c('w5', "But real APIs need three habits: prove who you are, never wait forever, and ask for every page."),
 ]),
 ('basics', [
  k('b1', "First, a simple call. Start Python. Type: python three, dash Q."),
  k('b2', "Import the requests library. It is installed in this virtual environment, with pip install requests. Type: import requests."),
  k('b3', "Now call the health address of our lab A P I. Always set a timeout. Type: r, equals, requests dot get, open bracket, the address in quotes, H T T P colon slash slash one two seven dot zero dot zero dot one, colon eight zero eight one, slash health, then comma, timeout equals five, close bracket."),
  k('b4', "Nothing printed, the answer is stored in r. Ask for the status code. Type: r dot status underscore code."),
  k('b5', "Two hundred, success. Now the data. Type: r dot jay son, open, close."),
  k('b6', "A Python dictionary, already decoded. Leave Python. Type: exit, open, close."),
  c('b7', "A status code, and JSON. Get, check, decode. That is the whole pattern."),
 ]),
 ('auth', [
  k('a1', "Most A P I s need a token. We keep it in an environment variable, never in the code. Type: export A P I underscore T O K E N equals lab dash token dash one two three."),
  k('a2', "That is a throwaway lab token, published in the repository. A real token is never typed on screen. Start Python. Type: python three, dash Q."),
  k('a3', "Import O S and requests. Type: import O S, comma, requests."),
  k('a4', "Store the address of the servers list. Type: U R L, equals, the address in quotes, H T T P colon slash slash one two seven dot zero dot zero dot one, colon eight zero eight one, slash servers."),
  k('a5', "First, call it with no token. Type: requests dot get, open bracket, U R L, comma, timeout equals five, close bracket, dot status underscore code."),
  k('a6', "Four oh one: not authorized. The server wants proof. Build a header with the token from the environment. Type: h, equals, brace, quote Authorization quote, colon, quote Bearer, space, quote, plus, O S dot environ, square bracket, quote A P I underscore T O K E N quote, close square bracket, close brace."),
  k('a7', "Now call again, with the header. Type: requests dot get, open bracket, U R L, comma, headers equals h, comma, timeout equals five, close bracket, dot status underscore code."),
  k('a8', "Two hundred, we are in. How many servers does the A P I say it has? Type: the same call, then dot jay son, open, close, square bracket, quote total quote, close square bracket."),
  c('a9', "Ten servers. Authentication is a header named Authorization, with the word Bearer, a space, and the token. The token comes from the environment, so it never sits in your code or your git history."),
 ]),
 ('timeout', [
  k('o1', "Next, timeouts. Without one, your script can hang forever on a slow server. Here is a script, timeout dot P Y. Type: cat timeout dot P Y."),
  k('o2', "It calls the slow address, which answers after three seconds, but we only wait one. If that fails with a Timeout error, we print a clear message. Run it. Type: python three, timeout dot P Y."),
  k('o3', "It gave up after one second, instead of hanging. Now allow five seconds, with sed. Type: sed, dash I, quote, S slash timeout equals one slash timeout equals five slash, quote, timeout dot P Y."),
  k('o4', "No output, the file was changed in place. Run it again. Type: python three, timeout dot P Y."),
  c('o5', "Now it waits long enough, and prints ok two hundred. The lesson: always pass a timeout, pick a number that fits the call, and handle the Timeout error."),
 ]),
 ('pages', [
  k('g1', "Last, pagination. Real APIs return a few items at a time. Here is pages dot P Y. Type: cat pages dot P Y."),
  k('g2', "It starts at page one. The loop asks for a page, raises an error for any bad status code, collects the names, and follows next page until the server says there is none. Run it. Type: python three, pages dot P Y."),
  c('g3', "Ten servers, from four pages of three. Without the loop you would have seen only the first three, and your script would silently miss servers."),
 ]),
 ('task', [
  c('t1', "Here is your task, with everything you need. The files are in the repository, and in the description."),
  k('t2', "The repository is git hub dot com, slash it dash waves, slash dev ops dash A I."),
  k('t3', "In the academy slash lesson fifty folder you will find the task file, the lab A P I, and the checker, check fifty dot S H."),
  c('t4', "You write one file, fetch dot P Y. It reads the token from the environment, calls the servers endpoint with a timeout, and follows every page."),
  c('t5', "Then it prints two lines: how many servers, and which are stopped. The checker starts its own copy of the API, and shows four pass lines."),
  c('t6', "Do not open the solution file until you have really tried."),
  c('t7', "Write your results in a report, with the commands and their output."),
 ]),
 ('rubric', [
  c('r1', "Here is how your work is judged. Six points, and you need all six."),
  c('r2', "The checker shows four pass lines."), c('r3', "The token comes from the environment, with a clear message when it is missing."),
  c('r4', "Every call has a timeout."), c('r5', "The status code is checked, with raise for status."),
  c('r6', "All pages are collected, not just the first."), c('r7', "The report is complete, and you worked in your own virtual machine."), c('r8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: get the lesson folder, activate your virtual environment, and pip install requests."),
  c('z3', "Two: start the lab API in one terminal, and set your token in another."),
  c('z4', "Three: write fetch dot P Y, with the header and a timeout."),
  c('z5', "Four: loop over the pages until next page is none."),
  c('z6', "Five: print the two summary lines."),
  c('z7', "Six: run the checker, and write your report."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Which header carries a bearer token?"), c('f13', "What happens to a request that has no timeout?"),
  c('f14', "What does raise for status do?"), c('f15', "How do you know there are more pages?"),
  c('f16', "Objective covered: MC06-O04, REST APIs with authentication, timeouts, and pagination."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: exceptions, logging, and retries."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'w5': 0.5, 'b7': 0.5, 'a9': 0.5, 'o5': 0.5, 'g3': 0.5, 'o2': 3.5, 'o4': 3.0, 'b1': 0.3, 'a2': 0.3, 't7': 0.5, 'r8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'why': 'What a REST API is', 'basics': 'A first request', 'auth': 'Authentication with a token', 'timeout': 'Timeouts', 'pages': 'Pagination', 'task': 'Get the lab and task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
