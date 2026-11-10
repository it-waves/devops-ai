#!/usr/bin/env python3
"""Tiny teaching helpers built on Python's standard ipaddress module.
Installed under three names: ipwhat, subnet, inside."""
import sys, os, ipaddress as ip
name = os.path.basename(sys.argv[0])
try:
    if name == 'ipwhat':
        a = ip.ip_address(sys.argv[1])
        if a.is_private: print(f'{a!s:<14} private  · stays inside the network')
        else: print(f'{a!s:<14} public   · reachable on the internet')
    elif name == 'subnet':
        n = ip.ip_network(sys.argv[1], strict=False); h = list(n.hosts()) if n.num_addresses < 70000 else None
        first = n.network_address + 1; last = n.broadcast_address - 1
        for k, v in [('network', f'{n.network_address}/{n.prefixlen}'), ('mask', n.netmask), ('first', first), ('last', last), ('broadcast', n.broadcast_address), ('hosts', n.num_addresses - 2)]:
            print(f'{k:<10} {v}')
    elif name == 'inside':
        n = ip.ip_network(sys.argv[1], strict=False); a = ip.ip_address(sys.argv[2])
        if a in n: print(f'{a} is inside {n} → send directly')
        else: print(f'{a} is outside {n} → send to the gateway')
    else: print('unknown helper')
except Exception as e:
    print('usage error:', e)
