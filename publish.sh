#!/usr/bin/env bash
# Publish the faculty proposal site.   bash labs/lab-proposals/publish.sh
# First run: creates the public repo junnynoh-tech/lab-proposals, pushes, turns on GitHub Pages.
# Later runs: rebuilds the four faculty proposals and the summary pages, commits, pushes.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"; cd "$HERE"
python3 build_site.py
git add -A
git -c user.name="junnynoh-tech" -c user.email="junnynoh-tech@users.noreply.github.com" commit -q -m "Update proposals" || echo "Nothing new to commit."
if ! git remote get-url origin >/dev/null 2>&1; then
  gh repo create junnynoh-tech/lab-proposals --public --source . --push --description "UNG Language Lab: proposals for faculty review"
  gh api -X POST repos/junnynoh-tech/lab-proposals/pages -f "source[branch]=main" -f "source[path]=/" >/dev/null
else
  git push -q
fi
echo "Live in about a minute:"
echo "  Spanish faculty: https://junnynoh-tech.github.io/lab-proposals/spanish/"
echo "  French faculty:  https://junnynoh-tech.github.io/lab-proposals/french/"
