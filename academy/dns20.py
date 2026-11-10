import sys
from dnslib import DNSRecord, RR, QTYPE, RCODE, A, CNAME, MX, TXT
from dnslib.server import DNSServer, BaseResolver
Z = {
 'web.lab.test.': {'A': ['127.0.0.1']}, 'www.lab.test.': {'CNAME': ['web.lab.test.']},
 'lab.test.': {'MX': [(10, 'mail.lab.test.')], 'TXT': ['lab demo zone']}, 'mail.lab.test.': {'A': ['127.0.0.1']},
}
class R(BaseResolver):
    def resolve(self, request, handler):
        r = request.reply(); r.header.aa = 1; q = request.q; name = str(q.qname).lower(); t = QTYPE[q.qtype]
        if name not in Z: r.header.rcode = RCODE.NXDOMAIN; return r
        d = Z[name]
        if 'CNAME' in d and t != 'CNAME':
            tgt = d['CNAME'][0]; r.add_answer(RR(name, QTYPE.CNAME, ttl=300, rdata=CNAME(tgt)))
            if tgt in Z and t in Z[tgt] and t == 'A':
                for a in Z[tgt]['A']: r.add_answer(RR(tgt, QTYPE.A, ttl=300, rdata=A(a)))
            return r
        if t in d:
            for v in d[t]:
                if t == 'A': r.add_answer(RR(name, QTYPE.A, ttl=300, rdata=A(v)))
                elif t == 'CNAME': r.add_answer(RR(name, QTYPE.CNAME, ttl=300, rdata=CNAME(v)))
                elif t == 'MX': r.add_answer(RR(name, QTYPE.MX, ttl=300, rdata=MX(v[1], v[0])))
                elif t == 'TXT': r.add_answer(RR(name, QTYPE.TXT, ttl=300, rdata=TXT(v)))
        return r
s = DNSServer(R(), port=53, address='127.0.0.1'); s.start_thread()
import time
while True: time.sleep(3600)
