def print_all(ls,ext):
    idx = 0
    while idx < len(ls):
        elem = ls[idx]
        print(elem, ext)
        idx += 1

def print_all2(ls,ext):
    # stull useful
    for idx in range(len(ls)):
        elem = ls[idx]
        print(elem, ext)


def print_all3(ls,ext):
    # simpler and more common 
    for elem in ls:
        print(elem, ext)


def remove_all(ls):
    for elem in ls:
        ls.remove(elem)


def get_temp():
    t = 100
    u = 'F'
    return t, u


beats = ['john','paul','george','ringo']
# print_all(beats,'beatle')
# print_all2(beats,'beatlegeuse')
# print_all3(beats,'beetlegeuse ' * 3)
remove_all(beats)
print_all(beats,'')


tmp = get_temp()
print('temp is ', tmp)
print('soon it will be', tmp[0] + 5)

tval, tunit = get_temp()
print('temp is',tval,tunit)