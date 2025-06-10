import os
import sys

# either find out how to use an alias and provide and argument at the same time,
# or just run the python file in terminal with an argument:
# push changes to main github repo,
# leave main repo and update the folder of the nekogit repo,
# then push the changes to nekogit

commandArg = sys.argv[1:]
message = "\""

for word in commandArg:
    print(word)
    if commandArg.index(word) != len(commandArg) - 1:
        message += word + " "
    else:
        message += word + "\""

os.system("git status")
os.system("git add .")
os.system("git status")
os.system("git commit -m {0}".format(message))
os.system("git push")
os.system("rsync -av --delete --info=name0 ag1rlisagun.com/ ../nekogit/ag1rlisagun")
os.system("cd ../nekogit/ag1rlisagun")
os.system("git status")
os.system("git push -u origin main")
os.system("cd ../../")

