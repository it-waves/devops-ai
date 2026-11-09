def c(cid, cap, say=None): return (cid, cap, say)
SCENES = [
 ('hook', [
  c('a1', "Do you want to become a DevOps engineer, but you have no idea where to start?"),
  c('a2', "Welcome to the DevOps Engineering Bootcamp. A step by step course that takes you from zero to building, securing, and running real systems."),
 ]),
 ('promise', [
  c('b1', "Here is how we teach every tool. Five steps."),
  c('b2', "Learn it: understand the idea, and why it exists."),
  c('b3', "Build it: set it up yourself, in a working lab."),
  c('b4', "Break it: watch what fails, in a safe lab."),
  c('b5', "Fix it: find the cause, and repair it."),
  c('b6', "And operate it: secure it, monitor it, and keep it running."),
 ]),
 ('path', [
  c('c1', "The course is planned in nine stages, and each stage builds on the one before."),
  c('c2', "Foundations: Linux, Bash, Python, and Git. Then applications and build tools: Java, Maven, Tomcat, and databases."),
  c('c3', "Then C I C D with Jenkins, SonarQube, and Nexus, and containers with Docker.", "Then C I C D with Jenkins, sonar cube, and Nexus, and containers with Docker."),
  c('c4', "Then the cloud, Terraform and Ansible, and Kubernetes. Then security, monitoring, reliability, and a final capstone project.", "Then the cloud, terra form and Ansible, and Kubernetes. Then security, monitoring, reliability, and a final capstone project."),
  c('c5', "This is the plan. Lessons are published stage by stage, in order, so each one has what it needs."),
 ]),
 ('lesson', [
  c('d1', "Every lesson follows the same shape."),
  c('d2', "First, why: the problem the tool solves. Then the concept, in plain words."),
  c('d3', "Then a demonstration, with real commands and real output. No made up results."),
  c('d4', "Then practice, which you do yourself, and a checker that tells you if you got it right."),
 ]),
 ('expect', [
  c('e1', "A few promises about what to expect."),
  c('e2', "No experience needed. We explain every new term and command the first time it appears."),
  c('e3', "Linux lessons use Ubuntu, a free system you can run on your own computer, in a virtual machine."),
  c('e4', "When something is an illustration instead of a real capture, we label it on screen."),
  c('e5', "Some cloud lessons may need an account with a cloud provider. We will tell you the cost before you click anything."),
  c('e6', "We cannot promise you a job. We can promise real practice, and a way to check your own progress."),
 ]),
 ('start', [
  c('f1', "Start with lesson one: the software development life cycle. How does an idea become something customers use?"),
  c('f2', "Subscribe, and follow the playlist in order. See you in lesson one."),
 ]),
]
