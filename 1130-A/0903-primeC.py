'''
public void DoStuff() {...}
def DoStuff():
public void DoStuff(int stuffWhat, string stuffIt) {...}
def DoStuff(stuffWhat, stuffIt):
public bool IsStuff(int stuffWhat) { ...; return true; }
def IsStuff(suffWhat):
'''

def is_prime(n):
    max_factor = n//2

    for f in range(2, max_factor + 1):  # INCLUDE max_factor by adding 1
        if n % f == 0:
            return False

    return True

print(is_prime(22))
print(is_prime(23))
print(is_prime(24))

cnt = 1
for test in range(3, 10000):
    if (is_prime(test)):
        print(cnt, test, "is prime")
        cnt += 1

