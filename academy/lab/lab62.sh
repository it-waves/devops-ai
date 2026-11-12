#!/bin/sh
# lab62.sh : Git and GitHub, lesson 62 checker (pull requests, reviews, protected branches).
#   sh lab62.sh check OWNER/REPO     for example: sh lab62.sh check sam-lee/team-app
# Mission: four checks must say PASS. It only READS your public GitHub repository through the public GitHub API (nothing is changed).
# Needs python3 (installed on Ubuntu). Optional: GITHUB_TOKEN=... in the environment, if you hit the rate limit.
cmd=$1; repo=$2
case $cmd in
  check) [ -n "$repo" ] || { echo "usage: sh lab62.sh check OWNER/REPO"; exit 1; } ;;
  *) echo "usage: sh lab62.sh check OWNER/REPO"; exit 1 ;;
esac
exec python3 - "$repo" <<'PY'
import sys, os, json, urllib.request, urllib.error
repo = sys.argv[1]; api = os.environ.get('GH_API', 'https://api.github.com'); tok = os.environ.get('GITHUB_TOKEN')
def get(path):
    rq = urllib.request.Request(api + path, headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'lab62'})
    if tok: rq.add_header('Authorization', 'Bearer ' + tok)
    try:
        with urllib.request.urlopen(rq, timeout=20) as r: return r.status, json.load(r)
    except urllib.error.HTTPError as e: return e.code, None
    except Exception as e: print('Could not reach the GitHub API:', e); sys.exit(2)
P = 0
def ok(m): global P; P += 1; print('PASS ', m)
def no(m): print('FAIL ', m)
st, prs = get(f'/repos/{repo}/pulls?state=closed&per_page=100')
if st == 404: print(f'Repository {repo} not found. It must be public, and written as owner/name.'); sys.exit(1)
merged = [p for p in (prs or []) if p.get('merged_at')]
if merged: ok('1 a pull request was merged')
else: no('1 a pull request was merged')
pr = merged[0] if merged else None
n_rev = 0
if pr:
    s1, r1 = get(f'/repos/{repo}/pulls/{pr["number"]}/reviews'); s2, r2 = get(f'/repos/{repo}/pulls/{pr["number"]}/comments')
    n_rev = len(r1 or []) + len(r2 or [])
if n_rev >= 1: ok('2 the merged pull request has a review or a review comment')
else: no('2 the merged pull request has a review or a review comment')
st, br = get(f'/repos/{repo}/branches/main')
if st == 200 and br and br.get('protected'): ok('3 main is protected')
else: no('3 main is protected')
if pr and pr.get('head', {}).get('ref') and pr['head']['ref'] != 'main':
    st, _ = get(f'/repos/{repo}/branches/{pr["head"]["ref"]}')
    if st == 404: ok('4 the pull request branch was deleted after the merge')
    else: no('4 the pull request branch was deleted after the merge')
else: no('4 the pull request branch was deleted after the merge')
print('ALL 4 PASS' if P == 4 else f'{P} of 4 pass')
PY
