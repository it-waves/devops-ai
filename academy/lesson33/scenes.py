def mono_panel(E, x, y, w, rows, t_show, fs=24, lh=40, col=None):
    """illustration terminal panel: a glass panel and monospaced lines that all appear at t_show"""
    h = len(rows) * lh + 48
    E.append(Pop(glass(w, h, col or MUTED), x, y, t_show))
    for i, (txt, c_) in enumerate(rows): E.append(El(T(txt, 'mono', fs, c_, align='left'), x + 28, y + 24 + i * lh, t_show + 0.25 + 0.12 * i, anim='fade', d=0.25))
    return h
def hbar(E, x, y, w, h, t0, t1, col=None): E.append(bar(x, y, w, h, t0, t1, col or WARN))


def s_hook(C, D, dur):
    E = [El(T('A disk is only useful with room to spare.', 'x', 64), 100, 130, C['h1'])]
    for i, (a, b, col) in enumerate([('Disk', 'where the data lives', ACC), ('Filesystem', 'the structure that holds files', VIO), ('Mount point', 'the folder it appears in', WARN)]):
        E.append(Pop(card(1100, 130, col, a, [(b, TXT)], 44, 32), 100, 280 + i * 160, C['h2'] + i * 2.8))
    E.append(takeaway('Check. Mount. Grow.', 850, C['h3'], GOOD, 1600)); return E
