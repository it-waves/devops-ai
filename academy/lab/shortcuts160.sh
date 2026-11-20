# source this file, then: lab up | agent | files | down
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab160.sh" "$@"; }
