
RB = 'REAL RECORDING  ·  Ubuntu 24.04'
def k(cid, s): return c(cid, s, s)
SCENES = [
 ('hook', [
  c('h1', "You tap Buy in a shopping app. A spinner turns for half a second, and then it says: done."),
  c('h2', "In that half second, at least three different programs just talked to each other."),
  c('h3', "Today you meet all three: the frontend, the backend, and the database. And then you take a real app apart with your own hands."),
  c('h4', "Because as a dev ops engineer, you will deploy, scale, and fix these pieces. So you must know which is which."),
 ]),
 ('roles', [
  c('r1', "Think of a restaurant. The dining room, the kitchen, and the pantry."),
  c('r2', "The frontend is the dining room. It is what the customer sees and touches: pages, buttons, forms. It runs in the browser."),
  c('r3', "The backend is the kitchen. It holds the rules. It checks the order, works out the price, and decides what happens."),
  c('r4', "The database is the pantry. It remembers. Products, users, orders, all stored safely, even when the power goes off."),
  c('r5', "They talk in a fixed order. The browser asks the backend. The backend asks the database. Then the answer travels back."),
  c('r6', "One more word. A monolith is when all of it lives in one program, running as one process."),
  c('r7', "A service is a smaller program that does one job. Split the monolith, and you get services."),
 ]),
 ('mono', [
  k('m1', "Let us see a real one. A tiny shop called cloud cart. Go in. Type: C D, cloud cart."),
  k('m2', "Look around. Type: L S."),
  c('m3', "app dot P Y is the whole shop in one file. Start it. Type: dot slash start dot S H, mono."),
  c('m4', "Now act like a browser. Ask for the page. Type: curl, dash S, local host, colon, eight zero eight zero, pipe, head, dash four.", "Now act like a browser. Ask for the page. Type: curl, dash S, local host colon eight zero eight zero, pipe, head, dash four."),
  c('m5', "That is the frontend: H T M L, the page itself. Now ask for the data. Type: curl, dash S, local host colon eight zero eight zero slash A P I slash products, pipe, J Q, dash C, quote, dot, open bracket, close bracket, quote.", "That is the frontend: H T M L, the page itself. Now ask for the data. Type: curl, dash S, local host colon eight zero eight zero slash A P I slash products, pipe, J Q, dash C, quote, dot bracket bracket, quote."),
  c('m6', "That is the backend talking: plain data, in jay son format. J Q only tidies it, one product per line."),
  c('m7', "Where does the backend get it? From the database. Type: python three, show D B dot P Y.", "Where does the backend get it? From the database file. Type: python three, show D B dot P Y."),
  c('m8', "The same three products, stored in a file called shop dot D B. Now count the running servers. Type: S S, dash L T N.", "The same three products, stored in a file called shop dot D B. Now see what is listening on the network. Type: S S, dash L T N."),
  c('m9', "One listener, port eight zero eight zero. The page and the data come from the same process. That is a monolith."),
 ]),
 ('split', [
  k('p0', "Now split it. Go in. Type: C D, cloud cart."),
 k('p1', "Same shop, two services. Type: dot slash start dot S H, split."),
  c('p2', "What is listening now? Type: S S, dash L T N.", "What is listening now? Type: S S, dash L T N."),
  c('p3', "Two listeners. Port five thousand is the backend. Port eight zero eight zero is the frontend. Ask the backend directly. Type: curl, dash S, local host colon five thousand slash A P I slash products, pipe, J Q, dash C, quote, dot bracket zero bracket, quote.", "Two listeners. Port five thousand is the backend. Port eight zero eight zero is the frontend. Ask the backend directly. Type: curl, dash S, local host colon five thousand slash A P I slash products, pipe, J Q, dash C, quote, dot bracket zero bracket, quote."),
  c('p4', "Only data. No page. Now the frontend. Which address does its page call? Type: curl, dash S, local host colon eight zero eight zero, pipe, grep, five thousand.", "Only data, no page. Now the frontend. Which address does its page call? Type: curl, dash S, local host colon eight zero eight zero, pipe, grep, five thousand."),
  c('p5', "There it is. The page itself calls the backend at port five thousand. Two programs, one job. Stop them both. Type: dot slash stop dot S H.", "There it is. The page calls the backend at port five thousand. Two programs, one job. Stop them both. Type: dot slash stop dot S H."),
  c('p6', "Clean. Nothing left running."),
 ]),
 ('browser', [
  c('w1', "Now see it the way a customer does. Open the shop in a real browser."),
  c('w2', "This is the frontend: the page, drawn by the browser, with cards, colors, and prices."),
  c('w3', "Where did those names and prices come from? The page asked the backend, and the backend asked the database."),
  c('w4', "Open the backend's own address, and there is no design at all. Just the data, as jay son. Same facts, two faces."),
  c('w5', "The frontend is for people. The backend is for programs. Remember that sentence."),
 ]),
 ('trade', [
  c('t1', "So which is better, a monolith or services? Neither. It is a trade."),
  c('t2', "Services can scale separately. A busy backend gets more copies, and the frontend stays small."),
  c('t3', "They can be deployed separately. Fix a button, and you do not touch the backend."),
  c('t4', "And one can fail without taking everything down."),
  c('t5', "But there is a price. More programs, more ports, more network calls, and more places to look when something breaks."),
  c('t6', "So a small team starts simple, and splits when it hurts. Your job is to know both shapes, and to see them on a server."),
  c('t7', "Remember the commands: S S shows what is listening, and curl shows what each one says."),
 ]),
 ('task', [
  c('k1', "Your task, in your own Ubuntu virtual machine."),
  k('k2', "The lab is lab sixty-seven dot S H, in the academy slash lab folder of git hub dot com, slash it dash waves, slash dev ops dash A I. Install it like before, then run lab up."),
  c('k3', "It starts cloud cart as one monolith on port eight zero eight zero. Your job is to split it."),
  c('k4', "One: start the backend alone, so port five thousand answers with the product list."),
  c('k5', "Two: make the frontend serve the page on port eight zero eight zero, and call the backend."),
  c('k6', "Three: the two must be separate processes. Read start dot S H; the answer is already there."),
  c('k7', "Four: in answers dot text, write one line: D B, colon, then the service that talks to the database."),
  c('k8', "Then run lab check. Four pass lines."),
 ]),
 ('rubric', [
  c('b1', "Six points, and you need all six."),
  c('b2', "The checker shows four pass lines."), c('b3', "You can show the backend alone with curl."),
  c('b4', "You can show who listens on which port with S S."),
  c('b5', "You can explain frontend, backend, and database in one sentence each."), c('b6', "You can explain one benefit and one cost of splitting."),
  c('b7', "You ran lab down, and nothing is left listening."), c('b8', "To pass, you need all six."),
 ]),
 ('yourturn', [
  c('z1', "Your turn, in your own Ubuntu virtual machine."),
  c('z2', "One: install the lab, and run lab up."),
  c('z3', "Two: run S S dash L T N, and find the monolith."),
  c('z4', "Three: split it, with the start script."),
  c('z5', "Four: curl the backend on port five thousand, and the page on port eight zero eight zero."),
  c('z6', "Five: write answers dot text, then run lab check."),
  c('z7', "Six: run lab down."),
  c('z8', "Pause the video, and begin now."),
 ]),
 ('recap', [
  c('f11', "Quick check."), c('f12', "What does the frontend do, and where does it run?"), c('f13', "What does the backend do that the frontend should not?"),
  c('f14', "Why does a database exist at all?"), c('f15', "Name one benefit and one cost of splitting a monolith."),
  c('f16', "Objective covered: M C zero eight, objective one, frontend, backend, monolith, service, and database."),
  c('f17', "Pause the video, and answer out loud."), c('f18', "Next: requests, responses, rest, status codes, and jay son."), c('f19', "If this helped, like, share and subscribe, so you do not miss it."),
 ]),
]
CLEAR = True
EXTRA = {'w5': 0.5, 'h4': 0.5, 'r7': 0.5, 'm9': 0.5, 'p6': 0.5, 't7': 0.5, 'k8': 0.5, 'b8': 0.5, 'z8': 14.0, 'f17': 10.0}
CHAP = {'roles': 'Three roles', 'mono': 'One process: a monolith', 'split': 'Two services', 'browser': 'The browser view', 'trade': 'The trade-off', 'task': 'Your lab task', 'rubric': 'Pass or fail rubric', 'yourturn': 'Your turn', 'recap': 'Quick check'}
