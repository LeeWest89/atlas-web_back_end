#!/bin/bash
for file in "$@"; 
do
  touch "$file" && chmod u+x "$file"
done