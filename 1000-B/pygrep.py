'''
usage:
python pygrep.py -s -i 'filname.blah' 'to find'
'''

from sys import argv, stdin
import getopt

opts, args = getopt.getopt(argv[1:], 'si:')
# (
#   [('-s', ''), ('-i', 'stupid.txt')],
#   ['Hello']
# )

# print(opts)  # [('-s', ''), ('-i', 'stupid.txt')],
# print(args)  # ['Hello']

tofind = args[0]

casesensitive = True
fn = ''

for flag, val in opts:
    if flag == '-s':
        casesensitive = False
    elif flag == '-i':
        fn = val

# for opt in opts:
#     if opt[0] == '-s':
#         casesensitive = False
#     elif opt[0] == '-i':
#         fn = opt[1]

if len(fn) == 0:
    lno = 0
    for line in stdin:
        line = line.rstrip()
        lno += 1
        if tofind.upper() in line.upper():
            print(str(lno) + ': ' + line)
else:
    with open(fn, 'r') as fi:
        lno = 0
        for line in fi:
            line = line.rstrip()
            lno += 1
            if tofind.upper() in line.upper():
                print(str(lno) + ': ' + line)
