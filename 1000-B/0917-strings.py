stooges=['mo', 'larry', 'curly', 'shemp']
larrythere = 'larry' in stooges

def is_sentence(sent):
    ans = sent.endswith('.') or sent.endswith('!') or sent.endswith('?')
    return ans

def is_num(s):
    s = s.strip()

    if len(s) == 0:
        return False
    
    dotcount = 0
    for ch in s:
        if ch == '.':
            if dotcount == 0:
                dotcount += 1
                continue
            else:
                return False
        elif ch.isdigit():
            continue
        else:
            return False

    return True


def better_is_num(s):
    try:
        float(s)
    except:
        return False
    return True


while True:
    test = input("Enter a number: ")
    if not is_num(test):
        print('You moron!!')
        break
    print(is_num(test))
    print(better_is_num(test))
