def viewall(l):
    idx = 0
    while idx < len(l):
        el = l[idx]
        print(el)
        idx += 1

def viewall2(l):
    for idx in range(len(l)):
        elem = l[idx]
        print(elem)


def viewall3(l):
    for elem in l:
        print(elem)



def deleteall_bad(l):
    for elem in l:
        l.remove(elem)

def deleteall(l):
    while len(l) > 0:
        del l[0]

def deleteval(l, val):
    if val not in l:
        print("ain't no " + val + " in here")
    else:
        while val in l:
            l.remove(val)


def findall(l,val):
    found = []
    while val in l:
        found.append(l.pop(l.index(val)))
    return found


def get_temp():
    tval = 101
    tunits = 'F'
    return tval, tunits


peeps = ['john','paul','george','ringo','paul']
# viewall(peeps)
# viewall2(peeps)
# viewall3(peeps)
# deleteall(peeps)
# viewall3(peeps)
# viewall3(peeps)
# deleteval(peeps,'paul')
# viewall3(peeps)
newlist = findall(peeps,'paul')
viewall3(peeps)
print()
viewall3(newlist)


print(get_temp())

t = get_temp()
print(t[0], t[1])

deg, unit, other = get_temp()
print(str(deg) + chr(176), unit)
