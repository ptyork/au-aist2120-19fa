import os
from sys import argv

# Get Current Directory
# WIN: cd
# NIX: pwd
print(os.getcwd())

# Change Directory
# WIN: cd PATH      (aka chdir PATH)
# NIX: cd PATH
os.chdir('..')
print(os.getcwd())

# List Directory
# WIN: dir    or    dir PATH
# NIX: ls     or    ls PATH
print(os.listdir(r'z:\aist2120\1130-A'))
print(os.listdir())

# for curdir, dirs, files in os.walk(r'z:\aist2120\1130-A'):
for curdir, dirs, files in os.walk(argv[1]):
    # print("CURR:", curdir)
    # print("DIRS:", dirs)
    # print("FILS:", files)
    for filestring in files:
        if filestring.endswith('.py'):
            print(curdir + os.sep + filestring)


