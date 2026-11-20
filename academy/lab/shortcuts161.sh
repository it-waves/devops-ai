# source this file, then: lab up | hook | files | down
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab161.sh" "$@"; }
