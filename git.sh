#!/bin/bash                                                         

git add . -A                                                        

read -p "Commit Description:" msg                                   

git commit -m "$msg"                                                

git push 