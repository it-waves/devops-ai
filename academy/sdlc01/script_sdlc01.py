def c(cid, cap, say=None): return (cid, cap, say)
SCENES = [
 ('hook', [
  c('h1', "Every app you use started as an idea in someone's head.", None),
  c('h2', "So how does an idea become something a customer can actually use? That is the software development life cycle. In this lesson, you will learn all seven stages.", "So how does an idea become something a customer can actually use? That is the software development life cycle. In this lesson, you will learn all seven stages."),
 ]),
 ('roadmap', [
  c('r1', "We will follow one small online shop, called CloudCart, from idea to customer."),
  c('r2', "By the end, you can name every stage, say what happens in it, and see where DevOps fits."),
 ]),
 ('plan', [
  c('p1', "Stage one: plan. Before anyone writes code, the team agrees on the problem. Who is it for, and what must it do?"),
  c('p2', "For CloudCart, the goal is simple: customers browse products and place an order."),
  c('p3', "A written plan avoids building the wrong thing, which is the most expensive mistake in software."),
 ]),
 ('req', [
  c('q1', "Stage two: requirements. Now the plan becomes a list of precise statements."),
  c('q2', "Functional requirements say what the system does, like show a list of products."),
  c('q3', "Non-functional requirements say how well it does it, like answer within one second. Vague requirements are why projects drift."),
 ]),
 ('design', [
  c('d1', "Stage three: design. Here the team decides the parts of the system, and how they talk to each other."),
  c('d2', "CloudCart has a browser, an A P I, and a data store. The browser asks, the A P I answers, and the data store remembers."),
  c('d3', "Drawing this first lets people spot problems while they are still cheap to fix."),
 ]),
 ('build', [
  c('b1', "Stage four: build. Developers turn the design into code. This is real CloudCart source."),
  c('b2', "This function calculates an order total. It checks the quantity, finds the product, and adds up the price."),
  c('b3', "Code lives in version control, so every change is tracked and can be undone."),
 ]),
 ('test', [
  c('t1', "Stage five: test. Automated tests check the code every time it changes."),
  c('t2', "This is a real run from our pipeline: eleven tests, zero failures, build success."),
  c('t3', "If even one test failed, the change would stop here, before any customer sees it."),
 ]),
 ('deploy', [
  c('y1', "Stage six: release and deploy. The tested package is placed on a server and started."),
  c('y2', "Then we check it again while it is running. The health check answers up, and an order for two items totals seven thousand cents."),
  c('y3', "Passing tests and a working deployment are two different checks. You need both."),
 ]),
 ('operate', [
  c('o1', "Stage seven: operate and learn. We watch the system, collect feedback, and the cycle starts again."),
  c('o2', "DevOps is about making this loop fast and safe, using tools you will learn in this course: Git, Maven, Jenkins, Docker, Kubernetes, and more."),
 ]),
 ('recap', [
  c('z1', "Quick check. Which stage decides what the system must do? Which stage catches a bad change before customers do? And which two checks prove an app really works?"),
  c('z2', "Pause the video, answer out loud, then keep going."),
  c('z3', "Next lesson: requirements, in depth. Subscribe so you do not miss it."),
 ]),
]
