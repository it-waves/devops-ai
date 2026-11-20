# source this file, then: lab up | check | backup | down
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab163.sh" "$@"; }
