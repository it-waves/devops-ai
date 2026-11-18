# source this file, then: lab up | lab jobs | lab down
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab154.sh" "$@"; }
