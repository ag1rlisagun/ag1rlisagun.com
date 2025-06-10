import os
import sys

# script to push changes to main repo, 
# then update the repo folder for nekogit then push changes there too

# to run:
# (venv) aaliyahwusu@Aaliyahs-MacBook-Air-3 ag1rlisagun.com % python3 updateGits.py commit message

# get arguments from commandline
commandArg = sys.argv[1:]
message = "\"" # add start quotation mark for commit message

# create a string for the commit message out of the commandline arguments
for word in commandArg:
    print(word)
    if commandArg.index(word) != len(commandArg) - 1:
        message += word + " "
    else:
        message += word + "\"" # end the message

# commit and push changes to main github
os.system("git status")
os.system("git add .")
os.system("git status")
os.system("git commit -m {0}".format(message))
os.system("git push")

# update nekogit repo folder
os.system("cd ..")
os.system("rsync -vaP --delete ag1rlisagun.com/ ../nekogit/ag1rlisagun")

# push changes to nekogit repo
os.system("cd nekogit/ag1rlisagun")
os.system("git status")
os.system("git push -u origin main")
os.system("cd ../../")

