# source this file, then: lab check
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab169.sh" "$@"; }
