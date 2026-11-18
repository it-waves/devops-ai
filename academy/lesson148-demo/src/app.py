import sys
env = sys.argv[1]
conf = dict(l.strip().split('=') for l in open(sys.argv[2]) if '=' in l)
print(f"shop 1.4.0 running in {env}: db={conf['db']} debug={conf['debug']}")
