# source this file, then: lab up | repo | bug | fix | bump | files | down
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab159.sh" "$@"; }
