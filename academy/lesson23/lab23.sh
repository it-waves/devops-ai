#!/bin/sh
# lab23.sh up|down : client -- r1 -- host(+bridge, 2 containers) and srv ("internet")
down() { for n in client r1 host srv c1 c2; do ip netns del $n 2>/dev/null; done; pkill -f web23.py; pkill -f web22.py; true; }
if [ "$1" = down ]; then down; exit 0; fi
down
for n in client r1 host srv c1 c2; do ip netns add $n; ip netns exec $n ip link set lo up; ip netns exec $n sysctl -qw net.ipv4.icmp_ratelimit=0; ip netns exec $n sysctl -qw net.ipv4.icmp_ratemask=0; done
v() { ip link add $2 type veth peer name $4; ip link set $2 netns $1; ip link set $4 netns $3; }
v client c0 r1 r1a; v r1 r1b host h0; v r1 r1c srv s0
ip -n client addr add 10.0.1.2/24 dev c0; ip -n client link set c0 up; ip -n client route add default via 10.0.1.1
ip -n r1 addr add 10.0.1.1/24 dev r1a; ip -n r1 addr add 10.0.2.1/24 dev r1b; ip -n r1 addr add 10.0.3.1/24 dev r1c
for i in r1a r1b r1c; do ip -n r1 link set $i up; done
ip netns exec r1 sysctl -qw net.ipv4.ip_forward=1
ip -n host addr add 10.0.2.2/24 dev h0; ip -n host link set h0 up; ip -n host route add default via 10.0.2.1
ip -n srv addr add 10.0.3.2/24 dev s0; ip -n srv link set s0 up; ip -n srv route add default via 10.0.3.1
# host bridge = docker0-style
ip -n host link add br0 type bridge; ip -n host addr add 172.18.0.1/24 dev br0; ip -n host link set br0 up
ip netns exec host sysctl -qw net.ipv4.ip_forward=1
for k in 1 2; do
  ip link add vh$k type veth peer name cp$k; ip link set vh$k netns host; ip link set cp$k netns c$k; ip -n c$k link set cp$k name eth0
  ip -n host link set vh$k master br0; ip -n host link set vh$k up
  ip -n c$k addr add 172.18.0.$((k+1))/24 dev eth0; ip -n c$k link set eth0 up; ip -n c$k route add default via 172.18.0.1
done
ip netns exec c1 sh -c 'nohup python3 /usr/local/bin/web23.py 8000 >/dev/null 2>&1 &'
ip netns exec srv sh -c 'nohup python3 /usr/local/bin/web23.py 8080 >/dev/null 2>&1 &'
sleep 6
