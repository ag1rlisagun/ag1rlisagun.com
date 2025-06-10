import os
import sys
import subprocess

# script to push changes to main repo, 
# then update the repo folder for nekogit then push changes there too

# to run:
# (venv) aaliyahwusu@Aaliyahs-MacBook-Air-3 ag1rlisagun.com % python3 updateGits.py commit message

# get arguments from commandline
commandArg = sys.argv[1:]
message = "\"" # add start quotation mark for commit message

# create a string for the commit message out of the commandline arguments
for word in commandArg:
    if commandArg.index(word) != len(commandArg) - 1:
        message += word + " "
    else:
        message += word + "\"" # end the message

# commit and push changes to main github
os.system("git remote -v")
os.system("git status")
os.system("git pull")
os.system("git add .")
os.system("git commit -m {0}".format(message))
os.system("git push")

# update nekogit repo folder
os.chdir("/Users/aaliyahwusu/Documents/projects/ag1rlisasite")
subprocess.call(["rsync", "-varP", "ag1rlisagun.com/", "/Users/aaliyahwusu/Documents/projects/ag1rlisasite/ag1rlisagun.nekoweb.org"])

# push changes to nekogit repo
os.chdir("/Users/aaliyahwusu/Documents/projects/ag1rlisasite/ag1rlisagun.nekoweb.org")
os.system("git remote -v")
os.system("git status")
os.system("git pull")
os.system("git add .")
os.system("git commit -m {0}".format(message))
os.system("git push --set-upstream origin main")
os.chdir("/Users/aaliyahwusu/Documents/projects/ag1rlisasite")

