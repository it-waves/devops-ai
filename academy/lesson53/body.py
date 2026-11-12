RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Today your scripts earn trust, because you will test them."),
  c('h2', "A script that works once proves little. A test proves it still works after every change. And a mock lets you test code that talks to the network, without any network at all."),
  c('h3', "Every demo is typed live on Ubuntu twenty-four oh four."),
 ]),
 ('why', [
  c('w1', "Every change can break something. A test is a small script that checks one behaviour, and fails loudly when that behaviour breaks."),
  c('w2', "Pytest finds files named test, underscore, something. It runs the functions named test, underscore, something, and it uses the plain assert statement. No classes, and no boilerplate."),
  c('w3', "Parametrize runs one test with many inputs. Pytest dot raises checks that the right error happens."),
  c('w4', "A mock is a stand-in. Our code calls the network, but a test must be fast, free, and repeatable. So we replace the network call with a fake answer, or a fake failure."),
  c('w5', "The rule: test one behaviour, fake what you do not control, and watch every test fail once, to prove it can."),
 ]),
 ('pytest', [
  k('p1', "First, the code we will test. Show it. Type: cat, inventory dot P Y."),
  k('p2', "Two small functions. Running returns the names of the running servers. Health calls an address and returns its status. First we test running. Show the test file. Type: cat, test underscore inventory dot P Y."),
  k('p3', "Three tests. Each is a function whose name starts with test, and the check is a plain assert. Parametrize runs the last one twice, with two different states. Run pytest. Type: pytest, dash Q."),
  k('p4', "Four dots, four passed. Each dot is one test. Green is good, but a test that can never fail proves nothing. So break it on purpose. Change the expected name on line eight. Type: sed, dash I, quote, eight, S slash, web dash zero one, slash, web dash zero nine, slash, quote, test underscore inventory dot P Y."),
  k('p5', "No output, the file is changed. Run the tests again, with the short traceback style. Type: pytest, dash Q, dash dash T B, equals, short."),
  k('p6', "One F, one failure. Pytest shows the failing line, and compares the two values: web dash zero one, against web dash zero nine. The summary names the test, so you know where to look. Now fix it. Type: sed, dash I, quote, eight, S slash, web dash zero nine, slash, web dash zero one, slash, quote, test underscore inventory dot P Y."),
  k('p7', "Fixed. Run everything once more. Type: pytest, dash Q."),
  c('p8', "Four passed again. That loop, red then green, is the heart of testing: write a test, watch it fail, then make it pass."),
 ]),
 ('mock', [
  k('m1', "Now the hard case. Health calls the network, and a test must never depend on a server being up. So we fake the answer. Show the test. Type: cat, test underscore health dot P Y."),
  k('m2', "Mock makes a fake object, and we tell it what its json method returns. Patch swaps requests dot get, inside our module, for the fake, only inside the with block. In the second test the fake raises a connection error, and pytest dot raises checks that our code lets it through. Run all the tests. Type: pytest, dash Q."),
  k('m3', "Six passed, with no network and no server, in a fraction of a second. Now list every test by name. Type: pytest, dash V."),
  k('m4', "Verbose mode shows each test with the word passed. Handy when you need to know exactly what ran. You can also run just some tests, by a word in the name. Type: pytest, dash Q, dash K, down."),
  c('m5', "One passed, five deselected. And in a pipeline, pytest returns exit code zero when everything passes, and a non zero code when anything fails, so the pipeline stops. That is last lesson's exit codes at work."),
 ]),
 ('task', [
  c('t1', "Here is your task, with everything you need. The files are in the repository, and in the description."),
  k('t2', "The repository is git hub dot com, slash it dash waves, slash dev ops dash A I."),
  k('t3', "In the academy slash lesson fifty-three folder you will find the task file, the module to test, and the checker, check fifty-three dot S H."),
  c('t4', "You write one file, test tools dot P Y, for a small module with two functions: one counts servers per environment, and one asks an A P I for its status."),
  c('t5', "Write at least five tests. Use parametrize, use pytest dot raises, and fake the network with mock and patch. No test may need a real server."),
  c('t6', "The checker is strict. It breaks the module three different ways, and your tests must catch every one. Do not open the solution file until you have really tried."),
  c('t7', "The checker shows six pass lines. Write your results in a report."),
 ]),
 ('rubric', [
  c('r1', "Here is how your work is judged. Six points, and you need all six."),
  c('r2', "The checker shows six pass lines."), c('r3', "At least five tests, and all of them pass."),
  c('r4', "You use parametrize, and pytest dot raises."), c('r5', "The network is faked, so no test needs a server."),
  c('r6', "Your tests catch bugs: the checker breaks the code, and your tests must fail."), c('r7', "The report is complete, and you worked in your own virtual machine."), c('r8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: get the lesson folder, and activate your virtual environment."),
  c('z3', "Two: install pytest and requests in your virtual environment."),
  c('z4', "Three: write test tools dot P Y with five tests, and use parametrize and pytest dot raises."),
  c('z5', "Four: fake the network with mock and patch. Test an ok answer, and an H T T P error."),
  c('z6', "Five: break the code yourself, and watch one of your tests fail."),
  c('z7', "Six: run the checker, and write your report."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "How does pytest find your tests?"), c('f13', "What does a mock replace?"),
  c('f14', "Why should you watch a test fail at least once?"), c('f15', "What exit code does pytest return when a test fails?"),
  c('f16', "Objective covered: MC06-O07, tests with pytest and mocks."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: cloud SDKs with least privilege.", "Next lesson: cloud S D Ks with least privilege."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'w5': 0.5, 'p8': 0.5, 'm5': 0.5, 'p1': 0.3, 'p3': 0.5, 'p5': 0.5, 'p7': 0.5, 'm2': 0.5, 'm3': 0.5, 'm4': 0.5, 't7': 0.5, 'r8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'why': 'Tests, asserts, mocks', 'pytest': 'pytest: red to green', 'mock': 'Mocks: fake the network', 'task': 'Get the lab and task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
