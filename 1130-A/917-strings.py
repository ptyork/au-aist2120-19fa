ls = ['moe','larry','curly']
if 'larry' in ls:
    print('hi larry')

islarrythere = 'larry' in ls
isshempthere = 'shemp' in ls
ismoenotthere = not 'moe' in ls
ismoenotthere = 'moe' not in ls

def is_sentence(chars):
    chars = chars.strip()
    if chars[0].islower():
        return False
    if chars.endswith('!') or chars.endswith('.') or chars.endswith('?'):
        return True
    else:
        return False

def is_sentenceb(chars):
    chars = chars.strip()
    if chars[0].islower():
        return False
    if chars[-1] in '.!?':
        return True
    else:
        return False


def is_floata(chars):
    chars = chars.strip()
    hasdot = False
    hasdigit = False
    for ch in chars:
        if ch == '.':
            if hasdot:
                return False
            else:
                hasdot = True
                continue
        if ch.isdigit():
            hasdigit = True
            continue
        else:
            return False
    # if hasdigit == True:
    #     return True
    # else:
    #     return False
    return hasdigit

while(True):
    inp = input("enter a sentnce: ")
    # if not imp:
    if len(inp) == 0:
        break
    if is_sentence(inp):
        print('yep')
    else:
        print('nope')
    if is_sentenceb(inp):
        print('yep')
    else:
        print('nope')

while(True):
    inp = input("enter a number: ")
    if not inp:
        break
    if is_floata(inp):
        print('yep')
    else:
        print('nope')
