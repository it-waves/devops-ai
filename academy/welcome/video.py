import sys, random; sys.path.insert(0, '/home/claude/academy/common')
from kit import *
ACC, GOOD, WARN, TXT, MUTED, PANEL = EN.ACC, EN.GOOD, EN.WARN, EN.TXT, EN.MUTED, EN.PANEL
LABEL = 'INTRO  ·  DEVOPS BOOTCAMP'
def c(cid, cap, say=None, gap=None): return (cid, cap, say, gap) if gap is not None else (cid, cap, say)
SCENES = [
 ('hook', [
  c('a1', "You can learn every DevOps tool,"), c('a2', "and still not know how they fit together."), c('a3', "That is where most beginners get stuck."),
  c('a4', "This bootcamp puts every tool in order."), c('a5', "Welcome to the DevOps Engineering Bootcamp."), c('a6', "A step by step course, from zero to building, securing, and running real systems."),
 ]),
 ('promise', [
  c('b1', "Here is how we teach every tool. Five steps."), c('b2', "Learn it: understand the idea, and why it exists."), c('b3', "Build it: set it up yourself, in a working lab."),
  c('b4', "Break it: watch what fails, in a safe lab."), c('b5', "Fix it: find the cause, and repair it."), c('b6', "Operate it: secure it, monitor it, and keep it running."),
 ]),
 ('path', [
  c('c1', "The course is planned in nine stages,"), c('c2', "and each stage builds on the one before."),
  c('c3', "Foundations:"), c('c4', "Linux,", "Linux,"), c('c5', "Bash,"), c('c6', "Python,"), c('c7', "and Git."),
  c('c8', "Applications and build tools:"), c('c9', "Java,"), c('c10', "Maven,"), c('c11', "Tomcat,"), c('c12', "and databases."),
  c('c13', "Then C I C D:", "Then C I C D:"), c('c14', "Jenkins,"), c('c15', "SonarQube,", "sonar cube,"), c('c16', "and containers with Docker."),
  c('c17', "Then the cloud,"), c('c17a', "AWS,", "A W S,"), c('c17b', "and Azure,"), c('c18', "Terraform,", "terra form,"), c('c19', "Ansible,"), c('c20', "and Kubernetes,"), c('c21', "with Helm and Argo CD.", "with Helm and Argo C D."),
  c('c22', "Then security,"), c('c22b', "monitoring, and reliability,"), c('c23', "and a final capstone project."),
  c('c24', "This is the plan. Lessons are published stage by stage, in order."),
 ]),
 ('lesson', [
  c('d1', "Every lesson follows the same shape."), c('d2', "First, why:"), c('d3', "the problem the tool solves."), c('d4', "Then the concept, in plain words."),
  c('d5', "Then a demonstration,"), c('d6', "with real commands, and real output."), c('d7', "No made up results."),
  c('d8', "Then practice,"), c('d9', "which you do yourself,"), c('d10', "and a checker that tells you if you got it right."), c('d11', "Each Masterclass ends with five hands-on projects."),
 ]),
 ('expect', [
  c('e1', "A few promises about what to expect."), c('e2', "No experience needed."), c('e3', "We explain every new term and command the first time it appears."),
  c('e4', "Linux lessons use Ubuntu,"), c('e5', "a free system you can run on your own computer, in a virtual machine."),
  c('e6', "When something is an illustration, and not a real capture, we label it on screen."),
  c('e7', "Some cloud lessons may need an account with a cloud provider."), c('e8', "We will tell you the cost before you click anything."),
  c('e9', "We cannot promise you a job."), c('e10', "We can promise real practice, and a way to check your own progress."),
 ]),
 ('start', [
  c('f1', "Start with lesson one:"), c('f2', "the software development life cycle."), c('f3', "How does an idea become something customers use?"),
  c('f4', "Subscribe, and follow the playlist in order."), c('f5', "See you in lesson one."),
 ]),
]
EXTRA = {'a3': 0.4, 'b6': 1.5, 'c24': 1.5, 'd11': 1.0, 'e10': 1.0, 'f3': 0.3, 'a4': 0.3}
CHAP = {'promise': 'How we teach', 'path': 'The roadmap', 'lesson': 'Every lesson', 'expect': 'What to expect', 'start': 'Start here'}
ALL = ['git', 'docker', 'kubernetes', 'jenkins', 'terraform', 'ansible', 'prometheus', 'grafana', 'maven', 'java', 'tomcat', 'postgresql', 'ubuntu', 'python', 'actions', 'sonarqube', 'argocd', 'helm', 'github', 'bash', 'trivy', 'vault']
def s_hook(C, D, dur):
    t_out = C['a4'] - 0.1
    E = [FloatEm('Person shrugging', 150, 470, 400, C['a1'] - 0.2, t_out, bob=8, sway=4, speed=2.2)]
    bub = bubble(T('Where do I even start?', 'x', 54, TXT, maxw=560), (200, 0)); bq = Pop(bub, 100, 190, C['a2'] + 0.15); bq.t1 = t_out; E.append(bq)
    for nm, qx, qy, sz, dl, ph in [('Thinking face', 560, 520, 130, 0.45, 0.0), ('Red question mark', 90, 520, 110, 0.85, 1.5), ('Confused face', 575, 700, 120, 1.25, 3.0), ('Anxious face with sweat', 60, 760, 110, 1.7, 4.5)]:
        E.append(FloatEm(nm, qx, qy, sz, C['a2'] + dl, t_out, bob=12, sway=8, speed=2.6, phase=ph, spin_in=True))
    E.append(Tilt(ALL, 1290, 500, C['a1'] - 0.2, t_out, C['a1'], C['a3'] + 1.0, cols=6, chip=118, gap=34))
    q2 = El(T('Too many tools. No order.', 'b', 34, MUTED, maxw=300), 620, 820, C['a3'], anim='fade'); q2.t1 = t_out; E.append(q2)
    row = ['ubuntu', 'git', 'maven', 'jenkins', 'docker', 'kubernetes', 'terraform', 'prometheus']
    for i, n in enumerate(row): E.append(Pop(LG.chip(n, 110, LG.PRETTY[n], F('b', 22)), 150 + i * 215, 150, C['a4'] + 0.25 + i * 0.28))
    for i in range(7): E.append(A([(150 + i * 215 + 118, 205), (150 + i * 215 + 205, 205)], C['a4'] + 0.6 + i * 0.28, MUTED, 5, 16, 0.3))
    E.append(El(T('DevOps Engineering', 'x', 96), 100, 430, C['a5']))
    E.append(El(T('Bootcamp', 'x', 96, ACC), 100, 540, C['a5'] + 0.25))
    E.append(El(T('Zero to production  ·  step by step', 'm', 40, MUTED), 100, 690, C['a6']))
    for i, (s_, col) in enumerate([('Real labs', GOOD), ('Real output', ACC), ('Clear explanations', VIO)]): E.append(pill(s_, 100 + i * 330, 800, C['a6'] + 2.0 + i * 1.3, col, INK, 30, 22, 12))
    return E
