#!/bin/bash
set_commit_message() {
  read -p "Enter commit message: " -e -i "$1" msg
}
git add . -A && git commit -m "$msg" && git push
