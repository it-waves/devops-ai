# source this file, then: lab up | lab pass | lab down
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab155.sh" "$@"; }