def s_promise(C, D, dur):
    E = [El(T('Learn it. Build it. Break it. Fix it. Operate it.', 'x', 54, maxw=1700), 100, 140, C['b1'])]
    steps = [('Learn', 'the idea and why it exists', ACC, 'b2', 'mag'), ('Build', 'set it up in a working lab', VIO, 'b3', 'pc'), ('Break', 'watch what fails, safely', WARN, 'b4', 'cross'), ('Fix', 'find the cause, repair it', GOOD, 'b5', 'check'), ('Operate', 'secure, monitor, keep it running', PINK, 'b6', 'lock')]
    cw, gap = 310, 42
    for i, (n, sub, col, cid, ic) in enumerate(steps):
        x = 100 + i * (cw + gap)
        E.append(Pop(card(cw, 400, col, f'{i + 1}  {n}', [(sub, TXT)], 44, 28), x, 330, C[cid])); E.append(Pop(icon(ic, 130, TXT, col), x + 28, 560, C[cid] + 0.3))
        if i < 4: E.append(A([(x + cw + 6, 530), (x + cw + gap - 6, 530)], C[cid] + 0.7, MUTED, 5, 18, 0.3))
    E.append(El(T('Every Masterclass follows these five steps.', 'm', 36, MUTED), 100, 800, C['b6'] + 1.0))
    return E
