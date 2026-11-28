# source this file, then: lab up, lab check, lab down, leakcheck
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab176.sh" "$@"; }
# leakcheck : look for plain-text passwords in the files of this folder, and show where
leakcheck() {
  if grep -rInE '<password>[^$<][^<]*</password>' . 2>/dev/null; then printf '\033[1;91mPASSWORD FOUND in the code (file and line above)\033[0m\n'; else printf '\033[1;92mNo password in the code\033[0m\n'; fi
}
