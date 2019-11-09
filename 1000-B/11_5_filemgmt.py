import os

# Current Directory
# WINDOWS: cd
# LINUX: pwd
# WHERE THE SCRIPT IS EXECUTED, 
# NOT WHERE THE SCRIPT IS LOCATED
print(os.getcwd())

# Change Directory
# WINDOWS: cd PATH   (aka: chdir)
# LINUX: cd PATH
os.chdir('..')
print(os.getcwd())


# List Directory Contents
# WINDOWS: dir    OR     dir PATH
# LINUX: ls     OR     ls PATH
print(os.listdir())
for curdir, dirs, files in os.walk('.'):
    if '.git' not in curdir:
        print('CURRENT:', curdir)
        print('FILES:', files)
        print('DIRECTORIES:', dirs)