def tchip(s, w, h=84):
    im = rrect(w, h, 16, fill=(28, 52, 60), outline=EN.EDGE, width=2); t = T(s, 'b', 24, TXT); im.alpha_composite(t, ((w - t.width) // 2, (h - t.height) // 2)); return im
PATH = [('A', 'Foundations', ACC, [('linux', 'c4'), ('bash', 'c5'), ('python', 'c6'), ('git', 'c7')]), ('B', 'Applications', VIO, [('java', 'c9'), ('maven', 'c10'), ('tomcat', 'c11'), ('postgresql', 'c12')]),
        ('C', 'CI/CD', GOOD, [('jenkins', 'c14'), ('sonarqube', 'c15'), ('docker', 'c16')]), ('D', 'Cloud', PINK, [('aws', 'c17a'), ('azure', 'c17b')]),
        ('E', 'Automation', ACC, [('terraform', 'c18'), ('ansible', 'c19')]), ('F', 'Kubernetes', VIO, [('kubernetes', 'c20'), ('helm', 'c21'), ('argocd', 'c21')]),
        ('G', 'Security', GOOD, [('trivy', 'c22'), ('vault', 'c22')]), ('H', 'Reliability', WARN, [('prometheus', 'c22b'), ('grafana', 'c22b')]), ('I', 'Capstone', PINK, [])]
TITLE_AT = {'A': 'c3', 'B': 'c8', 'C': 'c13', 'D': 'c17', 'E': 'c18', 'F': 'c20', 'G': 'c22', 'H': 'c22b', 'I': 'c23'}
def s_path(C, D, dur):
    E = [El(T('Nine stages. Each builds on the last.', 'x', 56, maxw=1500), 100, 130, C['c1']), ill(C['c1'], 1480, 140)]
    cw, ch = 560, 226
    for i, (k, n, col, lg) in enumerate(PATH):
        x = 100 + (i % 3) * (cw + 50); y = 235 + (i // 3) * (ch + 20)
        E.append(Pop(card(cw, ch, col, f'{k}  {n}', [], 38), x, y, C[TITLE_AT[k]] - 0.05 + (0.5 if k in 'EGH' else 0)))
        if k == 'I': E.append(Pop(icon('check', 90, TXT, col), x + 30, y + 100, C['c23'] + 0.4)); E.append(El(T('build and run it all', 'm', 28, MUTED), x + 140, y + 130, C['c23'] + 0.6, anim='fade'))
        for j, (nm, cid) in enumerate(lg):
            lx = x + 26 + j * 132; ly = y + 96
            E.append(Pop(LG.chip(nm, 84, LG.PRETTY[nm], F('b', 19)), lx, ly - 4, C[cid] + 0.05 + (0.25 * j if cid in ('c21', 'c22', 'c22b') else 0)))
    E.append(pill('Published stage by stage, in order', 1100, 150, C['c24'], WARN, INK, 28, 20, 10)) if False else None
    E.append(El(T('Published stage by stage, in order. This is the plan.', 'b', 32, WARN, maxw=1300), 100, 985, C['c24']))
    return E
def s_lesson(C, D, dur):
    E = [El(T('Every lesson has the same shape', 'x', 58, maxw=1700), 100, 140, C['d1'])]
    items = [('Why', 'the problem it solves', ACC, 'd2', 'q'), ('Concept', 'in plain words', VIO, 'd4', 'mag'), ('Demo', 'real commands, real output', GOOD, 'd5', 'pc'), ('Practice', 'you do it yourself', WARN, 'd8', 'server'), ('Check', 'a checker says pass or fail', PINK, 'd10', 'check'), ('Projects', 'five per Masterclass', ACC, 'd11', 'browser')]
    cw, gap = 270, 20
    for i, (n, sub, col, cid, ic) in enumerate(items):
        x = 100 + i * (cw + gap); E.append(Pop(card(cw, 330, col, n, [(sub, TXT)], 40, 26), x, 340, C[cid])); E.append(Pop(icon(ic, 100, TXT, col), x + 28, 560, C[cid] + 0.3))
    E.append(pill('REAL OUTPUT  ·  never invented', 100 + 2 * (cw + gap), 720, C['d7'], GOOD, INK, 30, 22, 12))
    E.append(El(T('You do the practice, the checker tells you the truth.', 'b', 36, MUTED), 100, 860, C['d10'] + 1.5))
    return E
def s_expect(C, D, dur):
    E = [El(T('What to expect', 'x', 66), 100, 130, C['e1'])]
    items = [('No experience needed', 'every new term explained once', 'e2', 'e3', ACC, None), ('Linux on Ubuntu', 'free, in a virtual machine', 'e4', 'e5', VIO, 'ubuntu'), ('Honest labels', 'illustrations are marked on screen', 'e6', 'e6', WARN, None),
             ('Costs told up front', 'some cloud lessons need an account', 'e7', 'e8', GOOD, None), ('No job promise', 'real practice and a way to check progress', 'e9', 'e10', PINK, None)]
    for i, (n, sub, c1, c2, col, lg) in enumerate(items):
        y = 270 + i * 135; E.append(Pop(rrect(1500, 112, 18, fill=PANEL, outline=col, width=3), 100, y, C[c1]))
        E.append(Pop(icon('check', 56, TXT, col), 130, y + 28, C[c1] + 0.15)); E.append(El(T(n, 'b', 40, col), 220, y + 12, C[c1] + 0.15, anim='fade')); E.append(El(T(sub, 'm', 30, MUTED), 220, y + 62, C[c2] + 0.1, anim='fade'))
        if lg: E.append(Pop(LG.chip(lg, 100), 1620, y + 6, C[c1] + 0.3))
    return E
def s_start(C, D, dur):
    E = [El(T('Start here', 'b', 36, ACC), 100, 150, C['f1']), El(T('Lesson 1', 'x', 110), 100, 200, C['f1'] + 0.1)]
    E.append(El(T('From Idea to Customer', 'x', 64, ACC), 100, 350, C['f2'])); E.append(El(T('The software development life cycle', 'm', 40, MUTED), 100, 450, C['f2'] + 0.3))
    E.append(Pop(bulb(120), 160, 620, C['f3'])); E.append(Move(parcel(120), [(C['f3'] + 0.4, 220, 680), (C['f3'] + 2.6, 1500, 680)], None, 5))
    E.append(A([(330, 700), (1380, 700)], C['f3'] + 0.5, MUTED, 5, 22, 1.5)) if False else None
    E.append(El(T('IDEA', 'x', 40, ACC), 160, 760, C['f3'], anim='fade')); E.append(El(T('CUSTOMER', 'x', 40, GOOD), 1400, 760, C['f3'] + 2.2, anim='fade'))
    E.append(FloatEm('Rocket', 1560, 190, 200, C['f1'] + 0.3, None, bob=14, sway=5, speed=1.8)); E.append(FloatEm('Thumbs up', 1480, 420, 190, C['f5'] - 0.1, None, bob=8, sway=6, speed=2.4, spin_in=True)); E.append(FloatEm('Party popper', 1700, 440, 170, C['f5'] + 0.2, None, bob=10, sway=10, speed=2.8, phase=1.0, spin_in=True))
    E.append(Pop(card(900, 150, GOOD, 'Follow the playlist in order', [('Each lesson builds on the one before.', TXT)], 38), 100, 880, C['f4'])); E.append(Pop(badge('SUBSCRIBE', F('b', 40), INK, ACC, padx=40, pady=20), 1250, 900, C['f4'] + 0.8))
    return E
FN = dict(hook=s_hook, promise=s_promise, path=s_path, lesson=s_lesson, expect=s_expect, start=s_start)
