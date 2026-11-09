import sys; sys.path.insert(0, '/home/claude/academy/sdlc01'); sys.path.insert(0, '/home/claude/academy/welcome')
from scenes_sdlc01 import *
def s_hook(C, D, dur):
    t = C['a1']; E = [El(T('Where do I even start?', 'x', 76, PINK, maxw=900), 100, 230, t)]
    E.append(El(icon('q', 260, TXT, ACC), 1300, 230, t + 0.3, anim='fade'))
    E.append(El(T('DevOps Engineering', 'x', 92), 100, 470, C['a2']))
    E.append(El(T('Bootcamp', 'x', 92, ACC), 100, 580, C['a2'] + 0.2))
    E.append(El(T('Zero to production  ·  step by step', 'm', 40, MUTED), 100, 720, C['a2'] + 1.5))
    for i, (s, col) in enumerate([('Real labs', GOOD), ('Real output', ACC), ('Clear explanations', VIO)]):
        E.append(El(badge(s, F('b', 30), (8, 24, 26), col, padx=22, pady=12), 100 + i * 290, 820, C['a2'] + 3.0 + i * 0.8, anim='fade'))
    return E
def s_promise(C, D, dur):
    E = [El(T('Learn it. Build it. Break it. Fix it. Operate it.', 'x', 54, maxw=1700), 100, 140, C['b1'])]
    steps = [('Learn', 'the idea and why it exists', ACC, 'b2'), ('Build', 'set it up in a working lab', VIO, 'b3'), ('Break', 'watch what fails, safely', WARN, 'b4'), ('Fix', 'find the cause, repair it', GOOD, 'b5'), ('Operate', 'secure, monitor, keep it running', PINK, 'b6')]
    cw, gap = 300, 55
    for i, (n, sub, col, cid) in enumerate(steps):
        x = 100 + i * (cw + gap); tt = C[cid]
        E.append(El(card(cw, 260, col, f'{i + 1}  {n}', [(sub, TXT)], 44, 28), x, 380, tt, anim='up'))
        if i < 4: E.append(A([(x + cw + 8, 510), (x + cw + gap - 8, 510)], tt + 0.6, MUTED, 5, 20))
    E.append(El(T('Every Masterclass follows these five steps.', 'm', 36, MUTED), 100, 700, C['b6'] + 2.0))
    return E
PATH = [('A', 'Foundations', 'Linux · Bash · Python · Git', ACC), ('B', 'Applications', 'Java · Maven · Tomcat · SQL', VIO), ('C', 'CI/CD', 'Jenkins · SonarQube · Nexus', GOOD),
        ('D', 'Containers', 'Docker · Compose', WARN), ('E', 'Cloud', 'AWS · Azure', PINK), ('F', 'Automation', 'Terraform · Ansible', ACC),
        ('G', 'Kubernetes', 'Helm · Argo CD · EKS · AKS', VIO), ('H', 'Reliability', 'DevSecOps · Prometheus · SRE', GOOD), ('I', 'Capstone', 'build and run it all', WARN)]
def s_path(C, D, dur):
    E = [El(T('Nine stages. Each builds on the last.', 'x', 56, maxw=1700), 100, 140, C['c1']), ill(C['c1'], 1480, 130)]
    cues = ['c2', 'c2', 'c3', 'c3', 'c4', 'c4', 'c4', 'c4', 'c4']; off = [0.5, 5.5, 0.5, 4.0, 0.3, 3.0, 5.5, 7.5, 11.0]
    cw, ch = 540, 165
    for i, (k, n, tools, col) in enumerate(PATH):
        x = 100 + (i % 3) * (cw + 50); y = 290 + (i // 3) * (ch + 30); tt = C[cues[i]] + off[i]
        E.append(El(card(cw, ch, col, f'{k}  {n}', [(tools, TXT)], 40, 28), x, y, tt, anim='up'))
    E.append(El(T('Published stage by stage, in order. This is the plan.', 'b', 36, WARN, maxw=1700), 100, 920, C['c5']))
    return E
def s_lesson(C, D, dur):
    E = [El(T('Every lesson has the same shape', 'x', 58, maxw=1700), 100, 140, C['d1'])]
    items = [('Why', 'the problem it solves', ACC, 'd2', 0.2), ('Concept', 'plain words', VIO, 'd2', 3.6), ('Demo', 'real commands, real output', GOOD, 'd3', 0.3), ('Practice', 'you do it yourself', WARN, 'd4', 0.2), ('Check', 'a checker says pass or fail', PINK, 'd4', 4.2)]
    cw, gap = 300, 55
    for i, (n, sub, col, cid, o) in enumerate(items):
        x = 100 + i * (cw + gap); tt = C[cid] + o
        E.append(El(card(cw, 250, col, n, [(sub, TXT)], 44, 28), x, 340, tt, anim='up'))
        if i < 4: E.append(A([(x + cw + 8, 465), (x + cw + gap - 8, 465)], tt + 0.6, MUTED, 5, 20))
    E.append(El(badge('REAL OUTPUT  ·  never invented', F('b', 30), (8, 24, 26), GOOD, padx=22, pady=12), 100 + 2 * (cw + gap), 640, C['d3'] + 1.5, anim='fade'))
    return E
def s_expect(C, D, dur):
    E = [El(T('What to expect', 'x', 66), 100, 130, C['e1'])]
    items = [('No experience needed', 'every new term explained once', 'e2', ACC), ('Linux on Ubuntu', 'free, in a virtual machine', 'e3', VIO), ('Honest labels', 'illustrations are marked on screen', 'e4', WARN),
             ('Costs told up front', 'some cloud lessons need an account', 'e5', GOOD), ('No job promise', 'real practice and a way to check progress', 'e6', PINK)]
    for i, (n, sub, cid, col) in enumerate(items):
        y = 280 + i * 125; tt = C[cid]
        E.append(El(rrect(1500, 105, 18, fill=PANEL, outline=col, width=3), 100, y, tt, anim='fade'))
        E.append(El(icon('check', 56, TXT, col), 130, y + 24, tt + 0.1, anim='fade'))
        E.append(El(T(n, 'b', 40, col), 220, y + 12, tt + 0.1, anim='fade')); E.append(El(T(sub, 'm', 30, MUTED), 220, y + 58, tt + 0.2, anim='fade'))
    return E
def s_start(C, D, dur):
    E = [El(T('Start here', 'b', 36, ACC), 100, 150, C['f1']), El(T('Lesson 1', 'x', 110), 100, 200, C['f1'] + 0.1)]
    E.append(El(T('From Idea to Customer', 'x', 64, ACC), 100, 350, C['f1'] + 0.3))
    E.append(El(T('The software development life cycle', 'm', 40, MUTED), 100, 450, C['f1'] + 0.5))
    E.append(El(card(900, 200, GOOD, 'Follow the playlist in order', [('Each lesson builds on the one before.', TXT)], 40), 100, 600, C['f2']))
    E.append(El(badge('SUBSCRIBE', F('b', 40), (8, 24, 26), ACC, padx=40, pady=20), 1200, 660, C['f2'] + 1.5, anim='fade'))
    return E
FN = dict(hook=s_hook, promise=s_promise, path=s_path, lesson=s_lesson, expect=s_expect, start=s_start)
