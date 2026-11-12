RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Today you build a real tool, and prove that it works."),
  c('h2', "A tool that checks a data file, reports every problem clearly, and exits with the right code. Plus tests that catch bugs. This lesson puts the whole Python for DevOps masterclass together."),
  c('h3', "Every demo is typed live on Ubuntu twenty-four oh four."),
 ]),
 ('why', [
  c('w1', "A good utility has three parts. A pure function that checks the data, and returns a list of errors. A thin main function that reads the file and sets the exit code. And tests."),
  c('w2', "Keeping the checking logic in a pure function, with no files and no printing, makes it easy to test. The main function stays small."),
  c('w3', "Report every problem, not just the first one, and say which item it is. Exit zero when the data is valid, one when it has problems, and two when the file cannot be read."),
  c('w4', "Test the edges: the largest valid value, and the first invalid one. Bugs love boundaries."),
  c('w5', "Then prove the tests work: break the code on purpose, and watch a test fail."),
 ]),
 ('tool', [
  k('e1', "Our example checks a list of services, each with a name, a port and a protocol. First, the checking logic. Type: head, dash sixteen, service check dot P Y."),
  k('e2', "The validate function loops over the items and collects errors in a list: a missing name, a duplicate name, a port outside one to sixty-five thousand five hundred thirty-five, and a protocol that is not T C P or U D P. It returns the list. Now the data. Type: cat, services dot jay son."),
  k('e3', "Four services, with three planted problems. Web appears twice, D N S has port seventy thousand, and the A P I has H T T P as its protocol. Run the tool. Type: dot slash, service check dot P Y, services dot jay son."),
  k('e4', "Three problems, found in one run, each with the name of the service, and a summary line. Now the exit code. Type: echo, dollar, question mark."),
  k('e5', "One: problems found. Now a file that does not exist. Type: dot slash, service check dot P Y, nope dot jay son."),
  k('e6', "A clear message, and no crash. Check the exit code. Type: echo, dollar, question mark."),
  c('e7', "Two: the file could not be read. Zero, one and two each mean something different, and a pipeline can act on that."),
 ]),
 ('tests', [
  k('f1', "Now the tests, and the main idea: prove it works. Show the test file. Type: cat, test service check dot P Y."),
  k('f2', "Four kinds of test. A valid list, including the top edge, port sixty-five thousand five hundred thirty-five. Bad ports, tried with parametrize. A duplicate name. And a missing name. Run them. Type: pytest, dash Q."),
  k('f3', "Seven passed. Now break the tool on purpose: move the upper limit up by one. Type: sed, dash I, quote, S, slash, six five five three five, slash, six five five three six, slash, quote, service check dot P Y."),
  k('f4', "Changed. Run the tests again, with no traceback. Type: pytest, dash Q, dash dash T B, equals, no."),
  k('f5', "One failure: the bad port test, with the value sixty-five thousand five hundred thirty-six. The edge test caught the bug, and told us exactly which value got through. Put it back. Type: sed, dash I, quote, S, slash, six five five three six, slash, six five five three five, slash, quote, service check dot P Y."),
  k('f6', "Fixed. Run all the tests once more. Type: pytest, dash Q."),
  c('f7', "Seven passed. That is what a test suite is for: when the code changes, one run tells you whether it still works."),
 ]),
 ('task', [
  c('t1', "Here is your task, with everything you need. The files are in the repository, and in the description."),
  k('t2', "The repository is git hub dot com, slash it dash waves, slash dev ops dash A I."),
  k('t3', "In the academy slash lesson fifty-five folder you will find the task file, the checker, check fifty-five dot S H, and a deliberately broken version, which the checker uses."),
  c('t4', "You write two files. First, inventory check dot P Y, a tool that validates a jay son inventory of servers. Each server needs a unique name, an environment that is dev, staging or prod, and a valid I P address. It prints one error per problem, and exits with code zero, one, or two."),
  c('t5', "Second, test inventory check dot P Y, with at least six tests, using parametrize. They must pass for your tool, and fail for the broken version, which accepts duplicates, accepts bad I P addresses, and ignores the environment."),
  c('t6', "The checker needs no server and no cloud account. Do not open the solution files until you have really tried."),
  c('t7', "The checker shows six pass lines. Write your results in a report."),
 ]),
 ('rubric', [
  c('r1', "Here is how your work is judged. Six points, and you need all six."),
  c('r2', "The checker shows six pass lines."), c('r3', "The tool prints every problem on its own line, and exits with zero, one, or two."),
  c('r4', "Your validate function follows every rule, with one error per problem."), c('r5', "You have at least six tests, all passing, and you use parametrize."),
  c('r6', "Your tests fail against the broken version."), c('r7', "The report is complete, and you worked in your own virtual machine."), c('r8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: get the lesson folder, activate your virtual environment, and install pytest."),
  c('z3', "Two: write the validate function first, and try it on small lists in the Python prompt."),
  c('z4', "Three: add the command line part, and check the exit codes with echo."),
  c('z5', "Four: write your tests, and include the edges."),
  c('z6', "Five: break your own code, and watch a test fail."),
  c('z7', "Six: run the checker, and write your report."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "Why keep the checking logic in a pure function?"), c('f13', "What do exit codes zero, one and two mean here?"),
  c('f14', "Which values should you test?"), c('f15', "How do you prove a test can fail?"),
  c('f16', "Objective covered: MC06-O09, a tested inventory validation utility."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: Python for DevOps mastery evidence."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'w5': 0.5, 'e7': 0.5, 'f7': 0.5, 'e1': 0.3, 'e3': 0.5, 'e5': 0.5, 'f2': 0.5, 'f4': 0.5, 'f6': 0.5, 't7': 0.5, 'r8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'why': 'Anatomy of a utility', 'tool': 'The tool and exit codes', 'tests': 'Tests: edges, red, green', 'task': 'Get the lab and task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