s_see = _lab('Free space, and who uses it', 'Check before it fills.', 's1', RB, [('s1', 'df -hT', 'Free space, per filesystem', ACC), ('s4', 'du -sh', 'Size of one folder', VIO), ('s6', 'sort -h | tail', 'Biggest folders last', WARN)])
s_make = _lab('Make a practice disk', 'A file plays the disk. Nothing real is at risk.', 'm1', RB, [('m1', 'truncate', 'A 100 MB pretend disk', ACC), ('m4', 'mkfs.ext4', 'Give it a filesystem', VIO), ('m6', 'blkid', 'Type and UUID', GOOD)])
s_mount = _lab('Mount it', 'A filesystem is usable only once mounted.', 't1', RB, [('t1', 'mkdir', 'A folder to mount on', ACC), ('t2', 'mount', 'Attach the filesystem', VIO), ('t3', 'df -h', 'Prove it is there', GOOD), ('t5', 'lsblk', 'The block devices', WARN)])
s_full = _lab('Fill it, then free it', 'What a full disk looks like.', 'u1', RB, [('u1', 'fallocate 60M', 'Reserve space', ACC), ('u2', 'df -h', 'About 73 percent used', WARN), ('u4', 'fallocate 40M', 'Does not fit', BAD), ('u6', 'rm, then df', 'The space returns', GOOD)])
s_grow = _lab('Grow a disk', 'Bigger disk first, then bigger filesystem.', 'g1', RB, [('g1', 'df -h', 'Before: about 90 MB', ACC), ('g3', 'truncate', 'Make the disk bigger', VIO), ('g4', 'e2fsck', 'Check first', WARN), ('g5', 'resize2fs', 'Grow the filesystem', PINK), ('g6', 'mount, df', 'After: about 184 MB', GOOD)])
def s_fstab(C, D, dur):
    E = head('Mount at boot', 'One line in /etc/fstab.', C['k1']); E.append(ill(C['k1'] + 0.2, 1260, 286))
    mono_panel(E, 100, 330, 1700, [('UUID=3a369b8a-cf9c-455d-9036-d1e37a94634b  /data  ext4  defaults,nofail  0  2', TXT)], C['k1'] + 0.4, fs=30, lh=60)
    it = [('1  What', 'UUID of the filesystem', ACC), ('2  Where', 'the mount point', VIO), ('3  Type', 'ext4, xfs, ...', GOOD), ('4  Options', 'defaults, nofail', WARN), ('5  Dump', 'backup flag, usually 0', PINK), ('6  Pass', 'check order at boot', ACC)]
    for i, (n, s, col) in enumerate(it): E.append(Pop(card(540, 160, col, n, [(s, TXT)], 40, 30, True), 100 + (i % 3) * 590, 500 + (i // 3) * 185, C['k2'] + i * 0.35))
    E.append(takeaway('Test with sudo mount -a before you reboot.', 880, C['k4'], GOOD, 1700)); return E
def s_myths(C, D, dur):
    E = head('Common myths', 'Four wrong ideas, corrected.', C['my1'])
    it = [('Myth: delete frees space', 'Not while a program holds it open.', 'my2'), ('Myth: formatting is safe', 'It erases the disk.', 'my3'), ('Myth: bigger disk, bigger fs', 'Resize the filesystem too.', 'my4'), ('Myth: mounted means permanent', 'Only /etc/fstab does that.', 'my5')]
    for i, (a, b, cid) in enumerate(it): E.append(Pop(card(840, 190, BAD, a, [(b, TXT)], 40, 32), 100 + (i % 2) * 880, 340 + (i // 2) * 220, C[cid]))
    E.append(takeaway('Check. Mount. Grow. Persist.', 800, C['my6'], GOOD, 1500)); return E
def s_rubric(C, D, dur):
    E = head('Pass or fail rubric', 'Six points. All six to pass.', C['b1'])
    items = [('Free space with df', 'b2'), ('Biggest folders with du', 'b3'), ('Format and read the UUID', 'b4'), ('Mount and prove it', 'b5'), ('Fill it, then free it', 'b6'), ('Grow it, and fstab', 'b7')]
    for i, (n, cid) in enumerate(items):
        x = 100 + (i % 2) * 880; y = 340 + (i // 2) * 170
        E.append(Pop(card(840, 140, [ACC, VIO, GOOD, WARN, PINK, ACC][i], '', [(f'{i + 1}   {n}', TXT)], 4, 34), x, y, C[cid])); E.append(Pop(icon('check', 48, TXT, GOOD), x + 770, y + 46, C[cid] + 0.4))
    E.append(Pop(badge('Pass = all six', F('x', 48), INK, GOOD, padx=34, pady=16, r=30), 100, 870, C['b8'])); return E
def s_yourturn(C, D, dur):
    E = head('Your turn', 'A practice file only. Never a real disk.', C['z1'])
    it = [('1  Look', 'df -hT and du', PINK, 'z2'), ('2  Format', 'truncate, mkfs.ext4', ACC, 'z3'), ('3  Mount', 'blkid, mount, df', WARN, 'z4'), ('4  Fill', 'fallocate, read the error', BAD, 'z5'), ('5  Grow', 'umount, e2fsck, resize2fs', VIO, 'z6'), ('6  Persist', 'write the fstab line', GOOD, 'z7')]
    grid6(E, C, it)
    E.append(Pop(badge('PAUSE  ·  do it before you continue', F('b', 38), INK, PINK, padx=30, pady=16), 100, 880, C['z8'])); return E
def s_recap(C, D, dur):
    E = [El(T('Quick check', 'x', 72), 100, 130, C['f11'])]
    qs = [('Which command shows free space?', 'f12'), ('Which command finds what is big?', 'f13'), ('Which two steps grow a filesystem?', 'f14'), ('Which file makes a mount permanent?', 'f15')]
    for i, (q, cid) in enumerate(qs):
        E.append(Pop(card(1100, 90, [ACC, VIO, GOOD, WARN][i], f'{i + 1}', [], 36), 100, 250 + i * 110, C[cid])); E.append(El(T(q, 'm', 30, maxw=930), 190, 282 + i * 110, C[cid] + 0.1, anim='fade'))
    E.append(Pop(card(1100, 100, GOOD, '', [], 4), 100, 710, C['f16'])); E.append(Pop(icon('check', 56, TXT, GOOD), 130, 732, C['f16'] + 0.2))
    E.append(El(T('Objective covered: MC04-O08', 'b', 28, TXT, maxw=960), 220, 748, C['f16'] + 0.3, anim='wipe', d=1.6))
    pb = badge('PAUSE  ·  answer aloud', F('b', 34), INK, PINK, padx=26, pady=14); E.append(Pop(pb, 100, 860, C['f17']))
    E.append(El(T('Next lesson: networking and security', 'x', 46, ACC, maxw=1700), 100, 960, C['f18'])); E.append(Pop(badge('LIKE  ·  SHARE  ·  SUBSCRIBE', F('b', 34), INK, GOOD, padx=26, pady=14), 100 + pb.width + 40, 860, C['f19']))
    return E
FN = dict(hook=s_hook, see=s_see, make=s_make, mount=s_mount, full=s_full, grow=s_grow, fstab=s_fstab, myths=s_myths, rubric=s_rubric, yourturn=s_yourturn, recap=s_recap)
_GL = dict(see=('eye', GOOD), make=('gear', ACC), mount=('eye', GOOD), full=('eye', GOOD), grow=('gear', ACC), fstab=('board', WARN), myths=('question', BAD), rubric=('test', GOOD), yourturn=('board', VIO))
def _wrap(name, fn):
    first = dict(SCENES)[name][0][0]
    def w(C, D, dur):
        E = fn(C, D, dur); g, col = _GL[name]; E.append(Pop(glyph(g, 120, col, True), 1230, 105, C[first] + 0.3)); return E
    return w
for _n in _GL: FN[_n] = _wrap(_n, FN[_n])
HL = {
 'see': [('s2', 2, 1, 330, 590, ''), ('s3', 2, 1, 590, 665, ''), ('s5', 1, 1, 4, 300, ''), ('s7', 3, 1, 4, 300, '')],
 'make': [('m3', 1, 1, 430, 510, ''), ('m7', 1, 1, 150, 985, '')],
 'mount': [('t4', 2, 1, 4, 860, ''), ('t6', 1, 1, 4, 530, '')],
 'full': [('u3', 2, 1, 4, 860, ''), ('u5', 1, 1, 4, 790, ''), ('u8', 2, 1, 4, 860, '')],
 'grow': [('g2', 2, 1, 250, 322, ''), ('g5', 1, 1, 4, 985, ''), ('g6', 1, 1, 4, 860, ''), ('g8', 2, 1, 240, 318, '')],
}
