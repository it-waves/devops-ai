# source this file, then: lab check | stop
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab165.sh" "$@"; }
