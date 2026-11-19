# source this file, then: lab files | lab show 1 | lab clean
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab156.sh" "$@"; }
