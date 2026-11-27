# source this file, then: lab up, lab check, lab down, leakcheck
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab172.sh" "$@"; }
# leakcheck : look for SonarQube tokens in the files of this repository, and show where
leakcheck() {
  if git grep -nE 'sq[apu]_[A-Za-z0-9]{20,}' 2>/dev/null; then printf '\033[1;91mTOKEN FOUND in the code (file and line above)\033[0m\n'; else printf '\033[1;92mNo token in the code\033[0m\n'; fi
}
