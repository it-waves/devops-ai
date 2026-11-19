# source this file, then: lab up | lab files | lab down
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab158.sh" "$@"; }
