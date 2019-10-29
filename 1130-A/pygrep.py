import sys, re

# print(sys.argv)

tofind = sys.argv[1]

if (len(sys.argv) > 2):
    filename = sys.argv[2]

    with open(filename, 'r') as fi:
        linenum = 0
        for line in fi:
            linenum += 1
            line = line.rstrip()
            xp = re.compile(tofind, re.IGNORECASE)
            if xp.search(line):
            #if tofind.upper() in line.upper():
                print(f"{linenum}: {line}")
else:
    linenum = 0
    for line in sys.stdin:
        linenum += 1
        line = line.rstrip()
        xp = re.compile(tofind, re.IGNORECASE)
        if xp.search(line):
        #if tofind.upper() in line.upper():
            print(f"{linenum}: {line}")
