# Short names used in the lessons. Load with:  source shortcuts.sh
lab() { sudo /usr/local/bin/lab25.sh "$@"; }                 # lab up | check | down
cl()  { sudo ip netns exec client env -i PATH=$PATH "$@"; }  # run a command inside the client
rt()  { sudo ip netns exec r1 "$@"; }                        # inside the router
sv()  { sudo ip netns exec srv "$@"; }                       # inside the server
