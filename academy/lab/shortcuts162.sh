# source this file, then: lab up | backup | restore JOB | old | down
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab162.sh" "$@"; }
