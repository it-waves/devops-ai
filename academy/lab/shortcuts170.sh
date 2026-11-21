# source this file, then: lab check, try_token, leakcheck
lab() { sh "$(dirname "${BASH_SOURCE[0]:-$0}")/lab170.sh" "$@"; }
# try_token NAME : ask SonarQube an administrator question (list webhooks) with the token stored in variable NAME
try_token() {
  code=$(curl -s -m 10 -o /dev/null -w '%{http_code}' -u "${!1}:" "${SONAR_URL:-http://localhost:9000}/api/webhooks/list")
  if [ "$code" = 200 ]; then printf '%-16s \033[1;92mallowed (%s)\033[0m\n' "$1" "$code"; else printf '%-16s \033[1;91mrefused (%s)\033[0m\n' "$1" "$code"; fi
}
# leakcheck : look for SonarQube tokens in the files of this repository
leakcheck() {
  if git grep -qE 'sq[apu]_[A-Za-z0-9]{20,}' 2>/dev/null; then printf '\033[1;91mTOKEN FOUND in the code\033[0m\n'; else printf '\033[1;92mNo token in the code\033[0m\n'; fi
}
