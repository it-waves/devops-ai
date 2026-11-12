RB = 'REAL RECORDING  ·  Ubuntu 24.04 on this computer'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "Today your scripts talk to the cloud, with only the power they need."),
  c('h2', "Cloud S D Ks let Python create and read cloud resources. One leaked key with too much power can cost real money. So we write least privilege policies, and we practise against a free mock, with no cloud account at all."),
  c('h3', "Every demo is typed live on Ubuntu twenty-four oh four."),
 ]),
 ('why', [
  c('w1', "Cloud code runs with an identity, and that identity has permissions. Least privilege means giving it only the actions it needs, on only the resources it needs, and nothing more."),
  c('w2', "A policy is a jay son document. Each statement has an effect, a list of actions, and the resources they apply to. A star means everything, so a star in an action, or in a resource, is a red flag."),
  c('w3', "An S D K lets your Python code call the cloud. For A W S it is boto three. Boto three finds credentials in a fixed order: environment variables, then the credentials file, then a role on the machine. So never write a key in your code, and never commit one to git."),
  c('w4', "To test cloud code without a cloud account, we use moto, a mock of A W S. Your code runs unchanged, against a fake that lives in memory. That keeps practice free, safe, and fast."),
  c('w5', "If you ever use a real account: free tier resources only, least privilege policies, and when you finish, delete everything you created, so nothing keeps costing you money."),
 ]),
 ('policy', [
  k('a1', "First, a policy that follows least privilege. Show it. Type: cat, policy dot jay son."),
  k('a2', "Two statements. The first lets you list one bucket. The second lets you get objects, only inside that bucket. No stars anywhere. Now an audit script that flags wildcards. Run it. Type: dot slash audit dot P Y, policy dot jay son."),
  k('a3', "Okay, no wildcards: least privilege. Now a bad policy, that allows everything on everything. Type: dot slash audit dot P Y, bad dot jay son."),
  k('a4', "Two problems found: the action is a star, and the resource is a star. That policy hands over the whole account. Anyone holding those keys could delete everything. Now check the exit code. Type: echo, dollar, question mark."),
  c('a5', "One. The audit fails with exit code one, so a pipeline can block the change before it ships."),
 ]),
 ('sdk', [
  k('d1', "Now the S D K itself. Boto three is the official Python library for A W S. Moto is a free mock of A W S, running inside your own script. Nothing leaves your computer, and nothing costs money. Show the script. Type: cat, S three list dot P Y."),
  k('d2', "The decorator, mock A W S, sends every boto three call to the fake. Notice what is missing: no access key, and no password in the code. Boto three finds credentials by itself. Run it. Type: python three, S three list dot P Y."),
  k('d3', "Three objects, with their sizes, from a bucket that exists only in memory. Real calls fail sometimes, so handle the error. Show the second script. Type: cat, S three miss dot P Y."),
  k('d4', "We ask for a bucket that does not exist, and catch client error. The error code says what went wrong. Run it. Type: python three, S three miss dot P Y."),
  c('d5', "Caught: no such bucket. With a real account you would also meet access denied, and that means your policy is doing its job. Catch the error, log it, and exit with a code."),
 ]),
 ('task', [
  c('t1', "Here is your task, with everything you need. The files are in the repository, and in the description."),
  k('t2', "The repository is git hub dot com, slash it dash waves, slash dev ops dash A I."),
  k('t3', "In the academy slash lesson fifty-four folder you will find the task file, and the checker, check fifty-four dot S H."),
  c('t4', "You write two files. First, policy dot jay son: read-only access to one bucket, with no star in any action, and only that bucket as the resource."),
  c('t5', "Second, S three tools dot P Y, with a function, big files. It takes a client, a bucket and a minimum size, and returns the sorted keys at least that big. It must handle more than a thousand objects, so use a paginator, and an empty bucket returns an empty list."),
  c('t6', "The checker uses moto, so you need no cloud account. Do not open the solution files until you have really tried."),
  c('t7', "The checker shows six pass lines. Write your results in a report, and end it with a cleanup line."),
 ]),
 ('rubric', [
  c('r1', "Here is how your work is judged. Six points, and you need all six."),
  c('r2', "The checker shows six pass lines."), c('r3', "The policy is read-only, with no star in any action."),
  c('r4', "The resources name only the one bucket, and its objects."), c('r5', "Big files handles more than a thousand objects, and an empty bucket."),
  c('r6', "No keys in your code, and the report ends with a cleanup line."), c('r7', "The report is complete, and you worked in your own virtual machine."), c('r8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: get the lesson folder, and activate your virtual environment."),
  c('z3', "Two: install boto three and moto in your virtual environment."),
  c('z4', "Three: write policy dot jay son, with the two statements, and no stars."),
  c('z5', "Four: write S three tools dot P Y, with a paginator, and test it against a moto bucket."),
  c('z6', "Five: put a star in your policy, run the checker, and watch it fail."),
  c('z7', "Six: fix it, run the checker, and write your report with the cleanup line."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What does least privilege mean?"), c('f13', "Where does boto three look for credentials?"),
  c('f14', "What does moto do for you?"), c('f15', "What must you do after trying a real cloud account?"),
  c('f16', "Objective covered: MC06-O08, cloud S D Ks with least privilege."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next lesson: a tested inventory validation utility."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'h3': 0.5, 'w5': 0.5, 'a5': 0.5, 'd5': 0.5, 'a1': 0.3, 'a2': 0.5, 'a3': 0.5, 'a4': 0.5, 'd2': 1.0, 'd4': 0.8, 't7': 0.5, 'r8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'why': 'Least privilege, SDKs, moto', 'policy': 'Policies and the audit', 'sdk': 'boto3 against moto', 'task': 'Get the lab and task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
