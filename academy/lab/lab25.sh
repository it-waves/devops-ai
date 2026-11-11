#!/bin/sh
# lab25.sh : networking mastery lab (client -- router -- server). Run with sudo.
#   up | down | reset | check | restart-app | client CMD | router CMD | server CMD
# Mission: from the client, http://cart.lab.test:8080 and https://cart.lab.test:8443 (trusting /opt/lab25/ca.pem) must both work.
D=/opt/lab25
down() { for n in client r1 srv; do ip netns del $n 2>/dev/null; done; pkill -f dns25.py; pkill -f web25.py; rm -rf /etc/netns/client; true; }
mkcerts() {
  [ -f $D/ca.pem ] && return; mkdir -p $D; cd $D
  openssl req -x509 -newkey rsa:2048 -nodes -keyout ca.key -out ca.pem -days 3650 -subj "/CN=Lab Root CA" 2>/dev/null
  openssl req -newkey rsa:2048 -nodes -keyout web.key -out web.csr -subj "/CN=cart.lab.test" 2>/dev/null
  printf 'subjectAltName=DNS:cart.lab.test\n' > san.ext
  openssl x509 -req -in web.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out web.pem -days 365 -extfile san.ext 2>/dev/null
  chmod 644 $D/*; cd /
}
up() {
  down; mkcerts
  for n in client r1 srv; do ip netns add $n; ip netns exec $n ip link set lo up; ip netns exec $n sysctl -qw net.ipv4.icmp_ratelimit=0; done
  ip link add c0 type veth peer name r1a; ip link set c0 netns client; ip link set r1a netns r1
  ip link add r1b type veth peer name s0; ip link set r1b netns r1; ip link set s0 netns srv
  ip -n client addr add 10.0.1.2/24 dev c0; ip -n client link set c0 up; ip -n client route add default via 10.0.1.1
  ip -n r1 addr add 10.0.1.1/24 dev r1a; ip -n r1 link set r1a up; ip -n r1 addr add 10.0.2.1/24 dev r1b; ip -n r1 link set r1b up
  ip -n srv addr add 10.0.2.2/24 dev s0; ip -n srv link set s0 up; ip -n srv route add default via 10.0.2.1
  mkdir -p /etc/netns/client
  ip netns exec srv sh -c 'nohup python3 /usr/local/bin/dns25.py >/dev/null 2>&1 &'
  echo 8081 > $D/app.port; chmod 666 $D/app.port
  ip netns exec srv sh -c "nohup python3 /usr/local/bin/web25.py $(cat $D/app.port) >/dev/null 2>&1 &"
  ip netns exec srv sh -c "nohup python3 /usr/local/bin/web25.py 8443 $D/web.pem $D/web.key >/dev/null 2>&1 &"
  # the faults, injected in advance
  echo "nameserver 10.0.2.9" > /etc/netns/client/resolv.conf
  ip netns exec r1 sysctl -qw net.ipv4.ip_forward=0
  ip netns exec srv iptables -A INPUT -p tcp --dport 8443 -j DROP
  sleep 9; echo "lab is up. Four things are wrong. Mission: both URLs must work from the client."
}
chk() { if eval "$2" >/dev/null 2>&1; then echo "PASS  $1"; else echo "FAIL  $1"; fi; }
check() {
  C="ip netns exec client"
  NS=$(awk '/^nameserver/{print $2; exit}' /etc/netns/client/resolv.conf 2>/dev/null)
  chk "1 name resolves (cart.lab.test)" "$C dig +short +time=1 +tries=1 @$NS cart.lab.test | grep -q 10.0.2.2"
  chk "2 server reachable (ping)" "$C ping -c 1 -W 1 10.0.2.2"
  chk "3 http works (port 8080)" "$C env -i curl -s -m 2 http://cart.lab.test:8080 | grep -q cart"
  chk "4 https works (trusting the lab CA)" "$C env -i curl -s -m 2 --cacert $D/ca.pem https://cart.lab.test:8443 | grep -q cart"
}
case "$1" in
 up) up;; down) down; echo "lab removed";; reset) up;; check) check;;
 restart-app) pkill -f "web25.py [0-9]*$"; ip netns exec srv sh -c "nohup python3 /usr/local/bin/web25.py $(cat $D/app.port) >/dev/null 2>&1 &"; sleep 2; echo "app restarted on port $(cat $D/app.port)";;
 client) shift; ip netns exec client "$@";; router) shift; ip netns exec r1 "$@";; server) shift; ip netns exec srv "$@";;
 *) echo "usage: sudo $0 up|down|reset|check|restart-app|client CMD|router CMD|server CMD";;
esac
