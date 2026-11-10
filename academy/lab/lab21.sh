#!/bin/sh
# lab21.sh up|down : client -- r1 -- srv, three network namespaces joined by veth pairs
down() { for n in client r1 srv; do ip netns del $n 2>/dev/null; done; pkill -f dns21.py; pkill -f web21.py; rm -rf /etc/netns/client; true; }
if [ "$1" = down ]; then down; exit 0; fi
down
for n in client r1 srv; do ip netns add $n; ip netns exec $n ip link set lo up; done
ip link add c0 type veth peer name r1a; ip link set c0 netns client; ip link set r1a netns r1
ip link add r1b type veth peer name s0; ip link set r1b netns r1; ip link set s0 netns srv
ip -n client addr add 10.0.1.2/24 dev c0; ip -n client link set c0 up; ip -n client route add default via 10.0.1.1
ip -n r1 addr add 10.0.1.1/24 dev r1a; ip -n r1 link set r1a up; ip -n r1 addr add 10.0.2.1/24 dev r1b; ip -n r1 link set r1b up
ip netns exec r1 sysctl -qw net.ipv4.ip_forward=1
ip netns exec r1 sysctl -qw net.ipv4.icmp_ratelimit=0
ip netns exec srv sysctl -qw net.ipv4.icmp_ratelimit=0
ip netns exec client sysctl -qw net.ipv4.icmp_ratelimit=0
for n in client r1 srv; do ip netns exec $n sysctl -qw net.ipv4.icmp_ratemask=0; done
ip -n srv addr add 10.0.2.2/24 dev s0; ip -n srv link set s0 up; ip -n srv route add default via 10.0.2.1
mkdir -p /etc/netns/client; echo "nameserver 10.0.2.2" > /etc/netns/client/resolv.conf
ip netns exec srv sh -c 'nohup python3 /usr/local/bin/dns21.py >/dev/null 2>&1 &'
ip netns exec srv sh -c 'nohup python3 /usr/local/bin/web21.py 8080 >/dev/null 2>&1 &'
sleep 5
