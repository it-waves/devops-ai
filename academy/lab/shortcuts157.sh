# source this file, then: lab up | lab repo | lab bad | lab fix | lab down
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab157.sh" "$@"; }
