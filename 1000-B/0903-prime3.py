# public void superprint(string text)
def superprint(text):
    print(text, end='')
    print('(', len(str(text)), ')')

superprint('Hello')

# public bool is_prime(int n)
def is_prime(n):
    if n % 2 == 0:
        return False

    max_num = n//2
    for t in range(3,max_num):
        if n % t == 0:
            return False

    return True

superprint(is_prime(174763))
superprint(is_prime(174764))

for a in range(3, 100000, 2):
    if (is_prime(a)):
        print(a, "is prime")

